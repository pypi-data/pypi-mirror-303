"""Dataclasses to hold the configuration details for the runners."""

from __future__ import annotations

from collections.abc import Callable, Mapping, MutableMapping
from dataclasses import dataclass
from datetime import datetime
import logging
import os
from pathlib import Path
import typing
from typing import Any, Final, Optional, Union, cast

import desert
from marshmallow import ValidationError, fields, validate
from marshmallow.validate import OneOf
from marshmallow_union import Union as M_Union

from bitfount.config import (
    _BITFOUNT_COMPATIBLE_YAML_VERSIONS,
    _DEVELOPMENT_ENVIRONMENT,
    _SANDBOX_ENVIRONMENT,
    _STAGING_ENVIRONMENT,
    BITFOUNT_DEFAULT_BATCHED_EXECUTION,
    _get_environment,
)
from bitfount.data.types import (
    DataPathModifiers,
    SchemaOverrideMapping,
    _ForceStypeValue,
    _SemanticTypeValue,
)
from bitfount.exceptions import BitfountVersionError
from bitfount.federated.algorithms.hugging_face_algorithms.hugging_face_perplexity import (  # noqa: E501
    DEFAULT_STRIDE,
)
from bitfount.federated.algorithms.hugging_face_algorithms.hugging_face_text_generation import (  # noqa: E501
    DEFAULT_MAX_LENGTH,
    DEFAULT_MIN_NEW_TOKENS,
    DEFAULT_NUM_BEAMS,
    DEFAULT_NUM_RETURN_SEQUENCES,
    DEFAULT_REPETITION_PENALTY,
)

# from bitfount.federated.algorithms.hugging_face_algorithms.timm_fine_tuning import (
#     _TimmBatchTransformationStep,
# )
from bitfount.federated.algorithms.hugging_face_algorithms.utils import (
    TIMMTrainingConfig,
)
from bitfount.federated.algorithms.ophthalmology.csv_report_generation_ophth_algorithm import (  # noqa: E501
    DFSortType,
    MatchPatientVisit,
)
from bitfount.federated.algorithms.ophthalmology.ophth_algo_types import (
    CNV_THRESHOLD,
    LARGEST_GA_LESION_LOWER_BOUND,
    TOTAL_GA_AREA_LOWER_BOUND,
    TOTAL_GA_AREA_UPPER_BOUND,
    ColumnFilter,
    OCTImageMetadataColumns,
    ReportMetadata,
    SLOImageMetadataColumns,
    SLOSegmentationLocationPrefix,
)
from bitfount.federated.authorisation_checkers import (
    DEFAULT_IDENTITY_VERIFICATION_METHOD,
    IDENTITY_VERIFICATION_METHODS,
)
from bitfount.federated.helper import POD_NAME_REGEX, USERNAME_REGEX
from bitfount.federated.privacy.differential import DPModellerConfig, DPPodConfig
from bitfount.federated.transport.config import (
    _DEV_MESSAGE_SERVICE_PORT,
    _DEV_MESSAGE_SERVICE_TLS,
    _DEV_MESSAGE_SERVICE_URL,
    _SANDBOX_MESSAGE_SERVICE_URL,
    _STAGING_MESSAGE_SERVICE_URL,
    MessageServiceConfig,
)
from bitfount.federated.types import AlgorithmType, ProtocolType
from bitfount.hub.authentication_handlers import _DEFAULT_USERNAME
from bitfount.hub.types import (
    _DEV_AM_URL,
    _DEV_HUB_URL,
    _DEV_IDP_URL,
    _PRODUCTION_IDP_URL,
    _SANDBOX_AM_URL,
    _SANDBOX_HUB_URL,
    _SANDBOX_IDP_URL,
    _STAGING_AM_URL,
    _STAGING_HUB_URL,
    _STAGING_IDP_URL,
    PRODUCTION_AM_URL,
    PRODUCTION_HUB_URL,
)
from bitfount.models.base_models import LoggerConfig
from bitfount.runners.utils import (
    get_concrete_config_subclasses,
    is_version_compatible_all,
    is_version_compatible_major_minor,
)
from bitfount.types import _JSONDict
from bitfount.utils import DEFAULT_SEED

_logger = logging.getLogger(__name__)


_DEFAULT_YAML_VERSION: Final[str] = "1.0.0"  # Default version is `1.0.0`
# so that unversioned yamls are still compatible with this version


@typing.overload
def _deserialize_path(path: str, context: dict[str, typing.Any]) -> Path: ...


@typing.overload
def _deserialize_path(path: None, context: dict[str, typing.Any]) -> None: ...


def _deserialize_path(
    path: Optional[str], context: dict[str, typing.Any]
) -> Optional[Path]:
    """Converts a str into a Path.

    If the input is None, the output is None.

    If the path to the config file is supplied in the `context` dict (in the
    "config_path" key) then any relative paths will be resolved relative to the
    directory containing the config file.
    """
    if path is None:
        return None

    ppath = Path(path)

    # If relative path, use relative to config file if present
    if not ppath.is_absolute() and "config_path" in context:
        config_dir = Path(context["config_path"]).parent
        orig_ppath = ppath
        ppath = config_dir.joinpath(ppath).resolve()
        _logger.debug(
            f"Making relative paths relative to {config_dir}: {orig_ppath} -> {ppath}"
        )

    return ppath.expanduser()


def _deserialize_model_ref(ref: str) -> Union[Path, str]:
    """Deserializes a model reference.

    If the reference is a path to a file (and that file exists), return a Path
    instance. Otherwise, returns the str reference unchanged.
    """
    path = Path(ref).expanduser()
    if path.is_file():  # also returns False if path doesn't exist
        return path
    else:
        return ref


# COMMON SCHEMAS
@dataclass
class AccessManagerConfig:
    """Configuration for the access manager."""

    url: str = desert.field(fields.URL(), default=PRODUCTION_AM_URL)


@dataclass
class HubConfig:
    """Configuration for the hub."""

    url: str = desert.field(fields.URL(), default=PRODUCTION_HUB_URL)


@dataclass
class APIKeys:
    """API keys for BitfountSession."""

    access_key_id: str = desert.field(fields.String())
    access_key: str = desert.field(fields.String())


@dataclass
class JWT:
    """Externally managed JWT for BitfountSession."""

    jwt: str = desert.field(fields.String())
    expires: datetime = desert.field(fields.DateTime())
    get_token: Callable[[], tuple[str, datetime]] = desert.field(fields.Function())


# POD SCHEMAS
@dataclass
class DataSplitConfig:
    """Configuration for the data splitter."""

    data_splitter: str = desert.field(
        fields.String(validate=OneOf(["percentage", "predefined"])),
        default="percentage",
    )
    args: _JSONDict = desert.field(fields.Dict(keys=fields.Str), default_factory=dict)


