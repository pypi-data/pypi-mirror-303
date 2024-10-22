"""Module containing DICOMOphthalmologySource class.

DICOMOphthalmologySource class handles loading of ophthalmological DICOM data.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from functools import cached_property
from hashlib import md5
import logging
import math
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Optional, TypedDict, Union, cast
import uuid

import numpy as np
import pandas as pd
import pydicom
from pydicom import DataElement, Dataset
from pydicom.encaps import encapsulate, encapsulate_extended, generate_pixel_data_frame
from pydicom.uid import JPEG2000Lossless
from pydicom.valuerep import VR

from bitfount.config import LOG_DICOM_FIXES
from bitfount.data.datasources.dicom_source import (
    DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE,
    DICOM_LATERALITY_POSSIBLE_FIELDS,
    DICOM_LEFT_RIGHT_LATERALITY,
    DICOM_PATIENT_DOB_ATTRIBUTE,
    DICOM_PATIENT_NAME_ATTRIBUTE,
    DICOM_SCAN_LATERALITY_ATTRIBUTE,
    DICOMSource,
    _DICOMSequenceField,
)
from bitfount.data.datasources.ophthalmology.ophth_ds_types import (
    DICOMImage,
    FunctionalGroupsSequenceField,
    FunctionalGroupsSequenceProcessingOutput,
    OphthalmologyModalityType,
    ProcessedDICOMImage,
    _AcquisitionDeviceTypeCodeSequenceField,
)
from bitfount.data.datasources.ophthalmology.ophth_ds_utils import (
    SLO_ORIGINAL_FILENAME_METADATA_COLUMN,
    make_path_absolute,
)
from bitfount.data.datasources.ophthalmology.ophthalmology_base_source import (
    ACQUISITION_DEVICE_TYPE_MODALITY_MAPPING,
    OCT_ACQUISITION_DEVICE_TYPE,
    OPHTHALMOLOGY_MODALITIES,
    SLO_IMAGE_ATTRIBUTE,
    _OphthalmologySource,
)
from bitfount.data.exceptions import DataSourceError
from bitfount.data.persistence.base import BulkResult
from bitfount.exceptions import BitfountError
from bitfount.utils import delegates

if TYPE_CHECKING:
    from typing_extensions import NotRequired

logger = logging.getLogger(__name__)


class MissingDICOMFieldError(BitfountError):
    """Error for DICOMSources.

    We raise this if an expected DICOM field is missing.
    """

    pass


@dataclass
class DICOMOphthalmologyCSVColumns:
    """Arguments for ophthalmology columns in the csv.

    Args:
        oct_column: The column pointing to OCT files in the filename. Refers to Optical
            Coherence Tomography (OCT), typically these are a series of 2D images used
            to show a cross-section of the tissue layers in the retina (specifically
            the macula), combined to form a 3D image. Defaults to 'oct'.
        slo_column: The string pointing to SLO files in the filename. Refers to Scanning
            Laser Ophthalmoscope (SLO), typically referred to as an 'en-face' image of
            the retina (specifically the macula). Defaults to None.
    """

    oct_column: Optional[str] = "oct"
    slo_column: Optional[str] = None

    def __post_init__(self) -> None:
        """Post-init method to validate the dataclass."""
        if not any((self.oct_column, self.slo_column)):
            raise DataSourceError(
                "At least one of 'oct_column' or 'slo_column' must be provided."
            )


class _DICOMOphthalmologyCSVColumnsTD(TypedDict):
    """Typed dict form of DICOMOphthalmologyCSVColumns dataclass."""

    oct_column: NotRequired[Optional[str]]
    slo_column: NotRequired[Optional[str]]


@delegates()
class DICOMOphthalmologySource(DICOMSource, _OphthalmologySource):
    """Data source for loading DICOM ophthalmology files.

    Args:
        path: The path to the directory containing the DICOM files or to a CSV
            containing paths to the DICOM files.
        dicom_ophthalmology_csv_columns: Which columns in the CSV, if using a CSV,
            relate to the OCT/SLO files.
        **kwargs: Keyword arguments passed to the parent base classes.
    """

    def __init__(
        self,
        path: Union[os.PathLike, str],
        dicom_ophthalmology_csv_columns: Optional[
            Union[DICOMOphthalmologyCSVColumns, _DICOMOphthalmologyCSVColumnsTD]
        ] = None,
        **kwargs: Any,
    ) -> None:
        # If a csv file has been provided, we load the files named in the csv file.
        # The file names, if relative, are assumed relative to the _CSV_. To enable
        # this, we then set path to path.parent.
        self.csv_df: Optional[pd.DataFrame] = None
        if Path(path).suffix == ".csv":
            csv_path = Path(path).resolve()  # ensures absolute path
            self.csv_df = pd.read_csv(csv_path)
            path = csv_path.parent

        super().__init__(path=path, **kwargs)

        # Parse the ophthalmology CSV columns, converting from the dict-form to
        # dataclass-form if needed
        if self.csv_df is None and dicom_ophthalmology_csv_columns:
            logger.warning(
                "CSV columns provided but no CSV file found. "
                "Ignoring `dicom_ophthalmology_csv_columns`."
            )
        self.dicom_ophthalmology_csv_columns: Optional[DICOMOphthalmologyCSVColumns] = (
            None
        )
        if self.csv_df is not None:
            if dicom_ophthalmology_csv_columns:
                if isinstance(
                    dicom_ophthalmology_csv_columns, DICOMOphthalmologyCSVColumns
                ):
                    self.dicom_ophthalmology_csv_columns = (
                        dicom_ophthalmology_csv_columns
                    )
                else:
                    self.dicom_ophthalmology_csv_columns = DICOMOphthalmologyCSVColumns(
                        **dicom_ophthalmology_csv_columns
                    )
            else:
                logger.info(
                    "No CSV columns provided, using "
                    "default values from `OphthalmologyCSVColumns`."
                )
                self.dicom_ophthalmology_csv_columns = DICOMOphthalmologyCSVColumns()

        # Now that dicom_ophthalmology_csv_columns has been set, we can check the
        # csv file for any issues.
        if self.csv_df is not None and self.dicom_ophthalmology_csv_columns:
            # Ensure the columns are found in the csv
            self._ensure_csv_columns_exist()
            # Ensure the file_names in the csv are unique
            self._ensure_csv_file_names_are_unique()
            # Ensure the csv file names match the specified modalities
            self._ensure_csv_columns_match_modality()
            # Ensure the modality is specified if using CSV
            self._ensure_csv_modality_specified()

        # Create hash table for OCT-SLO matching
        # The hash table is a dictionary where the key is the hash of the name, date of
        # birth, and laterality of the patient and the value is a list of tuples
        # containing the file name, modality, and acquisition datetime.
        self.__hash_table: dict[
            str, set[tuple[str, OphthalmologyModalityType, datetime]]
        ] = {}

        # Cache containing a mapping of file names to date of birth. This is only
        # used if date of birth filtering is enabled. Furthermore, if the datasource
        # cache is enabled, then this cache is only used temporarily until the data is
        # stored in the datasource cache at which point the corresponding entry is
        # deleted from this cache.
        self.__dob_cache: dict[str, str] = {}
        if self.modality is not None:
            self._datasource_filters_to_apply.append(self._filter_files_by_modality)

    ###########################################################
    # Public Properties
    ###########################################################

    @property
    def modality(self) -> OphthalmologyModalityType:
        """Returns the modality of the data source."""
        return self.ophthalmology_args.modality

    @property
    def match_slo(self) -> bool:
        """Returns whether the SLO files should be matched to the OCT files."""
        return self.ophthalmology_args.match_slo

    @property
    def drop_row_on_missing_slo(self) -> bool:
        """Returns whether to drop the OCT row if the corresponding SLO file is missing.

        This is only relevant if `match_slo` is True.
        """
        return self.ophthalmology_args.drop_row_on_missing_slo

    @property
    def file_names(self) -> list[str]:
        """Returns a list of file names in the directory.

        These file paths will be absolute paths, regardless of their origin.
        """
        file_names = [
            i
            for i in self._num_bscan_filtered_file_names
            if i not in self.skipped_files
        ]
        self._perform_max_file_check(file_names)
        return file_names

    @property
    def slo_file_names(self) -> list[str]:
        """Returns a list of SLO file names in the directory.

        These file paths will be absolute paths, regardless of their origin.
        """
        return [i for i in self._slo_file_names if i not in self.skipped_files]

    ###########################################################
    # Public Methods
    ###########################################################

    def process_sequence_field(
        self, elem: _DICOMSequenceField
    ) -> Optional[dict[str, Any]]:
        """Process 'Shared Functional Groups Sequence' sequence field.

        This sequence field contains the slice thickness and pixel spacing
        data. Other fields are ignored.

        Args:
            elem: The DICOM data element.

        Returns:
            A dictionary containing the processed sequence data or None.
        """
        if elem.name in (
            "Shared Functional Groups Sequence",
            "Per-frame Functional Groups Sequence",
        ):
            try:
                functional_groups_sequence = cast(FunctionalGroupsSequenceField, elem)
                return cast(
                    dict[str, Any],
                    self._get_slice_thickness_and_pixel_spacing(
                        functional_groups_sequence
                    ),
                )
            except MissingDICOMFieldError:
                logger.warning(
                    f"{elem.name} does not contain slice thickness or "
                    "pixel spacing data."
                )
            except Exception as e:
                logger.warning(
                    "Unexpected error when attempting to read slice "
                    "thickness or pixel spacing data."
                )
                logger.debug(e, exc_info=True)
        elif elem.name == "Acquisition Device Type Code Sequence":
            try:
                acquisition_device_type_sequence = cast(
                    _AcquisitionDeviceTypeCodeSequenceField, elem
                )
                acquisition_device_type = acquisition_device_type_sequence.value[
                    0
                ].CodeMeaning
                return {"Acquisition Device Type": acquisition_device_type}
            except Exception as e:
                logger.warning(
                    "Unexpected error when attempting to read acquisition device type."
                )
                logger.debug(e, exc_info=True)
        else:
            self._ignore_cols.append(elem.name)
            # This is an info level log rather than a warning because the user may
            # have intentionally excluded this field from processing.
            logger.info(f"Cannot process sequence data, ignoring column '{elem.name}'")

        return None

    def clear_file_names_cache(self) -> None:
        """Clears the list of selected file names.

        This allows the datasource to pick up any new files that have been added to the
        directory since the last time it was cached.
        """
        # See super class method for more details on how this works
        super().clear_file_names_cache()

        # Clear the OCT file names cache
        try:
            del self._oct_file_names
        except AttributeError:
            pass

        # Clear the SLO file names cache
        try:
            del self._slo_file_names
        except AttributeError:
            pass

        # Clear the DOB file names cache
        try:
            del self._dob_filtered_file_names
        except AttributeError:
            pass

        # Clear the num bscan file names cache
        try:
            del self._num_bscan_filtered_file_names
        except AttributeError:
            pass

    ###########################################################
    # Private Properties
    ###########################################################

    @cached_property
    def _slo_file_names(self) -> list[str]:
        """Returns a list of SLO file names in the directory.

        These file paths will be absolute paths, regardless of their origin.
        """
        # Both OCT and SLO modalities are supported for this property to support the
        # case where the user has specified SLO files as well as the case where the user
        # has specified OCT files but wants to match SLO files to OCT files.
        if self.modality not in OPHTHALMOLOGY_MODALITIES:
            return []
        return self._get_file_names_by_modality(modality="SLO")

    @cached_property
    def _oct_file_names(self) -> list[str]:
        """Returns a list of file names in the directory for the specified modality.

        These file paths will be absolute paths, regardless of their origin.
        """
        if self.modality != "OCT":
            return []
        return self._get_file_names_by_modality(modality="OCT")

    @cached_property
    def _dob_filtered_file_names(self) -> list[str]:
        """Returns a list of file names in the directory that match the DOB args.

        These file paths will be absolute paths, regardless of their origin.
        """
        file_names: list[str] = []

        if self.modality is None:
            # Same as DICOMSource parent class method
            file_names = self._file_names
        if self.modality == "OCT":
            file_names = self._oct_file_names
        if self.modality == "SLO":
            file_names = self.slo_file_names

        return self._filter_files_by_dob(file_names)

    @cached_property
    def _num_bscan_filtered_file_names(self) -> list[str]:
        """Returns a list of file names in the directory that match the num bscan args.

        These file paths will be absolute paths, regardless of their origin. This filter
        is applied after the DOB filter.
        """
        return self._filter_files_by_num_bscans(self._dob_filtered_file_names)

    ###########################################################
    # Private CSV Validation Methods
    ###########################################################

    def _ensure_csv_modality_specified(self) -> None:
        """Ensure that the modality is specified if using CSV.

        Raises:
            DataSourceError: If the modality is not specified in the OphthalmologyArgs
                and a CSV is provided.
        """
        if self.csv_df is not None and self.modality is None:
            raise DataSourceError(
                "Modality not specified. Please provide a modality in the "
                "OphthalmologyDataSourceArgs."
            )

    def _ensure_csv_columns_match_modality(self) -> None:
        """Ensure the csv columns match the specified modality.

        Raises:
            DataSourceError: If the columns do not match the specified modality.
        """
        self.dicom_ophthalmology_csv_columns = cast(
            DICOMOphthalmologyCSVColumns, self.dicom_ophthalmology_csv_columns
        )
        if (
            self.modality == "OCT"
            and not self.dicom_ophthalmology_csv_columns.oct_column
        ):
            raise DataSourceError(
                "No OCT column name specified. Please provide an OCT column."
            )
        if (
            self.modality == "SLO" or self.match_slo
        ) and not self.dicom_ophthalmology_csv_columns.slo_column:
            raise DataSourceError(
                "No SLO column name specified. Please provide an SLO column."
            )

    def _ensure_csv_columns_exist(self) -> None:
        """Ensure the columns are found in the csv.

        Raises:
            DataSourceError: If the columns are not found in the csv.
        """
        assert self.csv_df is not None  # nosec[assert_used] # Reason: Reassure mypy
        self.dicom_ophthalmology_csv_columns = cast(
            DICOMOphthalmologyCSVColumns, self.dicom_ophthalmology_csv_columns
        )
        for col in (
            self.dicom_ophthalmology_csv_columns.oct_column,
            self.dicom_ophthalmology_csv_columns.slo_column,
        ):
            if col and col not in self.csv_df.columns:
                raise DataSourceError(f"Column '{col}' not found in the CSV file.")

    def _ensure_csv_file_names_are_unique(self) -> None:
        """Ensure that the csv file names are unique.

        Raises:
            DataSourceError: If the csv file names are not unique.
        """
        assert self.csv_df is not None  # nosec[assert_used] # Reason: Reassure mypy
        self.dicom_ophthalmology_csv_columns = cast(
            DICOMOphthalmologyCSVColumns, self.dicom_ophthalmology_csv_columns
        )
        for col in (
            self.dicom_ophthalmology_csv_columns.oct_column,
            self.dicom_ophthalmology_csv_columns.slo_column,
        ):
            if col and self.csv_df[col].duplicated().any():
                raise DataSourceError(
                    f"Column '{col}' in the CSV file contains duplicate file names."
                )

    ###########################################################
    # Private Class/Static Methods
    ###########################################################

    @staticmethod
    def _get_zeiss_acquisition_device_type(
        ds: pydicom.FileDataset,
    ) -> Optional[str]:
        """Get the acquisition device type for a Zeiss DICOM.

        All "Cirrus" devices are known to be OCT devices.

        Args:
            ds: The DICOM data element.

        Returns:
            The acquisition device type that should have been set for a Zeiss DICOM
            but is not set.
        """
        if hasattr(ds, "OperatorsName") and "Cirrus" in cast(str, ds.OperatorsName):
            return OCT_ACQUISITION_DEVICE_TYPE

        # If the OperatorsName is not present or not known to be a Cirrus device, then
        # we return None
        return None

    @staticmethod
    def _is_image_compression_jpeg2000lossless(ds: pydicom.FileDataset) -> bool:
        """Check if the compression standard of the pixel array is JPEG2000Lossless."""
        filename = (
            f"DICOM file {str(ds.filename)}" if ds.filename else "Current DICOM file"
        )
        meta = ds.file_meta

        if not hasattr(meta, "TransferSyntaxUID"):
            logger.warning(
                f"{filename} does not specify encoding rules ('TransferSyntaxUID')."
            )
            return False

        if meta.TransferSyntaxUID != JPEG2000Lossless:
            logger.warning(
                "Only CZM DICOM files with a 'Transfer Syntax UID' of"
                " JPEG 2000 (Lossless) are supported;"
                f" got '{meta.TransferSyntaxUID.name}'."
            )
            return False

        return True

    @staticmethod
    def _is_zeiss_manufacturer(ds: pydicom.FileDataset) -> bool:
        """Check if the manufacturer starts with Zeiss prefix."""
        if not hasattr(ds, "Manufacturer"):
            if ds.filename:
                logger.warning(
                    f"DICOM file {str(ds.filename)} does not specify manufacturer"
                )
            else:
                logger.warning("Current DICOM file does not specify manufacturer")
            return False

        return cast(str, ds.Manufacturer).startswith(_ZEISS_MANUFACTURER_PREFIX)

    @staticmethod
    def _is_supported_zeiss_dicom(ds: pydicom.FileDataset) -> bool:
        """Determine if a pydicom.Dataset is a Zeiss DICOM that we support.

        In order to support a Zeiss DICOM, it needs to have a
        Manufacturer that starts with the Zeiss prefix and
        a TransferSyntaxUID of JPEG2000Lossless.
        """
        is_zeiss_manufacturer = DICOMOphthalmologySource._is_zeiss_manufacturer(ds)

        if is_zeiss_manufacturer:
            is_jpeg2000lossless_compression = (
                DICOMOphthalmologySource._is_image_compression_jpeg2000lossless(ds)
            )
            return is_zeiss_manufacturer and is_jpeg2000lossless_compression

        return False

    @staticmethod
    def _create_patient_key(name: str, dob: str, laterality: str) -> str:
        """Create a patient key from the name, date of birth, and laterality.

        Args:
            name: The name of the patient.
            dob: The date of birth of the patient.
            laterality: The laterality of the image.

        Returns:
            The patient key.
        """
        return md5(  # nosec[blacklist] md5 is not being used in a security context # noqa: E501
            (name + dob + laterality).encode(), usedforsecurity=False
        ).hexdigest()

    @staticmethod
    def _get_laterality(ds: pydicom.FileDataset) -> Optional[str]:
        """Get the laterality from the DICOM data element.

        Args:
            ds: The DICOM data element.

        Returns:
            The laterality if set in metadata, otherwise None.
        """
        for elem in ds:
            if (
                elem.name in DICOM_LATERALITY_POSSIBLE_FIELDS
                and str(elem.value) in DICOM_LEFT_RIGHT_LATERALITY
            ):
                return str(elem.value)

        return None

    ###########################################################
    # Other Private Methods
    ###########################################################

    def _get_num_bscans(self, file_name: str) -> Optional[int]:
        """Get the number of B-scans from the DICOM file.

        Args:
            file_name: The filename of the file to be processed.

        Returns:
            The number of B-scans in the file or None if the field is missing.
        """
        try:
            ds = cast(
                DICOMImage,
                self._post_dicom_read(
                    pydicom.dcmread(
                        file_name,
                        force=True,
                        specific_tags=[0x00280008],  # (0028, 0008) Number of Frames
                    )
                ),
            )
            return int(ds.NumberOfFrames)
        except Exception as e:
            logger.warning(f"Error reading DICOM file '{file_name}': {e}")
            # [LOGGING-IMPROVEMENTS]
            if LOG_DICOM_FIXES:
                logger.debug(e, exc_info=True)
            return None

    def _get_num_bscans_from_cache(self, file_names: list[str]) -> dict[str, int]:
        """Get the number of B-scans from the cache.

        Args:
            file_names: The filenames of the files to be processed.

        Returns:
            The number of B-scans in the file or None if the field is missing.
        """
        cached_data: Optional[BulkResult] = None

        # If the cache is enabled, then we check the cache for the file
        if self.data_cache:
            if LOG_DICOM_FIXES:
                logger.info(f"Checking cache for DICOM files '{file_names}'.")
            cache_results = self.data_cache.bulk_get(list(file_names))
            if cache_results.cached is not None:
                cached_data = cache_results

        file_to_num_bscans: dict[str, int] = {}
        for file_name in file_names:
            # If the file is in the cache, then we can extract the required fields
            # from the cache. If the cache is missing the field, then we read
            # the file.
            num_bscans: Optional[int] = None
            if cached_data is not None:
                cached_file_data = cached_data.get_cached_by_filename(file_name)
                if cached_file_data is not None:
                    try:
                        num_bscans = cast(
                            int, cached_file_data["Number of Frames"].iloc[0]
                        )
                    except Exception as e:
                        logger.warning(
                            f"Error reading cache for DICOM file '{file_name}': {e}"
                        )
                        # [LOGGING-IMPROVEMENTS]
                        if LOG_DICOM_FIXES:
                            logger.debug(e, exc_info=True)

            # If the DOB is not in the cache, then we read the file
            if num_bscans is None:
                if LOG_DICOM_FIXES:
                    logger.info(
                        f"Reading DICOM file properties of '{file_name}' to get number "
                        "of B-scans."
                    )
                num_bscans = self._get_num_bscans(file_name)

            if num_bscans is not None:
                file_to_num_bscans[file_name] = num_bscans

        return file_to_num_bscans

    def _get_dob(self, file_name: str) -> Optional[str]:
        """Get the date of birth from the DICOM file.

        Args:
            file_name: The filename of the file to be processed.

        Returns:
            The date of birth of the patient or None if the field is missing.
        """
        try:
            ds = cast(
                DICOMImage,
                self._post_dicom_read(
                    pydicom.dcmread(
                        file_name,
                        force=True,
                        specific_tags=[0x00100030],  # (0010, 0030) Patient's Birth Date
                    )
                ),
            )
            return str(
                self._convert_string_to_datetime(ds.PatientBirthDate[:8], fmt="%Y%m%d")
                .date()
                .isoformat()
            )
        except Exception as e:
            logger.warning(f"Error reading DICOM file '{file_name}': {e}.")
            # [LOGGING-IMPROVEMENTS]
            if LOG_DICOM_FIXES:
                logger.debug(e, exc_info=True)
            return None

    def _get_dob_from_cache(self, file_names: list[str]) -> dict[str, date]:
        """Get the date of birth from the cache.

        Args:
            file_names: The filenames of the files to be processed.

        Returns:
            The date of birth of the patient or None if the field is missing.
        """
        cached_data: Optional[BulkResult] = None

        # If the cache is enabled, then we check the cache for the file
        if self.data_cache:
            if LOG_DICOM_FIXES:
                logger.info(f"Checking cache for DICOM files '{file_names}'.")
            cache_results = self.data_cache.bulk_get(list(file_names))
            if cache_results.cached is not None:
                cached_data = cache_results

        file_to_dob: dict[str, date] = {}
        for file_name in file_names:
            # If the file is in the cache, then we can extract the required fields
            # from the cache. If the cache is missing any of the fields, then we read
            # the file.
            file_dob_str: Optional[str] = None
            if cached_data is not None:
                cached_file_data = cached_data.get_cached_by_filename(file_name)
                if cached_file_data is not None:
                    try:
                        dob_raw_timestamp = cast(
                            pd.Timestamp,
                            cached_file_data[DICOM_PATIENT_DOB_ATTRIBUTE].iloc[0],
                        )
                        file_dob_str = str(
                            dob_raw_timestamp.to_pydatetime().date().isoformat()
                        )
                        # Remove the entry from the cache if the read was successful
                        self.__dob_cache.pop(file_name, None)
                    except Exception as e:
                        logger.warning(
                            f"Error reading cache for DICOM file '{file_name}': {e}"
                        )
                        # [LOGGING-IMPROVEMENTS]
                        if LOG_DICOM_FIXES:
                            logger.debug(e, exc_info=True)

            # Attempt to get the DOB from the in-memory cache if it is not in the
            # datasource cache
            if file_dob_str is None:
                file_dob_str = self.__dob_cache.get(file_name)

            # If the DOB is not in either cache, then we read the file
            if file_dob_str is None:
                if LOG_DICOM_FIXES:
                    logger.info(
                        f"Reading DICOM file properties of '{file_name}' to get DOB."
                    )
                file_dob_str = self._get_dob(file_name)
                if file_dob_str is not None:
                    # Cache the DOB for later use if retrieved successfully
                    self.__dob_cache[file_name] = file_dob_str

            if file_dob_str is not None:
                file_to_dob[file_name] = self._convert_string_to_datetime(
                    file_dob_str, fmt="%Y-%m-%d"
                ).date()

        return file_to_dob

    def _get_file_properties(
        self, file_name: str
    ) -> Optional[
        tuple[Optional[str], Optional[str], Optional[str], Optional[str], Optional[str]]
    ]:
        """Get various properties of the DICOM file.

        Multiple properties are extracted from the DICOM file at once to avoid
        reading the file multiple times. Furthermore, the pixel data is not read
        to improve performance since it is not needed.

        Args:
            file_name: The filename of the file to be processed.

        Returns:
            A tuple containing the file device, name, date of birth, acquisition
            datetime, and laterality. If any of the properties are missing, then
            None is returned.
        """
        try:
            # [LOGGING-IMPROVEMENTS]
            if LOG_DICOM_FIXES:
                logger.info(f"Reading DICOM file properties of '{file_name}'.")
            ds = cast(
                DICOMImage,
                self._post_dicom_read(
                    pydicom.dcmread(file_name, force=True, stop_before_pixels=True)
                ),
            )
            if self._is_supported_zeiss_dicom(cast(pydicom.FileDataset, ds)):
                file_device = self._get_zeiss_acquisition_device_type(
                    cast(pydicom.FileDataset, ds)
                )
            else:
                acquisition_device_type = ds.AcquisitionDeviceTypeCodeSequence
                if acquisition_device_type:
                    file_device = acquisition_device_type[0].CodeMeaning
            name = str(ds.PatientName)
            dob = ds.PatientBirthDate
            acquisition_datetime_str = ds.AcquisitionDateTime
            laterality = self._get_laterality(cast(pydicom.FileDataset, ds))
        except Exception as e:
            logger.warning(f"Error reading DICOM file '{file_name}': {e}")
            # [LOGGING-IMPROVEMENTS]
            if LOG_DICOM_FIXES:
                logger.debug(e, exc_info=True)
            return None

        return file_device, name, dob, acquisition_datetime_str, laterality

    def _get_file_properties_from_cache(
        self, file_names: list[str]
    ) -> list[ProcessedDICOMImage]:
        """Get various properties of the DICOM files from the cache.

        If the files are in the cache, then we can extract the required fields
        from the cache. If the cache is missing any of the fields, then we process
        file by file for the required properties.

        Args:
            file_names: The filenames of the files to be processed.

        Returns:
            A tuple containing the modality, hashed_name_dob, and acquisition_datetime.
        """
        cached_data: Optional[BulkResult] = None
        results: list[ProcessedDICOMImage] = []

        # If the cache is enabled, then we check the cache for the file
        if self.data_cache:
            if LOG_DICOM_FIXES:
                logger.info(f"Checking cache for DICOM files '{file_names}'.")
            cache_results = self.data_cache.bulk_get(list(file_names))
            if cache_results.cached is not None:
                cached_data = cache_results

        for file_name in file_names:
            file_device: Optional[str] = None
            name: Optional[str] = None
            dob_date_str: Optional[str] = None
            acquisition_date_str: Optional[str] = None
            laterality: Optional[str] = None

            # If the file is in the cache, then we can extract the required fields
            # from the cache. If the cache is missing any of the fields, then we skip
            # the file.
            if cached_data is not None:
                cached_file_data = cached_data.get_cached_by_filename(file_name)
                if cached_file_data is not None:
                    try:
                        file_device = cached_file_data["Acquisition Device Type"].iloc[
                            0
                        ]
                        name = cached_file_data[DICOM_PATIENT_NAME_ATTRIBUTE].iloc[0]
                        dob_raw_timestamp = cast(
                            pd.Timestamp,
                            cached_file_data[DICOM_PATIENT_DOB_ATTRIBUTE].iloc[0],
                        )
                        acquisition_raw_timestamp = cast(
                            pd.Timestamp,
                            cached_file_data[
                                DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE
                            ].iloc[0],
                        )
                        laterality = cached_file_data[
                            DICOM_SCAN_LATERALITY_ATTRIBUTE
                        ].iloc[0]
                        dob_date_str = str(
                            dob_raw_timestamp.to_pydatetime().date().isoformat()
                        )
                        acquisition_date_str = str(
                            acquisition_raw_timestamp.to_pydatetime().date().isoformat()
                        )
                        logger.info(f"Cache hit for DICOM file '{file_name}'.")
                    except Exception as e:
                        logger.warning(
                            f"Error reading cache for DICOM file '{file_name}': {e}"
                        )
                        # [LOGGING-IMPROVEMENTS]
                        if LOG_DICOM_FIXES:
                            logger.debug(e, exc_info=True)
                        file_device = None
                        name = None
                        laterality = None
                        dob_date_str = None
                        acquisition_date_str = None

            processed_file = self._process_file_properties(
                file_name,
                file_device,
                name,
                dob_date_str,
                acquisition_date_str,
                laterality,
            )
            if processed_file is not None:
                results.append(processed_file)
        return results

    def _process_file_properties(
        self,
        file_name: str,
        file_device: Optional[str],
        name: Optional[str],
        dob_date_str: Optional[str],
        acquisition_date_str: Optional[str],
        laterality: Optional[str],
    ) -> Optional[ProcessedDICOMImage]:
        """Process DICOM properties retrieved from cache or read the file.

        Multiple properties are extracted from the DICOM file at once to avoid
        reading the file multiple times. If any of the properties are missing, the
        file is skipped. The modality is determined from the acquisition device type.
        """
        if (
            not file_device
            or not name
            or not dob_date_str
            or not acquisition_date_str
            or not laterality
        ):
            # Open the DICOM file and extract the required fields
            properties = self._get_file_properties(file_name)
            # Skip file if failed to extract data from file.
            if properties is None:
                self.skipped_files.add(file_name)
                return None

            file_device, name, dob_date_str, acquisition_date_str, laterality = (
                properties
            )

            properties_warnings = [
                (file_device, ("Acquisition Device Type", "")),
                (name, (DICOM_PATIENT_NAME_ATTRIBUTE, "")),
                (dob_date_str, (DICOM_PATIENT_DOB_ATTRIBUTE, "")),
                (acquisition_date_str, (DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE, "")),
                (laterality, (DICOM_LATERALITY_POSSIBLE_FIELDS, "")),
            ]

            # Loop over the properties and log a warning for each missing property
            for property_value, (attribute, warning) in properties_warnings:
                if not property_value:
                    attribute_str = (
                        ", ".join(attribute)
                        if isinstance(attribute, list)
                        else attribute
                    )
                    logger.warning(
                        f"No {attribute_str} defined for file '{file_name}'. {warning}"
                    )

            # Parse dates
            if dob_date_str is not None:
                try:
                    dob_date_str = str(
                        self._convert_string_to_datetime(dob_date_str[:8], fmt="%Y%m%d")
                        .date()
                        .isoformat()
                    )
                except Exception as e:
                    dob_date_str = None
                    logger.warning(
                        f"Error converting '{DICOM_PATIENT_DOB_ATTRIBUTE}' "
                        f"for file '{file_name}'."
                    )
                    # [LOGGING-IMPROVEMENTS]
                    if LOG_DICOM_FIXES:
                        logger.debug(e, exc_info=True)

            if acquisition_date_str is not None:
                try:
                    acquisition_date_str = str(
                        self._convert_string_to_datetime(
                            acquisition_date_str[:8], fmt="%Y%m%d"
                        )
                        .date()
                        .isoformat()
                    )
                except Exception as e:
                    acquisition_date_str = None
                    logger.warning(
                        f"Error converting '{DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE}' "
                        f"for file '{file_name}'."
                    )
                    # [LOGGING-IMPROVEMENTS]
                    if LOG_DICOM_FIXES:
                        logger.debug(e, exc_info=True)

        modality = None
        if file_device is not None:
            try:
                modality = ACQUISITION_DEVICE_TYPE_MODALITY_MAPPING[file_device]
            except KeyError:
                logger.warning(
                    f"Unsupported Acquisition Device Type value: '{file_device}'"
                    f" for file '{file_name}'."
                )

        if acquisition_date_str is None:
            acquisition_timestamp = None
        else:
            try:
                acquisition_timestamp = self._convert_string_to_datetime(
                    acquisition_date_str, fmt="%Y-%m-%d"
                )
            except Exception as e:
                acquisition_timestamp = None
                logger.warning(
                    f"Error converting '{DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE}' "
                    f"for file '{file_name}'."
                )
                # [LOGGING-IMPROVEMENTS]
                if LOG_DICOM_FIXES:
                    logger.debug(e, exc_info=True)

        # Cache the DOB for later use if DOB filtering is enabled
        if dob_date_str and (self.maximum_dob_date or self.minimum_dob_date):
            self.__dob_cache[file_name] = dob_date_str

        # Compute a dummy patient key (SHA) to satisfy ProcessedDICOMImage.
        patient_key = str(uuid.uuid4())
        # Patients that don't have all fields populated are not
        # added in the hash table for OCT / SLO matching.
        # Patients that have all fields populated we regenerate
        # the patient_key with those values as md5 hash and add
        # to the has table for OCT / SLO matching.
        if name and dob_date_str and acquisition_timestamp and laterality and modality:
            patient_key = self._create_patient_key(name, dob_date_str, laterality)
            # Add the data to the hash table
            if patient_key in self.__hash_table:
                self.__hash_table[patient_key].add(
                    (file_name, modality, acquisition_timestamp)
                )
            else:
                self.__hash_table[patient_key] = {
                    (file_name, modality, acquisition_timestamp)
                }

        return ProcessedDICOMImage(
            file_name, modality, patient_key, acquisition_timestamp
        )

    def _lookup_slo_file_name_in_hash_table(
        self, patient_key: str, acquisition_datetime: datetime
    ) -> Optional[Path]:
        """Get the SLO file name from OCT hash and datetime.

        Args:
            patient_key: The hash of the name, date of birth, and laterality of the
                patient.
            acquisition_datetime: The acquisition datetime of the OCT file.

        Returns:
            The filename of the SLO file or None if no SLO file exists.
        """
        # Return if CSV is used.
        if self.csv_df is not None:
            return None

        # Extract the OCT-SLO file pairs from the path
        # If the file is in the hash table, then we can extract the SLO file name
        # from the hash table. If the file is not in the hash table, then we need to
        # find a match for the OCT file in the SLO files
        patient_key_matches = self.__hash_table.get(patient_key)
        if patient_key_matches:
            for patient_key_match in patient_key_matches:
                (
                    slo_file_name,
                    modality,
                    slo_acquisition_datetime,
                ) = patient_key_match
                if modality == "SLO":
                    if abs((acquisition_datetime - slo_acquisition_datetime).days) <= 1:
                        logger.info(
                            f"Matching SLO file found for patient '{patient_key}'"
                            " with dates within 24 hours."
                        )
                        return make_path_absolute(slo_file_name, self.path)

                    logger.info(
                        f"Matching SLO file found for patient '{patient_key}'"
                        " but dates fall outside 24 hours. Ignoring..."
                    )
        return None

    def _get_slo_file_name_from_csv(self, oct_filename: str) -> Optional[Path]:
        """Get the SLO file name from the OCT file name.

        If a CSV file has been provided, then we use the CSV to map the OCT file
        to the SLO file. Otherwise, we use the ophthalmology_args to determine
        the SLO file name by simply replacing the `oct_string` with the `slo_string`.

        Args:
            oct_filename: The filename of the OCT file.

        Returns:
            The filename of the SLO file or None if no SLO file exists.
        """
        slo_filename: Optional[Path] = None

        if self.csv_df is not None and self.match_slo:
            # If csv_df is not None then neither is self.dicom_ophthalmology_csv_columns
            self.dicom_ophthalmology_csv_columns = cast(
                DICOMOphthalmologyCSVColumns, self.dicom_ophthalmology_csv_columns
            )
            oct_col = self.dicom_ophthalmology_csv_columns.oct_column
            slo_col = self.dicom_ophthalmology_csv_columns.slo_column
            # If match_slo is True, then we have already checked that both of these
            # column names are not None
            assert oct_col is not None  # nosec[assert_used] # Reason: Reassure mypy
            assert slo_col is not None  # nosec[assert_used] # Reason: Reassure mypy
            abs_oct_filename = make_path_absolute(oct_filename, self.path)
            # itertuples iteration
            for row in self.csv_df.itertuples():
                if (
                    make_path_absolute(getattr(row, oct_col), self.path)
                    == abs_oct_filename
                ):
                    slo_filename = make_path_absolute(getattr(row, slo_col), self.path)
                    break

        return slo_filename

    def _filter_files_by_modality(
        self,
        file_names: list[str],
        modality: OphthalmologyModalityType = None,
    ) -> list[str]:
        """Filter the files by modality based on the ophthalmology_args.

        Args:
            file_names: The list of file names to be filtered.
            modality: The modality to filter the files by. If None, then the
                default modality is used.

        Returns:
            The filtered list of file names.
        """
        filtered_file_names: list[str] = []
        if modality is None:
            modality = self.modality
        processed_files = self._get_file_properties_from_cache(file_names)
        for file_properties in processed_files:
            if file_properties.modality == modality:
                filtered_file_names.append(file_properties.file_name)
            elif modality is not None:
                self.skipped_files.add(file_properties.file_name)
        return filtered_file_names

    def _get_file_names_from_csv(
        self, modality: OphthalmologyModalityType
    ) -> list[str]:
        """Returns a list of file names in the CSV file for the specified modality.

        These file paths will be absolute paths, regardless of their origin.

        Args:
            modality: The modality to filter the CSV file by.

        Returns:
            The list of file names.
        """
        file_names: list[str] = []
        if self.csv_df is not None:
            self.dicom_ophthalmology_csv_columns = cast(
                DICOMOphthalmologyCSVColumns, self.dicom_ophthalmology_csv_columns
            )
            if modality == "OCT":
                col = self.dicom_ophthalmology_csv_columns.oct_column
            elif modality == "SLO":
                col = self.dicom_ophthalmology_csv_columns.slo_column
            else:
                raise DataSourceError(
                    f"Modality '{modality}' not recognised. Must be 'OCT' or 'SLO'."
                )
            file_names_raw: list[str] = list(self.csv_df[col])
            file_names_paths = [
                make_path_absolute(Path(i), self.path) for i in file_names_raw
            ]
            file_names = [str(i) for i in file_names_paths]

        return file_names

    def _get_file_names_from_path(
        self, modality: OphthalmologyModalityType
    ) -> list[str]:
        """Returns a list of file names in the path for the specified modality.

        These file paths will be absolute paths, regardless of their origin.

        Args:
            modality: The modality to filter the files by.

        Returns:
            The list of file names.
        """
        file_names: list[str] = []
        if self.csv_df is None:
            all_file_names = super().file_names
            file_names = self._filter_files_by_modality(
                all_file_names, modality=modality
            )
        return file_names

    def _get_file_names_by_modality(
        self, modality: OphthalmologyModalityType
    ) -> list[str]:
        """Returns a list of file names in the directory for the specified modality.

        These file paths will be absolute paths, regardless of their origin.

        Args:
            modality: The modality to filter the files by.

        Returns:
            The list of file names.
        """
        return (
            self._get_file_names_from_csv(modality=modality)
            if self.csv_df is not None
            else self._get_file_names_from_path(modality=modality)
        )

    def _add_slo(self, oct_filename: str, data: dict[str, Any]) -> dict[str, Any]:
        """Adds the SLO column to the data dictionary from the OCT filename.

        Args:
            oct_filename: The filename of the OCT file.
            data: The data dictionary to be updated.

        Returns:
            The updated data dictionary.
        """
        slo_filename: Optional[Path] = None
        cached_data: Optional[pd.DataFrame] = None
        if self.csv_df is not None:
            slo_filename = self._get_slo_file_name_from_csv(oct_filename)
        else:
            if self.data_cache:
                cached_data = self.data_cache.get(oct_filename)

            if (
                cached_data is not None
                and (
                    filename_series := cached_data.get(
                        SLO_ORIGINAL_FILENAME_METADATA_COLUMN
                    )
                )
                is not None
            ):
                # Get the first value in the series i.e. first row
                slo_filename = Path(str(filename_series.get(0)))

            # If the file is not in the cache, then we need to find a match for the OCT
            # file in the SLO files
            if not slo_filename:
                try:
                    dob_str = data[DICOM_PATIENT_DOB_ATTRIBUTE][:8]
                    dob_str = str(
                        self._convert_string_to_datetime(dob_str, fmt="%Y%m%d")
                        .date()
                        .isoformat()
                    )
                    patient_key = self._create_patient_key(
                        data[DICOM_PATIENT_NAME_ATTRIBUTE],
                        dob_str,
                        data[DICOM_SCAN_LATERALITY_ATTRIBUTE],
                    )
                    acquisition_datetime = self._convert_string_to_datetime(
                        data[DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE][:8], fmt="%Y%m%d"
                    )
                except Exception as e:
                    logger.warning(
                        f"Error converting DICOM fields for file '{oct_filename}' "
                        f"during SLO matching."
                    )
                    logger.debug(e, exc_info=True)
                    return data

                slo_filename = self._lookup_slo_file_name_in_hash_table(
                    patient_key, acquisition_datetime
                )
            else:
                logger.info("SLO file found in cache.")

        # If filename has been determined, then we can process the SLO image
        if slo_filename and slo_filename.exists():
            logger.info(f"Matching SLO file found for '{oct_filename}' exists.")
            slo_ds = pydicom.dcmread(slo_filename, force=True)
            pixel_data = self._process_dicom_slo_pixel_array(
                slo_ds, data, oct_filename, SLO_IMAGE_ATTRIBUTE
            )
            if pixel_data is not None:
                data.update(pixel_data)
                data[SLO_ORIGINAL_FILENAME_METADATA_COLUMN] = str(slo_filename)
        else:
            logger.warning(f"No SLO file found: '{slo_filename}'.")

        return data

    def _process_dicom_slo_pixel_array(
        self,
        ds: pydicom.FileDataset,
        data: dict[str, Any],
        filename: str,
        image_attribute: str = SLO_IMAGE_ATTRIBUTE,
    ) -> Optional[dict[str, Any]]:
        """Process the SLO pixel data from the DICOM file."""
        try:
            arr: np.ndarray = self._get_pixel_array(ds)
        except Exception as e:
            logger.warning(f"Error when reading pixel data from file {filename}: {e}")
            # If we are only loading images, we don't want to add the file data to
            # the dataframe if there is an error saving the image. We return None to
            # indicate that. If we are not only loading images, we will just continue
            # to the next field so we instead return the data dictionary.
            return None if self.images_only else data

        # SLO images are always 2d images, so we can just add the image to the data
        # dictionary as is.
        try:
            data = self._add_image_to_data(
                data=data,
                arr=arr,
                frame_num=0,
                image_attribute=image_attribute,
            )
        except Exception as e:
            logger.warning(f"Error when loading SLO image from file {filename}: {e}")
            # If we are only loading images, we don't want to add
            # the file data to the dataframe if there is an error
            # saving the image, even if there are other frames which
            # could be saved successfully.
            if self.images_only:
                # Return None so we don't add any of the
                # file data to the dataframe - including fields that
                # have already been processed.
                return None

        return data

    def _process_dicom_file(
        self,
        filename: str,
        stop_before_pixels: bool = False,
        **kwargs: Any,
    ) -> Optional[dict[str, Any]]:
        """Read and process the dicom file.

        Args:
            filename: The filename of the file to be processed.
            stop_before_pixels: Don't load pixel data from file.
            kwargs: Kwargs to pass through to parent _process_dicom_file().
        """
        data = super()._process_dicom_file(filename, stop_before_pixels, **kwargs)

        if data is not None:
            # Log a warning if the Patient's Birth Date or Name
            # are missing, or if laterality is missing
            for col in (
                DICOM_PATIENT_DOB_ATTRIBUTE,
                DICOM_PATIENT_NAME_ATTRIBUTE,
                DICOM_SCAN_LATERALITY_ATTRIBUTE,
            ):
                if col not in data:
                    logger.warning(
                        f"Column '{col}' not found in DICOM file '{filename}'."
                    )
            if self.match_slo:
                try:
                    logger.info(f"Matching SLO file for '{filename}'.")
                    data = self._add_slo(filename, data)
                    if (
                        self.drop_row_on_missing_slo
                        and SLO_IMAGE_ATTRIBUTE not in "".join(list(data))
                    ):
                        logger.warning(
                            f"Dropping row for file '{filename}' due to missing SLO."
                        )
                        return None
                except Exception as e:
                    logger.warning(
                        "Unexpected error when attempting to read SLO image data."
                    )
                    logger.warning(e, exc_info=True)
                    if self.drop_row_on_missing_slo:
                        logger.warning(
                            f"Dropping row for file '{filename}' due to missing SLO."
                        )
                        return None

        return data

    def _get_slice_thickness_and_pixel_spacing(
        self, elem: FunctionalGroupsSequenceField
    ) -> FunctionalGroupsSequenceProcessingOutput:
        """Get the slice thickness and pixel spacing from the DICOM data element.

        These attributes are nested deep within the DICOM data element within
        "Pixel Measures Sequence" which is itself within
        "Shared Functional Groups Sequence" or "Per-frame Functional Groups Sequence".
        They are required for area calculations.

        Args:
            elem: The DICOM data element.

        Returns:
            A dictionary containing the slice thickness and pixel spacing.

        Raises:
            MissingDICOMFieldError: If the slice thickness or pixel spacing fields
                are missing.
        """
        data: dict[str, float] = {}
        found_slice_thickness: bool = False
        found_pixel_spacing: bool = False

        for functional_groups in elem.value:
            for functional_group in functional_groups.elements():
                if functional_group.name == "Pixel Measures Sequence":
                    for pixel_measures in functional_group.value:
                        for pixel_measure in pixel_measures.elements():
                            if pixel_measure.name == "Slice Thickness":
                                data["Slice Thickness"] = float(pixel_measure.value)
                                # This allows us to exit early if we have found both
                                # slice thickness and pixel spacing regardless of the
                                # order they appear in the sequence.
                                found_slice_thickness = True
                                if found_pixel_spacing:
                                    return cast(
                                        FunctionalGroupsSequenceProcessingOutput,
                                        data,
                                    )
                            elif pixel_measure.name == "Pixel Spacing":
                                data["Pixel Spacing Row"] = float(
                                    pixel_measure.value[0]
                                )
                                data["Pixel Spacing Column"] = float(
                                    pixel_measure.value[1]
                                )
                                # This allows us to exit early if we have found both
                                # slice thickness and pixel spacing regardless of the
                                # order they appear in the sequence.
                                found_pixel_spacing = True
                                if found_slice_thickness:
                                    return cast(
                                        FunctionalGroupsSequenceProcessingOutput,
                                        data,
                                    )

        raise MissingDICOMFieldError()

    def _post_dicom_read(self, ds: pydicom.FileDataset) -> pydicom.FileDataset:
        """Apply post-read processing to the DICOM file.

        Handle special processing and sanitization of Zeiss DICOM files.
        """
        # This handling needs to be applied in both cases: Zeiss and non-Zeiss.
        ds = super()._post_dicom_read(ds)

        # If we're not dealing with a Zeiss DICOM, there's no special handling,
        # beyond what is defined in the original method.
        # Otherwise, we need to apply sanitization to the non-standard Zeiss fields.
        if self._is_supported_zeiss_dicom(ds):
            if ds.file_meta:
                ds.file_meta.walk(_czm_data_sanitization)
            ds.walk(_czm_data_sanitization)

        return ds

    def _get_pixel_array(self, ds: pydicom.FileDataset) -> np.ndarray:
        """Retrieve the pixel array from the dataset.

        Handle special processing and sanitization of Zeiss DICOM files.
        """
        # If we are handling a Zeiss DICOM we need to deobfuscate the pixel data
        # before returning it
        # NOTE: If errors are raised here it will cause the file to be skipped due
        #       to handling in the superclass.
        if self._is_supported_zeiss_dicom(ds):
            if "PixelData" not in ds:
                raise CZMError("No 'Pixel Data' found in the CZM DICOM file.")
            ds = _unscramble_pixel_data(ds)

        pixel_array = ds.pixel_array

        # Some ophthalmology DICOMs (particularly Zeiss) can return image arrays of a
        # "wrong" dtype; we want either `uint8` or `float32` to ensure the greatest
        # compatibility with other systems, so will attempt to fix this
        if (pixel_array_dtype := pixel_array.dtype) not in (np.uint8, np.float32):
            logger.debug(
                f"Image array had unexpected dtype:"
                f" got {pixel_array_dtype}, expected `uint8` or `float32`."
            )
            if np.issubdtype(pixel_array_dtype, np.integer):
                logger.debug(
                    f"Converting image array from {pixel_array_dtype} to `uint8`"
                )
                pixel_array = pixel_array.astype(np.uint8)
            elif np.issubdtype(pixel_array_dtype, np.floating):
                logger.debug(
                    f"Converting image array from {pixel_array_dtype} to `float32`"
                )
                pixel_array = pixel_array.astype(np.float32)
            else:
                logger.debug(
                    f"Unable to convert image array implicitly;"
                    f" array dtype is {pixel_array_dtype}"
                )

        return pixel_array


###################
# Zeiss Additions #
###################
# See:
#   - https://pydicom.github.io/pydicom/stable/guides/element_value_types.html
#   - https://dicom.nema.org/medical/dicom/current/output/html/part05.html#table_6.2-1
_NUM_STR_VR: Final[set[str]] = {
    VR.DS,  # Decimal String
    VR.IS,  # Integer String
}

# https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_U.html
_LATERALITY_CODE_MAP: Final[dict[str, str]] = {
    "OS": "L",
    "OD": "R",
    "OU": "B",
}

# The character that generally seems to indicate the end of the "valid" string and
# the start of the invalid Zeiss-specific suffix
_ZEISS_STRING_INVALID_DELIM: Final[str] = "\0"

_ZEISS_MANUFACTURER_PREFIX: Final[str] = "Carl Zeiss Meditec"

# Max size of pixel data allowed in a non-extended DICOM file
_MAX_BASIC_OFFSET_SIZE: Final[int] = 2**32 - 1


def _czm_data_sanitization(dataset: Dataset, dataelement: DataElement) -> None:
    """Callback sanitization function for CZM DICOMs.

    Should be used with pydicom.Dataset.walk().

    Args:
        dataset: the dataset being used in the callback.
        dataelement: the individual DICOM element that is currently being inspected.
    """
    # DICOMs generated by Zeiss devices often contain non-standard data entries,
    # normally containing \x00 and other hex characters at the of the "normal" entry.
    # In order to ensure that these DICOMs are parsable/used properly, we need to
    # apply some "best-effort" sanitization to the fields.
    #
    # We only concern ourselves with fields with "str" values as these are what the
    # expected type is for fields that Zeiss has added the "\x00" characters to;
    # their additions force these fields to have string values, even if pydicom
    # should instead parse it to other types.
    #
    # The sanitization has a cascading structure where multiple sanitization rules
    # may be applied to the same fields; this is by design to allow the most general
    # fixes to be applied first, then more specific ones for different types.

    # Sanitization 1: General string fix
    # If something is already a string, we can try to extract the values directly. We
    # want to get the portion of the string before the first "illegal" character,
    # which always seems to be "\x00".
    if dataelement.VM > 1:
        new_multi_value = []
        for sub_elem in dataelement.value:
            if isinstance(dataelement.value, str):
                # This will append the original value if we've not been able to split it
                new_multi_value.append(sub_elem.split(_ZEISS_STRING_INVALID_DELIM)[0])
        try:
            dataelement.value = new_multi_value
        except ValueError:
            # Even post-sanitization, some elements will not accept list[str] as
            # their input. These are handled explicitly elsewhere.
            pass
    # If there's only a single element as the value, work on that directly
    elif isinstance(dataelement.value, str):
        try:
            dataelement.value = dataelement.value.split(_ZEISS_STRING_INVALID_DELIM)[0]
        except ValueError:
            # Even post-sanitization, some elements will not accept str as their
            # input. These are handled explicitly elsewhere.
            pass

    # Sanitization 2: Number string fixes, in particular multi-value number strings
    #                 (e.g. "5.0,6.0")
    # Decimal/Integer strings, particularly those of >1 multiplicity, may not have
    # been set/parsed correctly due to the sanitization issues, and so we may need to
    # reset these (pydicom will then handle the conversion to the correct storage type).
    if dataelement.VR in _NUM_STR_VR:
        if isinstance(dataelement.value, str):
            # The previous block may not have handled the sanitization (for instance if
            # the sanitized str could not be set on the value), so we attempt it again
            # here just in case.
            sanitized: str = dataelement.value.split(_ZEISS_STRING_INVALID_DELIM)[0]
            split_value: list[str] = [s.strip() for s in sanitized.split(",")]

            # Want to set list[str] only if more than one element
            if len(split_value) > 1:
                dataelement.value = split_value
            else:
                dataelement.value = split_value[0]

    # Sanitization 3: Person Name fixes
    # Elements that are identified as PN (Person Name) will already have been
    # partially parsed and stored as a PersonName instance. Due to this, they will
    # have been skipped in the first pass to fix "\x00" strings.
    if dataelement.VR == VR.PN:
        old_name: str = str(dataelement.value)
        # pydicom will handle the value-setter converting the string into a new
        # PersonName instance
        dataelement.value = old_name.split(_ZEISS_STRING_INVALID_DELIM)[0]

    # Sanitization 4: Laterality field mapping
    # Laterality-related fields in Zeiss often use OS, OD, and OU, instead of the
    # standard's form of L, R, or B, respectively. To ensure compatibility with the
    # standard/with DICOMs from other sources, we need to map these fields. See:
    # https://dicom.nema.org/medical/dicom/current/output/chtml/part17/chapter_U.html
    if "laterality" in dataelement.name.lower():
        if isinstance(dataelement.value, str):
            try:
                dataelement.value = _LATERALITY_CODE_MAP[dataelement.value]
            except KeyError:
                # This means it wasn't a field we know how to map, so just ignore it
                pass


def _unscramble_czm_frame(frame: bytes) -> bytes:
    """Return an unscrambled image frame.

    Args:
        frame: The scrambled CZM JPEG 2000 data frame as found in the DICOM dataset.

    Returns:
        The unscrambled JPEG 2000 data.

    Raises:
        CZMError: if there is no JP2 header in the scrambled pixel data.
    """
    # Adapted from: https://github.com/pydicom/pydicom/discussions/1618
    #
    # The pixel data is obfuscated in two ways:
    #   - First the J2K data has sections transposed (for example, the first 253
    #     bytes are moved to 3/5ths of the way into the data)
    #   - Once the transpositions are done, every 7th byte starting at offset 0
    #     is overwritten by XORing it with 0x5A
    #
    # The pixel data also has a JP2 header, which again is non-conformant to the
    # DICOM Standard, so be aware of that and remove it if required (search for the
    # 0xFF 0x4F start-of-codestream J2K marker, which should be at offset 85 of the
    # unscrambled data).

    # Fix the 0x5A XORing
    frame = bytearray(frame)
    for ii in range(0, len(frame), 7):
        frame[ii] = frame[ii] ^ 0x5A

    # Offset to the start of the JP2 header - empirically determined
    jp2_offset = math.floor(len(frame) / 5 * 3)

    # Double check that our empirically determined jp2_offset is correct
    offset = frame.find(b"\x00\x00\x00\x0c")
    if offset == -1:
        raise CZMError("No JP2 header found in the scrambled pixel data")

    if jp2_offset != offset:
        logger.warning(
            f"JP2 header found at offset {offset} rather than the expected "
            f"{jp2_offset}"
        )
        jp2_offset = offset

    d = bytearray()
    d.extend(frame[jp2_offset : jp2_offset + 253])
    d.extend(frame[993:1016])
    d.extend(frame[276:763])
    d.extend(frame[23:276])
    d.extend(frame[1016:jp2_offset])
    d.extend(frame[:23])
    d.extend(frame[763:993])
    d.extend(frame[jp2_offset + 253 :])

    # Double check that everything has been added that was expected
    if len(d) != len(frame):
        raise CZMError(
            "Error whilst unscrambling frame data;"
            " length of unscrambled frame was not equal to scrambled frame."
        )

    return bytes(d)


def _unscramble_pixel_data(ds: pydicom.FileDataset) -> pydicom.FileDataset:
    """Unscramble pixel data stored on a CZM DICOM.

    Args:
        ds: The DICOM Dataset instance with scrambled pixel data.

    Returns:
        A DICOM Dataset instance with the data unscrambled.
    """
    # Find out if this dataset is already using the extended encapsulation capability
    # as if it is we will need to ensure the final output similarly uses this
    previously_ext: bool = hasattr(ds, "ExtendedOffsetTable") and hasattr(
        ds, "ExtendedOffsetTableLengths"
    )

    num_frames: int = getattr(ds, "NumberOfFrames", 1) or 1

    # Unscramble each frame already in the pixel data. The approach differs for
    # num_frames=1 and num_frames>1 as Zeiss stores a single frame in a
    # non-conformant, non-encapsulated format.
    unscrambled_pixel_data: list[bytes]
    if num_frames > 1:
        unscrambled_pixel_data = [
            _unscramble_czm_frame(frame)
            for frame in generate_pixel_data_frame(ds.PixelData, num_frames)
        ]
    else:
        # CZM is non-conformant for single frames
        unscrambled_pixel_data = [_unscramble_czm_frame(ds.PixelData)]

    # Encapsulate the data in the appropriate manner, depending on output size
    total_pixel_data_bytes = (num_frames - 1) * 8 + sum(
        [len(f) for f in unscrambled_pixel_data[:-1]]
    )
    if previously_ext or total_pixel_data_bytes > _MAX_BASIC_OFFSET_SIZE:
        (
            ds.PixelData,
            ds.ExtendedOffsetTable,
            ds.ExtendedOffsetTableLengths,
        ) = encapsulate_extended(unscrambled_pixel_data)
    else:
        ds.PixelData = encapsulate(unscrambled_pixel_data)

    # PS3.5 Annex A.4 - encapsulated pixel data uses undefined length
    ds["PixelData"].is_undefined_length = True

    # PS3.5 Annex A.4 - encapsulated datasets use explicit VR little endian
    ds.is_implicit_VR = False
    ds.is_little_endian = True

    return ds


class CZMError(DataSourceError):
    """Errors related to processing of Zeiss DICOMs."""

    pass
