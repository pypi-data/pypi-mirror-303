"""Algorithm for establishing number of results that match a given criteria."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Optional, cast

from marshmallow import fields
import pandas as pd

from bitfount.data.datasources.base_source import BaseSource
from bitfount.exceptions import BitfountError
from bitfount.federated.algorithms.base import (
    BaseAlgorithmFactory,
    BaseWorkerAlgorithm,
    NoResultsModellerAlgorithm,
)
from bitfount.federated.algorithms.ophthalmology.ophth_algo_types import (
    _BITFOUNT_PATIENT_ID_KEY,
    AGE_COL,
    CNV_THRESHOLD,
    DOB_COL,
    ELIGIBILE_VALUE,
    ELIGIBILITY_COL,
    FILTER_MATCHING_COLUMN,
    LARGEST_GA_LESION_LOWER_BOUND,
    LARGEST_LEGION_SIZE_COL_PREFIX,
    MAX_CNV_PROBABILITY_COL_PREFIX,
    NAME_COL,
    PATIENT_AGE_LOWER_BOUND,
    SCAN_DATE_COL,
    TOTAL_GA_AREA_COL_PREFIX,
    TOTAL_GA_AREA_LOWER_BOUND,
    TOTAL_GA_AREA_UPPER_BOUND,
    ColumnFilter,
)
from bitfount.federated.logging import _get_federated_logger
from bitfount.utils.logging_utils import deprecated_class_name
from bitfount.utils.pandas_utils import calculate_ages

if TYPE_CHECKING:
    from bitfount.federated.privacy.differential import DPPodConfig
    from bitfount.types import T_FIELDS_DICT


logger = _get_federated_logger("bitfount.federated")
# This algorithm is designed to find patients that match a set of clinical criteria.
# The criteria are as follows:
# 1. There are scans for both eyes for the same patient,
#   taken within 24 hours of each other
# 2. Age greater than or equal to PATIENT_AGE_LOWER_BOUND
# 3. Total GA area between TOTAL_GA_AREA_LOWER_BOUND and TOTAL_GA_AREA_UPPER_BOUND
# 4. Largest GA lesion size greater than LARGEST_GA_LESION_LOWER_BOUND
# 5. No CNV in either eye (CNV probability less than CNV_THRESHOLD)


class _WorkerSide(BaseWorkerAlgorithm):
    """Worker side of the algorithm."""

    def __init__(
        self,
        renamed_columns: Optional[Mapping[str, str]] = None,
        total_ga_area_lower_bound: float = TOTAL_GA_AREA_LOWER_BOUND,
        total_ga_area_upper_bound: float = TOTAL_GA_AREA_UPPER_BOUND,
        cnv_threshold: float = CNV_THRESHOLD,
        largest_ga_lesion_lower_bound: float = LARGEST_GA_LESION_LOWER_BOUND,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.renamed_columns = renamed_columns
        self._static_cols: list[str] = [NAME_COL]
        self._paired_col_prefixes: list[str] = [
            # TODO: [NO_TICKET: Imported from ophthalmology] ideally this would be
            #       static
            DOB_COL,
            TOTAL_GA_AREA_COL_PREFIX,
            LARGEST_LEGION_SIZE_COL_PREFIX,
            MAX_CNV_PROBABILITY_COL_PREFIX,
            SCAN_DATE_COL,
            _BITFOUNT_PATIENT_ID_KEY,
            FILTER_MATCHING_COLUMN,
        ]
        self.name_col = NAME_COL
        self.dob_col = DOB_COL
        self.total_ga_area = TOTAL_GA_AREA_COL_PREFIX
        self.largest_legion_size = LARGEST_LEGION_SIZE_COL_PREFIX
        self.max_cnv_probability = MAX_CNV_PROBABILITY_COL_PREFIX
        self.age_col = AGE_COL
        self.scan_date_col = SCAN_DATE_COL
        self.bitfount_patient_id = _BITFOUNT_PATIENT_ID_KEY
        self._paired_cols: Optional[defaultdict[str, list[str]]] = None
        self.total_ga_area_lower_bound = total_ga_area_lower_bound
        self.total_ga_area_upper_bound = total_ga_area_upper_bound
        self.cnv_threshold = cnv_threshold
        self.largest_ga_lesion_lower_bound = largest_ga_lesion_lower_bound

    def _get_all_paired_cols(self) -> list[str]:
        """Get all the paired column names as a single list."""
        if self._paired_cols is None:
            return []
        else:
            return [col for col_list in self._paired_cols.values() for col in col_list]

    def initialise(
        self,
        datasource: BaseSource,
        pod_dp: Optional[DPPodConfig] = None,
        pod_identifier: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Sets Datasource."""
        self.initialise_data(datasource=datasource)

    def get_column_filters(self) -> list[ColumnFilter]:
        """Returns the column filters for the algorithm.

        Returns a list of ColumnFilter objects that specify the filters for the
        columns that the algorithm is interested in. This is used to filter other
        algorithms using the same filters.
        """
        return [
            ColumnFilter(
                column=MAX_CNV_PROBABILITY_COL_PREFIX,
                operator="<=",
                value=self.cnv_threshold,
            ),
            ColumnFilter(
                column=LARGEST_LEGION_SIZE_COL_PREFIX,
                operator=">=",
                value=self.largest_ga_lesion_lower_bound,
            ),
            ColumnFilter(
                column=TOTAL_GA_AREA_COL_PREFIX,
                operator=">=",
                value=self.total_ga_area_lower_bound,
            ),
            ColumnFilter(
                column=TOTAL_GA_AREA_COL_PREFIX,
                operator="<=",
                value=self.total_ga_area_upper_bound,
            ),
        ]

    def get_matched_column_filters(self) -> list[ColumnFilter]:
        """Returns the column filters for the matched data."""
        return [
            ColumnFilter(
                column=ELIGIBILITY_COL,
                operator="equals",
                value=ELIGIBILE_VALUE,
                how="any",
            ),
            ColumnFilter(
                column=MAX_CNV_PROBABILITY_COL_PREFIX,
                operator="<=",
                value=self.cnv_threshold,
                how="all",
            ),
        ]

    def update_renamed_columns(self) -> None:
        """Update the renamed columns."""
        if self.renamed_columns:
            renamed_static_cols = []
            for col in self._static_cols:
                if col in self.renamed_columns.keys():
                    renamed_static_cols.append(self.renamed_columns[col])
                else:
                    renamed_static_cols.append(col)
            self._static_cols = renamed_static_cols

            renamed_paired_cols_list = []
            for col in self._paired_col_prefixes:
                if col in self.renamed_columns.keys():
                    renamed_paired_cols_list.append(self.renamed_columns[col])
                else:
                    renamed_paired_cols_list.append(col)
            self._paired_col_prefixes = renamed_paired_cols_list

            if self.dob_col in self.renamed_columns.keys():
                self.dob_col = self.renamed_columns[self.dob_col]
            if self.name_col in self.renamed_columns.keys():
                self.name_col = self.renamed_columns[self.name_col]
            if self.total_ga_area in self.renamed_columns.keys():
                self.total_ga_area = self.renamed_columns[self.total_ga_area]
            if self.largest_legion_size in self.renamed_columns.keys():
                self.largest_legion_size = self.renamed_columns[
                    self.largest_legion_size
                ]
            if self.max_cnv_probability in self.renamed_columns.keys():
                self.max_cnv_probability = self.renamed_columns[
                    self.max_cnv_probability
                ]
            if self.age_col in self.renamed_columns.keys():
                self.age_col = self.renamed_columns[self.age_col]
            if self.scan_date_col in self.renamed_columns.keys():
                self.scan_date_col = self.renamed_columns[self.scan_date_col]
            if self.bitfount_patient_id in self.renamed_columns.keys():
                self.bitfount_patient_id = self.renamed_columns[
                    self.bitfount_patient_id
                ]

    def run(
        self,
        matched_csv_path: Path,
    ) -> tuple[int, int, int]:
        """Finds number of patients that match the clinical criteria.

        Args:
            matched_csv_path: The path to the CSV containing matched patient info.

        Returns:
            A tuple of counts of patients that match the clinical criteria.
            Tuple is of form (match criteria, don't match criteria).
        """
        self.update_renamed_columns()
        # Get the dataframe from the CSV file
        df = self._get_df_for_criteria(matched_csv_path)

        # Calculate age from DoB
        df = self._add_age_col(df)
        # Get the number of patients for which we have scans for both eyes
        number_of_patients_matched_eyes_records = len(
            df[self.bitfount_patient_id].unique()
        )
        # number of patients for which the ophthalmology trial criteria has been met
        number_of_patients_with_matching_ophthalmology_criteria = len(
            df[df[ELIGIBILITY_COL] == ELIGIBILE_VALUE][
                self.bitfount_patient_id
            ].unique()
        )
        number_excluded_due_to_eye_criteria = (
            number_of_patients_matched_eyes_records
            - number_of_patients_with_matching_ophthalmology_criteria
        )
        matched_df, _ = self._filter_by_criteria(df)
        if not matched_df.empty:
            num_patients_matching_all_criteria = len(
                matched_df[self.bitfount_patient_id].unique()
            )
        else:
            num_patients_matching_all_criteria = 0
        number_of_patients_excluded_due_to_age = (
            number_of_patients_with_matching_ophthalmology_criteria
            - num_patients_matching_all_criteria
        )
        return (
            num_patients_matching_all_criteria,
            number_excluded_due_to_eye_criteria,
            number_of_patients_excluded_due_to_age,
        )

    def _add_age_col(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add age column to the dataframe based on the DOB column.

        Args:
            df: the original dataframe

        Returns:
            The same dataframe with the extra age column.
        """
        # This will be set post _get_df_for_criteria()
        assert self._paired_cols is not None  # nosec[assert_used]

        # TODO: [NO_TICKET: Imported from ophthalmology] This needs to happen across
        #       two cols atm as it's included in the post-merge suffixing; should
        #       ideally just be the one column
        # df[_DOB_COL] = pd.to_datetime(df[_DOB_COL], utc=True)
        # now = pd.to_datetime("now", utc=True)
        # # This gets us the year-only element of the timedelta (i.e. age)
        # df[_AGE_COL] = (now - df[_DOB_COL]).astype("timedelta64[Y]")  # type: ignore[operator] # Reason: df["dob"] is a Series[Timestamp], so this works # noqa: E501
        now = pd.to_datetime("now", utc=True)
        for dob_col in self._paired_cols[self.dob_col]:
            df[dob_col] = pd.to_datetime(df[dob_col], utc=True)

            dob_col_suffix = dob_col[len(self.dob_col) :]  # e.g. _L or _R
            age_col = f"{AGE_COL}{dob_col_suffix}"
            self._paired_cols[AGE_COL].append(age_col)

            # This gets us the year-only element of the timedelta (i.e. age)
            try:
                age_series: pd.Series[int] = calculate_ages(df[dob_col], now)
            except OverflowError:
                # If the difference in time is too large, we will get an OverflowError.
                # This should only happen when the DOB is unknown and set to
                # `pd.Timestamp.min` as a placeholder.
                age_series = (
                    now.to_pydatetime() - df[dob_col].dt.to_pydatetime()
                ) / datetime.timedelta(days=365.25)

            df[age_col] = age_series
        return df

    def _get_df_for_criteria(self, matched_csv_path: Path) -> pd.DataFrame:
        """Gets a dataframe from a CSV file but only the columns we care about."""
        # This file could be very large, so we read it in chunk-wise, drop the columns
        # we don't care about, and concatenate
        filtered_chunks: list[pd.DataFrame] = []
        for chunk in pd.read_csv(matched_csv_path, chunksize=100, index_col=False):
            chunk = cast(pd.DataFrame, chunk)
            chunk = self._filter_chunk(chunk)
            filtered_chunks.append(chunk)
        return pd.concat(filtered_chunks, axis="index", ignore_index=True)

    def _filter_chunk(self, chunk: pd.DataFrame) -> pd.DataFrame:
        """Filters out columns from a chunk that we don't need."""
        # If we've not found the paired columns yet, find them
        if self._paired_cols is None:
            paired_cols = defaultdict(list)

            # Find the set of columns that start with any of the
            # self._paired_col_prefixes strings.
            #
            # Map them to the prefix they matched against.
            for col in chunk.columns:
                col_str = str(col)
                for col_prefix in self._paired_col_prefixes:
                    if col_str.startswith(col_prefix):
                        logger.debug(f"Found paired col {col_str}")
                        paired_cols[col_prefix].append(col_str)
            self._paired_cols = paired_cols
            logger.debug(f"Paired cols are: {self._get_all_paired_cols()}")

        # Return only the subset of the chunk that correspond to the columns we
        # care about
        col_list: list[str] = [*self._static_cols, *self._get_all_paired_cols()]

        try:
            return chunk[col_list]
        except KeyError as ke:
            raise DataProcessingError(
                f"Unable to extract expected columns from matched CSV: {ke}"
            ) from ke

    def _filter_by_criteria(self, df: pd.DataFrame) -> tuple[pd.DataFrame, set[str]]:
        """Filter the dataframe based on the clinical criteria."""
        assert self._paired_cols is not None  # nosec[assert_used]
        # Establish which rows fit all the criteria
        match_rows: dict[str, pd.Series] = {}
        bitfount_patient_id_set: set[str] = set()
        for _idx, row in df.iterrows():
            bitfount_patient_id: str = str(
                row[self._paired_cols[self.bitfount_patient_id]].iloc[0]
            )
            bitfount_patient_id_set.add(bitfount_patient_id)

            # 2.5 < Total GA area < 17.5
            ga_area_entries = row[self._paired_cols[self.total_ga_area]]
            # TODO: [NO_TICKET: Imported from ophthalmology] Should this be `any()`
            #       or `all()`
            if not (
                (ga_area_entries > TOTAL_GA_AREA_LOWER_BOUND)
                & (ga_area_entries < TOTAL_GA_AREA_UPPER_BOUND)
            ).any():
                logger.debug(
                    f"Patient {bitfount_patient_id} excluded due to"
                    f" total GA area being out of bounds"
                )
                continue

            # Largest GA lesion > 1.26
            ga_lesion_entries = row[self._paired_cols[self.largest_legion_size]]
            # TODO: [NO_TICKET: Imported from ophthalmology] Should this be `any()`
            #       or `all()`
            if not (ga_lesion_entries > LARGEST_GA_LESION_LOWER_BOUND).any():
                logger.debug(
                    f"Patient {bitfount_patient_id} excluded due to"
                    f" largest GA lesion size being smaller than target"
                )
                continue

            # Neither eye has CNV
            cnv_entries = row[self._paired_cols[self.max_cnv_probability]]
            if (cnv_entries >= CNV_THRESHOLD).any():
                logger.debug(
                    f"Patient {bitfount_patient_id} excluded due to"
                    f" CNV in one or both eyes"
                )
                continue

            # Age >= 60
            age_entries = row[self._paired_cols[self.age_col]]
            if not (age_entries >= PATIENT_AGE_LOWER_BOUND).any():
                logger.debug(f"Patient {bitfount_patient_id} excluded due to age")
                continue

            # If we reach here, all criteria have been matched
            logger.debug(
                f"Patient {bitfount_patient_id} included: matches all criteria"
            )

            # Keep the latest row for each patient
            existing_row = match_rows.get(bitfount_patient_id)
            existing_row_scan_date_entries = (
                existing_row[self._paired_cols[self.scan_date_col]]
                if existing_row is not None
                else None
            )
            new_row_scan_date_entries = row[self._paired_cols[self.scan_date_col]]
            # No need to parse Scan dates to date as with ISO timestamp strings
            # lexicographical order is equivalent to chronological order
            if (
                existing_row_scan_date_entries is None
                or (existing_row_scan_date_entries <= new_row_scan_date_entries).any()
            ):
                match_rows[bitfount_patient_id] = row

        # Create new dataframe from the matched rows
        return pd.DataFrame(match_rows.values()), bitfount_patient_id_set


class TrialInclusionCriteriaMatchAlgorithmJade(BaseAlgorithmFactory):
    """Algorithm for establishing number of patients that match clinical criteria."""

    fields_dict: ClassVar[T_FIELDS_DICT] = {
        "renamed_columns": fields.Dict(
            keys=fields.Str(), values=fields.Str(), allow_none=True
        ),
    }

    def __init__(
        self,
        renamed_columns: Optional[Mapping[str, str]] = None,
        **kwargs: Any,
    ) -> None:
        self.renamed_columns = renamed_columns
        super().__init__(**kwargs)

    def modeller(self, **kwargs: Any) -> NoResultsModellerAlgorithm:
        """Modeller-side of the algorithm."""
        return NoResultsModellerAlgorithm(
            log_message="Running Trial Inclusion Criteria Match Algorithm",
            **kwargs,
        )

    def worker(self, **kwargs: Any) -> _WorkerSide:
        """Worker-side of the algorithm."""
        return _WorkerSide(renamed_columns=self.renamed_columns, **kwargs)


# TODO: [NO_TICKET: Imported from ophthalmology] Move to a common exceptions module,
#       maybe in the main repo
class DataProcessingError(BitfountError):
    """Error related to data processing.

    This is distinct from DataSourceError, as it is related to later processing
    of the data.
    """

    pass


# Kept for backwards compatibility
@deprecated_class_name
class TrialInclusionCriteriaMatchAlgorithm(TrialInclusionCriteriaMatchAlgorithmJade):
    """Algorithm for establishing number of patients that match clinical criteria."""

    pass
