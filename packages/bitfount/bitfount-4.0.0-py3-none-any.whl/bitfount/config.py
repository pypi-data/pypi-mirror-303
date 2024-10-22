"""Dealing with interactions with configuration and environment variables."""

from __future__ import annotations

from collections.abc import Callable
from functools import lru_cache
from importlib import util
from importlib.machinery import ModuleSpec
import logging
import os
from pathlib import Path
import platform
from typing import Final, Literal, Optional, cast

from environs import Env
import GPUtil

from bitfount.__version__ import __yaml_versions__ as yaml_versions

__all__: list[str] = [
    # Storage and log locations
    "BITFOUNT_HOME",
    "BITFOUNT_STORAGE_PATH",
    "BITFOUNT_PLUGIN_PATH",
    "BITFOUNT_FEDERATED_PLUGIN_PATH",
    "BITFOUNT_KEY_STORE",
    "BITFOUNT_LOGS_DIR",
    "BITFOUNT_OUTPUT_DIR",
    "BITFOUNT_CACHE_DIR",
    "BITFOUNT_DATASET_CACHE_DIR",
    # Compatibility/extras options
    "USE_MPS",
    "PROXY_SUPPORT",
    "DEFAULT_TORCH_DEVICE",
    "POD_VITALS_PORT",
    # Message Service
    "HANDLER_REGISTER_GRACE_PERIOD",
    "ONLINE_CHECK_HARD_LIMIT",
    "ONLINE_CHECK_SOFT_LIMIT",
    # Logging/Error Handling
    "AUTO_CONFIGURE_LOGGING",
    "LOG_LEVEL",
    "LOG_FORMAT",
    "LOG_DATE_FORMAT",
    "FILE_LOG_FORMAT",
    "_LIMIT_LOGS",
    "LOG_TO_FILE",
    "_TB_LIMIT",
    "LOG_AUTHENTICATION_HEADERS",
    "LOG_DICOM_FIXES",
    "LOG_HOOKS",
    "LOG_MESSAGE_SERVICE",
    "LOG_POD_HEARTBEAT",
    "LOG_TRANSFORMATION_APPLY",
    "LOG_WEB_UTILS",
    "LOG_HTTPCORE",
    "LOG_HTTPX",
    "LOG_MATPLOTLIB",
    "LOG_URLLIB3",
    # Task environment variables
    "BITFOUNT_TASK_BATCH_SIZE",
    "BITFOUNT_DEFAULT_BATCHED_EXECUTION",
    # Backend engine
    "BITFOUNT_ENGINE",
    # GPU
    "get_gpu_metadata",
    # YAML versioning
    "_BITFOUNT_COMPATIBLE_YAML_VERSIONS",
    # Environment
    "_get_environment",
    # DP Support
    "DP_AVAILABLE",
    # Shutdown variables
    "POD_HEARTBEAT_SHUTDOWN_TIMEOUT",
    "POD_VITALS_HANDLER_SHUTDOWN_TIMEOUT",
    # Feature flags
    "BITFOUNT_FILE_MULTIPROCESSING_ENABLED",
    # Datasource environment variables
    "MAX_NUMBER_OF_DATASOURCE_FILES",
]

from marshmallow import ValidationError

logger = logging.getLogger(__name__)


# Validators
def _validate_torch_device(arg: str) -> None:
    if arg in ("cpu", "mps") or arg.startswith("cuda"):
        return
    else:
        raise ValidationError(
            "Invalid choice for default torch device, should be one of:"
            ' "cpu",'
            ' "mps",'
            ' "cuda",'
            ' or "cuda:<device_id>" (e.g. "cuda:1").'
        )


# This is needed at the top of the module so all the envvars can be linked to it
env = Env()

