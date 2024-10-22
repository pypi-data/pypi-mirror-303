"""Module containing BaseSource class.

BaseSource is the abstract data source class from which all concrete data sources
must inherit.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Callable, Iterable, Iterator, Sequence
import contextlib
from datetime import date, datetime
import functools
from functools import cached_property
import inspect
import logging
from logging.handlers import QueueHandler
import os
from pathlib import Path
import traceback
from typing import (
    TYPE_CHECKING,
    Any,
    Final,
    Literal,
    Optional,
    Protocol,
    Union,
    cast,
    overload,
)

from filetype import guess_extension
import methodtools
import numpy as np
import pandas as pd
from pandas.core.dtypes.cast import (  # type: ignore[attr-defined] # Reason: this function _is_ defined but is technically private # noqa: E501
    find_common_type,
)
from pandas.core.dtypes.common import is_datetime64_any_dtype as is_datetime
import psutil

from bitfount.config import (
    BITFOUNT_CACHE_DIR,
    BITFOUNT_FILE_MULTIPROCESSING_ENABLED,
    BITFOUNT_TASK_BATCH_SIZE,
    FAST_LOAD_MAXIMUM_NUMBER_OF_FILES_TO_LOAD,
    MAX_NUMBER_OF_DATASOURCE_FILES,
)
from bitfount.data.datasources.types import Date, DateTD
from bitfount.data.datasources.utils import (
    FILE_SYSTEM_ITERABLE_METADATA_COLUMNS,
    LAST_MODIFIED_METADATA_COLUMN,
    ORIGINAL_FILENAME_METADATA_COLUMN,
    _modify_column,
    _modify_file_paths,
)
from bitfount.data.datasplitters import DatasetSplitter, SplitterDefinedInData
from bitfount.data.exceptions import DataNotLoadedError, IterableDataSourceError
from bitfount.data.persistence.base import DataPersister
from bitfount.data.persistence.sqlite import SQLiteDataPersister
from bitfount.data.types import (
    DataPathModifiers,
    _Column,
    _GetColumnCallable,
    _GetDtypesCallable,
    _SingleOrMulti,
)
from bitfount.data.utils import _generate_dtypes_hash, _hash_str
from bitfount.hooks import HookType, get_hooks
from bitfount.types import _Dtypes
from bitfount.utils import delegates, seed_all
from bitfount.utils.fs_utils import (
    get_file_creation_date,
    get_file_last_modification_date,
    get_file_size,
    is_file,
    scantree,
)
from bitfount.utils.logging_utils import (
    SampleFilter,
    _get_bitfount_console_handler,
    _get_bitfount_log_file_handler,
)

if TYPE_CHECKING:
    from queue import Queue

logger = logging.getLogger(__name__)
logger.addFilter(SampleFilter())

# Used for converting megabytes to bytes
NUM_BYTES_IN_A_MEGABYTE: Final[int] = 1024 * 1024

# This is used for annotating the data in the datasource with
# the inferred label
BITFOUNT_INFERRED_LABEL_COLUMN: str = "BITFOUNT_INFERRED_LABEL"

# This determines the maximum number of multiprocessing workers that can be used
# for file processing parallelisation.
MAX_NUM_MULTIPROCESSING_WORKERS: Final[int] = 5


class _LockType(contextlib.AbstractContextManager, Protocol):
    """Protocol for the Multiprocessing Manager Lock class."""

    def acquire(self, block: bool, timeout: float) -> bool:
        """Acquire the lock."""

    def release(self) -> None:
        """Release the lock."""


class BaseSource(ABC):
    """Abstract Base Source from which all other data sources must inherit.

    Args:
        data_splitter: Approach used for splitting the data into training, test,
            validation. Defaults to None.
        seed: Random number seed. Used for setting random seed for all libraries.
            Defaults to None.
        modifiers: Dictionary used for modifying paths/ extensions in the dataframe.
            Defaults to None.
        ignore_cols: Column/list of columns to be ignored from the data.
            Defaults to None.

    Attributes:
        data: A Dataframe-type object which contains the data.
        data_splitter: Approach used for splitting the data into training, test,
            validation.
        seed: Random number seed. Used for setting random seed for all libraries.
    """

    # TODO: [BIT-3722] Method Resolution Order appears to be broken such that if methods
    # that are defined in a base class are overridden in a subclass, the base class
    # implementation is preferentially called over the subclass implementation. Be
    # mindful of this when overriding methods.

    def __init__(
        self,
        data_splitter: Optional[DatasetSplitter] = None,
        seed: Optional[int] = None,
        modifiers: Optional[dict[str, DataPathModifiers]] = None,
        ignore_cols: Optional[Union[str, Sequence[str]]] = None,
        **kwargs: Any,
    ) -> None:
        self._base_source_init = True
        self.data_splitter = data_splitter
        self.seed = seed
        self._modifiers = modifiers
        self._data_is_split: bool = False
        self._data_is_loaded: bool = False
        self._is_task_running: bool = False
        seed_all(self.seed)

        self._train_idxs: Optional[np.ndarray] = None
        self._validation_idxs: Optional[np.ndarray] = None
        self._test_idxs: Optional[np.ndarray] = None

        self._data: pd.DataFrame
        self._table_hashes: set[str] = set()

        self._ignore_cols: list[str] = []
        if isinstance(ignore_cols, str):
            self._ignore_cols = [ignore_cols]
        elif ignore_cols is not None:
            self._ignore_cols = list(ignore_cols)
        self.image_columns: set[str] = set()
        for unexpected_kwarg in kwargs:
            logger.warning(f"Ignoring unexpected keyword argument {unexpected_kwarg}")

        super().__init__()

    @abstractmethod
    def get_dtypes(self, **kwargs: Any) -> _Dtypes:
        """Implement this method to get the columns and column types from dataset."""
        raise NotImplementedError

    def __init_subclass__(cls, **kwargs: Any) -> None:
        if not (inspect.isabstract(cls) or ABC in cls.__bases__):
            cls.get_dtypes = cls._get_dtypes()  # type: ignore[method-assign] # reason: wrap subclass get_dtypes # noqa: E501
            cls.get_column = cls._get_column()  # type: ignore[method-assign] # reason: wrap subclass get_column # noqa: E501

    @classmethod
    def _get_dtypes(cls) -> _GetDtypesCallable:
        """Decorate subclass' get_dtypes implementation.

        Decorate subclass' implementation of get_dtypes to handle ignored
        columns and handle `_table_hashes`.
        """
        subclass_get_dtypes = cls.get_dtypes

        def get_dtypes(self: BaseSource, *args: Any, **kwargs: Any) -> _Dtypes:
            dtypes: _Dtypes = subclass_get_dtypes(self, *args, **kwargs)
            if self._ignore_cols:
                for col in self._ignore_cols:
                    if col in dtypes:
                        del dtypes[col]
            self._table_hashes.add(_generate_dtypes_hash(dtypes))
            return dtypes

        return get_dtypes

    @classmethod
    def _get_column(
        cls,
    ) -> _GetColumnCallable:
        """Decorate subclass' get_column implementation.

        Decorate subclass' implementation of get_column to handle ignored
        columns and modifiers.
        """
        subclass_get_column = cls.get_column

        def get_column(
            self: BaseSource, col_name: str, *args: Any, **kwargs: Any
        ) -> _Column:
            column = subclass_get_column(self, col_name, *args, **kwargs)
            if self._modifiers:
                if modifier_dict := self._modifiers.get(col_name):
                    column = _modify_column(column, modifier_dict)
            return column

        return get_column

    @property
    def is_task_running(self) -> bool:
        """Returns True if a task is running."""
        return self._is_task_running

    @is_task_running.setter
    def is_task_running(self, value: bool) -> None:
        """Sets `_is_task_running` to `value`."""
        self._is_task_running = value

    @property
    def is_initialised(self) -> bool:
        """Checks if `BaseSource` was initialised."""
        if hasattr(self, "_base_source_init"):
            return True
        else:
            return False

    @property
    def data(self) -> pd.DataFrame:
        """A property containing the underlying dataframe if the data has been loaded.

        Raises:
            DataNotLoadedError: If the data has not been loaded yet.
        """
        if self._data_is_loaded:
            return self._data
        else:
            raise DataNotLoadedError(
                "Data is not loaded yet. Please call `load_data` first."
            )

    @data.setter
    def data(self, _data: Optional[pd.DataFrame]) -> None:
        """Data setter."""
        self._data_setter(_data)

    def _data_setter(self, _data: Optional[pd.DataFrame]) -> None:
        """Implementation method for data setter."""
        if _data is not None:
            if isinstance(_data, pd.DataFrame):
                if self._ignore_cols:
                    # If columns already ignored in data, ignore errors.
                    _data = _data.drop(columns=self._ignore_cols, errors="ignore")
                self._data = _data

                if self._modifiers:
                    _modify_file_paths(self._data, self._modifiers)

                self._data_is_loaded = True
            else:
                raise TypeError(
                    "Invalid data attribute. "
                    "Expected pandas dataframe for attribute 'data' "
                    f"but received :{type(_data)}"
                )

    @property
    def hash(self) -> str:
        """The hash associated with this BaseSource.

        This is the hash of the static information regarding the underlying DataFrame,
        primarily column names and content types but NOT anything content-related
        itself. It should be consistent across invocations, even if additional data
        is added, as long as the DataFrame is still compatible in its format.

        Returns:
            The hexdigest of the DataFrame hash.
        """
        if not self._table_hashes:
            raise DataNotLoadedError(
                "Data is not loaded yet. Please call `get_dtypes` first."
            )
        else:
            return _hash_str(str(sorted(self._table_hashes)))

    @staticmethod
    def _get_data_dtypes(data: pd.DataFrame) -> _Dtypes:
        """Returns the nullable column types of the dataframe.

        This is called by the `get_dtypes` method. This method also overrides datetime
        column dtypes to be strings. This is not done for date columns which are of
        type object.
        """
        data = data.convert_dtypes()
        dtypes: _Dtypes = data.dtypes.to_dict()
        for name in list(dtypes):
            if is_datetime(data[name]):
                dtypes[name] = pd.StringDtype()

        return dtypes

    def load_data(self, **kwargs: Any) -> None:
        """Load the data for the datasource.

        Raises:
            TypeError: If data format is not supported.
        """
        if not self._data_is_loaded:
            if (data := self.get_data(**kwargs)) is not None:
                self.data = data
            elif not self.iterable:
                logger.warning(
                    f"Datasource {self} returned None from get_data()"
                    f" but {self.iterable=}"
                )
            else:
                logger.debug(
                    f"Datasource {self} returned None from get_data()"
                    f" (expected as {self.iterable=})"
                )
        else:
            logger.warning(
                f"Datasource {self} has already been loaded; will not load again."
            )

    def get_values(
        self, col_names: list[str], **kwargs: Any
    ) -> dict[str, Iterable[Any]]:
        """Get distinct values from list of columns."""
        dic: dict[str, Iterable[Any]] = {}

        for col in col_names:
            try:
                dic[col] = self.data[col].unique()
            except TypeError:
                logger.warning(f"Found unhashable value type, skipping column {col}.")
        return dic

    def get_column_names(self, **kwargs: Any) -> Iterable[str]:
        """Get the column names as an iterable."""
        return list(self.data.columns)

    def get_column(self, col_name: str, **kwargs: Any) -> _Column:
        """Get a single column from dataset.

        Used to iterate over image columns for the purposes of schema generation.
        """
        return self.data[col_name]

    @abstractmethod
    def get_data(self, **kwargs: Any) -> Optional[pd.DataFrame]:
        """Implement this method to load and return dataset."""
        raise NotImplementedError

    def get_project_db_sqlite_create_table_query(self) -> str:
        """Implement this method to return the required columns and types.

        This is used by the "run on new data only" feature. This should be in the format
        that can be used after a "CREATE TABLE" statement and is used to create the task
        table in the project database.
        """
        raise NotImplementedError

    def get_project_db_sqlite_columns(self) -> list[str]:
        """Implement this method to get the required columns.

        This is used by the "run on new data only" feature. This is used to add data to
        the task table in the project database.
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """Get the number of rows in the dataset."""
        return len(self.data)

    @property
    def iterable(self) -> bool:
        """This returns False if the DataSource does not subclass `IterableSource`.

        However, this property must be re-implemented in `IterableSource`, therefore it
        is not necessarily True if the DataSource inherits from `IterableSource`.
        """
        return False


