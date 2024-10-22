"""Useful types for Federated Learning."""

from __future__ import annotations

from enum import Enum, auto
from typing import (
    TYPE_CHECKING,
    Optional,
    Protocol,
    TypedDict,
    Union,
    runtime_checkable,
)

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from typing_extensions import NotRequired, TypeAlias

from bitfount.types import _StrAnyDict

if TYPE_CHECKING:
    from bitfount.hub.api import BitfountHub


class TextGenerationDictionary(TypedDict):
    """Hugging Face dictionary response for text generation."""

    generated_text: str


class HuggingFaceImageClassificationInferenceDictionary(TypedDict):
    """Hugging Face dictionary response for image classification."""

    image_classification: str


TextGenerationDefaultReturnType: TypeAlias = list[list[TextGenerationDictionary]]


class SerializedModel(TypedDict):
    """Serialized representation of a model."""

    class_name: str
    hub: NotRequired[Optional[BitfountHub]]
    schema: NotRequired[_StrAnyDict]


class SerializedAlgorithm(TypedDict):
    """Serialized representation of an algorithm."""

    class_name: str  # value from AlgorithmType enum
    model: NotRequired[SerializedModel]


class SerializedAggregator(TypedDict):
    """Serialized representation of an aggregator."""

    class_name: str  # value from AggregatorType enum


class SerializedProtocol(TypedDict):
    """Serialized representation of a protocol."""

    class_name: str  # value from ProtocolType enum
    algorithm: Union[SerializedAlgorithm, list[SerializedAlgorithm]]
    aggregator: NotRequired[SerializedAggregator]


class ProtocolType(Enum):
    """Available protocol names from `bitfount.federated.protocol`."""

    FederatedAveraging = "bitfount.FederatedAveraging"
    ResultsOnly = "bitfount.ResultsOnly"
    Conversation = "bitfount.Conversation"
    InferenceAndCSVReport = "bitfount.InferenceAndCSVReport"
    InstrumentedInferenceAndCSVReport = "bitfount.InstrumentedInferenceAndCSVReport"
    InferenceAndReturnCSVReport = "bitfount.InferenceAndReturnCSVReport"
    # Ophthalmology Protocols
    GAScreeningProtocolAmethyst = "bitfount.GAScreeningProtocolAmethyst"
    GAScreeningProtocolJade = "bitfount.GAScreeningProtocolJade"
    GAScreeningProtocol = (
        "bitfount.GAScreeningProtocol"  # Kept for backwards compatibility
    )
    RetinalDiseaseProtocolCobalt = "bitfount.RetinalDiseaseProtocolCobalt"
    BasicOCTProtocol = "bitfount.BasicOCTProtocol"  # Kept for backwards compatibility