@dataclass
class PodDataConfig:
    """Configuration for the Schema, BaseSource and Pod.

    Args:
        force_stypes: The semantic types to force for the data. This is passed to the
            `BitfountSchema`. This should be a mapping from pod name to a mapping from
            the type to a list of column names
            (e.g. `{"pod_name": {categorical: ["col1", "col2"]}}`),
        ignore_cols: The columns to ignore. This is passed to the data source.
        modifiers: The modifiers to apply to the data. This is passed to the
            `BaseSource`.
        datasource_args: Key-value pairs of arguments to pass to the data source
            constructor.
        data_split: The data split configuration. This is passed to the data source.
        auto_tidy: Whether to automatically tidy the data. This is used by the
            `Pod` and will result in removal of NaNs and normalisation of numeric
            values. Defaults to False.
    """  # noqa: E501

    force_stypes: Optional[
        Mapping[
            str, MutableMapping[Union[_ForceStypeValue, _SemanticTypeValue], list[str]]
        ]
    ] = desert.field(
        fields.Dict(
            keys=fields.String(),
            values=fields.Dict(
                keys=fields.String(validate=OneOf(typing.get_args(_ForceStypeValue))),
                values=fields.List(fields.String()),
            ),
        ),
        default=None,
    )
    column_descriptions: Optional[Mapping[str, Mapping[str, str]]] = desert.field(
        fields.Dict(
            keys=fields.String(),
            values=fields.Dict(keys=fields.String(), values=fields.String()),
            default=None,
        ),
        default=None,
    )
    table_descriptions: Optional[Mapping[str, str]] = desert.field(
        fields.Dict(keys=fields.String(), values=fields.String(), default=None),
        default=None,
    )
    ignore_cols: Optional[Mapping[str, list[str]]] = desert.field(
        fields.Dict(keys=fields.String(), values=fields.List(fields.String())),
        default=None,
    )

    modifiers: Optional[dict[str, DataPathModifiers]] = desert.field(
        fields.Dict(
            keys=fields.Str,
            values=fields.Dict(
                keys=fields.String(
                    validate=OneOf(DataPathModifiers.__annotations__.keys())
                )
            ),
            default=None,
        ),
        default=None,
    )
    datasource_args: _JSONDict = desert.field(
        fields.Dict(keys=fields.Str), default_factory=dict
    )
    data_split: DataSplitConfig = desert.field(
        fields.Nested(desert.schema_class(DataSplitConfig)),
        default_factory=DataSplitConfig,
    )
    auto_tidy: bool = False


@dataclass
class PodDetailsConfig:
    """Configuration for the pod details.

    Args:
        display_name: The display name of the pod.
        description: The description of the pod.
    """

    display_name: str
    description: str = ""


@dataclass
class DatasourceConfig:
    """Datasource configuration for a multi-datasource Pod."""

    datasource: str
    data_config: PodDataConfig = desert.field(
        fields.Nested(desert.schema_class(PodDataConfig)),
        default_factory=PodDataConfig,
    )
    name: Optional[str] = desert.field(
        fields.String(validate=validate.Regexp(POD_NAME_REGEX)), default=None
    )
    datasource_details_config: Optional[PodDetailsConfig] = desert.field(
        fields.Nested(desert.schema_class(PodDetailsConfig)),
        default=None,
    )
    schema: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )


@dataclass
class PodDbConfig:
    """Configuration of the Pod DB."""

    path: Path = desert.field(fields.String())

    def __post_init__(self) -> None:
        self.path = _deserialize_path(path=cast(str, self.path), context={})


@dataclass
class PodConfig:
    """Full configuration for the pod.

    Raises:
        ValueError: If a username is not provided alongside API keys.
    """

    name: str = desert.field(fields.String(validate=validate.Regexp(POD_NAME_REGEX)))
    secrets: Optional[Union[APIKeys, JWT]] = desert.field(
        M_Union(
            [
                fields.Nested(desert.schema_class(APIKeys)),
                fields.Nested(desert.schema_class(JWT)),
            ]
        ),
        default=None,
    )
    pod_details_config: Optional[PodDetailsConfig] = None
    datasource: Optional[str] = desert.field(fields.String(), default=None)
    data_config: Optional[PodDataConfig] = desert.field(
        fields.Nested(desert.schema_class(PodDataConfig)),
        default=None,
    )
    schema: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    datasources: Optional[list[DatasourceConfig]] = desert.field(
        fields.List(fields.Nested(desert.schema_class(DatasourceConfig))),
        default=None,
    )
    access_manager: AccessManagerConfig = desert.field(
        fields.Nested(desert.schema_class(AccessManagerConfig)),
        default_factory=AccessManagerConfig,
    )
    hub: HubConfig = desert.field(
        fields.Nested(desert.schema_class(HubConfig)), default_factory=HubConfig
    )
    message_service: MessageServiceConfig = desert.field(
        fields.Nested(desert.schema_class(MessageServiceConfig)),
        default_factory=MessageServiceConfig,
    )
    differential_privacy: Optional[DPPodConfig] = None
    approved_pods: Optional[list[str]] = None
    username: str = desert.field(
        fields.String(validate=validate.Regexp(USERNAME_REGEX)),
        default=_DEFAULT_USERNAME,
    )
    update_schema: bool = False
    pod_db: Union[bool, PodDbConfig] = False
    # This is kept for backwards compatibility but is not used
    show_datapoints_with_results_in_db: bool = True
    version: Optional[str] = None

    def __post_init__(self) -> None:
        environment = _get_environment()
        if environment == _STAGING_ENVIRONMENT:
            _logger.warning(f"{environment=} detected; changing URLs in config")
            self.hub.url = _STAGING_HUB_URL
            self.access_manager.url = _STAGING_AM_URL
            self.message_service.url = _STAGING_MESSAGE_SERVICE_URL
        elif environment == _DEVELOPMENT_ENVIRONMENT:
            _logger.warning(
                f"{environment=} detected; changing URLs and ports in config"
            )
            self.hub.url = _DEV_HUB_URL
            self.access_manager.url = _DEV_AM_URL
            self.message_service.url = _DEV_MESSAGE_SERVICE_URL
            self.message_service.port = _DEV_MESSAGE_SERVICE_PORT
            self.message_service.tls = _DEV_MESSAGE_SERVICE_TLS
        elif environment == _SANDBOX_ENVIRONMENT:
            _logger.warning(f"{environment=} detected; changing URLs in config")
            self.hub.url = _SANDBOX_HUB_URL
            self.access_manager.url = _SANDBOX_AM_URL
            self.message_service.url = _SANDBOX_MESSAGE_SERVICE_URL
        if self.version is None:
            self.version = _DEFAULT_YAML_VERSION
        # datasource xor datasources must be defined
        if (self.datasource is None) == (self.datasources is None):
            raise ValueError(
                "You must either supply a datasource or a set of datasources"
            )

        # Use API Keys for authentication if provided
        if isinstance(self.secrets, APIKeys):
            if self.username == _DEFAULT_USERNAME:
                raise ValueError("Must specify a username when using API Keys.")

            _logger.info("Setting API Keys as environment variables.")

            if os.environ.get("BITFOUNT_API_KEY_ID") or os.environ.get(
                "BITFOUNT_API_KEY"
            ):
                _logger.warning(
                    "Existing environment variable API keys detected. Overriding with "
                    "those provided in the pod config."
                )
            os.environ["BITFOUNT_API_KEY_ID"] = self.secrets.access_key_id
            os.environ["BITFOUNT_API_KEY"] = self.secrets.access_key
        # If no plugins, we only check major/minor compatibility,
        # else we check patch as well
        # This first `if` needs to be removed after we only support
        # `datasources` for the pod config.
        if self.datasource:
            if self.datasource.startswith("bitfount"):
                compatible, message = is_version_compatible_major_minor(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "dataset"
                )
            else:
                compatible, message = is_version_compatible_all(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "dataset"
                )
        else:  # if datasources, check done a few lines prior
            if all(
                item.datasource.startswith("bitfount")
                for item in cast(list[DatasourceConfig], self.datasources)
            ):
                compatible, message = is_version_compatible_major_minor(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "dataset"
                )
            else:
                compatible, message = is_version_compatible_all(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "dataset"
                )
        if compatible:
            _logger.debug(message)
        else:
            # TODO: [BIT-3281] Revert back to raising error
            _logger.warning(message)

    @property
    def pod_id(self) -> str:
        """The pod ID of the pod specified."""
        return f"{self.username}/{self.name}"