#######################################
# Public Config/Environment Variables #
#######################################
# Storage and log locations
with env.prefixed("BITFOUNT_"):
    # NOTE: These variables have the BITFOUNT_ prefix whilst others below don't,
    #       as their names are otherwise very generic/ambiguous
    BITFOUNT_HOME: Path = env.path("HOME", default=Path.home()).expanduser()
    BITFOUNT_STORAGE_PATH: Path = env.path(
        "STORAGE_PATH", default=BITFOUNT_HOME / ".bitfount"
    ).expanduser()
    BITFOUNT_PLUGIN_PATH: Path = env.path(
        "PLUGIN_PATH", default=BITFOUNT_STORAGE_PATH / "_plugins"
    ).expanduser()
    BITFOUNT_FEDERATED_PLUGIN_PATH: Path = env.path(
        "FEDERATED_PLUGIN_PATH", default=BITFOUNT_PLUGIN_PATH / "federated"
    ).expanduser()
    BITFOUNT_KEY_STORE: Path = env.path(
        "KEY_STORE", default=BITFOUNT_STORAGE_PATH / "known_workers.yml"
    ).expanduser()
    BITFOUNT_LOGS_DIR: Path = env.path(
        # NOTE: The default here is a relative path of "bitfount_logs"
        "LOGS_DIR",
        default=Path("bitfount_logs"),
    ).expanduser()
    BITFOUNT_OUTPUT_DIR: Path = env.path(
        # NOTE: The default here is current working directory
        "OUTPUT_DIR",
        default=Path("."),
    ).expanduser()
    BITFOUNT_CACHE_DIR: Path = env.path(
        "CACHE_DIR",
        default=BITFOUNT_STORAGE_PATH / "cache",
    ).expanduser()
    BITFOUNT_DATASET_CACHE_DIR: Path = env.path(
        "DATASET_CACHE_DIR",
        default=BITFOUNT_CACHE_DIR / "datasets",
    ).expanduser()

    BITFOUNT_PROXY_CERT_DIR: Optional[Path] = env.path("PROXY_CERT_DIR", default=None)
    if BITFOUNT_PROXY_CERT_DIR is not None:
        BITFOUNT_PROXY_CERT_DIR = BITFOUNT_PROXY_CERT_DIR.expanduser()

# Compatibility/extras options
with env.prefixed("BITFOUNT_"):
    USE_MPS: bool = env.bool("USE_MPS", default=False)
    PROXY_SUPPORT: bool = env.bool("PROXY_SUPPORT", default=True)
    DEFAULT_TORCH_DEVICE: Optional[str] = env.str(
        "DEFAULT_TORCH_DEVICE", default=None, validate=_validate_torch_device
    )
    ENABLE_DATA_CACHE: bool = env.bool("ENABLE_DATA_CACHE", default=True)
    POD_VITALS_PORT: int = env.int("POD_VITALS_PORT", default=29209)

# Message Service
with env.prefixed("BITFOUNT_"):
    # The window in which handlers can be registered for them to be dispatched for a
    # given message.
    HANDLER_REGISTER_GRACE_PERIOD: int = env.int(
        "HANDLER_REGISTER_GRACE_PERIOD", default=30, validate=lambda n: n > 0
    )

    ONLINE_CHECK_SOFT_LIMIT: int = env.int(
        "ONLINE_CHECK_SOFT_LIMIT", default=180, validate=lambda n: n > 0
    )
    ONLINE_CHECK_HARD_LIMIT: int = env.int(
        "ONLINE_CHECK_HARD_LIMIT", default=180, validate=lambda n: n > 0
    )

