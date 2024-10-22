"""Algorithm for outputting GA model results to CSV on the pod-side."""

from __future__ import annotations

from collections.abc import Iterable
import datetime
import json
import math
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Optional, Union, cast

import desert as desert
from marshmallow import fields
import numpy as np
import pandas as pd
import PIL

import bitfount
from bitfount.data.datasources.base_source import BaseSource, FileSystemIterableSource
from bitfount.data.datasources.dicom_source import DICOM_SCAN_LATERALITY_ATTRIBUTE
from bitfount.data.datasources.utils import ORIGINAL_FILENAME_METADATA_COLUMN
from bitfount.federated.algorithms.base import (
    BaseAlgorithmFactory,
    BaseWorkerAlgorithm,
    NoResultsModellerAlgorithm,
)
from bitfount.federated.algorithms.ophthalmology.dataframe_generation_extensions import (  # noqa: E501
    DataFrameExtensionError,
    generate_bitfount_patient_id,
)
from bitfount.federated.algorithms.ophthalmology.ophth_algo_types import (
    DATASOURCE_IMAGE_PREFIX_COLUMNS,
    FILTER_MATCHING_COLUMN,
    NAME_COL,
    NUMBER_OF_FRAMES_COLUMN,
    RESULTS_IMAGE_PREFIX,
    RESULTS_SUFFIX,
    SEGMENTATION_LABELS,
    TOTAL_GA_AREA_LOWER_BOUND,
    TOTAL_GA_AREA_UPPER_BOUND,
    ColumnFilter,
    GAMetrics,
    ReportMetadata,
)
from bitfount.federated.algorithms.ophthalmology.ophth_algo_utils import (
    _add_filtering_to_df,
    draw_segmentation_mask_on_orig_image,
    get_data_for_files,
    get_dataframe_iterator_from_datasource,
    is_file_iterable_source,
    parse_mask_json,
)
from bitfount.federated.logging import _get_federated_logger
from bitfount.utils.logging_utils import deprecated_class_name
from bitfount.visualisation.ga_trial_pdf_jade import (
    AltrisRecordInfo,
    AltrisScan,
    generate_pdf,
)

if TYPE_CHECKING:
    from bitfount.federated.privacy.differential import DPPodConfig
    from bitfount.types import T_FIELDS_DICT


logger = _get_federated_logger("bitfount.federated")

ELIGIBLE_PATIENTS = "Eligible"
NON_ELIGIBLE_PATIENTS = "Not-eligible"