@dataclass
class PathConfig:
    """Configuration for the path."""

    path: Path = desert.field(fields.Function(deserialize=_deserialize_path))


@dataclass
class DataStructureSelectConfig:
    """Configuration for the datastructure select argument."""

    include: list[str] = desert.field(
        fields.List(fields.String()), default_factory=list
    )
    include_prefix: Optional[str] = None
    exclude: list[str] = desert.field(
        fields.List(fields.String()), default_factory=list
    )


@dataclass
class DataStructureAssignConfig:
    """Configuration for the datastructure assign argument."""

    target: Optional[Union[str, list[str]]] = desert.field(
        M_Union([fields.String(), fields.List(fields.String())]), default=None
    )
    image_cols: Optional[list[str]] = None
    image_prefix: Optional[str] = None


@dataclass
class DataStructureTransformConfig:
    """Configuration for the datastructure transform argument."""

    dataset: Optional[list[dict[str, _JSONDict]]] = None
    batch: Optional[list[dict[str, _JSONDict]]] = None
    image: Optional[list[dict[str, _JSONDict]]] = None
    auto_convert_grayscale_images: bool = True


@dataclass
class DataStructureTableConfig:
    """Configuration for the datastructure table arguments."""

    table: Optional[Union[str, dict[str, str]]] = desert.field(
        M_Union(
            [
                fields.String(),
                fields.Dict(keys=fields.String(), values=fields.String(), default=None),
            ],
            # This 'allow_none' is needed to allow the value of 'None' and must be
            # within the M_Union. However, this makes the yaml spec incorrect as it
            # sets the type of the whole field to be null.
            allow_none=True,
        ),
        default=None,
    )
    query: Optional[Union[str, dict[str, str]]] = desert.field(
        M_Union(
            [
                fields.String(),
                fields.Dict(keys=fields.String(), values=fields.String(), default=None),
            ],
            # This 'allow_none' is needed to allow the value of 'None' and must be
            # within the M_Union. However, this makes the yaml spec incorrect as it
            # sets the type of the whole field to be null.
            allow_none=True,
        ),
        default=None,
    )
    schema_types_override: Optional[
        Union[SchemaOverrideMapping, Mapping[str, SchemaOverrideMapping]]
    ] = desert.field(
        fields.Dict(
            keys=fields.String(),
            values=fields.List(
                M_Union([fields.String(default=None), fields.Dict(default=None)])
            ),
            default=None,
            allow_none=True,
        ),
        default=None,
    )


@dataclass
class DataStructureConfig:
    """Configuration for the modeller schema and dataset options."""

    table_config: DataStructureTableConfig = desert.field(
        fields.Nested(desert.schema_class(DataStructureTableConfig)),
    )
    assign: DataStructureAssignConfig = desert.field(
        fields.Nested(desert.schema_class(DataStructureAssignConfig)),
        default_factory=DataStructureAssignConfig,
    )
    select: DataStructureSelectConfig = desert.field(
        fields.Nested(desert.schema_class(DataStructureSelectConfig)),
        default_factory=DataStructureSelectConfig,
    )
    transform: DataStructureTransformConfig = desert.field(
        fields.Nested(desert.schema_class(DataStructureTransformConfig)),
        default_factory=DataStructureTransformConfig,
    )
    data_split: Optional[DataSplitConfig] = desert.field(
        fields.Nested(desert.schema_class(DataSplitConfig)),
        default=None,
    )


# MODELLER SCHEMAS
@dataclass
class ModellerUserConfig:
    """Configuration for the modeller.

    Args:
        username: The username of the modeller. This can be picked up automatically
            from the session but can be overridden here.
        identity_verification_method: The method to use for identity verification.
            Accepts one of the values in `IDENTITY_VERIFICATION_METHODS`, i.e. one of
            `key-based`, `oidc-auth-code` or `oidc-device-code`.
        private_key_file: The path to the private key file for key-based identity
            verification.
    """

    username: str = desert.field(
        fields.String(validate=validate.Regexp(USERNAME_REGEX)),
        default=_DEFAULT_USERNAME,
    )

    identity_verification_method: str = desert.field(
        fields.String(validate=OneOf(IDENTITY_VERIFICATION_METHODS)),
        default=DEFAULT_IDENTITY_VERIFICATION_METHOD,
    )
    private_key_file: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )

    def __post_init__(self) -> None:
        environment = _get_environment()
        self._identity_provider_url: str

        if environment == _STAGING_ENVIRONMENT:
            self._identity_provider_url = _STAGING_IDP_URL
        elif environment == _DEVELOPMENT_ENVIRONMENT:
            self._identity_provider_url = _DEV_IDP_URL
        elif environment == _SANDBOX_ENVIRONMENT:
            self._identity_provider_url = _SANDBOX_IDP_URL
        else:
            self._identity_provider_url = _PRODUCTION_IDP_URL


@dataclass
class ModellerConfig:
    """Full configuration for the modeller."""

    pods: PodsConfig
    task: TaskConfig
    secrets: Optional[Union[APIKeys, JWT]] = desert.field(
        M_Union(
            [
                fields.Nested(desert.schema_class(APIKeys)),
                fields.Nested(desert.schema_class(JWT)),
            ]
        ),
        default=None,
    )
    modeller: ModellerUserConfig = desert.field(
        fields.Nested(desert.schema_class(ModellerUserConfig)),
        default_factory=ModellerUserConfig,
    )
    hub: HubConfig = desert.field(
        fields.Nested(desert.schema_class(HubConfig)), default_factory=HubConfig
    )
    message_service: MessageServiceConfig = desert.field(
        fields.Nested(desert.schema_class(MessageServiceConfig)),
        default_factory=MessageServiceConfig,
    )
    version: Optional[str] = None
    project_id: Optional[str] = None
    run_on_new_data_only: bool = False
    batched_execution: Optional[bool] = None

    def __post_init__(self) -> None:
        environment = _get_environment()
        if environment == _STAGING_ENVIRONMENT:
            self.hub.url = _STAGING_HUB_URL
            self.message_service.url = _STAGING_MESSAGE_SERVICE_URL
        elif environment == _DEVELOPMENT_ENVIRONMENT:
            self.hub.url = _DEV_HUB_URL
            self.message_service.url = _DEV_MESSAGE_SERVICE_URL
            self.message_service.port = _DEV_MESSAGE_SERVICE_PORT
            self.message_service.tls = _DEV_MESSAGE_SERVICE_TLS
        elif environment == _SANDBOX_ENVIRONMENT:
            self.hub.url = _SANDBOX_HUB_URL
            self.message_service.url = _SANDBOX_MESSAGE_SERVICE_URL
        if self.batched_execution is None:
            self.batched_execution = BITFOUNT_DEFAULT_BATCHED_EXECUTION
        if self.version is None:
            self.version = _DEFAULT_YAML_VERSION

        # check if algorithms are built-in
        if isinstance(self.task.algorithm, list):
            if all(
                [item.name.startswith("bitfount") for item in self.task.algorithm]
            ) and self.task.protocol.name.startswith("bitfount"):
                # Only need to match major and minor versions since protocol
                # and all algorithms are build in
                compatible, message = is_version_compatible_major_minor(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "task"
                )
            else:
                compatible, message = is_version_compatible_all(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "task"
                )
        else:
            if self.task.algorithm.name.startswith(
                "bitfount"
            ) and self.task.protocol.name.startswith("bitfount"):
                # Only need to match major and minor versions since protocol
                # and all algorithms are build in
                compatible, message = is_version_compatible_major_minor(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "task"
                )
            else:
                compatible, message = is_version_compatible_all(
                    _BITFOUNT_COMPATIBLE_YAML_VERSIONS, self.version, "task"
                )
        if compatible:
            _logger.debug(message)
        else:
            raise BitfountVersionError(message)