# Logging/Error Handling
LogLevel = Literal[
    50,  # logging.CRITICAL
    40,  # logging.ERROR
    30,  # logging.WARNING
    20,  # logging.INFO
    10,  # logging.DEBUG
]
_DEFAULT_LOG_FORMAT: Final[str] = (
    "%(asctime)s:"
    " %(processName)s.%(threadName)s:"
    " %(levelname)s"
    " %(name)s:%(filename)s:%(lineno)d"
    " %(message)s"
)
_DEFAULT_LOG_DATE_FORMAT: Final[str] = "%H:%M:%S"
with env.prefixed("BITFOUNT_"):
    AUTO_CONFIGURE_LOGGING: bool = env.bool("AUTO_CONFIGURE_LOGGING", default=True)

    LOG_LEVEL: LogLevel = env.log_level("LOG_LEVEL", default=logging.INFO)
    LOG_FORMAT: str = env.str("LOG_FORMAT", default=_DEFAULT_LOG_FORMAT)
    LOG_DATE_FORMAT: str = env.str("LOG_DATE_FORMAT", default=_DEFAULT_LOG_DATE_FORMAT)
    FILE_LOG_FORMAT: str = env.str("FILE_LOG_FORMAT", default=_DEFAULT_LOG_FORMAT)

    _LIMIT_LOGS: bool = env.bool("LIMIT_LOGS", default=False)
    LOG_TO_FILE: bool = env.bool("LOG_TO_FILE", default=True)
    _TB_LIMIT: int = env.int("TB_LIMIT", default=3)
    _MULTITHREADING_DEBUG: bool = env.bool("MULTITHREADING_DEBUG", default=False)
    _DATA_CACHE_DEBUG: bool = env.bool("DATA_CACHE_DEBUG", default=False)
    _DATA_CACHE_SQL_DEBUG: bool = env.bool("DATA_CACHE_SQL_DEBUG", default=False)

    # [LOGGING-IMPROVEMENTS]
    LOG_AUTHENTICATION_HEADERS: bool = env.bool(
        "LOG_AUTHENTICATION_HEADERS", default=False
    )
    LOG_DICOM_FIXES: bool = env.bool("LOG_DICOM_FIXES", default=False)
    LOG_HOOKS: bool = env.bool("LOG_HOOKS", default=False)
    LOG_MESSAGE_SERVICE: bool = env.bool("LOG_MESSAGE_SERVICE", default=False)
    LOG_POD_HEARTBEAT: bool = env.bool("LOG_POD_HEARTBEAT", default=False)
    LOG_TRANSFORMATION_APPLY: bool = env.bool("LOG_TRANSFORMATION_APPLY", default=False)
    LOG_WEB_UTILS: bool = env.bool("LOG_WEB_UTILS", default=False)
    # Third-party
    LOG_HTTPCORE: bool = env.bool("LOG_HTTPCORE", default=False)
    LOG_HTTPX: bool = env.bool("LOG_HTTPX", default=False)
    LOG_MATPLOTLIB: bool = env.bool("LOG_MATPLOTLIB", default=False)
    LOG_PRIVATE_EYE: bool = env.bool("LOG_PRIVATE_EYE", default=False)
    LOG_URLLIB3: bool = env.bool("LOG_URLLIB3", default=False)

    LOG_FULLY: bool = env.bool("LOG_FULLY", default=False)
    if LOG_FULLY:
        LOG_AUTHENTICATION_HEADERS = True
        LOG_DICOM_FIXES = True
        LOG_HOOKS = True
        LOG_MESSAGE_SERVICE = True
        LOG_POD_HEARTBEAT = True
        LOG_TRANSFORMATION_APPLY = True
        LOG_WEB_UTILS = True

        LOG_HTTPCORE = True
        LOG_HTTPX = True
        LOG_MATPLOTLIB = True
        LOG_PRIVATE_EYE = True
        LOG_URLLIB3 = True

# Task environment variables
# NOTE: These variables have the BITFOUNT_ prefix whilst others don't,
#       as their names are otherwise very generic/ambiguous
with env.prefixed("BITFOUNT_"):
    # This is used by the pod to determine how many batches to split a task into
    # if the modeller has requested batched execution
    BITFOUNT_TASK_BATCH_SIZE: int = env.int(
        "TASK_BATCH_SIZE", default=16, validate=lambda n: n > 0
    )

    # For easier control of the batched execution in the app
    BITFOUNT_DEFAULT_BATCHED_EXECUTION: bool = env.bool(
        "DEFAULT_BATCHED_EXECUTION", default=False
    )

# Shutdown variables
with env.prefixed("BITFOUNT_"):
    POD_HEARTBEAT_SHUTDOWN_TIMEOUT: int = env.int(
        "POD_HEARTBEAT_SHUTDOWN_TIMEOUT", default=15, validate=lambda n: n > 0
    )
    POD_VITALS_HANDLER_SHUTDOWN_TIMEOUT: int = env.int(
        "POD_VITALS_HANDLER_SHUTDOWN_TIMEOUT", default=10, validate=lambda n: n > 0
    )

# Data environment variables
with env.prefixed("BITFOUNT_"):
    # The maximum number of files that can be selected in a FileSystemIterableSource
    # after filtering. This is to prevent the user from selecting a directory with
    # too many files.
    MAX_NUMBER_OF_DATASOURCE_FILES: int = env.int(
        "MAX_NUMBER_OF_DATASOURCE_FILES", default=500_000, validate=lambda n: n > 0
    )

    # The maximum number of files to load for `fast_load` in a FileSystemIterableSource
    FAST_LOAD_MAXIMUM_NUMBER_OF_FILES_TO_LOAD: int = env.int(
        "FAST_LOAD_MAXIMUM_NUMBER_OF_FILES_TO_LOAD",
        default=50,
        validate=lambda n: n > 0,
    )
##############################################
# End of Public Config/Environment Variables #
##############################################