class _WorkerSide(BaseWorkerAlgorithm):
    """Worker side of the algorithm."""

    def __init__(
        self,
        *,
        path: Union[str, os.PathLike],
        report_metadata: ReportMetadata,
        filename_prefix: Optional[str] = None,
        filter: Optional[list[ColumnFilter]] = None,
        pdf_filename_columns: Optional[list[str]] = None,
        total_ga_area_lower_bound: float = TOTAL_GA_AREA_LOWER_BOUND,
        total_ga_area_upper_bound: float = TOTAL_GA_AREA_UPPER_BOUND,
        trial_name: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.report_metadata = report_metadata
        self.filter = filter
        self.path = Path(path)
        self.pdf_filename_columns: list[str] = (
            pdf_filename_columns if pdf_filename_columns is not None else [NAME_COL]
        )
        self.filename_prefix = filename_prefix
        self.total_ga_area_lower_bound = total_ga_area_lower_bound
        self.total_ga_area_upper_bound = total_ga_area_upper_bound
        self.trial_name = trial_name

    def initialise(
        self,
        datasource: BaseSource,
        pod_dp: Optional[DPPodConfig] = None,
        pod_identifier: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Sets Datasource."""
        self.initialise_data(datasource=datasource)
        if not pod_identifier:
            raise ValueError("Pod_identifier must be provided.")

    def run(
        self,
        results_df: pd.DataFrame,
        ga_dict: dict[str, Optional[GAMetrics]],
        task_id: Optional[str] = None,
        filenames: Optional[list[str]] = None,
    ) -> pd.DataFrame:
        """Generates PDF reports for the GA model results.

        Args:
            results_df: The DataFrame containing the predictions from the GA model.
                This DataFrame doesn't contain the full set of file details, but
                rather just the model outputs for each file.
                If `filenames` is provided, each dataframe must contain a
                ORIGINAL_FILENAME_METADATA_COLUMN which describes which file each
                row is associated with.
            ga_dict: The GA metrics calculated from the model outputs, associated
                with each file name.
            task_id: The ID of the task run, if present.
            filenames: The list of files that the results correspond to. If not
                provided, will iterate through all files in the dataset to find
                the corresponding ones.

        Returns:
            A DataFrame with the original filename and the path to the saved PDF.
        """
        # We need a dataframe (of the correct length, i.e. the number of files)
        # so we construct it from the ga_metrics dict. Some of the values in
        # this dict may be None, so we handle that conversion.
        # Note: order will be correct as dict is sorted by insertion order,
        # and we only do clean/new insertions into this dict.
        metrics_df = pd.DataFrame.from_records(
            ga_d if ga_d is not None else dict()  # type: ignore[typeddict-item] # Reason: we are explicitly not creating a GAMetric instance with our call to `dict()` # noqa: E501
            for ga_d in ga_dict.values()
        )
        metrics_df[ORIGINAL_FILENAME_METADATA_COLUMN] = list(ga_dict.keys())
        # First, we need to extract the appropriate data from the datasource by
        # combining it with the predictions supplied (i.e. joining on the identifiers).
        test_data_dfs: Iterable[pd.DataFrame]
        if filenames and is_file_iterable_source(self.datasource):
            logger.debug(f"Retrieving data for: {filenames}")
            # use_cache is False as we need the image data to produce the images in
            # the PDF
            df: pd.DataFrame = get_data_for_files(
                cast(FileSystemIterableSource, self.datasource),
                filenames,
                use_cache=False,
            )
            # Merge the metrics with the data
            df = df.merge(metrics_df, on=ORIGINAL_FILENAME_METADATA_COLUMN)
            test_data_dfs = [df]

            # Check that we have the expected number of results for the number of files
            assert len(filenames) == len(test_data_dfs[0])  # nosec [assert_used]
        else:
            logger.warning(
                "Iterating over all files to find results<->file match;"
                " this may take a long time."
            )
            # use_cache is False as we need the image data to produce the images in
            # the PDF
            test_data_dfs = get_dataframe_iterator_from_datasource(
                self.datasource, use_cache=False
            )

        # Check that we have the expected number of results for the number of files
        if filenames:
            assert len(filenames) == len(results_df)  # nosec [assert_used]
            assert len(filenames) == len(ga_dict)  # nosec [assert_used]

        pdf_output_paths: list[tuple[str, Optional[Path]]] = []

        len_test_data_dfs = 0
        for test_df in test_data_dfs:
            len_test_data_dfs += len(test_df)

            # Add BitfountPatientID to the DataFrame
            try:
                test_df = generate_bitfount_patient_id(test_df)
            except DataFrameExtensionError as e:
                logger.error(f"Error whilst calculating Bitfount Patient IDs: {e}")

            # Apply row filtering to supplied dataframe based on some criteria.
            # Assumption here is that the results_df maps correctly
            # to the test_df

            files_matching_filters = self._find_entries_matching_filter(
                results_df, test_df
            )
            for idx, datasource_row in test_df.iterrows():
                # Iterrows() iterates over DataFrame rows as (index, Series) pairs.
                index = cast(pd.Index, idx)

                original_filename = datasource_row[ORIGINAL_FILENAME_METADATA_COLUMN]
                if original_filename in files_matching_filters:
                    eligibility = ELIGIBLE_PATIENTS
                else:
                    eligibility = NON_ELIGIBLE_PATIENTS
                if (
                    original_filename
                    in results_df[ORIGINAL_FILENAME_METADATA_COLUMN].values
                ):
                    ga_metrics = self._get_ga_metric_from_dictionary(
                        ga_dict, original_filename
                    )
                    if ga_metrics is not None:
                        scan = self._get_scan(
                            datasource_row,
                            results_df,
                            index,
                            bscan_idx=ga_metrics["max_ga_bscan_index"],
                        )
                        record_info = self._get_record_info(datasource_row)
                        # TODO: [NO_TICKET: Imported from ophthalmology] Matching of
                        #       same patient eye
                        # Get the output path for the PDF report
                        (
                            pdf_output_path,
                            _,
                        ) = self._get_pdf_output_path(
                            Path(original_filename),
                            datasource_row,
                            task_id,
                            eligibility,
                        )
                        try:
                            start = datetime.datetime.now()

                            generate_pdf(
                                pdf_output_path,
                                record_info,
                                scan,
                                ga_metrics,
                                total_ga_area_lower_bound=self.total_ga_area_lower_bound,
                                total_ga_area_upper_bound=self.total_ga_area_upper_bound,
                            )

                            end = datetime.datetime.now()
                            logger.debug(
                                f"Generated PDF {str(pdf_output_path)}"
                                f" in {(end-start).total_seconds()} seconds"
                            )
                        except Exception as e:
                            # Generate PDF
                            logger.error(
                                "Error generating PDF report for "
                                f"{original_filename}."
                                " Skipping"
                            )
                            pdf_output_paths.append(
                                (
                                    original_filename,
                                    None,
                                )
                            )
                            logger.debug(e, exc_info=True)
                            continue
                        pdf_output_paths.append(
                            (
                                original_filename,
                                pdf_output_path,
                            )
                        )
                    else:
                        logger.warning(
                            "No GA metrics found for "
                            f"{original_filename}."
                            " Skipping"
                        )
                        pdf_output_paths.append((original_filename, None))
                else:
                    pdf_output_paths.append((original_filename, None))

        if filenames and isinstance(self.datasource, FileSystemIterableSource):
            # Assert that the number of predictions (results_df) matched the number
            # of retrieved records (test_data_dfs) (found during iteration);
            # in the case where filenames was supplied we should _only_ be iterating
            # through that number
            assert len(results_df) == len_test_data_dfs  # nosec [assert_used]

        # NOTE: The orders of these should match the input order of the predictions
        return pd.DataFrame(
            pdf_output_paths,
            columns=[ORIGINAL_FILENAME_METADATA_COLUMN, "pdf_output_path"],
        )

    def _get_ga_metric_from_dictionary(
        self, ga_dict: dict[str, Optional[GAMetrics]], original_filename: str
    ) -> Optional[GAMetrics]:
        """Get the GA metrics from the dictionary from the original filename."""
        try:
            return ga_dict[original_filename]
        except KeyError:
            return None

    def _get_record_info(self, datasource_row: pd.Series) -> AltrisRecordInfo:
        """Extract required text fields for report.

        Args:
            datasource_row: The datasource row from which we need to extract data for.
        """
        # For each of the text fields we need the value to be a string
        record_info_text_fields: list[tuple[str, str]] = []
        if self.report_metadata.text_fields is not None:
            for text_field in self.report_metadata.text_fields:
                # Get the field's value in the appropriate format
                field_value: str

                # If the record metadata just references an explicit value, use that
                if text_field.value:
                    field_value = text_field.value

                # Otherwise, it will be referencing data stored in a column,
                # so we need to extract/parse it
                else:
                    # Post_init check verifies that one of `column` or `value` is set.
                    # If `value` is not set, then `column` must be set.
                    text_field.column = cast(str, text_field.column)

                    # Apply various parsing attempts to the column value to try and
                    # get it in the most meaningful format.
                    # The parsing is attempted in the following order:
                    #   - DateTime
                    #   - Date
                    #   - float
                    #   - int
                    #   - raw
                    try:
                        datasource_entry: Union[
                            datetime.datetime, datetime.date, float, int, str
                        ] = datasource_row[text_field.column]

                        # If NaN, NaT
                        if pd.isna(datasource_entry):
                            field_value = "Not found"  # type: ignore[unreachable] # Reason: entry could always be NaN so need to handle that case, even if not represented in typing # noqa: E501
                            continue

                        # Parse DateTime fields
                        if isinstance(
                            datasource_entry,
                            datetime.datetime,
                        ):
                            # Find the explicit format, or use default
                            if text_field.datetime_format:
                                dt_format = text_field.datetime_format
                            else:
                                dt_format = "%Y-%m-%d %H:%M:%S.%f"

                            field_value = datasource_entry.strftime(dt_format)

                        # Parse Date fields
                        elif isinstance(datasource_entry, datetime.date):
                            # Find the explicit format, or use default
                            if text_field.datetime_format:
                                date_format = text_field.datetime_format
                            else:
                                date_format = "%Y-%m-%d"

                            field_value = datasource_entry.strftime(date_format)

                        # Parse float fields
                        # We round them to two DP
                        elif isinstance(datasource_entry, float):
                            field_value = str(round(datasource_entry, 2))

                        # Parse int fields
                        elif isinstance(datasource_entry, int):
                            field_value = str(datasource_entry)

                        # Parse anything else as raw
                        else:
                            field_value = str(datasource_entry)
                    except (KeyError, ValueError):
                        field_value = "Not found"

                record_info_text_fields.append((text_field.heading, field_value))

        return AltrisRecordInfo(
            text_fields=record_info_text_fields,
            heading=self.report_metadata.heading,
        )

    def _get_scan(
        self,
        datasource_row: pd.Series,
        results_df: pd.DataFrame,
        idx: pd.Index,
        bscan_idx: Optional[int],
    ) -> AltrisScan:
        """Get the scans from the datasource row and the results dataframe."""
        # Extract images and metadata about the images
        if NUMBER_OF_FRAMES_COLUMN in datasource_row.index:
            total_frames = datasource_row[NUMBER_OF_FRAMES_COLUMN]
            middle_frame_idx = int(math.floor(total_frames // 2))
        else:
            # We assume that there is only one frame
            total_frames = 1
            middle_frame_idx = 0

        # If the total GA area is 0, then we set the bscan_idx to the middle frame
        if bscan_idx is None:
            bscan_idx = middle_frame_idx

        frame = datasource_row[f"{DATASOURCE_IMAGE_PREFIX_COLUMNS} {bscan_idx}"]

        # TODO: [NO_TICKET: Imported from ophthalmology] Revisit for the protocol
        #       after matching
        try:
            mask_json_str = str(
                results_df.loc[idx][
                    f"{RESULTS_IMAGE_PREFIX}_{bscan_idx}{RESULTS_SUFFIX}"
                ]
            )
            mask_json_str = mask_json_str.replace("'", '"')
            try:
                # Model version <  11
                mask_json = json.loads(mask_json_str)[0][0]["mask"]
            except KeyError:
                # Model version >= 11
                mask_json = json.loads(mask_json_str)[0]["mask"]
            mask = parse_mask_json(mask_json, SEGMENTATION_LABELS)
        except Exception as e:
            # if mask is not found in the results_df, then we create an empty mask
            logger.error(
                "Error parsing mask for "
                f"{datasource_row[ORIGINAL_FILENAME_METADATA_COLUMN]}."
                " Skipping"
            )
            logger.debug(
                "Error parsing mask for "
                f"{datasource_row[ORIGINAL_FILENAME_METADATA_COLUMN]}: {e}"
            )
            mask = np.zeros((1, 1, 1))

        # PDF algorithm is only compatible with fileiterable sources,
        # assuring mypy of it
        assert isinstance(self.datasource, FileSystemIterableSource)  # nosec assert-used

        # If filepaths are not cached, then we get image from numpy array
        orig_bscan = PIL.Image.fromarray(frame)
        # Get the laterality of the scan
        try:
            laterality = datasource_row[DICOM_SCAN_LATERALITY_ATTRIBUTE]
        except KeyError:
            laterality = None

        img_w_mask, legend2color = draw_segmentation_mask_on_orig_image(
            mask, orig_bscan
        )
        scan = AltrisScan(
            bscan_image=orig_bscan,
            bscan_idx=bscan_idx,
            bscan_total=total_frames,
            bscan_w_mask=img_w_mask,
            legend2color=legend2color,
            laterality=laterality,
        )
        return scan

    def _get_pdf_output_path(
        self,
        orig_filename: Path,
        row: pd.Series,
        task_id: Optional[str],
        eligibility: Optional[str] = None,
    ) -> tuple[Path, str]:
        """Get the output path to save report PDF to.

        Will automatically add version suffixes to get a unique name.
        """
        filename_prefix = f"{self.filename_prefix}-" if self.filename_prefix else ""
        filename_prefix = (
            f"{filename_prefix}{eligibility}-"
            if eligibility is not None
            else filename_prefix
        )
        filename_prefix = (
            f"{filename_prefix}{self.trial_name}"
            if self.trial_name is not None
            else filename_prefix
        )
        pdf_filename_extension = ".pdf"
        # Extract the values from the columns for the pdf name.
        pdf_filename = filename_prefix
        for col in self.pdf_filename_columns:
            try:
                pdf_filename = pdf_filename + "-" + str(row[col])
            except KeyError:
                logger.warning(
                    f"Column {col} not found in the data. "
                    "Skipping this column for the PDF filename."
                )
                continue
        # If no columns are found in the data, then save the pdf under
        # the original filename stem
        if pdf_filename == filename_prefix:
            logger.warning(
                "Column values for PDF filename are empty. "
                "Saving pdf under original filename."
            )
            pdf_filename = (
                f"{filename_prefix}-" f"{orig_filename.stem}{pdf_filename_extension}"
            )
        else:
            pdf_filename = f"{pdf_filename}{pdf_filename_extension}"

        if task_id is not None:
            Path(self.path / f"{task_id}").mkdir(parents=True, exist_ok=True)
            pdf_path = self.path / f"{task_id}" / pdf_filename
        else:
            Path(self.path).mkdir(parents=True, exist_ok=True)
            pdf_path = self.path / pdf_filename

        # If the filename already exists, then add a version suffix to the filename
        original_stem = pdf_path.stem
        i = 1
        while pdf_path.exists():
            pdf_path = pdf_path.with_name(f"{original_stem} ({i}){pdf_path.suffix}")
            i += 1

        return pdf_path, original_stem

    def _find_entries_matching_filter(
        self, df: pd.DataFrame, test_df: pd.DataFrame
    ) -> list[str]:
        """Apply row filtering to supplied dataframe based on some criteria.

        Returns:
            A list of filenames that match the filter criteria.
        """
        # Assumption here is that the results_df maps correctly
        # to the test_df
        if ORIGINAL_FILENAME_METADATA_COLUMN not in df.columns:
            df[ORIGINAL_FILENAME_METADATA_COLUMN] = test_df[
                ORIGINAL_FILENAME_METADATA_COLUMN
            ]
        # From the results, only take the ones that match the
        # filter if a filter is provided
        if self.filter is not None:
            logger.info("Applying filters to the data.")
            test_df[FILTER_MATCHING_COLUMN] = True
            for col_filter in self.filter:
                try:
                    test_df = _add_filtering_to_df(test_df, col_filter)
                except (KeyError, TypeError) as e:
                    if isinstance(e, KeyError):
                        logger.warning(
                            f"No column `{col_filter.column}` found in the data. "
                            "Filtering only on remaining given columns."
                        )
                    else:
                        # if TypeError
                        logger.warning(
                            f"Filter column {col_filter.column} is incompatible with "  # noqa: E501
                            f"operator type {col_filter.operator}. "
                            f"Raised TypeError: {str(e)}"
                        )
                    logger.info(
                        f"Filtering will skip `{col_filter.column} "
                        f"{col_filter.operator} {col_filter.value}`."
                    )

        # Filter out rows that don't match the filter. We leave the original index,
        # so we can match the rows with the original data when we iterate over it.
        test_df_subset = (
            test_df.loc[test_df[FILTER_MATCHING_COLUMN]]
            if self.filter is not None
            else test_df
        )
        return test_df_subset[ORIGINAL_FILENAME_METADATA_COLUMN].tolist()


class GATrialPDFGeneratorAlgorithmJade(BaseAlgorithmFactory):
    """Algorithm for generating the PDF results report for the GA Algorithm.

    Args:
        report_metadata: A ReportMetadata for the pdf report metadata fields.
        filter: A list of ColumnFilter objects to filter the data by.
        save_path: The folder path where the pdf report should be saved.
        filename_prefix: The prefix for the pdf filename. Defaults to None.
        pdf_filename_columns: The columns from the datasource that should
             be used for the pdf filename. If not provided, the filename will
             be saved as "Patient_index_i.pdf" where `i` is the index in the
             filtered datasource. Defaults to None.
        total_ga_area_lower_bound: The lower bound for the total GA area.
            Defaults to 2.5.
        total_ga_area_upper_bound: The upper bound for the total GA area.
            Defaults to 17.5.
    """

    fields_dict: ClassVar[T_FIELDS_DICT] = {
        "report_metadata": fields.Nested(desert.schema_class(ReportMetadata)),
        "filter": fields.Nested(
            desert.schema_class(ColumnFilter), many=True, allow_none=True
        ),
        "save_path": fields.Str(),
        "filename_prefix": fields.Str(allow_none=True),
        "pdf_filename_columns": fields.List(fields.Str(), allow_none=True),
        "total_ga_area_lower_bound": fields.Float(allow_none=True),
        "total_ga_area_upper_bound": fields.Float(allow_none=True),
        "trial_name": fields.Str(allow_none=True),
    }

    def __init__(
        self,
        *,
        report_metadata: ReportMetadata,
        filter: Optional[list[ColumnFilter]] = None,
        save_path: Optional[Union[str, os.PathLike]] = None,
        filename_prefix: Optional[str] = None,
        pdf_filename_columns: Optional[list[str]] = None,
        total_ga_area_lower_bound: float = TOTAL_GA_AREA_LOWER_BOUND,
        total_ga_area_upper_bound: float = TOTAL_GA_AREA_UPPER_BOUND,
        trial_name: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self.save_path: Path
        if save_path is None:
            self.save_path = bitfount.config.BITFOUNT_OUTPUT_DIR
        else:
            self.save_path = Path(save_path)
        self.filter = filter
        self.report_metadata = report_metadata
        self.filename_prefix = filename_prefix
        self.pdf_filename_columns = pdf_filename_columns
        self.total_ga_area_lower_bound = total_ga_area_lower_bound
        self.total_ga_area_upper_bound = total_ga_area_upper_bound
        self.trial_name = trial_name
        super().__init__(**kwargs)

    def modeller(self, **kwargs: Any) -> NoResultsModellerAlgorithm:
        """Modeller-side of the algorithm."""
        return NoResultsModellerAlgorithm(
            log_message="Running GA Trial PDF Generator Algorithm",
            **kwargs,
        )

    def worker(self, **kwargs: Any) -> _WorkerSide:
        """Worker-side of the algorithm."""
        return _WorkerSide(
            report_metadata=self.report_metadata,
            filename_prefix=self.filename_prefix,
            path=self.save_path,
            filter=self.filter,
            pdf_filename_columns=self.pdf_filename_columns,
            total_ga_area_lower_bound=self.total_ga_area_lower_bound,
            total_ga_area_upper_bound=self.total_ga_area_upper_bound,
            trial_name=self.trial_name,
            **kwargs,
        )


# Keep old name for backwards compatibility
@deprecated_class_name
class GATrialPDFGeneratorAlgorithm(GATrialPDFGeneratorAlgorithmJade):
    """Algorithm for generating the PDF results report for the GA Algorithm."""

    pass