@delegates()
class IterableSource(BaseSource, ABC):
    """Abstract base source that supports iterating over the data.

    This is used for streaming data in batches as opposed to loading the entire dataset
    into memory.

    Args:
        partition_size: The size of each partition when iterating over the data.
    """

    def __init__(
        self,
        partition_size: int = BITFOUNT_TASK_BATCH_SIZE,
        **kwargs: Any,
    ) -> None:
        # TODO: [BIT-3486] Make partition size configurable?
        self.partition_size = partition_size
        super().__init__(**kwargs)

    @property
    @abstractmethod
    def iterable(self) -> bool:
        """Implement this method to define whether the data source is iterable.

        The datasource must inherit from `IterableSource` if this is True. However,
        the inverse is not necessarily True.
        """
        raise NotImplementedError

    def get_data(self, **kwargs: Any) -> Optional[pd.DataFrame]:
        """This method must return None if the data source is iterable."""
        if self.iterable:
            logger.warning(f"Datasource {self} is iterable; get_data() returns None")
            return None
        else:
            return super().get_data(**kwargs)  # type: ignore[safe-super] # Reason: parent implementation raises NotImplementedError if ends up being called # noqa: E501

    @abstractmethod
    def yield_data(self, **kwargs: Any) -> Iterator[pd.DataFrame]:
        """Implement this method to yield dataframes."""
        raise NotImplementedError

    @property
    def data(self) -> pd.DataFrame:
        """A property containing the underlying dataframe if the data has been loaded.

        If the datasource is iterable, this will raise an exception.

        Raises:
            IterableDataSourceError: If the datasource is set to iterable.
            DataNotLoadedError: If the data has not been loaded yet.
        """
        if self.iterable:
            raise IterableDataSourceError(
                ".data property cannot be used when datasource is iterable."
            )
        else:
            return super().data

    @data.setter
    def data(self, _data: Optional[pd.DataFrame]) -> None:
        """Data property setter."""
        if self.iterable:
            raise IterableDataSourceError(
                ".data property cannot be used when datasource is iterable."
            )
        else:
            super()._data_setter(_data)

    def get_values(
        self, col_names: list[str], **kwargs: Any
    ) -> dict[str, Iterable[Any]]:
        """Implement this method to get distinct values from list of columns."""
        """Get values for iterable datasource."""
        values: dict[str, set[Any]] = defaultdict(set)
        cols_to_skip: set[str] = set()

        for chunk in self.yield_data(**kwargs):
            for col in col_names:
                if col in cols_to_skip:
                    continue

                try:
                    values[col].update(chunk[col].unique())
                except TypeError:
                    logger.warning(
                        f"Found unhashable value type, skipping column {col}."
                    )
                    # Remove from `values` dict, if present, and add to skip list
                    values.pop(col, None)
                    cols_to_skip.add(col)

        return {k: list(v) for k, v in values.items()}

    def get_column_names(self, **kwargs: Any) -> Iterable[str]:
        """Get column names for iterable datasource."""
        # The dataframes should be the same throughout the yield_data iteration
        # so we should only need to get one of them.
        df_0: pd.DataFrame = next(self.yield_data(**kwargs))
        return list(df_0.columns)

    def get_column(self, col_name: str, **kwargs: Any) -> _Column:
        """Get column for iterable datasource."""

        def extend_series(s1: pd.Series, s2: pd.Series) -> pd.Series:
            # mypy_reason: does not map to correct overload, but
            #              concat(Iterable[Series]) -> Series is possible
            return cast(pd.Series, pd.concat([s1, s2]))

        # We use a for-loop and per-chunk concat to avoid holding all the chunks
        # in memory together _and_ trying to create a concatenated one
        col: pd.Series = functools.reduce(
            extend_series,
            (chunk[col_name] for chunk in self.yield_data(**kwargs)),
        )
        return col

    def get_dtypes(self, **kwargs: Any) -> _Dtypes:
        """Get dtypes for iterable datasource."""
        dtypes: _Dtypes = {}

        # We iterate through each chunk, finding the common type that best
        # expresses the dtype for a column from all the chunks seen so far
        for chunk in self.yield_data(**kwargs):
            chunk_dtypes: _Dtypes = self._get_data_dtypes(chunk)
            for k, dtype in chunk_dtypes.items():
                if k not in dtypes:
                    dtypes[k] = dtype
                else:
                    dtypes[k] = find_common_type([dtypes[k], dtype])

        return dtypes

    def __len__(self) -> int:
        """Get len for iterable datasource."""
        chunk_lens: Iterable[int] = map(len, self.yield_data())
        return sum(chunk_lens)


