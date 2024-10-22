"""Module containing DICOMSource class.

DICOMSource class handles loading of DICOM data.
"""

from __future__ import annotations

import logging
import os
from typing import Any, Optional, Union, cast

import numpy as np
import pandas as pd
import pydicom
from pydicom.uid import UID

from bitfount.config import LOG_DICOM_FIXES
from bitfount.data.datasources.base_source import FileSystemIterableSourceInferrable
from bitfount.data.datasources.types import _DICOMImage, _DICOMSequenceField
from bitfount.data.datasources.utils import LAST_MODIFIED_METADATA_COLUMN
from bitfount.utils import delegates

logger = logging.getLogger(__name__)

DICOM_NUMBER_OF_FRAMES_TAG = (0x0028, 0x0008)
DICOM_NUMBER_OF_FRAMES = "Number of Frames"
DICOM_TEXT_REPRESENTATIONS = ["AS", "LO", "LT", "OW", "PN", "SH", "ST", "UN", "UT"]
DICOM_DATETIME = ["DT", "DA"]
DICOM_IMAGE_ATTRIBUTE = "Pixel Data"
DICOM_LATERALITY_POSSIBLE_FIELDS = [
    "Laterality",
    "Image Laterality",
    "Frame Laterality",
    "Measurement Laterality",
]
DICOM_LEFT_RIGHT_LATERALITY = ["L", "R"]
DICOM_SCAN_LATERALITY_ATTRIBUTE = "Scan Laterality"
DICOM_PATIENT_NAME_ATTRIBUTE = "Patient's Name"
DICOM_PATIENT_DOB_ATTRIBUTE = "Patient's Birth Date"
DICOM_ACQUISISTION_DATE_TIME_ATTRIBUTE = "Acquisition DateTime"
DICOM_MEDIA_STORAGE_SOP_CLASS_UID_NO_IMAGES: list[str] = [
    "Basic Text SR Storage",
    "Enhanced SR Storage",
    "Comprehensive SR Storage",
    "Procedure Log Storage",
    "Mammography CAD SR Storage",
    "Key Object Selection Document Storage",
    "Chest CAD SR Storage",
    "X-Ray Radiation Dose SR Storage",
    "Encapsulated PDF Storage",
    "Encapsulated CDA Storage",
    "12-lead ECG Waveform Storage",
    "General ECG Waveform Storage",
    "Ambulatory ECG Waveform Storage",
    "Hemodynamic Waveform Storage",
    "Cardiac Electrophysiology Waveform Storage",
    "Basic Voice Audio Waveform Storage",
    "General Audio Waveform Storage",
    "Arterial Pulse Waveform Storage",
    "Respiratory Waveform Storage",
]