@dataclass
class TemplatedModellerConfig(ModellerConfig):
    """Schema for task templates."""

    template: Any = None


@dataclass
class ModelStructureConfig:
    """Configuration for the ModelStructure."""

    name: str
    arguments: _JSONDict = desert.field(
        fields.Dict(keys=fields.Str), default_factory=dict
    )


@dataclass
class BitfountModelReferenceConfig:
    """Configuration for BitfountModelReference."""

    model_ref: Union[Path, str] = desert.field(
        fields.Function(deserialize=_deserialize_model_ref)
    )
    model_version: Optional[int] = None
    username: Optional[str] = None
    weights: Optional[str] = None


@dataclass
class ModelConfig:
    """Configuration for the model."""

    # For existing models
    name: Optional[str] = None
    structure: Optional[ModelStructureConfig] = None

    # For custom models
    bitfount_model: Optional[BitfountModelReferenceConfig] = None

    # Other
    hyperparameters: _JSONDict = desert.field(
        fields.Dict(keys=fields.Str), default_factory=dict
    )
    logger_config: Optional[LoggerConfig] = None
    dp_config: Optional[DPModellerConfig] = None

    def __post_init__(self) -> None:
        # Validate either name or bitfount_model reference provided
        self._name_or_bitfount_model()

    def _name_or_bitfount_model(self) -> None:
        """Ensures that both `name` and `bitfount_model` can't be set.

        Raises:
            ValidationError: if both `name` and `bitfount_model` are set
        """
        if self.name:
            raise ValidationError(
                "Model name support has been removed. Must specify a bitfount model."
            )
        if not self.bitfount_model:
            raise ValidationError("No model specified. Must specify a bitfount_model.")


@dataclass
class PodsConfig:
    """Configuration for the pods to use for the modeller."""

    identifiers: list[str]


@dataclass
class ProtocolConfig:
    """Configuration for the Protocol."""

    name: str
    arguments: Optional[Any] = None

    @classmethod
    def _get_subclasses(cls) -> tuple[type[ProtocolConfig], ...]:
        """Get all the concrete subclasses of this config class."""
        return get_concrete_config_subclasses(cls)


@dataclass
class AggregatorConfig:
    """Configuration for the Aggregator."""

    secure: bool
    weights: Optional[dict[str, Union[int, float]]] = None

    def __post_init__(self) -> None:
        if self.secure and self.weights:
            # TODO: [BIT-1486] Remove this constraint
            raise NotImplementedError(
                "SecureAggregation does not support update weighting"
            )


@dataclass
class AlgorithmConfig:
    """Configuration for the Algorithm."""

    name: str
    arguments: Optional[Any] = None

    @classmethod
    def _get_subclasses(cls) -> tuple[type[AlgorithmConfig], ...]:
        """Get all the concrete subclasses of this config class."""
        return get_concrete_config_subclasses(cls)


@dataclass
class ModelAlgorithmConfig(AlgorithmConfig):
    """Configuration for the Model algorithms."""

    __config_type: typing.ClassVar[str] = "intermediate"

    model: Optional[ModelConfig] = None
    pretrained_file: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )


# ALGORITHMS
@dataclass
class FederatedModelTrainingArgumentsConfig:
    """Configuration for the FederatedModelTraining algorithm arguments."""

    modeller_checkpointing: bool = True
    checkpoint_filename: Optional[str] = None


@dataclass
class FederatedModelTrainingAlgorithmConfig(ModelAlgorithmConfig):
    """Configuration for the FederatedModelTraining algorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(AlgorithmType.FederatedModelTraining.value)
        )
    )
    arguments: Optional[FederatedModelTrainingArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(FederatedModelTrainingArgumentsConfig)),
        default=FederatedModelTrainingArgumentsConfig(),
    )


@dataclass
class ModelTrainingAndEvaluationArgumentsConfig:
    """Configuration for the ModelTrainingAndEvaluation algorithm arguments."""

    # Currently there are no arguments


@dataclass
class ModelTrainingAndEvaluationAlgorithmConfig(ModelAlgorithmConfig):
    """Configuration for the ModelTrainingAndEvaluation algorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(AlgorithmType.ModelTrainingAndEvaluation.value)
        )
    )
    arguments: Optional[ModelTrainingAndEvaluationArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(ModelTrainingAndEvaluationArgumentsConfig))
    )


@dataclass
class ModelEvaluationArgumentsConfig:
    """Configuration for the ModelEvaluation algorithm arguments."""

    # Currently there are no arguments


@dataclass
class ModelEvaluationAlgorithmConfig(ModelAlgorithmConfig):
    """Configuration for the ModelEvaluation algorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.ModelEvaluation.value))
    )
    arguments: Optional[ModelEvaluationArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(ModelEvaluationArgumentsConfig))
    )


@dataclass
class ModelInferenceArgumentsConfig:
    """Configuration for the ModelInference algorithm arguments."""

    class_outputs: Optional[list[str]] = None


@dataclass
class ModelInferenceAlgorithmConfig(ModelAlgorithmConfig):
    """Configuration for the ModelInference algorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.ModelInference.value))
    )
    arguments: ModelInferenceArgumentsConfig = desert.field(
        fields.Nested(desert.schema_class(ModelInferenceArgumentsConfig)),
        default=ModelInferenceArgumentsConfig(),
    )


@dataclass
class SqlQueryArgumentsConfig:
    """Configuration for the SqlQuery algorithm arguments."""

    query: str
    table: Optional[str] = None


@dataclass
class SqlQueryAlgorithmConfig(AlgorithmConfig):
    """Configuration for the SqlQuery algorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.SqlQuery.value))
    )
    arguments: SqlQueryArgumentsConfig = desert.field(
        fields.Nested(desert.schema_class(SqlQueryArgumentsConfig))
    )


@dataclass
class PrivateSqlQueryColumnArgumentsConfig:
    """Configuration for the PrivateSqlQuery algorithm column arguments."""

    lower: Optional[int] = None
    upper: Optional[int] = None


PrivateSqlQueryColumnArgumentsConfigSchema = desert.schema_class(
    PrivateSqlQueryColumnArgumentsConfig
)


@dataclass
class PrivateSqlQueryArgumentsConfig:
    """Configuration for the PrivateSqlQuery algorithm arguments."""

    query: str
    epsilon: float
    delta: float
    column_ranges: dict[str, Optional[PrivateSqlQueryColumnArgumentsConfig]] = (
        desert.field(
            M_Union(
                [
                    fields.Dict(
                        keys=fields.String(),
                        values=fields.Nested(
                            PrivateSqlQueryColumnArgumentsConfigSchema,
                        ),
                    ),
                    fields.Dict(
                        keys=fields.String(),
                        values=fields.Dict(
                            keys=fields.String(),
                            values=fields.Nested(
                                PrivateSqlQueryColumnArgumentsConfigSchema,
                            ),
                        ),
                    ),
                ]
            )
        )
    )
    table: Optional[str] = None
    db_schema: Optional[str] = None


@dataclass
class PrivateSqlQueryAlgorithmConfig(AlgorithmConfig):
    """Configuration for the PrivateSqlQuery algorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.PrivateSqlQuery.value))
    )
    arguments: PrivateSqlQueryArgumentsConfig = desert.field(
        fields.Nested(desert.schema_class(PrivateSqlQueryArgumentsConfig))
    )


@dataclass
class HuggingFacePerplexityEvaluationArgumentsConfig:
    """Configuration for the HuggingFacePerplexityEvaluation algorithm arguments."""

    model_id: str
    text_column_name: str
    stride: int = DEFAULT_STRIDE
    seed: int = DEFAULT_SEED


