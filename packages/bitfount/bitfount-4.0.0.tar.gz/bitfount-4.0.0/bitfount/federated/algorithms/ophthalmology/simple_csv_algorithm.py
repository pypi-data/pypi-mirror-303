"""Algorithms and related functionality for simply outputting data to CSV."""

from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Optional, Union

from marshmallow import fields
import pandas as pd

import bitfount.config
from bitfount.data.datasources.base_source import BaseSource, FileSystemIterableSource
from bitfount.federated.algorithms.base import (
    BaseAlgorithmFactory,
    BaseWorkerAlgorithm,
    NoResultsModellerAlgorithm,
)
from bitfount.federated.logging import _get_federated_logger
from bitfount.types import T_FIELDS_DICT
from bitfount.utils.pandas_utils import append_dataframe_to_csv

if TYPE_CHECKING:
    from bitfount.federated.privacy.differential import DPPodConfig


_logger = _get_federated_logger("bitfount.federated")


class _WorkerSide(BaseWorkerAlgorithm):
    """Worker side of the algorithm."""

    def __init__(self, save_path: Optional[Path] = None, **kwargs: Any) -> None:
        """Create a new worker side of the algorithm.

        Args:
            save_path: Optional. The path to output the CSV to from the worker.
            **kwargs: Passed to parent.
        """
        super().__init__(**kwargs)
        self.save_path = save_path

    def initialise(
        self,
        datasource: BaseSource,
        pod_dp: Optional[DPPodConfig] = None,
        pod_identifier: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Sets Datasource."""
        self.initialise_data(datasource=datasource)

    def run(
        self,
        df: Optional[pd.DataFrame] = None,
        task_id: Optional[str] = None,
    ) -> None:
        """Output the dataframe to CSV."""
        if (df is None) and (self.save_path is not None):
            _logger.warning(
                f"_SimpleCSVAlgorithm ({self.__class__.__name__})"
                f' specified save path "{str(self.save_path)}",'
                f" but was not passed a dataframe"
            )
        elif (df is not None) and (self.save_path is None):
            _logger.warning(
                f"_SimpleCSVAlgorithm ({self.__class__.__name__})"
                " was passed a dataframe but had no save path specified"
            )
        elif df is not None and self.save_path:
            if (
                isinstance(self.datasource, FileSystemIterableSource)
                and self.datasource.cache_images is False
            ):
                img_columns = list(self.datasource.image_columns)
                # Find the intersection of image_cols and data.columns
                existing_img_columns = list(set(img_columns) & set(df.columns))
                missing_img_columns = set(img_columns) - set(df.columns)

                if missing_img_columns:
                    _logger.warning(
                        f"DataFrame has {len(existing_img_columns)} out of"
                        f" {len(img_columns)} image columns."
                        f"Missing {len(missing_img_columns)} image columns."
                    )
                    _logger.debug(
                        "The following image columns are missing from"
                        f" the DataFrame: {missing_img_columns}"
                    )

                # Add True/None to indicate the number of frame based
                # on the pixel data columns if images are not cached.
                if existing_img_columns:
                    img_df = df[existing_img_columns]
                    # Replace non-NA elements with True
                    img_df = img_df.mask(img_df.notna(), other=True)
                    # Replace NA elements with False
                    img_df = img_df.mask(img_df.isna(), other=None)
                    df[existing_img_columns] = img_df

            # Get the path to the CSV file.
            if task_id is not None:
                Path(self.save_path / f"{task_id}").mkdir(parents=True, exist_ok=True)
                csv_path = self.save_path / f"{task_id}" / "results.csv"
            else:
                Path(self.save_path).mkdir(parents=True, exist_ok=True)
                csv_path = self.save_path / "results.csv"
            _logger.info(f"Saving dataframe to CSV at {csv_path}")

            # Write the dataframe to CSV, handling appending to existing CSV
            csv_path = append_dataframe_to_csv(csv_path, df)
            _logger.info(f"CSV output to {csv_path}")
        else:
            _logger.debug(
                "Neither dataframe or save path were specified"
                f" for _SimpleCSVAlgorithm ({self.__class__.__name__})."
                " Ignoring..."
            )


class _SimpleCSVAlgorithm(BaseAlgorithmFactory):
    """Algorithm that allows simple outputting of dataframes to CSV.

    Allows the data to be saved to CSV from either the worker or the modeller (or both).
    """

    fields_dict: ClassVar[T_FIELDS_DICT] = {
        "save_path": fields.Str(allow_none=True),
    }

    def __init__(
        self,
        save_path: Optional[Union[str, os.PathLike]] = None,
        **kwargs: Any,
    ) -> None:
        """Create a new _SimpleCSVAlgorithm.

        Args:
            save_path: Optional. The path to save the CSV to from the worker.
            **kwargs: Passed to parent.
        """
        super().__init__(**kwargs)
        if save_path is None:
            self.save_path = bitfount.config.BITFOUNT_OUTPUT_DIR
        else:
            self.save_path = Path(save_path)

        # Sanity check if nothing was supplied
        if not self.save_path:
            _logger.warning(
                f"Worker save path was not specified"
                f" for {self.__class__.__name__}, so nothing will be saved out."
                f" Was this intentional?"
            )

    def modeller(self, **kwargs: Any) -> NoResultsModellerAlgorithm:
        """Modeller-side of the algorithm."""
        return NoResultsModellerAlgorithm(
            log_message="Running Simple CSV Algorithm",
            **kwargs,
        )

    def worker(self, **kwargs: Any) -> _WorkerSide:
        """Worker-side of the algorithm."""
        return _WorkerSide(
            self.save_path,
            **kwargs,
        )