class MultiProcessingMixIn:
    """MixIn class for multiprocessing of `_get_data`."""

    skipped_files: set[str]
    image_columns: set[str]
    data_cache: Optional[DataPersister]

    @abstractmethod
    def _get_data(
        self,
        file_names: list[str],
        use_cache: bool = True,
        skip_non_tabular_data: bool = False,
        **kwargs: Any,
    ) -> pd.DataFrame: ...

    @staticmethod
    def get_num_workers(file_names: list[str]) -> int:
        """Gets the number of workers to use for multiprocessing.

        Ensures that the number of workers is at least 1 and at most equal to
        MAX_NUM_MULTIPROCESSING_WORKERS. If the number of files is less than
        MAX_NUM_MULTIPROCESSING_WORKERS, then we use the number of files as the
        number of workers. Unless the number of machine cores is also less than
        MAX_NUM_MULTIPROCESSING_WORKERS, in which case we use the lower of the
        two.

        Args:
            file_names: The list of file names to load.

        Returns:
            The number of workers to use for multiprocessing.
        """
        return min(
            max(1, len(file_names)),
            # Make sure we don't use all the available cores
            max(1, psutil.cpu_count(logical=False) - 1),
            MAX_NUM_MULTIPROCESSING_WORKERS,
        )

    def use_file_multiprocessing(self, file_names: list[str]) -> bool:
        """Check if file multiprocessing should be used.

        Returns True if file multiprocessing has been enabled by the environment
        variable and the number of workers would be greater than 1, otherwise False.
        There is no need to use file multiprocessing if we are just going to use one
        worker - it would be slower than just loading the data in the main process.

        Returns:
            True if file multiprocessing should be used, otherwise False.
        """
        if BITFOUNT_FILE_MULTIPROCESSING_ENABLED:
            return self.get_num_workers(file_names) > 1
        return False

    @staticmethod
    def _mp_configure_listener_logger(log_file_name: str) -> None:
        """Configure the logger for the listener process.

        Adds the same handlers as the main process logger to the listener process
        logger. This requires passing the name of the log file to use to the listener
        because otherwise it can't be found because it has a timestamp in the name.

        Args:
            log_file_name: The name of the log file to use.
        """
        logger = logging.getLogger()
        logger.addHandler(_get_bitfount_log_file_handler(log_file_name=log_file_name))
        logger.addHandler(_get_bitfount_console_handler())
        logger.propagate = False

    @classmethod
    def _mp_listener_process(cls, queue: Queue, log_file_name: str) -> None:
        """Process that listens for log messages from the worker processes.

        Whenever a log message is received, it is handled by the logger.

        Args:
            queue: The queue to listen on.
            log_file_name: The name of the log file to use.
        """
        cls._mp_configure_listener_logger(log_file_name)
        while True:
            try:
                record = queue.get()
                if record is None:  # Sentinel to tell the listener to quit
                    break
                logger.handle(record)
            except Exception:
                import traceback

                traceback.print_exc()

    @staticmethod
    def _mp_configure_worker_logger(queue: Queue) -> None:
        """Configure the logger for the worker processes.

        Adds a QueueHandler to the logger to send log messages to the listener process.

        Args:
            queue: The queue to send log messages to.
        """
        h = QueueHandler(queue)
        bf_logger = logging.getLogger("bitfount")
        bf_logger.setLevel(logging.DEBUG)
        plugins_logger = logging.getLogger("plugins")
        plugins_logger.setLevel(logging.DEBUG)
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.WARNING)
        for _logger in (bf_logger, plugins_logger, root_logger):
            _logger.handlers.clear()  # Clear existing handlers
            _logger.addHandler(h)
            _logger.propagate = False

    def _mp_worker_get_data_process(
        self,
        queue: Queue,
        sqlite_path: Optional[Path],
        lock: _LockType,
        file_names: list[str],
        use_cache: bool = True,
        **kwargs: Any,
    ) -> tuple[pd.DataFrame, list[str], list[str]]:
        """Process that calls `_get_data` to load data.

        This is called by the main process to load data in parallel. This method
        configures the logger for the worker process and calls `_get_data`.

        Args:
            queue: The queue to send log messages to.
            sqlite_path: The path to the SQLite file to use for recreating the data
                cache.
            lock: The lock to use for accessing the data cache.
            file_names: The list of file names to load.
            use_cache: Whether the cache should be used to retrieve data for these
                files. Note that cached data may have some elements, particularly
                image-related fields such as image data or file paths, replaced
                with placeholder values when stored in the cache.

                If data_cache is set on the instance, data will be _set_ in the
                cache, regardless of this argument.
            kwargs: Keyword arguments to pass to `_get_data`.

        Returns:
            The loaded data as a dataframe, a list of skipped files and a list of image
            columns. The skipped files and image columns are returned so that they can
            be added to the `skipped_files` and `image_columns` sets respectively
            in the main process - otherwise this information would be lost when the
            worker process is terminated. The skipped files and images columns are
            returned as a list rather than a set because sets are not pickleable.
        """
        logger.debug(f"Using cache: {use_cache}")
        if sqlite_path:
            logger.debug(f"Recreating data cache from {sqlite_path}.")
            self.data_cache = SQLiteDataPersister(sqlite_path, lock=lock)
        self._mp_configure_worker_logger(queue)
        data = self._get_data(file_names=file_names, use_cache=use_cache, **kwargs)
        return data, list(self.skipped_files), list(self.image_columns)

    def _mp_get_data(
        self, file_names: list[str], use_cache: bool = True, **kwargs: Any
    ) -> pd.DataFrame:
        """Call `_get_data` in parallel.

        This method sets up the multiprocessing queue and processes and calls
        `_get_data` in parallel. It also sets up the listener process to handle log
        messages from the worker processes.

        Args:
            file_names: The list of file names to load.
            use_cache: Whether the cache should be used to retrieve data for these
                files. Note that cached data may have some elements, particularly
                image-related fields such as image data or file paths, replaced
                with placeholder values when stored in the cache.

                If data_cache is set on the instance, data will be _set_ in the
                cache, regardless of this argument.
            kwargs: Keyword arguments to pass to `_get_data`.

        Returns:
            The loaded data as a dataframe.
        """
        from concurrent.futures import Future, ProcessPoolExecutor, as_completed
        from multiprocessing import Manager, Process

        # If there is more than one file, we use multiprocessing to load the data
        logger.info("Loading data in parallel using multiprocessing.")
        log_file_name: str = ""
        for handler in logging.getLogger("bitfount").handlers:
            if isinstance(handler, logging.FileHandler):
                # Already have a file handler, so return it
                log_file_name = Path(handler.baseFilename).stem
                break

        if not log_file_name:
            # If there is no file handler, then there is no need for this message
            # to be logged any higher than debug anyway
            logger.debug("No existing file handler found for logger.")

        log_queue: Optional[Queue] = None
        log_listener: Optional[Process] = None
        executor: Optional[ProcessPoolExecutor] = None
        try:
            # Set environment variable to indicate that the spawned processes are
            # child processes since they will inherit the environment from the parent
            os.environ["_BITFOUNT_CHILD_PROCESS"] = "True"

            # Initialization must be done before creating the process
            data_cache_sqlite_path: Optional[Path] = None
            data_cache: Optional[DataPersister] = self.data_cache
            if self.data_cache and isinstance(self.data_cache, SQLiteDataPersister):
                data_cache_sqlite_path = self.data_cache._sqlite_path
                # TODO: [BIT-3723] There may be a better way to pass the data cache to
                # the worker processes by disposing of the connection pool rather than
                # having to recreate the cache in each worker process
                self.data_cache = None

            manager = Manager()
            log_queue = manager.Queue(-1)
            log_listener = Process(
                target=self._mp_listener_process, args=(log_queue, log_file_name)
            )
            log_listener.start()

            # Create a pool of worker processes
            max_workers = self.get_num_workers(file_names)
            logger.info(f"Multiprocessing max workers: {max_workers}")
            executor = ProcessPoolExecutor(max_workers=max_workers)
            lock = manager.Lock()
            futures: list[Future] = [
                executor.submit(
                    self._mp_worker_get_data_process,
                    log_queue,
                    data_cache_sqlite_path,
                    lock,
                    [i],
                    use_cache,
                    **kwargs,
                )
                for i in file_names
            ]

            total_num_files = len(file_names)
            dfs: list[pd.DataFrame] = []
            # Wait for the results to come in one by one as they complete
            for i, future in enumerate(as_completed(futures)):
                # Signal file finished processing
                for hook in get_hooks(HookType.POD):
                    hook.on_file_process_end(
                        cast(FileSystemIterableSource, self),
                        file_num=i + 1,
                        total_num_files=total_num_files,
                    )
                data, skipped_files, image_columns = future.result()
                self.skipped_files.update(set(cast(list[str], skipped_files)))
                self.image_columns.update(set(cast(list[str], image_columns)))
                dfs.append(cast(pd.DataFrame, data))

            logger.debug("Finished loading data in parallel using multiprocessing.")
        finally:
            logger.debug("Cleaning up multiprocessing environment.")

            # Reset environment variable to indicate that this is not a child process
            os.environ["_BITFOUNT_CHILD_PROCESS"] = "False"

            # Reset the data cache if it was set in the first place
            if data_cache:
                logger.debug("Reverting data cache to original state.")
                self.data_cache = data_cache

            if log_queue:
                log_queue.put_nowait(None)  # Send sentinel to tell listener to quit

            if log_listener:
                # Wait for listener to quit. Must be done before terminating the process
                # to ensure all the log messages continue to get processed
                log_listener.join()
                # Terminate listener process
                log_listener.terminate()

            # Shutdown the executor. We don't wait for it to finish as we have already
            # waited for the results to come in one by one as they complete
            if executor:
                executor.shutdown(wait=False)

        # If no data was loaded, return an empty dataframe as `pd.concat` will fail
        # if no dataframes are passed to it
        return pd.concat(dfs, axis=0, ignore_index=True) if dfs else pd.DataFrame()