@dataclass
class HuggingFacePerplexityEvaluationAlgorithmConfig(AlgorithmConfig):
    """Configuration for the HuggingFacePerplexityEvaluation algorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(AlgorithmType.HuggingFacePerplexityEvaluation.value)
        )
    )

    arguments: Optional[HuggingFacePerplexityEvaluationArgumentsConfig] = desert.field(
        fields.Nested(
            desert.schema_class(HuggingFacePerplexityEvaluationArgumentsConfig)
        )
    )


@dataclass
class HuggingFaceTextGenerationInferenceArgumentsConfig:
    """Configuration for the HuggingFaceTextGenerationInference algorithm arguments."""

    model_id: str
    text_column_name: Optional[str] = None
    prompt_format: Optional[str] = None
    max_length: int = DEFAULT_MAX_LENGTH
    num_return_sequences: int = DEFAULT_NUM_RETURN_SEQUENCES
    seed: int = DEFAULT_SEED
    min_new_tokens: int = DEFAULT_MIN_NEW_TOKENS
    repetition_penalty: float = DEFAULT_REPETITION_PENALTY
    num_beams: int = DEFAULT_NUM_BEAMS
    early_stopping: bool = True
    pad_token_id: Optional[int] = None
    eos_token_id: Optional[int] = None
    device: Optional[str] = None
    torch_dtype: str = "float32"

    def __post_init__(self) -> None:
        if self.torch_dtype not in ("bfloat16", "float16", "float32", "float64"):
            raise ValueError(
                f"Invalid torch_dtype {self.torch_dtype}. Must be one of "
                "'bfloat16', 'float16', 'float32', 'float64'."
            )


@dataclass
class HuggingFaceTextGenerationInferenceAlgorithmConfig(AlgorithmConfig):
    """Configuration for the HuggingFaceTextGenerationInference algorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(
                AlgorithmType.HuggingFaceTextGenerationInference.value
            )
        )
    )

    arguments: Optional[HuggingFaceTextGenerationInferenceArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(HuggingFaceTextGenerationInferenceArgumentsConfig)
            )
        )
    )


@dataclass
class CSVReportAlgorithmArgumentsConfig:
    """Configuration for CSVReportAlgorithm arguments."""

    save_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    original_cols: Optional[list[str]] = None
    filter: Optional[list[ColumnFilter]] = desert.field(
        fields.Nested(desert.schema_class(ColumnFilter), many=True, allow_none=True),
        default=None,
    )


@dataclass
class CSVReportAlgorithmConfig(AlgorithmConfig):
    """Configuration for CSVReportAlgorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.CSVReportAlgorithm.value))
    )
    arguments: Optional[CSVReportAlgorithmArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(CSVReportAlgorithmArgumentsConfig)),
        default=CSVReportAlgorithmArgumentsConfig(),
    )


@dataclass
class HuggingFaceImageClassificationInferenceArgumentsConfig:
    """Configuration for HuggingFaceImageClassificationInference arguments."""

    model_id: str
    image_column_name: str
    apply_softmax_to_predictions: bool = True
    batch_size: int = 1
    seed: int = DEFAULT_SEED
    top_k: int = 5


@dataclass
class HuggingFaceImageClassificationInferenceAlgorithmConfig(AlgorithmConfig):
    """Configuration for HuggingFaceImageClassificationInference."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(
                AlgorithmType.HuggingFaceImageClassificationInference.value
            )
        )
    )
    arguments: Optional[HuggingFaceImageClassificationInferenceArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    HuggingFaceImageClassificationInferenceArgumentsConfig
                )
            ),
        )
    )


@dataclass
class HuggingFaceImageSegmentationInferenceArgumentsConfig:
    """Configuration for HuggingFaceImageSegmentationInference arguments."""

    model_id: str
    image_column_name: str
    alpha: float = 0.3
    batch_size: int = 1
    dataframe_output: bool = False
    mask_threshold: float = 0.5
    overlap_mask_area_threshold: float = 0.5
    seed: int = DEFAULT_SEED
    save_path: Optional[str] = None
    subtask: Optional[str] = None
    threshold: float = 0.9


@dataclass
class HuggingFaceImageSegmentationInferenceAlgorithmConfig(AlgorithmConfig):
    """Configuration for HuggingFaceImageSegmentationInference."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(
                AlgorithmType.HuggingFaceImageSegmentationInference.value
            )
        )
    )
    arguments: Optional[HuggingFaceImageSegmentationInferenceArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    HuggingFaceImageSegmentationInferenceArgumentsConfig
                )
            ),
        )
    )


@dataclass
class HuggingFaceTextClassificationInferenceArgumentsConfig:
    """Configuration for HuggingFaceTextClassificationInference arguments."""

    model_id: str
    target_column_name: str
    batch_size: int = 1
    function_to_apply: Optional[str] = None
    seed: int = DEFAULT_SEED
    top_k: int = 5


@dataclass
class HuggingFaceTextClassificationInferenceAlgorithmConfig(AlgorithmConfig):
    """Configuration for HuggingFaceTextClassificationInference."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(
                AlgorithmType.HuggingFaceTextClassificationInference.value
            )
        )
    )
    arguments: Optional[HuggingFaceTextClassificationInferenceArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    HuggingFaceTextClassificationInferenceArgumentsConfig
                )
            ),
        )
    )


@dataclass
class TIMMFineTuningArgumentsConfig:
    """Configuration for TIMMFineTuning algorithm arguments."""

    model_id: str
    args: Optional[TIMMTrainingConfig] = desert.field(
        fields.Nested(desert.schema_class(TIMMTrainingConfig), allow_none=True),
        default=None,
    )
    batch_transformations: Optional[
        Union[
            list[Union[str, _JSONDict]],
            dict[str, list[Union[str, _JSONDict]]],
        ]
    ] = desert.field(
        fields.Dict(
            keys=fields.Str(validate=OneOf(["train", "validation"])),
        ),
        default=None,
    )
    image_column_name: Optional[str] = None
    labels: Optional[list[str]] = None
    return_weights: bool = False
    save_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    target_column_name: Optional[str] = None


@dataclass
class TIMMFineTuningAlgorithmConfig(AlgorithmConfig):
    """Configuration for TIMMFineTuning algorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.TIMMFineTuning.value))
    )
    arguments: Optional[TIMMFineTuningArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(TIMMFineTuningArgumentsConfig)),
    )


@dataclass
class TIMMInferenceArgumentsConfig:
    """Configuration for TIMMInference algorithm arguments."""

    model_id: str
    image_column_name: str
    num_classes: Optional[int] = None
    checkpoint_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    class_outputs: Optional[list[str]] = None


@dataclass
class TIMMInferenceAlgorithmConfig(AlgorithmConfig):
    """Configuration for TIMMInference algorithm."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(AlgorithmType.TIMMInference.value))
    )
    arguments: Optional[TIMMInferenceArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(TIMMInferenceArgumentsConfig)),
    )


@dataclass
class HuggingFaceZeroShotImageClassificationInferenceArgumentsConfig:
    """Configuration for HuggingFaceZeroShotImageClassificationInference arguments."""  # noqa: E501

    model_id: str
    image_column_name: str
    candidate_labels: list[str]
    batch_size: int = 1
    class_outputs: Optional[list[str]] = None
    hypothesis_template: Optional[str] = None
    seed: int = DEFAULT_SEED