########################################
# Private Config/Environment Variables #
########################################
_BITFOUNT_CLI_MODE: bool = False
_PRODUCTION_ENVIRONMENT: Final[str] = "production"
_STAGING_ENVIRONMENT: Final[str] = "staging"
_DEVELOPMENT_ENVIRONMENT: Final[str] = "dev"
_SANDBOX_ENVIRONMENT: Final[str] = "sandbox"
_ENVIRONMENT_CANDIDATES: tuple[str, ...] = (
    _PRODUCTION_ENVIRONMENT,
    _STAGING_ENVIRONMENT,
    _DEVELOPMENT_ENVIRONMENT,
    _SANDBOX_ENVIRONMENT,
)
# A Bitfount child process is a process that is spawned by the main Bitfount process
# to perform a specific task. This is used to determine if the current process is a
# child process or not and therefore if certain actions should be taken or not.
_BITFOUNT_CHILD_PROCESS: bool = env.bool("_BITFOUNT_CHILD_PROCESS", default=False)

# TODO: [BIT-3597] Remove this feature flag
# Should match the default of the app
BITFOUNT_FILE_MULTIPROCESSING_ENABLED: bool = env.bool(
    "BITFOUNT_FILE_MULTIPROCESSING_ENABLED", default=False
)


def _get_compatible_yaml_versions() -> Optional[list[str]]:
    """Get the compatible yaml versions.

    If plugins are used, they need to contain the compatible
    version in the plugins directory in a __version__.py file.
    Else we use the version defined in __version__.py
    """
    # check if __version__.py exists in the plugins directory
    if os.path.exists(BITFOUNT_PLUGIN_PATH / "__version__.py"):
        spec = util.spec_from_file_location(
            "__version__", BITFOUNT_PLUGIN_PATH / "__version__.py"
        )
        spec = cast(
            ModuleSpec, spec
        )  # safe to cast as the version module is always present
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr] # reason: this should not be None as the module always exists # noqa: E501
        plugin_yaml_version: Optional[list[str]] = None
        try:
            plugin_yaml_version = mod.__yaml__versions__
        except AttributeError:
            logger.debug(
                "No yaml versioning found in the plugins directory, "
                "using yaml versioning from the bitfount package."
            )
        return plugin_yaml_version
    else:
        logger.debug(
            "The current plugins directory is not versioned, "
            "using yaml versioning from the bitfount package."
        )
        return None


plugin_versions = _get_compatible_yaml_versions()
_BITFOUNT_COMPATIBLE_YAML_VERSIONS: list[str] = (
    plugin_versions if plugin_versions is not None else yaml_versions
)


@lru_cache(maxsize=1)
def _get_environment() -> str:
    """Returns bitfount environment to be used from BITFOUNT_ENVIRONMENT variable.

    The result is cached to avoid multiple warning messages. This means that changes to
    the `BITFOUNT_ENVIRONMENT` environment variable will not be detected whilst the
    library is running.

    Returns:
        str: PRODUCTION_ENVIRONMENT, STAGING_ENVIRONMENT, DEVELOPMENT_ENVIRONMENT or
            SANDBOX_ENVIRONMENT

    """

    BITFOUNT_ENVIRONMENT = os.getenv("BITFOUNT_ENVIRONMENT", _PRODUCTION_ENVIRONMENT)
    if BITFOUNT_ENVIRONMENT == "":
        #   It can happen that the environment variable is set to an empty string,
        #   we default to the prod environment in this case.
        BITFOUNT_ENVIRONMENT = _PRODUCTION_ENVIRONMENT

    if BITFOUNT_ENVIRONMENT not in _ENVIRONMENT_CANDIDATES:
        raise ValueError(
            f"The environment specified by the environment variable "
            f"BITFOUNT_ENVIRONMENT ({BITFOUNT_ENVIRONMENT}) is not in the supported "
            f"list of environments ({_ENVIRONMENT_CANDIDATES})"
        )
    if BITFOUNT_ENVIRONMENT == _STAGING_ENVIRONMENT:
        logger.warning(
            "Using the staging environment. "
            + "This will only work for Bitfount employees."
        )
    if BITFOUNT_ENVIRONMENT == _DEVELOPMENT_ENVIRONMENT:
        logger.warning(
            "Using the development environment. "
            + "This will only work if you have all Bitfount services running locally."
        )
    if BITFOUNT_ENVIRONMENT == _SANDBOX_ENVIRONMENT:
        logger.warning(
            "Using the sandbox environment. "
            + "This will only work for Bitfount employees."
        )
    return BITFOUNT_ENVIRONMENT


###############################################
# End of Private Config/Environment Variables #
###############################################

##################
# Backend Engine #
##################
_PYTORCH_ENGINE: Final[str] = "pytorch"
_BASIC_ENGINE: Final[str] = "basic"
_ENGINE_CANDIDATES: tuple[str, ...] = (
    _BASIC_ENGINE,
    _PYTORCH_ENGINE,
)

