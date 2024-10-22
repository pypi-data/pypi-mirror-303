"""Algorithm for establishing number of results that match a given criteria."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING, Any, ClassVar, Optional

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
    CNV_THRESHOLD,
    LARGEST_GA_LESION_LOWER_BOUND,
    LARGEST_LEGION_SIZE_COL_PREFIX,
    MAX_CNV_PROBABILITY_COL_PREFIX,
    NAME_COL,
    TOTAL_GA_AREA_COL_PREFIX,
    TOTAL_GA_AREA_LOWER_BOUND,
    TOTAL_GA_AREA_UPPER_BOUND,
    ColumnFilter,
)
from bitfount.federated.logging import _get_federated_logger

if TYPE_CHECKING:
    from bitfount.federated.privacy.differential import DPPodConfig
    from bitfount.types import T_FIELDS_DICT


logger = _get_federated_logger("bitfount.federated")

# This algorithm is designed to find patients that match a set of clinical criteria.
# The criteria are as follows:
# 1. Total GA area between TOTAL_GA_AREA_LOWER_BOUND and TOTAL_GA_AREA_UPPER_BOUND
# 2. Largest GA lesion size greater than LARGEST_GA_LESION_LOWER_BOUND
# 3. No CNV (CNV probability less than CNV_THRESHOLD)


class _WorkerSide(BaseWorkerAlgorithm):
    """Worker side of the algorithm."""

    def __init__(
        self,
        cnv_threshold: float = CNV_THRESHOLD,
        largest_ga_lesion_lower_bound: float = LARGEST_GA_LESION_LOWER_BOUND,
        total_ga_area_lower_bound: float = TOTAL_GA_AREA_LOWER_BOUND,
        total_ga_area_upper_bound: float = TOTAL_GA_AREA_UPPER_BOUND,
        **kwargs: Any,
    ) -> None:
        self.cnv_threshold = cnv_threshold
        self.largest_ga_lesion_lower_bound = largest_ga_lesion_lower_bound
        self.total_ga_area_lower_bound = total_ga_area_lower_bound
        self.total_ga_area_upper_bound = total_ga_area_upper_bound
        super().__init__(**kwargs)

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
        dataframe: pd.DataFrame,
    ) -> tuple[int, int]:
        """Finds number of patients that match the clinical criteria.

        Args:
            dataframe: The dataframe to process.

        Returns:
            A tuple of counts of patients that match the clinical criteria.
            Tuple is of form (match criteria, don't match criteria).
        """
        matched_df = self._filter_by_criteria(dataframe)
        num_matches = len(matched_df)
        return num_matches, len(dataframe) - num_matches

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

    def _filter_by_criteria(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter the dataframe based on the clinical criteria."""
        # Establish which rows fit all the criteria
        match_rows: list[pd.Series] = []
        for _idx, row in df.iterrows():
            # TODO: [NO_TICKET: Imported from ophthalmology] Do we need a better way
            #       of identifying this?
            patient_name: str = str(row[NAME_COL])
            patient_name_hash: str = hashlib.md5(patient_name.encode()).hexdigest()  # nosec[blacklist] # Reason: this is not a security use case

            # 2.5 < Total GA area < 17.5
            ga_area_entry = row[TOTAL_GA_AREA_COL_PREFIX]
            # TODO: [NO_TICKET: Imported from ophthalmology] Should this be `any()`
            #       or `all()`
            if not (
                (ga_area_entry > self.total_ga_area_lower_bound)
                & (ga_area_entry < self.total_ga_area_upper_bound)
            ):
                logger.debug(
                    f"Patient {patient_name_hash} excluded due to"
                    f" total GA area being out of bounds"
                )
                continue

            # Largest GA lesion > 1.26
            ga_lesion_entry = row[LARGEST_LEGION_SIZE_COL_PREFIX]
            # TODO: [NO_TICKET: Imported from ophthalmology] Should this be `any()`
            #       or `all()`
            if not (ga_lesion_entry > self.largest_ga_lesion_lower_bound):
                logger.debug(
                    f"Patient {patient_name_hash} excluded due to"
                    f" largest GA lesion size being smaller than target"
                )
                continue

            # Eye does not have CNV
            cnv_entry = row[MAX_CNV_PROBABILITY_COL_PREFIX]
            if cnv_entry >= self.cnv_threshold:
                logger.debug(
                    f"Patient {patient_name_hash} excluded due to"
                    f" CNV in one or both eyes"
                )
                continue

            # If we reach here, all criteria have been matched
            logger.debug(f"Patient {patient_name_hash} included: matches all criteria")
            match_rows.append(row)

        # Create new dataframe from the matched rows
        return pd.DataFrame(match_rows)


class TrialInclusionCriteriaMatchAlgorithmAmethyst(BaseAlgorithmFactory):
    """Algorithm for establishing number of patients that match clinical criteria."""

    fields_dict: ClassVar[T_FIELDS_DICT] = {
        "cnv_threshold": fields.Float(allow_none=True),
        "largest_ga_lesion_lower_bound": fields.Float(allow_none=True),
        "total_ga_area_lower_bound": fields.Float(allow_none=True),
        "total_ga_area_upper_bound": fields.Float(allow_none=True),
    }

    def __init__(
        self,
        cnv_threshold: float = CNV_THRESHOLD,
        largest_ga_lesion_lower_bound: float = LARGEST_GA_LESION_LOWER_BOUND,
        total_ga_area_lower_bound: float = TOTAL_GA_AREA_LOWER_BOUND,
        total_ga_area_upper_bound: float = TOTAL_GA_AREA_UPPER_BOUND,
        **kwargs: Any,
    ) -> None:
        self.cnv_threshold = cnv_threshold
        self.largest_ga_lesion_lower_bound = largest_ga_lesion_lower_bound
        self.total_ga_area_lower_bound = total_ga_area_lower_bound
        self.total_ga_area_upper_bound = total_ga_area_upper_bound
        super().__init__(**kwargs)

    def modeller(self, **kwargs: Any) -> NoResultsModellerAlgorithm:
        """Modeller-side of the algorithm."""
        return NoResultsModellerAlgorithm(
            log_message="Running Trial Inclusion Criteria Match Algorithm",
            **kwargs,
        )

    def worker(self, **kwargs: Any) -> _WorkerSide:
        """Worker-side of the algorithm."""
        return _WorkerSide(
            cnv_threshold=self.cnv_threshold,
            largest_ga_lesion_lower_bound=self.largest_ga_lesion_lower_bound,
            total_ga_area_lower_bound=self.total_ga_area_lower_bound,
            total_ga_area_upper_bound=self.total_ga_area_upper_bound,
            **kwargs,
        )


# TODO: [NO_TICKET: Imported from ophthalmology] Move to a common exceptions module,
#       maybe in the main repo
class DataProcessingError(BitfountError):
    """Error related to data processing.

    This is distinct from DataSourceError, as it is related to later processing
    of the data.
    """

    pass
