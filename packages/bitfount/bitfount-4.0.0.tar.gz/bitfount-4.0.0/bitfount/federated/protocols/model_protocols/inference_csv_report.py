"""Protocol for combinging a single model inference and a csv algorithm."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import os
import time
from typing import (
    TYPE_CHECKING,
    Any,
    Optional,
    Protocol,
    Union,
    cast,
    runtime_checkable,
)

import pandas as pd

from bitfount.data.datasources.utils import ORIGINAL_FILENAME_METADATA_COLUMN
from bitfount.federated.algorithms.csv_report_algorithm import (
    _WorkerSide as _CSVWorkerSide,
)
from bitfount.federated.algorithms.model_algorithms.base import (
    _BaseWorkerModelAlgorithm,
)
from bitfount.federated.logging import _get_federated_logger
from bitfount.federated.pod_vitals import _PodVitals
from bitfount.federated.protocols.base import (
    BaseCompatibleAlgoFactory,
    BaseCompatibleModellerAlgorithm,
    BaseCompatibleWorkerAlgorithm,
    BaseModellerProtocol,
    BaseProtocolFactory,
    BaseWorkerProtocol,
)
from bitfount.federated.transport.modeller_transport import (
    _ModellerMailbox,
)
from bitfount.federated.transport.worker_transport import (
    _WorkerMailbox,
)
from bitfount.types import (
    DistributedModelProtocol,
    PredictReturnType,
    _SerializedWeights,
    _StrAnyDict,
)

if TYPE_CHECKING:
    from bitfount.federated.model_reference import BitfountModelReference
    from bitfount.hub.api import BitfountHub


logger = _get_federated_logger("bitfount.federated.protocols" + __name__)


@runtime_checkable
class _InferenceAndCSVReportCompatibleModellerAlgorithm(
    BaseCompatibleModellerAlgorithm, Protocol
):
    """Defines modeller-side algorithm compatibility."""

    def run(self, results: Mapping[str, Any]) -> _StrAnyDict:
        """Runs the modeller-side algorithm."""
        ...


@runtime_checkable
class _InferenceAndCSVReportCompatibleWorkerAlgorithm(
    BaseCompatibleWorkerAlgorithm, Protocol
):
    """Defines worker-side algorithm compatibility."""

    pass


@runtime_checkable
class _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm(
    _InferenceAndCSVReportCompatibleWorkerAlgorithm, Protocol
):
    """Defines worker-side algorithm compatibility without model params."""

    def run(self, *, return_data_keys: bool = False, final_batch: bool = False) -> Any:
        """Runs the worker-side algorithm."""
        ...


@runtime_checkable
class _InferenceAndCSVReportModelCompatibleWorkerAlgorithm(
    _InferenceAndCSVReportCompatibleWorkerAlgorithm, Protocol
):
    """Defines worker-side algorithm compatibility with model params needed."""

    def run(
        self,
        model_params: _SerializedWeights,
        *,
        return_data_keys: bool = False,
    ) -> Any:
        """Runs the worker-side algorithm."""
        ...


@runtime_checkable
class _InferenceAndCSVReportCSVCompatibleWorkerAlgorithm(
    _InferenceAndCSVReportCompatibleWorkerAlgorithm, Protocol
):
    """Defines worker-side algorithm compatibility for CSV algorithm."""

    def run(
        self,
        results_df: Union[pd.DataFrame, list[pd.DataFrame]],
        task_id: Optional[str] = None,
    ) -> str:
        """Runs the worker-side algorithm."""
        ...


class _ModellerSide(BaseModellerProtocol):
    """Modeller side of the protocol.

    Args:
        algorithm: A list of algorithms to be run by the protocol. This should be
            a list of two algorithms, the first being the model inference algorithm
            and the second being the csv report algorithm.
        mailbox: The mailbox to use for communication with the Workers.
        **kwargs: Additional keyword arguments.
    """

    algorithm: Sequence[_InferenceAndCSVReportCompatibleModellerAlgorithm]

    def __init__(
        self,
        *,
        algorithm: Sequence[_InferenceAndCSVReportCompatibleModellerAlgorithm],
        mailbox: _ModellerMailbox,
        **kwargs: Any,
    ):
        super().__init__(algorithm=algorithm, mailbox=mailbox, **kwargs)

    async def run(
        self,
        iteration: int = 0,
        *,
        results_from_worker: bool = False,
        **kwargs: Any,
    ) -> Optional[_StrAnyDict]:
        """Runs Modeller side of the protocol.

        This just sends the model parameters to the workers and then tells
        the workers when the protocol is finished.
        """

        results = await self.mailbox.get_evaluation_results_from_workers()
        return None if not results_from_worker else results


class _WorkerSide(BaseWorkerProtocol):
    """Worker side of the protocol.

    Args:
        algorithm: A list of algorithms to be run by the protocol. This should be
            a list of two algorithms, the first being the model inference algorithm
            and the second being the csv report algorithm.
        mailbox: The mailbox to use for communication with the Modeller.
        **kwargs: Additional keyword arguments.
    """

    algorithm: Sequence[
        Union[
            _InferenceAndCSVReportModelCompatibleWorkerAlgorithm,
            _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm,
            _InferenceAndCSVReportCSVCompatibleWorkerAlgorithm,
        ]
    ]

    def __init__(
        self,
        *,
        algorithm: Sequence[
            Union[
                _InferenceAndCSVReportModelCompatibleWorkerAlgorithm,
                _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm,
                _InferenceAndCSVReportCSVCompatibleWorkerAlgorithm,
            ]
        ],
        mailbox: _WorkerMailbox,
        **kwargs: Any,
    ):
        super().__init__(algorithm=algorithm, mailbox=mailbox, **kwargs)

    async def run(
        self,
        pod_vitals: Optional[_PodVitals] = None,
        *,
        return_results_to_modeller: bool = False,
        **kwargs: Any,
    ) -> pd.DataFrame:
        """Runs the algorithm on worker side."""
        final_batch: bool = kwargs.get("final_batch", False)
        # Unpack the algorithm into the two algorithms
        model_inference_algo, csv_report_algo = self.algorithm

        if pod_vitals:
            pod_vitals.last_task_execution_time = time.time()

        # Run Inference Algorithm
        logger.info("Running model inference algorithm")
        model_predictions: Union[PredictReturnType, pd.DataFrame]
        if isinstance(model_inference_algo, _BaseWorkerModelAlgorithm):
            model_predictions = model_inference_algo.run(
                return_data_keys=True, final_batch=final_batch
            )
        else:
            assert not isinstance(  # nosec[assert_used]
                model_inference_algo, _CSVWorkerSide
            )
            model_inference_algo = cast(
                _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm,
                model_inference_algo,
            )
            model_predictions = model_inference_algo.run(
                return_data_keys=True, final_batch=final_batch
            )

        # Output will either be a dataframe (if model_inference_algo.class_outputs is
        # set), or a PredictReturnType, which may have the predictions stored as a
        # dataframe.
        model_predictions_df: pd.DataFrame
        if isinstance(model_predictions, PredictReturnType):
            if isinstance(model_predictions.preds, pd.DataFrame):
                model_predictions_df = model_predictions.preds
            else:
                raise TypeError(
                    f"Model prediction must return a Dataframe"
                    f" to enable CSV report output;"
                    f" got {type(model_predictions)}"
                    f" with {type(model_predictions.preds)} predictions instead."
                )

            # Add keys to DataFrame
            if model_predictions.keys is not None:
                model_predictions_df[ORIGINAL_FILENAME_METADATA_COLUMN] = (
                    model_predictions.keys
                )
        else:  # is DataFrame
            model_predictions_df = model_predictions

        # Run CSV Report Generation
        logger.info("Running CSV report algorithm")
        csv_report_algo = cast(_CSVWorkerSide, csv_report_algo)
        csv_formatted_predictions = csv_report_algo.run(
            results_df=model_predictions_df,
            task_id=self.mailbox._task_id,
        )

        if return_results_to_modeller:
            # Sends results to modeller if enabled.
            await self.mailbox.send_evaluation_results(
                {"csv": csv_formatted_predictions}
            )
        else:
            # Sends empty results to modeller just to inform it to move on to the
            # next algorithm.
            await self.mailbox.send_evaluation_results()

        # Return the model_predictions from the model inference
        # algorithm so we can enable saving to the project database
        # for this protocol type
        return model_predictions_df


@runtime_checkable
class _InferenceAndCSVReportCompatibleAlgoFactory(BaseCompatibleAlgoFactory, Protocol):
    """Defines algo factory compatibility."""

    def modeller(
        self, **kwargs: Any
    ) -> _InferenceAndCSVReportCompatibleModellerAlgorithm:
        """Create a modeller-side algorithm."""
        ...


@runtime_checkable
class _InferenceAndCSVReportCompatibleAlgoFactory_(
    _InferenceAndCSVReportCompatibleAlgoFactory, Protocol
):
    """Defines algo factory compatibility."""

    def worker(
        self, **kwargs: Any
    ) -> Union[
        _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm,
        _InferenceAndCSVReportModelCompatibleWorkerAlgorithm,
    ]:
        """Create a worker-side algorithm."""
        ...


@runtime_checkable
class _InferenceAndCSVReportCompatibleHuggingFaceAlgoFactory(
    _InferenceAndCSVReportCompatibleAlgoFactory, Protocol
):
    """Defines algo factory compatibility."""

    model_id: str

    def worker(
        self, hub: BitfountHub, **kwargs: Any
    ) -> Union[
        _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm,
        _InferenceAndCSVReportModelCompatibleWorkerAlgorithm,
    ]:
        """Create a worker-side algorithm."""
        ...


@runtime_checkable
class _InferenceAndCSVReportCompatibleModelAlgoFactory(
    _InferenceAndCSVReportCompatibleAlgoFactory, Protocol
):
    """Defines algo factory compatibility."""

    model: Union[DistributedModelProtocol, BitfountModelReference]
    pretrained_file: Optional[Union[str, os.PathLike]] = None

    def worker(
        self, hub: BitfountHub, **kwargs: Any
    ) -> Union[
        _InferenceAndCSVReportModelIncompatibleWorkerAlgorithm,
        _InferenceAndCSVReportModelCompatibleWorkerAlgorithm,
    ]:
        """Create a worker-side algorithm."""
        ...


class InferenceAndCSVReport(BaseProtocolFactory):
    """Protocol for running a model inference generating a csv report."""

    def __init__(
        self,
        *,
        algorithm: Sequence[
            Union[
                _InferenceAndCSVReportCompatibleAlgoFactory_,
                _InferenceAndCSVReportCompatibleModelAlgoFactory,
                _InferenceAndCSVReportCompatibleHuggingFaceAlgoFactory,
            ]
        ],
        **kwargs: Any,
    ) -> None:
        super().__init__(algorithm=algorithm, **kwargs)

    @classmethod
    def _validate_algorithm(cls, algorithm: BaseCompatibleAlgoFactory) -> None:
        """Validates the algorithm."""
        if algorithm.class_name not in (
            "bitfount.ModelInference",
            "bitfount.HuggingFaceImageClassificationInference",
            "bitfount.HuggingFaceImageSegmentationInference",
            "bitfount.HuggingFaceZeroShotImageClassificationInference",
            "bitfount.HuggingFaceTextClassificationInference",
            "bitfount.HuggingFaceTextGenerationInference",
            "bitfount.HuggingFacePerplexityEvaluation",
            "bitfount.CSVReportAlgorithm",
            "bitfount.TIMMInference",
        ):
            raise TypeError(
                f"The {cls.__name__} protocol does not support "
                + f"the {type(algorithm).__name__} algorithm.",
            )

    def modeller(self, mailbox: _ModellerMailbox, **kwargs: Any) -> _ModellerSide:
        """Returns the Modeller side of the protocol."""
        algorithms = cast(
            Sequence[
                Union[
                    _InferenceAndCSVReportCompatibleAlgoFactory_,
                    _InferenceAndCSVReportCompatibleModelAlgoFactory,
                    _InferenceAndCSVReportCompatibleHuggingFaceAlgoFactory,
                ]
            ],
            self.algorithms,
        )
        modeller_algos = []
        for algo in algorithms:
            if hasattr(algo, "pretrained_file"):
                modeller_algos.append(
                    algo.modeller(pretrained_file=algo.pretrained_file)
                )
            else:
                modeller_algos.append(algo.modeller())
        return _ModellerSide(
            algorithm=modeller_algos,
            mailbox=mailbox,
            **kwargs,
        )

    def worker(
        self, mailbox: _WorkerMailbox, hub: BitfountHub, **kwargs: Any
    ) -> _WorkerSide:
        """Returns worker side of the protocol."""
        algorithms = cast(
            Sequence[
                Union[
                    _InferenceAndCSVReportCompatibleAlgoFactory_,
                    _InferenceAndCSVReportCompatibleModelAlgoFactory,
                    _InferenceAndCSVReportCompatibleHuggingFaceAlgoFactory,
                ]
            ],
            self.algorithms,
        )
        return _WorkerSide(
            algorithm=[algo.worker(hub=hub) for algo in algorithms],
            mailbox=mailbox,
            **kwargs,
        )