@delegates()
class DICOMSource(FileSystemIterableSourceInferrable):
    """Data source for loading DICOM files.

    Args:
        path: The path to the directory containing the DICOM files.
        file_extension: The file extension of the DICOM files. Defaults to '.dcm'.
        images_only: If True, only dicom files containing image data will be loaded.
            If the file does not contain any image data, or it does but there was an
            error loading or saving the image(s), the whole file will be skipped.
            Defaults to True.
        **kwargs: Keyword arguments passed to the parent base classes.
    """

    _datetime_columns: set[str] = set()

    def __init__(
        self,
        path: Union[os.PathLike, str],
        file_extension: Optional[str] = ".dcm",
        images_only: bool = True,
        **kwargs: Any,
    ) -> None:
        super().__init__(path=path, file_extension=file_extension, **kwargs)
        self.images_only = images_only
        if self.images_only:
            self._datasource_filters_to_apply.append(
                self._filter_images_only_from_media_storage_sop_class_uid
            )

    def _process_file(
        self,
        filename: str,
        skip_non_tabular_data: bool = False,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Loads the DICOM file specified by `filename`.

        Args:
            filename: The name of the file to process.
            skip_non_tabular_data: Whether we can avoid loading non-tabular data,
                e.g. image data (can be set to True when generating schemas).
            **kwargs: Additional keyword arguments.

        Returns:
            The processed DICOM as a dictionary of keys and values within a list
            containing just that element.
        """
        try:
            if self.images_only:
                file_name = self._filter_images_only_from_media_storage_sop_class_uid(
                    [filename]
                )
                if len(file_name) == 0:
                    return []
            data = self._process_dicom_file(
                filename, stop_before_pixels=skip_non_tabular_data
            )
        except Exception as e:
            # However, just in case there is an unexpected error that we didn't
            # catch, we will log it here and skip the file.
            logger.warning(f"Unexpected error when processing file {filename}: {e}.")
            data = None

        # Skip file if specified or empty
        if not data:
            # There should already be another logger message explaining why the file
            # was skipped, so we don't need to log anything extra here.
            logger.warning(f"Skipping file {filename}.")
            self.skipped_files.add(filename)
            return []

        # Skip files that don't contain any image data if images_only is True or
        # simply log this fact if images_only is False as it is not necessarily an
        # error but is probably unexpected.
        if not any(key.startswith(DICOM_IMAGE_ATTRIBUTE) for key in data):
            if self.images_only:
                logger.warning(
                    f"File {filename} does not contain any image data, skipping."
                )
                self.skipped_files.add(filename)
                return []

            logger.warning(
                f"File {filename} does not contain any image data but contains "
                "other data. If this is not expected, please check the file."
            )

        return [data]

    def _filter_images_only_from_media_storage_sop_class_uid(
        self, file_names: list[str]
    ) -> list[str]:
        """Filter out files based on the Media Storage SOP Class UID.

        Args:
            file_names: The list of file names to filter.

        Returns:
            The filtered list of file names.
        """
        filtered_files = []
        for file_name in file_names:
            try:
                file_meta = pydicom.filereader.read_file_meta_info(file_name)
                media_storage_sop_class_uid = UID(
                    file_meta.get("MediaStorageSOPClassUID", "Unknown")
                ).name
                if (
                    media_storage_sop_class_uid
                    not in DICOM_MEDIA_STORAGE_SOP_CLASS_UID_NO_IMAGES
                ):
                    filtered_files.append(file_name)
                else:
                    logger.warning(
                        f"Media Storage SOP Class UID is {media_storage_sop_class_uid},"
                        " indicating the file contains no images. "
                        f"Skipping file {file_name}."
                    )
                    self.skipped_files.add(file_name)
            except Exception as e:
                logger.warning(
                    "Error when reading Media Storage SOP Class UID "
                    f"from file {file_name}: {e}"
                )
        return filtered_files

    def _process_dataset(self, dataframe: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
        """Converts the datetime columns to datetime."""
        self._datetime_columns.add(LAST_MODIFIED_METADATA_COLUMN)
        return self._convert_datetime_columns(dataframe)

    def _convert_datetime_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Converts the datetime columns to datetime.

        Args:
            df: The dataframe to convert.

        Returns:
            The converted dataframe.
        """
        for col_name in self._datetime_columns:
            try:
                df[col_name] = pd.to_datetime(df[col_name])
            except Exception as e:
                # if not a 'standard' date, get the first 8 characters,
                # assuming it is in the format %Y%m%d. If this doesn't work
                # ignore errors and pass-through the original string.
                logger.debug(
                    f"Field `{col_name}` not in a standard date format. "
                    f"Raised error: `{e}`"
                )
                try:
                    df[col_name] = pd.to_datetime(df[col_name].str[:8], format="%Y%m%d")
                except Exception as e:
                    logger.debug(f"Error when converting to datetime: {e}")
                    logger.warning(
                        f"Field `{col_name}` cannot be loaded as datetime, "
                        "loading as string."
                    )

        return df

    def process_sequence_field(
        self, elem: _DICOMSequenceField
    ) -> Optional[dict[str, Any]]:
        """Process a sequence field.

        This method is called when a sequence field is encountered. It can be
        overridden by plugins to process specific sequence data.

        :::tip

        Override this method in your plugin if you want to process specific sequence
        data.

        :::

        Args:
            elem: The DICOM data element which has its 'VR' set to 'SQ'.

        Returns:
            A dictionary containing the processed sequence data or None.
        """
        self._ignore_cols.append(elem.name)
        logger.warning(
            f"Cannot process sequence data, ignoring column '{elem.name}'. "
            "Consider overriding the `process_sequence_field` method in a plugin "
            "to process specific sequence data."
        )

        return None

    @staticmethod
    def _process_specific_dicom_tag(
        filename: str, specific_tag: tuple[Any, Any]
    ) -> Any:
        """Retrieve a specific tag from the DICOM file.

        Args:
            filename: The filename of the DICOM.
            specific_tag: The specific tag to be retrieved.

        Returns:
            The value of the retrieved tag or `None` if the field is not found.
        """
        try:
            ds = pydicom.dcmread(filename, force=True, specific_tags=[specific_tag])
            return ds[specific_tag].value
        except KeyError:
            return None

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
            **kwargs: Additional keyword arguments.

        Returns:
            The processed DICOM data as a dictionary.
        """
        # TODO: [BIT-4161] revisit this after pydicom 3.0.0 release
        # and upgrade to see if it can be improved with the new
        # pixel_array functionality
        try:
            ds = pydicom.dcmread(
                filename, force=True, stop_before_pixels=stop_before_pixels
            )
            ds = self._post_dicom_read(ds)
        except Exception as e:
            logger.warning(
                f"Skipping file {filename} as it could not be loaded. "
                f"Raised error: {e}."
            )
            self.skipped_files.add(filename)
            return None

        data: dict[str, Any] = {}

        # Specific handling for the `Number of Frames` tag
        if stop_before_pixels:
            # populate the skipped `Pixel Data` columns based on the `Number of Frames`
            num_frames_element = ds.get_item(DICOM_NUMBER_OF_FRAMES_TAG)
            if num_frames_element is not None and num_frames_element.value > 0:
                for frame_num in range(num_frames_element.value):
                    image_col_name = f"{DICOM_IMAGE_ATTRIBUTE} {frame_num}"
                    self.image_columns.add(image_col_name)
                    data[image_col_name] = "<SKIPPED>"
            else:
                # Try to get the specific `Number of Frames` tag
                num_of_frames = self._process_specific_dicom_tag(
                    filename, specific_tag=DICOM_NUMBER_OF_FRAMES_TAG
                )
                if (
                    num_of_frames is not None
                    and num_of_frames.isdigit()
                    and int(num_of_frames) > 0
                ):
                    for frame_num in range(int(num_of_frames)):
                        image_col_name = f"{DICOM_IMAGE_ATTRIBUTE} {frame_num}"
                        self.image_columns.add(image_col_name)
                        data[image_col_name] = "<SKIPPED>"
                else:
                    logger.warning(
                        (
                            f"stop_before_pixels is {stop_before_pixels} but could not"
                            " get Number of Frames so re-loading the whole DICOM file"
                        )
                    )
                    return self._process_dicom_file(filename, stop_before_pixels=False)

        skip_file = False
        for elem in ds:
            if elem.name not in self._ignore_cols:
                if elem.VR == "SQ":
                    # A DICOM file has different Value Representation (VR).
                    # Sequence data (SQ) can be very nested and tricky to process
                    # so we ignore those fields by default but allow plugins
                    # to override the `process_sequence_field` method to process
                    # specific sequence data if needed.
                    sequence_field = cast(_DICOMSequenceField, elem)
                    sequence_data = self.process_sequence_field(sequence_field)
                    if sequence_data is not None:
                        data.update(sequence_data)
                elif elem.name == DICOM_IMAGE_ATTRIBUTE:
                    # We need to set the image columns here to ensure the pod_db
                    # is correctly populated
                    if self.cache_images is False:
                        # Once we know the image has an image attribute, we can
                        # cast the dicom image to the DICOMImage type, which
                        # is a TypedDict. This allows us to access the
                        # NumberOfFrames fields with type safety.
                        ds_dict = cast(_DICOMImage, ds)
                        # If the image is 3D, we need to save each frame separately.
                        num_frames = self._get_num_frames(ds_dict, filename)
                        for frame_num in range(num_frames):
                            image_col_name = f"{DICOM_IMAGE_ATTRIBUTE} {frame_num}"
                            self.image_columns.add(image_col_name)
                    pixel_data = self._process_dicom_pixel_array(
                        ds, data, filename, DICOM_IMAGE_ATTRIBUTE
                    )
                    if pixel_data is None:
                        skip_file = True
                        self.skipped_files.add(filename)
                        break

                    data.update(pixel_data)
                elif (
                    elem.name in DICOM_LATERALITY_POSSIBLE_FIELDS
                    and str(elem.value) in DICOM_LEFT_RIGHT_LATERALITY
                ):
                    # We want to store the laterality under a consistent field name.
                    # We check if the value is present in the list of possible values
                    # as to not overwrite it in case one of the values is present
                    # but not populated.
                    data[DICOM_SCAN_LATERALITY_ATTRIBUTE] = str(elem.value)

                elif elem.VR in DICOM_TEXT_REPRESENTATIONS:
                    data[elem.name] = str(elem.value)
                elif elem.VR in DICOM_DATETIME:
                    self._datetime_columns.add(elem.name)
                    data[elem.name] = elem.value
                elif hasattr(elem, "VM") and elem.VM > 1:
                    # The Value Multiplicity of a Data Element specifies the number
                    # of Values that can be encoded in the Value Field of that Data
                    # Element. The VM of each Data Element is specified explicitly
                    # in PS3.6. If the number of Values that may be encoded in a
                    # Data Element is variable, it shall be represented by two
                    # numbers separated by a dash; e.g., "1-10" means that there
                    # may be 1 to 10 Values in the Data Element. Similar to the
                    # SQ case, dataframes do not support sequence data, so we only
                    # take the first element.
                    data[elem.name] = elem[0]
                else:
                    # For all other fields, we just take the value of the column
                    data[elem.name] = elem.value

        if skip_file:
            return None

        if not data:
            logger.warning(f"File {filename} is empty.")

        return data

    def _post_dicom_read(self, ds: pydicom.FileDataset) -> pydicom.FileDataset:
        """Apply post-read processing to the DICOM file.

        Override this method in subclasses to apply different post-read processing.
        """
        # Decode the file if it is encoded. This is necessary for some files where the
        # sequence data has been encoded and cannot otherwise be read. This is harmless
        # for files that are not encoded.
        ds.decode()
        # [LOGGING-IMPROVEMENTS]
        if LOG_DICOM_FIXES:
            logger.debug("Successfully decoded dicom file.")

        # Fix metadata fields to ensure they are valid
        ds.fix_meta_info()
        # [LOGGING-IMPROVEMENTS]
        if LOG_DICOM_FIXES:
            logger.debug("Successfully fixed metadata fields.")

        # Remove "private elements" from the Dataset as these are inherently
        # unparsable for us; we don't know what the tag is related to, etc.
        ds.remove_private_tags()
        # [LOGGING-IMPROVEMENTS]
        if LOG_DICOM_FIXES:
            logger.debug("Successfully removed private elements from DICOM.")

        return ds

    def _process_dicom_pixel_array(
        self,
        ds: pydicom.FileDataset,
        data: dict[str, Any],
        filename: str,
        image_attribute: str = DICOM_IMAGE_ATTRIBUTE,
    ) -> Optional[dict[str, Any]]:
        try:
            arr: np.ndarray = self._get_pixel_array(ds)
        except Exception as e:
            logger.warning(f"Error when reading pixel data from file {filename}: {e}")
            # If we are only loading images, we don't want to add the file data to
            # the dataframe if there is an error saving the image. We return None to
            # indicate that. If we are not only loading images, we will just continue
            # to the next field so we instead return the data dictionary.
            return None if self.images_only else data

        # Once we have the pixel array, we can cast the dicom image to
        # the DICOMImage type, which is a TypedDict. This allows us to
        # access the NumberOfFrames, PatientID, StudyDate and StudyTime
        # fields with type safety.
        ds_dict = cast(_DICOMImage, ds)

        # If the image is 3D, we need to save each frame separately.
        num_frames = self._get_num_frames(ds_dict, filename)
        if num_frames == 0:
            return None
        data[DICOM_NUMBER_OF_FRAMES] = num_frames
        # If there is just one frame, the loop will simply only run once
        for frame_num in range(num_frames):
            try:
                if num_frames > 1:
                    frame_data = arr[frame_num]
                else:
                    frame_data = arr
                data = self._add_image_to_data(
                    data=data,
                    arr=frame_data,
                    frame_num=frame_num,
                    image_attribute=image_attribute,
                )
            except Exception as e:
                logger.warning(
                    f"Error when loading image {frame_num} from file {filename}: {e}"
                )
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

    def _get_pixel_array(self, ds: pydicom.FileDataset) -> np.ndarray:
        """Retrieve the pixel array from the dataset.

        Override this method in subclasses to apply different pixel array loading.
        """
        return ds.pixel_array

    def _add_image_to_data(
        self,
        data: dict[str, Any],
        arr: np.ndarray,
        frame_num: int,
        image_attribute: str = DICOM_IMAGE_ATTRIBUTE,
    ) -> dict[str, Any]:
        """Add the image to the data dictionary and possibly save it to disk.

        To avoid unnecessary latency, we will only write the raw images to disk if
        Args:
            ds: The DICOM data.
            data: The dictionary containing the data.
            arr: The pixel array from the dataset.
            save_path: The path to the absolute filename where the image will be saved.
            frame_num: The frame number of the image.

        Returns:
            The updated data dictionary.
        """
        # For each image we assign a column according to the
        # frames order and write in the df the path where
        # the image is saved.They need to be converted to
        # string, so they can be used in the pod's sql database
        image_col_name = f"{image_attribute} {frame_num}"
        data[image_col_name] = arr
        return data

    @staticmethod
    def _get_num_frames(image: _DICOMImage, filename: str) -> int:
        """Get the number of frames in the image.

        If `NumberOfFrames` is not present, we assume it is a 2D image.

        Args:
            image: The DICOM image.
            filename: The filename of the file to be processed.

        Returns:
            The number of frames in the image.
        """

        try:
            num_frames = int(image["NumberOfFrames"].value)
        except KeyError:
            try:
                if hasattr(image, "pixel_array"):
                    if len(image.pixel_array.shape) == 3:  # type: ignore[attr-defined] # Reason: pixel array check is done above # noqa: E501
                        num_frames = image.pixel_array.shape[0]  # type: ignore[attr-defined] # Reason: pixel array check is done above # noqa: E501
                    elif len(image.pixel_array.shape) == 2:  # type: ignore[attr-defined] # Reason: pixel array check is done above # noqa: E501
                        logger.debug(
                            f"NumberOfFrames attribute not present on {filename}, "
                            "and the pixel array only has 2 dimensions so assuming "
                            "2D image."
                        )
                        num_frames = 1
                    else:
                        logger.debug(
                            f"NumberOfFrames attribute not present on {filename}, "
                            "and could not determine the shape of the pixel array."
                        )
                        num_frames = 0
                else:
                    logger.debug(f"No pixel array attribute found on {filename}. ")
                    num_frames = 0
            except Exception as e:
                logger.warning(
                    "Error when reading NumberOfFrames or the pixel array from "
                    f"file {filename}: {e}"
                )
                num_frames = 0
        return num_frames