@dataclass
class HuggingFaceZeroShotImageClassificationInferenceAlgorithmConfig(AlgorithmConfig):
    """Configuration for HuggingFaceZeroShotImageClassificationInference."""  # noqa: E501

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(
                AlgorithmType.HuggingFaceZeroShotImageClassificationInference.value
            )
        )
    )
    arguments: Optional[
        HuggingFaceZeroShotImageClassificationInferenceArgumentsConfig
    ] = desert.field(
        fields.Nested(
            desert.schema_class(
                HuggingFaceZeroShotImageClassificationInferenceArgumentsConfig
            )
        ),
    )


@dataclass
class GenericAlgorithmConfig(AlgorithmConfig):
    """Configuration for unspecified algorithm plugins.

    Raises:
        ValueError: if the algorithm name starts with `bitfount.`
    """

    __config_type: typing.ClassVar[str] = "fallback"

    name: str
    arguments: _JSONDict = desert.field(
        fields.Dict(keys=fields.Str), default_factory=dict
    )

    def __post_init__(self) -> None:
        _logger.warning(
            f"Algorithm configuration was parsed as {self.__class__.__name__};"
            f" was this intended?"
        )

        if self.name.startswith("bitfount."):
            raise ValueError(
                "Algorithm names starting with 'bitfount.' are reserved for built-in "
                "algorithms. It is likely the provided arguments don't match the "
                "expected schema for the algorithm. Please check the documentation "
            )


# Protocols
@dataclass
class ResultsOnlyProtocolArgumentsConfig:
    """Configuration for the ResultsOnly Protocol arguments."""

    aggregator: Optional[AggregatorConfig] = None
    secure_aggregation: bool = False


@dataclass
class ResultsOnlyProtocolConfig(ProtocolConfig):
    """Configuration for the ResultsOnly Protocol."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(ProtocolType.ResultsOnly.value))
    )
    arguments: Optional[ResultsOnlyProtocolArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(ResultsOnlyProtocolArgumentsConfig)),
        default=ResultsOnlyProtocolArgumentsConfig(),
    )


@dataclass
class FederatedAveragingProtocolArgumentsConfig:
    """Configuration for the FedreatedAveraging Protocol arguments."""

    aggregator: Optional[AggregatorConfig] = None
    steps_between_parameter_updates: Optional[int] = None
    epochs_between_parameter_updates: Optional[int] = None
    auto_eval: bool = True
    secure_aggregation: bool = False


@dataclass
class FederatedAveragingProtocolConfig(ProtocolConfig):
    """Configuration for the FederatedAveraging Protocol."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(ProtocolType.FederatedAveraging.value))
    )
    arguments: Optional[FederatedAveragingProtocolArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(FederatedAveragingProtocolArgumentsConfig)),
        default=FederatedAveragingProtocolArgumentsConfig(),
    )


@dataclass
class InferenceAndCSVReportArgumentsConfig:
    """Configuration for InferenceAndCSVReport arguments."""

    aggregator: Optional[AggregatorConfig] = None


@dataclass
class InferenceAndCSVReportConfig(ProtocolConfig):
    """Configuration for InferenceAndCSVReport."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(ProtocolType.InferenceAndCSVReport.value))
    )
    arguments: Optional[InferenceAndCSVReportArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(InferenceAndCSVReportArgumentsConfig)),
        default=InferenceAndCSVReportArgumentsConfig(),
    )


@dataclass
class InstrumentedInferenceAndCSVReportArgumentsConfig:
    """Configuration for InstrumentedInferenceAndCSVReport arguments."""

    aggregator: Optional[AggregatorConfig] = None


@dataclass
class InstrumentedInferenceAndCSVReportConfig(ProtocolConfig):
    """Configuration for InstrumentedInferenceAndCSVReport."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(
                ProtocolType.InstrumentedInferenceAndCSVReport.value
            )
        )
    )
    arguments: Optional[InstrumentedInferenceAndCSVReportArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(InstrumentedInferenceAndCSVReportArgumentsConfig)
            ),
            default=InstrumentedInferenceAndCSVReportArgumentsConfig(),
        )
    )


@dataclass
class InferenceAndReturnCSVReportArgumentsConfig:
    """Configuration for InferenceAndReturnCSVReport arguments."""

    aggregator: Optional[AggregatorConfig] = None


@dataclass
class InferenceAndReturnCSVReportConfig(ProtocolConfig):
    """Configuration for InferenceAndReturnCSVReport."""

    name: str = desert.field(
        fields.String(
            validate=validate.Equal(ProtocolType.InferenceAndReturnCSVReport.value)
        )
    )
    arguments: Optional[InferenceAndReturnCSVReportArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(InferenceAndReturnCSVReportArgumentsConfig)),
        default=InferenceAndReturnCSVReportArgumentsConfig(),
    )


@dataclass
class ConversationArgumentsConfig:
    """Configuration for the Conversation arguments."""

    # Currently there are no arguments


@dataclass
class ConversationConfig(ProtocolConfig):
    """Configuration for Conversation."""

    name: str = desert.field(
        fields.String(validate=validate.Equal(ProtocolType.Conversation.value))
    )
    arguments: Optional[ConversationArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(ConversationArgumentsConfig)),
        default=ConversationArgumentsConfig(),
    )


@dataclass
class GenericProtocolConfig(ProtocolConfig):
    """Configuration for unspecified protocol plugins.

    Raises:
        ValueError: if the protocol name starts with `bitfount.`
    """

    __config_type: typing.ClassVar[str] = "fallback"

    name: str
    arguments: _JSONDict = desert.field(
        fields.Dict(keys=fields.Str), default_factory=dict
    )

    def __post_init__(self) -> None:
        _logger.warning(
            f"Protocol configuration was parsed as {self.__class__.__name__};"
            f" was this intended?"
        )
        if self.name.startswith("bitfount."):
            raise ValueError(
                "Protocol names starting with 'bitfount.' are reserved for built-in "
                "protocols. It is likely the provided arguments don't match the "
                "expected schema for the protocol. Please check the documentation "
            )


@dataclass
class TaskConfig:
    """Configuration for the task."""

    protocol: Union[ProtocolConfig._get_subclasses()]  # type: ignore[valid-type] # reason: no dynamic typing # noqa: E501
    # NOTE: Union[AlgorithmConfig._get_subclasses()] cannot be
    # replaced with a TypeAlias here without breaking the dynamic subtyping
    algorithm: Union[  # type: ignore[valid-type] # reason: no dynamic typing # noqa: E501
        Union[AlgorithmConfig._get_subclasses()],
        list[Union[AlgorithmConfig._get_subclasses()]],
    ]
    data_structure: Optional[DataStructureConfig] = None
    aggregator: Optional[AggregatorConfig] = None
    transformation_file: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )


#############################################################################
#  _____       _     _   _           _                 _                    #
# |  _  |     | |   | | | |         | |               | |                   #
# | | | |_ __ | |__ | |_| |__   __ _| |_ __ ___   ___ | | ___   __ _ _   _  #
# | | | | '_ \| '_ \| __| '_ \ / _` | | '_ ` _ \ / _ \| |/ _ \ / _` | | | | #
# \ \_/ / |_) | | | | |_| | | | (_| | | | | | | | (_) | | (_) | (_| | |_| | #
#  \___/| .__/|_| |_|\__|_| |_|\__,_|_|_| |_| |_|\___/|_|\___/ \__, |\__, | #
#       | |                                                     __/ | __/ | #
#       |_|                                                    |___/ |___/  #
#############################################################################
####################
# PROTOCOL CONFIGS #
####################


@dataclass
class RetinalDiseaseProtocolCobaltArgumentsConfig:
    """Configuration for RetinalDiseaseProtocolCobalt arguments."""

    aggregator: Optional[AggregatorConfig] = None