class AlgorithmType(Enum):
    """Available algorithm names from `bitfount.federated.algorithm`."""

    FederatedModelTraining = "bitfount.FederatedModelTraining"
    ModelTrainingAndEvaluation = "bitfount.ModelTrainingAndEvaluation"
    ModelEvaluation = "bitfount.ModelEvaluation"
    ModelInference = "bitfount.ModelInference"
    SqlQuery = "bitfount.SqlQuery"
    PrivateSqlQuery = "bitfount.PrivateSqlQuery"
    HuggingFacePerplexityEvaluation = "bitfount.HuggingFacePerplexityEvaluation"
    HuggingFaceTextGenerationInference = "bitfount.HuggingFaceTextGenerationInference"
    HuggingFaceImageClassificationInference = (
        "bitfount.HuggingFaceImageClassificationInference"
    )
    HuggingFaceImageSegmentationInference = (
        "bitfount.HuggingFaceImageSegmentationInference"
    )
    HuggingFaceTextClassificationInference = (
        "bitfount.HuggingFaceTextClassificationInference"
    )
    HuggingFaceZeroShotImageClassificationInference = (
        "bitfount.HuggingFaceZeroShotImageClassificationInference"
    )
    CSVReportAlgorithm = "bitfount.CSVReportAlgorithm"
    TIMMFineTuning = "bitfount.TIMMFineTuning"
    TIMMInference = "bitfount.TIMMInference"
    # Ophthalmology Algorithms
    CSVReportGeneratorOphthalmologyAlgorithm = (
        "bitfount.CSVReportGeneratorOphthalmologyAlgorithm"
    )
    CSVReportGeneratorAlgorithm = (
        "bitfount.CSVReportGeneratorAlgorithm"  # Kept for backwards compatibility
    )
    ETDRSAlgorithm = "bitfount.ETDRSAlgorithm"
    FoveaCoordinatesAlgorithm = "bitfount.FoveaCoordinatesAlgorithm"
    GATrialCalculationAlgorithmJade = "bitfount.GATrialCalculationAlgorithmJade"
    GATrialCalculationAlgorithm = (
        "bitfount.GATrialCalculationAlgorithm"  # Kept for backwards compatibility
    )
    TrialInclusionCriteriaMatchAlgorithmAmethyst = (
        "bitfount.TrialInclusionCriteriaMatchAlgorithmAmethyst"
    )
    TrialInclusionCriteriaMatchAlgorithmJade = (
        "bitfount.TrialInclusionCriteriaMatchAlgorithmJade"
    )
    TrialInclusionCriteriaMatchAlgorithm = "bitfount.TrialInclusionCriteriaMatchAlgorithm"  # Kept for backwards compatibility # noqa: E501
    GATrialPDFGeneratorAlgorithmAmethyst = (
        "bitfount.GATrialPDFGeneratorAlgorithmAmethyst"
    )
    GATrialPDFGeneratorAlgorithmJade = "bitfount.GATrialPDFGeneratorAlgorithmJade"
    GATrialPDFGeneratorAlgorithm = (
        "bitfount.GATrialPDFGeneratorAlgorithm"  # Kept for backwards compatibility
    )
    _SimpleCSVAlgorithm = "bitfount._SimpleCSVAlgorithm"


class AggregatorType(Enum):
    """Available aggregator names from `bitfount.federated.aggregator`."""

    Aggregator = "bitfount.Aggregator"
    SecureAggregator = "bitfount.SecureAggregator"


class _PodResponseType(Enum):
    """Pod response types sent to `Modeller` on a training job request.

    Responses correspond to those from /api/access.
    """

    ACCEPT = auto()
    NO_ACCESS = auto()
    INVALID_PROOF_OF_IDENTITY = auto()
    UNAUTHORISED = auto()
    NO_PROOF_OF_IDENTITY = auto()
    NO_DATA = auto()


class _DataLessAlgorithm:
    """Base algorithm class for tagging purposes.

    Used in algorithms for which data loading is done at runtime.
    """

    ...


_RESPONSE_MESSAGES = {
    # /api/access response messages
    _PodResponseType.ACCEPT: "Job accepted",
    _PodResponseType.NO_ACCESS: "There are no permissions for this modeller/pod combination.",  # noqa: E501
    _PodResponseType.INVALID_PROOF_OF_IDENTITY: "Unable to verify identity; ensure correct login used.",  # noqa: E501
    _PodResponseType.UNAUTHORISED: "Insufficient permissions for the requested task on this pod.",  # noqa: E501
    _PodResponseType.NO_PROOF_OF_IDENTITY: "Unable to verify identity, please try again.",  # noqa: E501
    _PodResponseType.NO_DATA: "No data available for the requested task.",
}


@runtime_checkable
class _TaskRequestMessageGenerator(Protocol):
    """Callback protocol describing a task request message generator."""

    def __call__(
        self,
        serialized_protocol: SerializedProtocol,
        pod_identifiers: list[str],
        aes_key: bytes,
        pod_public_key: RSAPublicKey,
        project_id: Optional[str],
        run_on_new_data_only: bool = False,
        batched_execution: Optional[bool] = None,
    ) -> bytes:
        """Function signature for the callback."""
        ...