@delegates()
class FileSystemIterableSource(IterableSource, MultiProcessingMixIn, ABC):
    """Abstract base source that supports iterating over file-based data.

    This is used for Iterable data sources that whose data is stored as files on disk.

    Args:
        path: Path to the directory which contains the data files. Subdirectories
            will be searched recursively.
        output_path: The path where to save intermediary output files. Defaults to
            'preprocessed/'.
        iterable: Whether the data source is iterable. This is used to determine
            whether the data source can be used in a streaming context during a task.
            Defaults to True.
        fast_load: Whether the data will be loaded in fast mode. This is used to
            determine whether the data will be iterated over during set up for schema
            generation and splitting (where necessary). Only relevant if `iterable` is
            True, otherwise it is ignored. Defaults to True.
        file_extension: File extension(s) of the data files. If None, all files
            will be searched. Can either be a single file extension or a list of
            file extensions. Case-insensitive. Defaults to None.
        strict: Whether File loading should be strictly done on files with the
            explicit file extension provided. If set to True will only load
            those files in the dataset. Otherwise, it will scan the given path
            for files of the same type as the provided file extension. Only
            relevant if `file_extension` is provided. Defaults to False.
        cache_images: Whether to cache images in the file system. Defaults to False.
            This is ignored if `fast_load` is True.
        file_creation_min_date: The oldest possible date to consider for file
            creation. If None, this filter will not be applied. Defaults to None.
        file_modification_min_date: The oldest possible date to consider for file
            modification. If None, this filter will not be applied. Defaults to None.
        file_creation_max_date: The newest possible date to consider for file
            creation. If None, this filter will not be applied. Defaults to None.
        file_modification_max_date: The newest possible date to consider for file
            modification. If None, this filter will not be applied. Defaults to None.
        min_file_size: The minimum file size in megabytes to consider. If None, all
            files will be considered. Defaults to None.
        max_file_size: The maximum file size in megabytes to consider. If None, all
            files will be considered. Defaults to None.

    Raises:
        ValueError: If `iterable` is False or `fast_load` is False or `cache_images`
            is True.
    """

    def __init__(
        self,
        path: Union[os.PathLike, str],
        output_path: Optional[Union[os.PathLike, str]] = None,
        iterable: bool = True,
        fast_load: bool = True,
        file_extension: Optional[_SingleOrMulti[str]] = None,
        strict: bool = False,
        cache_images: bool = False,
        file_creation_min_date: Optional[Union[Date, DateTD]] = None,
        file_modification_min_date: Optional[Union[Date, DateTD]] = None,
        file_creation_max_date: Optional[Union[Date, DateTD]] = None,
        file_modification_max_date: Optional[Union[Date, DateTD]] = None,
        min_file_size: Optional[float] = None,
        max_file_size: Optional[float] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)

        if not iterable:
            raise ValueError("FileSystemIterableSource must be iterable.")

        if not fast_load:
            raise ValueError("FileSystemIterableSource must use fast_load.")

        if cache_images:
            raise ValueError("FileSystemIterableSource must not cache images.")

        self._iterable = iterable
        self.fast_load = fast_load
        self.cache_images = cache_images

        # Path related attributes
        self._unsanitized_path = path
        self.out_path: Path
        if output_path is None:
            self.out_path = BITFOUNT_CACHE_DIR
        else:
            self.out_path = Path(output_path).expanduser().absolute().resolve()
        logger.debug(f"File output path set to {self.out_path}")
        self.out_path.mkdir(exist_ok=True, parents=True)  # create if not exists

        # File extension and strict mode
        self.file_extension: Optional[list[str]] = None
        if file_extension:
            file_extension_: list[str] = (
                [file_extension]
                if isinstance(file_extension, str)
                else list(file_extension)
            )
            self.file_extension = [
                f".{fe}" if not fe.startswith(".") else fe for fe in file_extension_
            ]

        self.strict = strict if self.file_extension is not None else False

        # Set the min and max file creation and modification date filters
        self.file_creation_min_date: Optional[date] = self._get_datetime(
            file_creation_min_date
        )
        self.file_modification_min_date: Optional[date] = self._get_datetime(
            file_modification_min_date
        )
        self.file_creation_max_date: Optional[date] = self._get_datetime(
            file_creation_max_date
        )
        self.file_modification_max_date: Optional[date] = self._get_datetime(
            file_modification_max_date
        )

        if not any(
            [
                self.file_creation_min_date,
                self.file_modification_min_date,
                self.file_creation_max_date,
                self.file_modification_max_date,
            ]
        ):
            logger.warning(
                "No file creation or modification min/max dates provided. All files in "
                "the directory will be considered which may impact performance."
            )

        # Set the min and max file sizes in megabytes
        self.min_file_size: Optional[float] = min_file_size
        self.max_file_size: Optional[float] = max_file_size

        if not self.min_file_size and not self.max_file_size:
            logger.warning(
                "No file size limits provided. All files in the directory will be "
                "considered which may impact performance."
            )

        # This is used to select a subset of file names by the data splitter rather than
        # every file that has been loaded or that is in the directory. In particular,
        # this is used to subset the files for batched execution of a task.
        self.selected_file_names_override: list[str] = []
        # This is used to filter the file names to only new records.
        # In particular, this is used only when pod database exists and task
        # is set with `run_on_new_data_only` flag.
        self.new_file_names_only_set: Union[set[str], None] = None
        # A list of files that have previously been skipped either because of errors or
        # because they don't contain any image data and `images_only` is True. This
        # allows us to skip these files again more quickly if they are still present in
        # the directory.
        self.skipped_files: set[str] = set()

        # A list of image column names, so we can keep track of them when
        # cache_images is False.
        self.image_columns: set[str] = set()

        # Fast-load related attributes
        self._sampled_data_priv: Optional[pd.DataFrame] = None

        # Placeholder for datasource-specific filters

        # All filters should take a list of filenames and return
        # a list of file names or an empty list if no files
        # matching the filters are found.
        self._datasource_filters_to_apply: list[Callable] = []

    def get_project_db_sqlite_create_table_query(self) -> str:
        """Returns the required columns and types to identify a data point.

        The file name is used as the primary key and the last modified date is used to
        determine if the file has been updated since the last time it was processed. If
        there is a conflict on the file name, the row is replaced with the new data to
        ensure that the last modified date is always up to date.
        """
        return (
            f"{ORIGINAL_FILENAME_METADATA_COLUMN} TEXT PRIMARY KEY, "
            f"'{LAST_MODIFIED_METADATA_COLUMN}' VARCHAR(30), "
            f"UNIQUE({ORIGINAL_FILENAME_METADATA_COLUMN}) ON CONFLICT REPLACE"
        )

    def get_project_db_sqlite_columns(self) -> list[str]:
        """Returns the required columns to identify a data point."""
        return [ORIGINAL_FILENAME_METADATA_COLUMN, LAST_MODIFIED_METADATA_COLUMN]

    def _perform_max_file_check(self, file_names: list[str]) -> None:
        """Check if the number of files in the directory exceeds the maximum allowed.

        This check is performed after filtering the files by date and size. If the
        number of files in the directory exceeds the maximum allowed, an error is
        raised.

        Raises:
            IterableDataSourceError: If the number of files in the directory exceeds the
                maximum allowed.
        """
        num_files = len(file_names)
        if num_files > MAX_NUMBER_OF_DATASOURCE_FILES:
            raise IterableDataSourceError(
                f"Too many files in the directory match the criteria. Found "
                f"{num_files} files, but the maximum number of files "
                f"allowed is {MAX_NUMBER_OF_DATASOURCE_FILES}."
            )

    @staticmethod
    def _get_datetime(date: Optional[Union[Date, DateTD]]) -> Optional[date]:
        """Convert a Date or DateTD object to a datetime.date object.

        Args:
            date: The Date or DateTD object to convert.

        Returns:
            The datetime.date object if date is a Date object, otherwise None.
        """
        if date:
            if isinstance(date, Date):
                return date.get_date()
            else:  # is typed dict
                return Date(**date).get_date()

        return None

    ####################
    # Other Properties #
    ####################
    @property
    def iterable(self) -> bool:
        """Defines whether the data source is iterable.

        This is defined by the user when instantiating the class.
        """
        return self._iterable

    @property
    def path(self) -> Path:
        """Resolved absolute path to data.

        Provides a consistent version of the path provided by the user
        which should work throughout regardless of operating system
        and of directory structure.
        """
        return Path(self._unsanitized_path).expanduser().absolute().resolve()

    @property
    def _sampled_data(self) -> pd.DataFrame:
        """Subset of data, as loaded by fast load."""
        if self._sampled_data_priv is None:
            self._fast_load_data(use_cache=False)
        # We can make this cast as the above `is None` check causes data to be loaded
        return cast(pd.DataFrame, self._sampled_data_priv)

    @_sampled_data.setter
    def _sampled_data(self, data: pd.DataFrame) -> None:
        """Setter for sampled data."""
        self._sampled_data_priv = data

    ####################
    # File Properties #
    ####################
    @overload
    def file_names_iter(self, as_strs: Literal[False] = False) -> Iterator[Path]: ...

    @overload
    def file_names_iter(self, as_strs: Literal[True]) -> Iterator[str]: ...

    def file_names_iter(
        self, as_strs: bool = False
    ) -> Union[Iterator[Path], Iterator[str]]:
        """Iterate over files in a directory, yielding those that match the criteria.

        Args:
            as_strs: By default the files yielded will be yielded as Path objects.
                If this is True, yield them as strings instead.
        """
        if not os.path.exists(self.path):
            logger.warning(
                "The specified path for the datasource was not found. "
                "No files can be loaded."
            )
            return

        # Counters/sets for logging details
        ignored_file_types: set[str] = set()
        num_ignored_files: int = 0
        num_skipped_files: int = 0
        num_found_files: int = 0

        # We need to be careful to avoid any method that _isn't_ a generator,
        # as otherwise this method will not benefit from actual iteration over the
        # files.
        #
        # Additionally, we want to avoid repeated `os.stat()` calls where possible,
        # as these provide overhead.
        for i, entry in enumerate(scantree(self.path.resolve())):
            # Stop iteration early if we have reached the maximum number of files to
            # consider
            if num_found_files >= MAX_NUMBER_OF_DATASOURCE_FILES:
                logger.warning(
                    f"Directory exceeds maximum number of files matching criteria;"
                    f" maximum is {MAX_NUMBER_OF_DATASOURCE_FILES},"
                    f" found {num_found_files}."
                    f" Further files will not be iterated over."
                )
                break

            # Log out some progress details. These are sampled using the
            # SampleFilter, so won't output every loop.
            logger.info(
                f"{num_skipped_files} skipped so far"
                f" (cause: filtering, disallowed type, processing error)",
                extra={"sample": True},
            )
            logger.info(
                f"{num_ignored_files} ignored so far"
                f" (cause: disallowed file types)",
                extra={"sample": True},
            )
            if self.strict and self.file_extension:
                logger.info(
                    f"{num_found_files} with explicit extensions {self.file_extension}"
                    f" and matching other file-system criteria found so far",
                    extra={"sample": True},
                )
            elif self.file_extension:  # and strict=False
                logger.info(
                    f"{num_found_files} files that match file types"
                    f" {self.file_extension} and other file-system criteria"
                    f" found so far",
                    extra={"sample": True},
                )
            else:
                logger.info(
                    f"{num_found_files} matching file-system criteria found so far",
                    extra={"sample": True},
                )
            logger.info(
                f"Checking file {i+1} against file-system criteria",
                extra={"sample": True},
            )

            try:
                # This is the fully resolved path of the entry
                path: Path = Path(entry.path)

                # Get the `os.stat()` details here so that we can avoid multiple calls.
                # We use entry.stat as this makes use of the potential caching
                # mechanisms of scandir().
                stat: os.stat_result = entry.stat()

                # Check the following things in order:
                # - is this a file?
                # - is this file already marked as skipped?
                # - is this an allowed type of file?
                # - does this file meet the date criteria?
                # - does this file meet the file size criteria?

                # - is this a file?
                if not is_file(entry, stat):
                    continue

                # - is this file already marked as skipped?
                if str(path) in self.skipped_files:
                    num_skipped_files += 1
                    continue

                # - is this an allowed type of file?
                if self.strict:
                    file_type = path.suffix
                else:
                    file_type = path.suffix or f".{guess_extension(path)}"
                if not self._filter_file_by_extension(
                    path, self.file_extension, file_type, strict=self.strict
                ):
                    self.skipped_files.add(str(path))
                    num_skipped_files += 1

                    # If guessing the extension failed the result is ".None",
                    # otherwise the exclusion reason must be that the file_type
                    # wasn't allowed
                    if file_type != ".None":
                        ignored_file_types.add(file_type)
                        num_ignored_files += 1

                    continue

                # - does this file meet the date criteria?
                if not self._filter_file_by_dates(path, stat):
                    self.skipped_files.add(str(path))
                    num_skipped_files += 1
                    continue

                # - does this file meet the file size criteria?
                if not self._filter_file_by_size(path, stat):
                    self.skipped_files.add(str(path))
                    num_skipped_files += 1
                    continue

                # Otherwise, has passed all filters
                num_found_files += 1
                if as_strs:
                    yield str(path)
                else:
                    yield path
            except Exception as e:
                logger.warning(
                    f"Error whilst iterating through filenames on {path}, skipping."
                    f" Error was: {e}"
                )
                self.skipped_files.add(str(path))
                num_skipped_files += 1

        # Do some final logging
        if self.strict and self.file_extension:
            logger.info(
                f"Found {num_found_files} files with the explicit extensions "
                f"{self.file_extension}."
            )
        elif self.file_extension:  # and strict=False
            logger.info(
                f"Found {num_found_files} files that match file types "
                f"{self.file_extension}."
            )
        else:
            logger.info(f"Found {num_found_files} files.")
        logger.info(f"Skipping {num_skipped_files} files.")
        if ignored_file_types:
            logger.info(
                f"Ignoring {num_ignored_files} files with file types "
                f"{ignored_file_types}."
            )

    @cached_property
    def _file_names(self) -> list[str]:
        """Returns a cached list of file names in the directory."""
        if not self.is_task_running:
            logger.warning(
                "A call was made to `.file_names` outside of a running task context:\n"
                + "".join(traceback.format_stack())
            )

        # TODO: [BIT-3721] This method should probably return a sorted list, to
        #       enable consistency in ordering.
        return list(self.file_names_iter(as_strs=True))

    @property
    def file_names(self) -> list[str]:
        """Returns a list of file names in the specified directory.

        This property accounts for files skipped at runtime by filtering them out of
        the list of cached file names. Files may get skipped at runtime due to errors
        or because they don't contain any image data and `images_only` is True. This
        allows us to skip these files again more quickly if they are still present in
        the directory.
        """
        # TODO: [BIT-3721] This method should probably return a sorted list, to
        #       enable consistency in ordering.
        file_names = [i for i in self._file_names if i not in self.skipped_files]
        self._perform_max_file_check(file_names)
        return file_names

    def clear_file_names_cache(self) -> None:
        """Clears the list of selected file names.

        This allows the datasource to pick up any new files that have been added to the
        directory since the last time it was cached.
        """
        # This is the specified way to clear the cache on a cached_property
        # https://docs.python.org/3/library/functools.html#functools.cached_property
        try:
            del self._file_names
        except AttributeError:
            # If the file_names property hasn't been accessed yet, it will raise an
            # AttributeError. We can safely ignore this.
            pass

    @property
    def selected_file_names(self) -> list[str]:
        """Returns a list of selected file names.

        Selected file names are affected by the
        `selected_file_names_override` and `new_file_names_only` attributes.
        """
        filenames = []
        try:
            if self.selected_file_names_override:
                filenames = self.selected_file_names_override
            elif len(self.data) > 0:
                filenames = list(self.data[ORIGINAL_FILENAME_METADATA_COLUMN])
        except (DataNotLoadedError, IterableDataSourceError):
            filenames = self.file_names

        # If self.new_file_names_only_set is set to None (default), we don't want
        # to apply any filter.
        # Otherwise, if empty set or a set that has at least one record,
        # filter filenames to match the new records only as set by the
        # worker.
        if self.new_file_names_only_set is not None:
            filenames = [
                filename
                for filename in filenames
                if filename in self.new_file_names_only_set
            ]
            logger.debug(f"Filtered {len(filenames)} files as new entries.")

        # TODO: [BIT-3721] This method should probably return a sorted list, to
        #       enable consistency in ordering.
        return filenames

    def _filter_file_by_extension(
        self,
        file: Union[str, os.PathLike],
        allowed_extensions: Optional[list[str]],
        file_type: Optional[str] = None,
        strict: bool = False,
    ) -> bool:
        """Return True if file matches extension/file type criteria, False otherwise.

        If allowed_extensions is provided, files will be matched against those,
        disallowed if their file types aren't in that set. If not provided, as long
        as a file type can be determined, it will be allowed.

        If strict is True, only explicit file extensions will be checked. Otherwise,
        if a file has no extension, the extension will be inferred based on file type.
        """
        file = Path(file)

        allowed_extensions_lower: Optional[set[str]]
        if allowed_extensions is not None:
            allowed_extensions_lower = {x.lower() for x in allowed_extensions}
        else:
            allowed_extensions_lower = None

        # Order: file extension, guessed extension
        if file_type is None:
            if strict:
                file_type = file.suffix
            else:
                file_type = file.suffix or f".{guess_extension(file)}"

        # If guessing the extension failed the result is ".None"
        if file_type == ".None":
            logger.warning(
                f"Could not determine file type of '{file.resolve()}'. Ignoring..."
            )
            return False
        # Otherwise, is it of the correct file type
        elif (
            allowed_extensions_lower is not None
            and file_type.lower() not in allowed_extensions_lower
        ):
            return False
        else:
            return True

    def _filter_file_by_dates(
        self, file: Union[str, os.PathLike], stat: Optional[os.stat_result] = None
    ) -> bool:
        """True iff file matches creation/modification date criteria."""
        try:
            file = Path(file)

            # We want to do this just once here, to avoid having to make multiple
            # `.stat()` calls later
            if stat is None:
                stat = os.stat(file)

            # Check creation date in range
            if self.file_creation_min_date or self.file_creation_max_date:
                file_creation_date = get_file_creation_date(file, stat)

                # Check if before min
                if (
                    self.file_creation_min_date
                    and file_creation_date < self.file_creation_min_date
                ):
                    return False

                # Check if after max
                if (
                    self.file_creation_max_date
                    and file_creation_date > self.file_creation_max_date
                ):
                    return False

            # Check modification date criteria
            if self.file_modification_min_date or self.file_modification_max_date:
                file_modification_date = get_file_last_modification_date(file, stat)

                # Check if before min
                if (
                    self.file_modification_min_date
                    and file_modification_date < self.file_modification_min_date
                ):
                    return False

                # Check if after max
                if (
                    self.file_modification_max_date
                    and file_modification_date > self.file_modification_max_date
                ):
                    return False

            # If we've gotten here, must match all of the above criteria
            return True
        except Exception as e:
            logger.warning(
                f"Could not determine creation/modification date of '{file}';"
                f" error was: {e}. Ignoring..."
            )
            return False

    def _filter_file_by_size(
        self, file: Union[str, os.PathLike], stat: Optional[os.stat_result] = None
    ) -> bool:
        """True iff file matches file size criteria."""
        try:
            file = Path(file)

            # We want to do this just once here, to avoid having to make multiple
            # `.stat()` calls later
            if stat is None:
                stat = os.stat(file)

            file_size = get_file_size(file, stat)

            # Check if too small
            if self.min_file_size and file_size < (
                self.min_file_size * NUM_BYTES_IN_A_MEGABYTE
            ):
                return False

            # Check if too large
            if self.max_file_size and file_size > (
                self.max_file_size * NUM_BYTES_IN_A_MEGABYTE
            ):
                return False

            # If we've gotten here, must match all of the above criteria
            return True
        except Exception as e:
            logger.warning(
                f"Could not determine size of '{file}'; error was: {e}. Ignoring..."
            )
            return False

    ##################
    # Data Retrieval #
    ##################

    def _apply_datasource_specific_filters_to_file(
        self, file_name: str
    ) -> Optional[str]:
        """Apply datasource specific filters to the file name.

        Args:
            file_name: The name of the file we need to check the filters against.

        Returns:
            The file_name if the file matches all filters or None otherwise.
        """
        file_list = [file_name]
        for filter_func in self._datasource_filters_to_apply:
            file_list = filter_func(file_list)
            if len(file_list) == 0:
                return None
        return file_list[0]

    def _fast_load_data(self, **kwargs: Any) -> None:
        """Load the data in fast mode.

        Loads a small random subset of the data to speed up the process of schema
        generation. The number of files loaded is determined by the number of files
        in the directory and the variability of the data. The more unique fields that
        get discovered with each file, the more files will be loaded.

        This data sample is saved onto the `_sampled_data` attribute of the class.

        Args:
            **kwargs: Kwargs to be passed through to the `_get_data()` call.
        """
        # This method is done iteratively now; rather than constructing a list and
        # then going over it in a for-loop, we directly iterate over an iterator
        # until we hit the desired criteria.
        dfs: list[pd.DataFrame] = []

        # Iterate through the filesystem-filtered files
        for fast_load_idx, file_candidate in enumerate(
            self.file_names_iter(as_strs=True), start=1
        ):
            logger.debug(f"fast_load: Considering file {fast_load_idx}")

            # We aim to only load FAST_LOAD_MINIMUM_NUMBER_OF_FILES_TO_LOAD files,
            # so we need to break out if we've got what we need
            if len(dfs) >= FAST_LOAD_MAXIMUM_NUMBER_OF_FILES_TO_LOAD:
                logger.debug(
                    f"Found {len(dfs)} entries in fast_load; leaving fast_load"
                )
                break

            # Check if the candidate matches the datasource filters as well
            file = self._apply_datasource_specific_filters_to_file(file_candidate)
            if file is None:
                logger.info(
                    f"File {file_candidate} filtered due to datasource filters;"
                    f" {fast_load_idx} files considered for fast_load so far"
                )
                continue

            # We now need to actually see if we can read it/if it contains a sample
            # usable for the fast_load data
            df = self._get_data(file_names=[file], skip_non_tabular_data=True, **kwargs)
            if not df.empty:
                dfs.append(df)
                logger.debug(f"{len(dfs)} entries found in fast_load sampling")
        else:  # runs if reach end of for-loop
            if len(dfs) > 0:
                logger.warning(
                    f"Reached end of file iterator during fast_load sampling;"
                    f" only found {len(dfs)} entries"
                )
            else:
                logger.error(
                    "No files compatible with the selected datasource found"
                    " during fast_load sampling."
                    " Tasks will not run on this datasource."
                )

        self._sampled_data = (
            pd.concat(dfs, axis=0, ignore_index=True) if dfs else pd.DataFrame()
        )

    @abstractmethod
    def _get_data(
        self,
        file_names: list[str],
        use_cache: bool = True,
        skip_non_tabular_data: bool = False,
        **kwargs: Any,
    ) -> pd.DataFrame:
        """Implement to return data corresponding to the provided file names.

        This method is called under the hood by `get_data` and `yield_data`. This
        method must return a dataframe with the columns `_original_filename` and
        `_last_modified` containing the original file name of each row, and the
        timestamp when the file was last modified in ISO 8601 format, respectively.

        Args:
            file_names: list of file names to load.
            use_cache: Whether the cache should be used to retrieve data for these
                files. Note that cached data may have some elements, particularly
                image-related fields such as image data or file paths, replaced
                with placeholder values when stored in the cache. If data_cache is
                set on the instance, data will be _set_ in the cache, regardless of
                this argument.
            skip_non_tabular_data: Whether we can avoid loading non-tabular data,
                e.g. image data (can be set to True when generating schemas).
            **kwargs: Additional keyword arguments.

        Returns:
            A dataframe containing the data.
        """
        raise NotImplementedError

    def yield_data(
        self,
        file_names: Optional[list[str]] = None,
        use_cache: bool = True,
        partition_size: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterator[pd.DataFrame]:
        """Yields data in batches from files that match the given file names.

        Args:
            file_names: An optional list of file names to use for yielding data.
                Otherwise, all files that have already been found will be used.
                `file_names` is always provided when this method is called from the
                Dataset as part of a task.
            use_cache: Whether the cache should be used to retrieve data for these
                files. Note that cached data may have some elements, particularly
                image-related fields such as image data or file paths, replaced
                with placeholder values when stored in the cache. If data_cache is
                set on the instance, data will be _set_ in the cache, regardless of
                this argument.
            partition_size: The number of file names to load in each iteration.
            **kwargs: Additional keyword arguments.

        Raises:
            ValueError: If no file names provided and no files have been found.
        """

        # With the file_names_iter approach, we can no longer have direct calls
        # to self.file_names
        if self.fast_load and not self.is_task_running:
            yield self._sampled_data
            return
        # If any matching files are found, we self.sampled_data should not be empty,
        # so we can check if there are matching datasource files based on it.
        if not file_names and self._sampled_data.empty:
            logger.warning("No files found to yield data from.")
            # if there are no files, log a warning, and yield an empty dataframe
            yield pd.DataFrame()
            return

        # We should only reach this point if there are files to load and only
        # in a task running context, so we can load the data.

        file_names_: list[str] = file_names or self.file_names
        partition_size_: int = partition_size or self.partition_size

        # if file_names is provided, then we load files from that list
        for idx, file_names_partition in enumerate(
            self.partition(file_names_, partition_size_)
        ):
            file_names_partition = cast(list[str], file_names_partition)
            logger.debug(f"Yielding partition {idx} from {self}")
            if self.use_file_multiprocessing(file_names_partition):
                yield self._mp_get_data(
                    file_names=file_names_partition, use_cache=use_cache, **kwargs
                )
            else:
                yield self._get_data(
                    file_names=file_names_partition, use_cache=use_cache, **kwargs
                )
                file_num = idx * partition_size_ + len(file_names_partition)
                for hook in get_hooks(HookType.POD):
                    hook.on_file_process_end(
                        self,
                        file_num=file_num,
                        total_num_files=len(file_names_),
                    )

    def partition(self, iterable: Sequence, partition_size: int = 1) -> Iterable:
        """Takes an iterable and yields partitions of size `partition_size`.

        The final partition may be less than size `partition_size` due to the variable
        length of the iterable.
        """
        for hook in get_hooks(HookType.POD):
            # Signal files partition
            hook.on_files_partition(
                self, total_num_files=len(iterable), batch_size=partition_size
            )

        len_ = len(iterable)
        for partition_start_idx in range(0, len_, partition_size):
            yield iterable[
                partition_start_idx : min(partition_start_idx + partition_size, len_)
            ]

    ########################
    # Dataframe Processing #
    ########################
    def get_column_names(self, **kwargs: Any) -> Iterable[str]:
        """Get column names for fast-load datasource."""
        return list(self._sampled_data.columns)

    def get_column(self, col_name: str, **kwargs: Any) -> Union[np.ndarray, pd.Series]:
        """Loads and returns single column from the dataset.

        Args:
            col_name: The name of the column which should be loaded.
            **kwargs: Additional keyword arguments to pass to the `load_data` method
                if the data is stale.

        Returns:
            The column request as a series.
        """
        if self.fast_load and not self.is_task_running:
            return self._get_column_fast_load(col_name, **kwargs)
        else:
            return super().get_column(col_name, **kwargs)

    def _get_column_fast_load(self, col_name: str, **kwargs: Any) -> _Column:
        """Get column for fast-load datasource."""
        return self._sampled_data[col_name]

    @methodtools.lru_cache(maxsize=1)
    def get_dtypes(self, **kwargs: Any) -> _Dtypes:
        """Loads and returns the column names and types of the dataframe.

        Args:
            **kwargs: Additional keyword arguments to pass to the `load_data` method
                if the data is stale.

        Returns:
            A mapping from column names to column types.
        """
        return self._get_data_dtypes(self._sampled_data)

    def get_values(
        self, col_names: list[str], **kwargs: Any
    ) -> dict[str, Iterable[Any]]:
        """Get distinct values from columns in the dataset.

        Args:
            col_names: The list of the columns whose distinct values should be
                returned.
            **kwargs: Additional keyword arguments to pass to the `load_data` method
                if the data is stale.

        Returns:
            The distinct values of the requested column as a mapping from col name to
            a series of distinct values.
        """
        if not self.is_task_running:
            return self._get_values_fast_load(col_names, **kwargs)
        else:
            return super().get_values(col_names, **kwargs)

    def _get_values_fast_load(
        self, col_names: list[str], **kwargs: Any
    ) -> dict[str, Iterable[Any]]:
        """Get column values for fast-load datasource."""
        return self._get_values_from_dataframe(self._sampled_data, col_names, **kwargs)

    @staticmethod
    def _get_values_from_dataframe(
        data: pd.DataFrame, col_names: list[str], **kwargs: Any
    ) -> dict[str, Iterable[Any]]:
        """Helper method to get values from a dataframe.

        Handles non-hashable elements.
        """
        dic: dict[str, Iterable[Any]] = {}
        for col in col_names:
            try:
                dic[col] = data[col].unique()
            except TypeError:
                logger.warning(f"Found unhashable value type, skipping column {col}.")
            except KeyError:
                logger.warning(f"Column {col} not found in the dataframe.")
        return dic

    def __len__(self) -> int:
        return len(self.selected_file_names)


@delegates()
class FileSystemIterableSourceInferrable(FileSystemIterableSource, ABC):
    """Abstract base source that supports iterating over file-based data.

    This is used for Iterable data sources that whose data is stored as files on disk.

    Args:
        path: Path to the directory which contains the data files. Subdirectories
            will be searched recursively.
        data_cache: A DataPersister instance to use for data caching.
        infer_class_labels_from_filepaths: Whether class labels should be
            added to the data based on the filepath of the files.
            Defaults to the first directory within `self.path`,
            but can go a level deeper if the datasplitter is provided
            with `infer_data_split_labels` set to true
    """

    _first_directory_in_path: Final[str] = "_first_directory"
    _second_directory_in_path: Final[str] = "_second_directory"
    _unused_directory_in_path: Final[str] = "_unused_path_segment"

    def __init__(
        self,
        path: Union[os.PathLike, str],
        data_cache: Optional[DataPersister] = None,
        infer_class_labels_from_filepaths: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(path=path, **kwargs)
        self.data_cache = data_cache
        self.infer_class_labels_from_filepaths = infer_class_labels_from_filepaths
        self.infer_data_split_column_name: Union[str, Literal[False]]
        if (
            isinstance(self.data_splitter, SplitterDefinedInData)
            and self.data_splitter.infer_data_split_labels
        ):
            # The folder structure may provide labels for the data split (i.e. train,
            # test, validation), the class labels for the data, or both.
            self.infer_data_split_column_name = self.data_splitter.column_name
            # We extract the split labels from the data splitter for
            # SplitterDefinedInData
            self.datasplitter_labels = [
                self.data_splitter.training_set_label,
                self.data_splitter.validation_set_label,
                self.data_splitter.test_set_label,
            ]
        else:
            self.infer_data_split_column_name = False
            self.datasplitter_labels = []

    def _get_data(
        self,
        file_names: list[str],
        use_cache: bool = True,
        skip_non_tabular_data: bool = False,
        **kwargs: Any,
    ) -> pd.DataFrame:
        """Returns data corresponding to the provided file names.

        Args:
            file_names: list of file names to load.
            use_cache: Whether the cache should be used to retrieve data for these
                files. Note that cached data may have some elements, particularly
                image-related fields such as image data or file paths, replaced
                with placeholder values when stored in the cache.
                If data_cache is set on the instance, data will be _set_ in the
                cache, regardless of this argument.
            skip_non_tabular_data: Whether we can avoid loading non-tabular data,
                e.g. image data (can be set to True when generating schemas).
            **kwargs: Additional keyword arguments to pass to the `_process_file`
                method.

        Returns:
            A dataframe containing the data.
        """
        bulk_cached_data: Optional[pd.DataFrame] = None
        num_files_loaded_from_cache: int = 0
        file_names_to_be_processsed = file_names

        if self.data_cache and use_cache:
            cache_results = self.data_cache.bulk_get(list(file_names))
            # Data stored in the cache will already be in the form that is output
            # post-`_process_dataset()` so we can simply skip processing and append
            # it to a separate list (to be joined after all processing is done)
            bulk_cached_data = cache_results.data
            file_names_to_be_processsed = [str(f) for f in cache_results.misses]
            files_loaded_from_cache = set()
            if cache_results.hits is not None:
                files_loaded_from_cache = set(cache_results.hits.to_list())
            num_files_loaded_from_cache = len(files_loaded_from_cache)
            logger.info(
                "Retrieved cached data for "
                f"{num_files_loaded_from_cache} files: {files_loaded_from_cache}"
            )

        processed_data_list: list[dict[str, Any]] = []
        num_files_loaded: int = 0
        for filename in file_names_to_be_processsed:
            # If data was not in the cache (or was invalid) we will need to process
            # the file
            logger.info(f"Processing file {filename}...")
            processed_data = self._process_file(
                filename,
                skip_non_tabular_data=skip_non_tabular_data,
                **kwargs,
            )

            if processed_data:
                num_files_loaded += 1
                # File has not been skipped and is not empty,
                # so we can add some metadata
                # columns and append it to the list of data points.
                for row in processed_data:
                    processed_data_with_metadata = self._add_metadata_to_data(
                        row, filename
                    )
                    processed_data_list.append(processed_data_with_metadata)

        # Log out details about the number of files loaded/from where
        num_files_expected = len(file_names)
        total_files_loaded = num_files_loaded + num_files_loaded_from_cache
        if num_files_expected == 1:
            if total_files_loaded == 0:
                logger.warning("File could not be loaded.")
        elif num_files_expected > 1:
            if total_files_loaded == 0:
                logger.warning("No files could be loaded.")
            # We don't want to log when we're just loading a single file because this is
            # not a meaningful log message as sometimes we iterate through all the files
            # one by one calling this method.
            if total_files_loaded > 1:
                if total_files_loaded < num_files_expected:
                    logger.warning(
                        f"{total_files_loaded} files loaded successfully out of"
                        f" {num_files_expected} files."
                    )
                else:
                    logger.info(f"{total_files_loaded} files loaded successfully.")

                logger.info(
                    f"{num_files_loaded} file(s) freshly processed,"
                    f" {num_files_loaded_from_cache} file(s) loaded from cache."
                )

        # Create the (processed items) dataframe
        # Note: if everything was loaded from cache this could be empty
        df = pd.DataFrame.from_records(processed_data_list)

        # Add metadata columns if they were not added (e.g. if no files where
        # processed).
        # This is because we want to ensure that the metadata columns are always
        # present in the dataframe as they are relied upon downstream even if
        # they are empty.
        # If df is empty, this doesn't invalidate that, it simply adds columns to
        # the metadata.
        for col in FILE_SYSTEM_ITERABLE_METADATA_COLUMNS:
            if col not in df.columns:
                df[col] = None

        if not df.empty:
            # Perform any subclass defined processing of the dataframe
            df = self._process_dataset(df, **kwargs)

            # Infer the data split and class labels if necessary
            df = self._infer_data_split_and_class_labels(df, **kwargs)

            # Save any new processed data to the cache
            if self.data_cache:
                # We need to avoid caching anything that cannot/should not be placed
                # in the cache, such as image data or image filepaths that won't be
                # relevant after this pass
                try:
                    cacheable_df = self.data_cache.prep_data_for_caching(
                        df, image_cols=self.image_columns
                    )
                    self.data_cache.bulk_set(cacheable_df)
                except Exception as e:
                    logger.warning(
                        f"Error whilst attempting to bulk set new cache entries: {e}"
                    )

        # Combine newly processed data with the data retrieved from the cache (which
        # was already in the format needed post-`_process_dataset()`)
        if bulk_cached_data is not None:
            df = pd.concat(
                [df, bulk_cached_data], axis="index", join="outer", ignore_index=True
            )

        return df

    def _infer_data_split_and_class_labels(
        self, df: pd.DataFrame, **kwargs: Any
    ) -> pd.DataFrame:
        """Infers the data split and class labels from the file paths.

        Args:
            df: The dataframe to infer the data split and class labels for.
            **kwargs: Additional keyword arguments to pass to the `load_data` method
                if the data is stale.

        Returns:
            The dataframe with the data split and class labels inferred.
        """
        # We now can infer the various labels of the data from the folder structure
        # if needed.

        unique_first_directory_column_values: list[str] = []
        unique_second_directory_column_values: list[str] = []

        if self.infer_class_labels_from_filepaths or self.infer_data_split_column_name:
            # We need to extract unique values from the first and second directories
            # so we can differentiate between the data split and the class label
            # directories.
            first_directory_col_in_df: bool = (
                self._first_directory_in_path in df.columns
            )

            if first_directory_col_in_df:
                unique_first_directory_column_values = (
                    df[self._first_directory_in_path].unique().tolist()
                )

            second_directory_col_in_df: bool = (
                self._second_directory_in_path in df.columns
            )

            if second_directory_col_in_df:
                unique_second_directory_column_values = (
                    df[self._second_directory_in_path].unique().tolist()
                )

            inferred_class_label_column_name: str = (
                BITFOUNT_INFERRED_LABEL_COLUMN
                if self.infer_class_labels_from_filepaths
                else self._unused_directory_in_path
            )

            if self.infer_data_split_column_name:
                # infer_data_split_column_name will *only* be
                # truthy for SplitterDefinedInData
                self.data_splitter = cast(SplitterDefinedInData, self.data_splitter)

                datasplitter_labels: list[str] = [
                    label.lower() for label in self.datasplitter_labels
                ]

                # We then identify which column is the data split labels. We then
                # mark the other column as the inferred class labels.
                if unique_first_directory_column_values and set(
                    i.lower() for i in unique_first_directory_column_values
                ).issubset(datasplitter_labels):
                    logger.info(
                        f"`{self._first_directory_in_path}` column contains"
                        f" data split labels."
                        " Inferring class labels from second directory."
                    )

                    df = df.rename(
                        columns={
                            self._first_directory_in_path: self.infer_data_split_column_name,  # noqa: E501
                            self._second_directory_in_path: inferred_class_label_column_name,  # noqa: E501
                        },
                        # "ignore" as we may not have the second directory/class labels
                        errors="ignore",
                    )
                elif unique_second_directory_column_values and set(
                    i.lower() for i in unique_second_directory_column_values
                ).issubset(datasplitter_labels):
                    logger.info(
                        f"`{self._second_directory_in_path}` column contains"
                        f" data split labels."
                        " Inferring class labels from first directory."
                    )

                    df = df.rename(
                        columns={
                            self._first_directory_in_path: inferred_class_label_column_name,  # noqa: E501
                            self._second_directory_in_path: self.infer_data_split_column_name,  # noqa: E501
                        },
                        # "raise" as if we have the second directory we _must_ have
                        # the first
                        errors="raise",
                    )
                else:
                    # If we reach here, either the appropriate columns aren't in
                    # the dataframe or the columns don't contain the expected values.
                    #
                    # Either way, we cannot proceed with the requested label inference.
                    datasplitter_labels_str: str = ", ".join(datasplitter_labels)

                    logger.debug(
                        f"Neither directory column seemed to contain"
                        f" datasplitter labels ({datasplitter_labels_str}):"
                        f" {first_directory_col_in_df=},"
                        f" {unique_first_directory_column_values=},"
                        f" {second_directory_col_in_df=},"
                        f" {unique_second_directory_column_values=}"
                    )
                    raise ValueError(
                        f"Neither the '{self._first_directory_in_path}' column"
                        f" nor the '{self._second_directory_in_path}' column"
                        f" seem to contain only datasplit labels"
                        f" ({datasplitter_labels_str}),"
                        f" or are not present;"
                        f" unable to infer datasplits."
                    )

                # Finally, we convert the datasplitter labels (i.e. train, test,
                # validation) to match the case expected by the datasplitter.
                #
                # This is needed as we perform a case-insensitive matching above
                # (see the `.lower()` usages), but the datasplitter is very much
                # case-sensitive.
                #
                # We convert all the labels to lowercase, then replace them with
                # the actual version of the label.
                df[self.infer_data_split_column_name] = df[
                    self.infer_data_split_column_name
                ].str.lower()
                df[self.infer_data_split_column_name].replace(
                    {label.lower(): label for label in self.datasplitter_labels},
                    inplace=True,
                )
            else:  # self.infer_class_labels_from_filepaths is True
                # We only need the class labels
                df = df.rename(
                    columns={
                        self._first_directory_in_path: inferred_class_label_column_name,
                    },
                    # We use raise here as there's _only_ the one column we care
                    # about so it _needs_ to be present
                    errors="raise",
                )

        # Drop any intermediate columns that aren't needed
        df = df.drop(
            columns=[
                self._first_directory_in_path,
                self._second_directory_in_path,
                self._unused_directory_in_path,
            ],
            errors="ignore",
        )
        return df

    @abstractmethod
    def _process_file(
        self,
        filename: str,
        skip_non_tabular_data: bool = False,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Implement to process a single file.

        Files may contain more than one datapoint, so this function can return a list
        of dictionaries.

        Args:
            filename: The name of the file to process.
            skip_non_tabular_data: Whether we can avoid loading non-tabular data,
                e.g. image data (can be set to True when generating schemas).
            **kwargs: Additional keyword arguments.

        """
        raise NotImplementedError

    @abstractmethod
    def _process_dataset(self, dataframe: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
        """This method can be overridden to perform any processing of the dataset."""
        raise NotImplementedError

    def _add_metadata_to_data(
        self, data: dict[str, Any], filename: str
    ) -> dict[str, Any]:
        """Adds metadata to the data.

        Args:
            data: The data to add metadata to.
            filename: The filename of the file to be processed.

        Returns:
            The data with metadata added.
        """
        data[ORIGINAL_FILENAME_METADATA_COLUMN] = filename
        modify_time = os.path.getmtime(filename)
        data[LAST_MODIFIED_METADATA_COLUMN] = datetime.fromtimestamp(
            modify_time
        ).isoformat()
        # Track the first two directory levels so that we can easily
        # process the possible labels later on as needed
        relative_filepath = Path(filename).relative_to(self.path).parts
        if len(relative_filepath) > 1:
            data[self._first_directory_in_path] = relative_filepath[0]
        if len(relative_filepath) > 2:
            data[self._second_directory_in_path] = relative_filepath[1]

        return data