# Set BITFOUNT_ENGINE, defaulting to PYTORCH_ENGINE or BASIC_ENGINE
# Start with BASIC_ENGINE as default
BITFOUNT_ENGINE: str = _BASIC_ENGINE
try:
    # Use the type specified by envvar if present
    BITFOUNT_ENGINE = os.environ["BITFOUNT_ENGINE"]
    # Check that the engine option is a valid one
    if BITFOUNT_ENGINE not in _ENGINE_CANDIDATES:
        raise ValueError(
            f"The backend engine specified by the environment variable "
            f"BITFOUNT_ENGINE ({BITFOUNT_ENGINE}) is not in the supported list of "
            f"backends ({_ENGINE_CANDIDATES})"
        )
except KeyError:
    # Don't import pytorch if in a child process
    if not _BITFOUNT_CHILD_PROCESS:
        # Otherwise, if PyTorch is installed use PYTORCH_ENGINE
        try:
            import torch

            BITFOUNT_ENGINE = _PYTORCH_ENGINE
        except ImportError:
            pass
    else:
        logger.warning("Not importing PyTorch in a child process.")

#########################
# End of Backend Engine #
#########################

##############
# DP Support #
##############
DP_AVAILABLE: bool
try:
    import opacus  # noqa: F401

    DP_AVAILABLE = True
except ImportError:
    logger.debug("Differential Privacy requirements not installed.")
    DP_AVAILABLE = False
#####################
# End of DP Support #
#####################


#############################
# GPU information retrieval #
#############################
def _get_gpu_metadata_gputil() -> tuple[Optional[str], int]:
    """Returns gpu metadata from GPUtil.

    Uses the name of the first GPU thereby assuming that there is only 1 type of GPU
    attached to the machine.

    Returns:
        tuple[Optional[str], int]: name of gpu and how many there are
    """
    gpus = GPUtil.getGPUs()
    if gpus:
        return gpus[0].name, len(gpus)
    # nvidia-smi installed, but no GPU available
    return None, 0


def get_cuda_metadata_pytorch() -> tuple[Optional[str], int]:
    """Return gpu metadata from pytorch.

    Returns:
        tuple[Optional[str], int]: name of gpu and how many there are
    """
    try:
        if torch.cuda.is_available():
            gpus: int = torch.cuda.device_count()
            if gpus > 0:
                gpu_0_name: str = torch.cuda.get_device_name(0)
                logger.info(f"CUDA support detected. GPU ({gpu_0_name}) will be used.")
                return gpu_0_name, gpus
            else:
                logger.debug("CUDA is available to PyTorch but there are no GPUs")
        else:
            logger.debug("CUDA is not available to PyTorch")
    except Exception as ex:
        logger.info(f"CUDA is not available to PyTorch: {ex}")

    return None, 0


_GPU_COUNT_FUNCTION_LOOKUP: dict[str, Callable[..., tuple[Optional[str], int]]] = {
    _BASIC_ENGINE: _get_gpu_metadata_gputil,
    _PYTORCH_ENGINE: get_cuda_metadata_pytorch,
}


def get_gpu_metadata() -> tuple[Optional[str], int]:
    """Retrieve details about GPUs if available.

    Uses tools available in the appropriate backend,
    to find GPUs that are usable by the backend.

    Returns: a tuple of GPU name and count.
    """
    # noinspection PyBroadException
    try:
        return _GPU_COUNT_FUNCTION_LOOKUP[BITFOUNT_ENGINE]()
    except Exception as ex:
        # Broad exception handling here as libraries may throw various exceptions
        # But if anything is raised we can assume we don't have GPU access
        logger.warning(f"Encountered exception whilst gathering GPU information: {ex}")
        logger.warning("No GPU info will be used.")
        return None, 0


def has_mps() -> bool:
    """Detect if MPS is available and torch can use it."""
    mps = False
    try:
        # Older PyTorch versions don't have this attribute so need to catch
        if torch.backends.mps.is_available() and platform.processor() in (
            "arm",
            "arm64",
        ):
            if USE_MPS:
                mps = True
                logger.info("MPS is available to PyTorch.")
            else:
                logger.debug("MPS support detected, but has been switched off.")
    except AttributeError:
        logger.info("Pytorch version does not support MPS.")
    return mps


def has_cuda() -> bool:
    """Detect if CUDA is available and torch can use it."""
    cuda_device_name, _ = get_cuda_metadata_pytorch()
    return cuda_device_name is not None


####################################
# End of GPU information retrieval #
####################################