@dataclass
class RetinalDiseaseProtocolCobaltConfig(ProtocolConfig):
    """Configuration for RetinalDiseaseProtocolCobalt."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    ProtocolType.RetinalDiseaseProtocolCobalt.value,
                    ProtocolType.BasicOCTProtocol.value,  # Kept for backwards compatibility # noqa: E501
                    # Without ".bitfount" prefix for backwards compatibility
                    "RetinalDiseaseProtocolCobalt",
                    "BasicOCTProtocol",  # Kept for backwards compatibility
                ],
            )
        )
    )
    arguments: Optional[RetinalDiseaseProtocolCobaltArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(RetinalDiseaseProtocolCobaltArgumentsConfig)),
        default=RetinalDiseaseProtocolCobaltArgumentsConfig(),
    )


@dataclass
class GAScreeningProtocolJadeArgumentsConfig:
    """Configuration for GAScreeningProtocolJade arguments."""

    aggregator: Optional[AggregatorConfig] = None
    results_notification_email: Optional[bool] = False
    trial_name: Optional[str] = desert.field(fields.String(), default=None)
    rename_columns: Optional[dict[str, str]] = desert.field(
        fields.Dict(keys=fields.Str(), values=fields.Str()), default=None
    )


@dataclass
class GAScreeningProtocolJadeConfig(ProtocolConfig):
    """Configuration for GAScreeningProtocolJade."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    ProtocolType.GAScreeningProtocolJade.value,
                    ProtocolType.GAScreeningProtocol.value,  # Kept for backwards compatibility # noqa: E501
                    # Without ".bitfount" prefix for backwards compatibility
                    "GAScreeningProtocolJade",
                    "GAScreeningProtocol",  # Kept for backwards compatibility
                ],
            )
        )
    )
    arguments: Optional[GAScreeningProtocolJadeArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(GAScreeningProtocolJadeArgumentsConfig)),
        default=GAScreeningProtocolJadeArgumentsConfig(),
    )


@dataclass
class GAScreeningProtocolAmethystArgumentsConfig:
    """Configuration for GAScreeningProtocolAmethyst arguments."""

    aggregator: Optional[AggregatorConfig] = None
    results_notification_email: Optional[bool] = False
    trial_name: Optional[str] = desert.field(fields.String(), default=None)
    rename_columns: Optional[dict[str, str]] = desert.field(
        fields.Dict(keys=fields.Str(), values=fields.Str()), default=None
    )


@dataclass
class GAScreeningProtocolAmethystConfig(ProtocolConfig):
    """Configuration for GAScreeningProtocolAmethyst."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    ProtocolType.GAScreeningProtocolAmethyst.value,
                    # Without ".bitfount" prefix for backwards compatibility
                    "GAScreeningProtocolAmethyst",
                ]
            )
        )
    )
    arguments: Optional[GAScreeningProtocolAmethystArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(GAScreeningProtocolAmethystArgumentsConfig)),
        default=GAScreeningProtocolAmethystArgumentsConfig(),
    )


#####################
# ALGORITHM CONFIGS #
#####################
@dataclass
class CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig:
    """Configuration for CSVReportGeneratorOphthalmologyAlgorithm arguments."""

    save_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    trial_name: Optional[str] = desert.field(fields.String(), default=None)
    original_cols: Optional[list[str]] = None
    rename_columns: Optional[dict[str, str]] = desert.field(
        fields.Dict(keys=fields.Str(), values=fields.Str()), default=None
    )
    filter: Optional[list[ColumnFilter]] = desert.field(
        fields.Nested(desert.schema_class(ColumnFilter), many=True, allow_none=True),
        default=None,
    )
    match_patient_visit: Optional[MatchPatientVisit] = desert.field(
        fields.Nested(desert.schema_class(MatchPatientVisit), allow_none=True),
        default=None,
    )
    matched_csv_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    produce_matched_only: bool = True
    csv_extensions: Optional[list[str]] = None
    produce_trial_notes_csv: bool = False
    sorting_columns: Optional[dict[str, str]] = desert.field(
        fields.Dict(
            keys=fields.Str(),
            values=fields.Str(validate=validate.OneOf(typing.get_args(DFSortType))),
        ),
        default=None,
    )


@dataclass
class CSVReportGeneratorOphthalmologyAlgorithmConfig(AlgorithmConfig):
    """Configuration for CSVReportGeneratorOphthalmologyAlgorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.CSVReportGeneratorOphthalmologyAlgorithm.value,
                    AlgorithmType.CSVReportGeneratorAlgorithm.value,  # Kept for backwards compatibility # noqa: E501
                    # Without ".bitfount" prefix for backwards compatibility
                    "CSVReportGeneratorOphthalmologyAlgorithm",
                    "CSVReportGeneratorAlgorithm",  # Kept for backwards compatibility
                ]
            )
        )
    )
    arguments: Optional[CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig
                )
            ),
            default=CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig(),
        )
    )


@dataclass
class ETDRSAlgorithmArgumentsConfig:
    """Configuration for ETDRSAlgorithm arguments."""

    laterality: str
    slo_photo_location_prefixes: Optional[SLOSegmentationLocationPrefix] = desert.field(
        fields.Nested(
            desert.schema_class(SLOSegmentationLocationPrefix), allow_none=True
        ),
        default=None,
    )
    slo_image_metadata_columns: Optional[SLOImageMetadataColumns] = desert.field(
        fields.Nested(desert.schema_class(SLOImageMetadataColumns), allow_none=True),
        default=None,
    )
    oct_image_metadata_columns: Optional[OCTImageMetadataColumns] = desert.field(
        fields.Nested(
            desert.schema_class(OCTImageMetadataColumns),
            allow_none=True,
        ),
        default=None,
    )
    threshold: float = 0.7
    calculate_on_oct: bool = False
    slo_mm_width: float = 8.8
    slo_mm_height: float = 8.8


@dataclass
class ETDRSAlgorithmConfig(AlgorithmConfig):
    """Configuration for ETDRSAlgorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.ETDRSAlgorithm.value,
                    # Without ".bitfount" prefix for backwards compatibility
                    "ETDRSAlgorithm",
                ]
            )
        )
    )
    arguments: Optional[ETDRSAlgorithmArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(ETDRSAlgorithmArgumentsConfig)),
    )


@dataclass
class FoveaCoordinatesAlgorithmArgumentsConfig:
    """Configuration for FoveaCoordinatesAlgorithm arguments."""

    bscan_width_col: str = "size_width"
    location_prefixes: Optional[SLOSegmentationLocationPrefix] = desert.field(
        fields.Nested(
            desert.schema_class(SLOSegmentationLocationPrefix),
            allow_none=True,
        ),
        default=None,
    )


@dataclass
class FoveaCoordinatesAlgorithmConfig(AlgorithmConfig):
    """Configuration for FoveaCoordinatesAlgorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.FoveaCoordinatesAlgorithm.value,
                    # Without ".bitfount" prefix for backwards compatibility
                    "FoveaCoordinatesAlgorithm",
                ]
            )
        )
    )
    arguments: Optional[FoveaCoordinatesAlgorithmArgumentsConfig] = desert.field(
        fields.Nested(desert.schema_class(FoveaCoordinatesAlgorithmArgumentsConfig)),
        default=FoveaCoordinatesAlgorithmArgumentsConfig(),
    )


@dataclass
class _SimpleCSVAlgorithmArgumentsConfig:
    """Configuration for _SimpleCSVAlgorithm arguments."""

    save_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )


@dataclass
class _SimpleCSVAlgorithmAlgorithmConfig(AlgorithmConfig):
    """Configuration for _SimpleCSVAlgorithm."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType._SimpleCSVAlgorithm.value,
                    # Without ".bitfount" prefix for backwards compatibility
                    "_SimpleCSVAlgorithm",
                ]
            )
        )
    )
    arguments: Optional[CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig
                )
            ),
            default=CSVReportGeneratorOphthalmologyAlgorithmArgumentsConfig(),
        )
    )


@dataclass
class GATrialCalculationAlgorithmJadeArgumentsConfig:
    """Configuration for GATrialCalculationAlgorithmJade arguments."""

    ga_area_include_segmentations: Optional[list[str]] = None
    ga_area_exclude_segmentations: Optional[list[str]] = None


@dataclass
class GATrialCalculationAlgorithmJadeConfig(AlgorithmConfig):
    """Configuration for GATrialCalculationAlgorithmJade."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.GATrialCalculationAlgorithmJade.value,
                    AlgorithmType.GATrialCalculationAlgorithm.value,  # Kept for backwards compatibility # noqa: E501
                    # Without ".bitfount" prefix for backwards compatibility
                    "GATrialCalculationAlgorithmJade",
                    "GATrialCalculationAlgorithm",  # Kept for backwards compatibility
                ]
            )
        )
    )
    arguments: Optional[GATrialCalculationAlgorithmJadeArgumentsConfig] = desert.field(
        fields.Nested(
            desert.schema_class(GATrialCalculationAlgorithmJadeArgumentsConfig)
        ),
        default=GATrialCalculationAlgorithmJadeArgumentsConfig(),
    )


@dataclass
class GATrialPDFGeneratorAlgorithmJadeArgumentsConfig:
    """Configuration for GATrialPDFGeneratorAlgorithmJade arguments."""

    # TODO: [BIT-2926] ReportMetadata should not be optional
    report_metadata: Optional[ReportMetadata] = desert.field(
        fields.Nested(desert.schema_class(ReportMetadata)),
        default=None,
    )
    filename_prefix: Optional[str] = desert.field(
        fields.String(validate=validate.Regexp("[a-zA-Z]+")), default=None
    )
    save_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    filter: Optional[list[ColumnFilter]] = desert.field(
        fields.Nested(desert.schema_class(ColumnFilter), many=True, allow_none=True),
        default=None,
    )
    pdf_filename_columns: Optional[list[str]] = None
    trial_name: Optional[str] = desert.field(fields.String(), default=None)


@dataclass
class GATrialPDFGeneratorAlgorithmJadeConfig(AlgorithmConfig):
    """Configuration for GATrialPDFGeneratorAlgorithmJade."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.GATrialPDFGeneratorAlgorithmJade.value,
                    AlgorithmType.GATrialPDFGeneratorAlgorithm.value,  # Kept for backwards compatibility # noqa: E501
                    # Without ".bitfount" prefix for backwards compatibility
                    "GATrialPDFGeneratorAlgorithmJade",
                    "GATrialPDFGeneratorAlgorithm",  # Kept for backwards compatibility
                ]
            )
        )
    )
    arguments: Optional[GATrialPDFGeneratorAlgorithmJadeArgumentsConfig] = desert.field(
        fields.Nested(
            desert.schema_class(GATrialPDFGeneratorAlgorithmJadeArgumentsConfig)
        ),
        default=GATrialPDFGeneratorAlgorithmJadeArgumentsConfig(),
    )


@dataclass
class GATrialPDFGeneratorAlgorithmAmethystArgumentsConfig:
    """Configuration for GATrialPDFGeneratorAlgorithmAmethyst arguments."""

    # TODO: [BIT-2926] ReportMetadata should not be optional
    report_metadata: Optional[ReportMetadata] = desert.field(
        fields.Nested(desert.schema_class(ReportMetadata)),
        default=None,
    )
    filename_prefix: Optional[str] = desert.field(
        fields.String(validate=validate.Regexp("[a-zA-Z]+")), default=None
    )
    save_path: Optional[Path] = desert.field(
        fields.Function(deserialize=_deserialize_path), default=None
    )
    filter: Optional[list[ColumnFilter]] = desert.field(
        fields.Nested(desert.schema_class(ColumnFilter), many=True, allow_none=True),
        default=None,
    )
    pdf_filename_columns: Optional[list[str]] = None
    trial_name: Optional[str] = desert.field(fields.String(), default=None)


@dataclass
class GATrialPDFGeneratorAlgorithmAmethystConfig(AlgorithmConfig):
    """Configuration for GATrialPDFGeneratorAlgorithmAmethyst."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.GATrialPDFGeneratorAlgorithmAmethyst.value,
                    # Without ".bitfount" prefix for backwards compatibility
                    "GATrialPDFGeneratorAlgorithmAmethyst",
                ]
            )
        )
    )
    arguments: Optional[GATrialPDFGeneratorAlgorithmAmethystArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(GATrialPDFGeneratorAlgorithmAmethystArgumentsConfig)
            ),
            default=GATrialPDFGeneratorAlgorithmAmethystArgumentsConfig(),
        )
    )


@dataclass
class TrialInclusionCriteriaMatchAlgorithmJadeArgumentsConfig:
    """Configuration for TrialInclusionCriteriaMatchAlgorithmJade arguments."""

    pass


@dataclass
class TrialInclusionCriteriaMatchAlgorithmJadeConfig(AlgorithmConfig):
    """Configuration for TrialInclusionCriteriaMatchAlgorithmJade."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.TrialInclusionCriteriaMatchAlgorithmJade.value,
                    AlgorithmType.TrialInclusionCriteriaMatchAlgorithm.value,  # Kept for backwards compatibility # noqa: E501
                    # Without ".bitfount" prefix for backwards compatibility
                    "TrialInclusionCriteriaMatchAlgorithmJade",
                    "TrialInclusionCriteriaMatchAlgorithm",  # Kept for backwards compatibility # noqa: E501
                ]
            )
        )
    )
    arguments: Optional[TrialInclusionCriteriaMatchAlgorithmJadeArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    TrialInclusionCriteriaMatchAlgorithmJadeArgumentsConfig
                )
            ),
            default=TrialInclusionCriteriaMatchAlgorithmJadeArgumentsConfig(),
        )
    )


@dataclass
class TrialInclusionCriteriaMatchAlgorithmAmethystArgumentsConfig:
    """Configuration for TrialInclusionCriteriaMatchAlgorithmAmethyst arguments."""

    cnv_threshold: float = desert.field(fields.Float(), default=CNV_THRESHOLD)
    largest_ga_lesion_lower_bound: float = desert.field(
        fields.Float(), default=LARGEST_GA_LESION_LOWER_BOUND
    )
    total_ga_area_lower_bound: float = desert.field(
        fields.Float(), default=TOTAL_GA_AREA_LOWER_BOUND
    )
    total_ga_area_upper_bound: float = desert.field(
        fields.Float(), default=TOTAL_GA_AREA_UPPER_BOUND
    )


@dataclass
class TrialInclusionCriteriaMatchAlgorithmAmethystConfig(AlgorithmConfig):
    """Configuration for TrialInclusionCriteriaMatchAlgorithmAmethyst."""

    name: str = desert.field(
        fields.String(
            validate=validate.OneOf(
                [
                    AlgorithmType.TrialInclusionCriteriaMatchAlgorithmAmethyst.value,
                    # without "bitfount." prefix for backward compatibility
                    "TrialInclusionCriteriaMatchAlgorithmAmethyst",
                ],
            )
        )
    )
    arguments: Optional[TrialInclusionCriteriaMatchAlgorithmAmethystArgumentsConfig] = (
        desert.field(
            fields.Nested(
                desert.schema_class(
                    TrialInclusionCriteriaMatchAlgorithmAmethystArgumentsConfig
                )
            ),
            default=TrialInclusionCriteriaMatchAlgorithmAmethystArgumentsConfig(),
        )
    )
