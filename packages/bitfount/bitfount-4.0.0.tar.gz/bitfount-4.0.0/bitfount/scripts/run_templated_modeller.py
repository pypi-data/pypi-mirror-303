#!/usr/bin/env python3
"""Run a task from a templated yaml config file.

Usage:
python -m python -m bitfount.scripts.run_templated_modeller \
`path-to-yaml-config` '[missing-default-1, missing-default-2]'

"""

from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import Any, Optional, Union

import desert
import fire
import yaml

from bitfount import config
from bitfount.federated import _Modeller
from bitfount.runners.config_schemas import ModellerConfig
from bitfount.runners.modeller_runner import (
    DEFAULT_MODEL_OUT,
    run_modeller,
    setup_modeller_from_config,
)
from bitfount.utils.logging_utils import log_pytorch_env_info_if_available

config._BITFOUNT_CLI_MODE = True


def dict_replace_value(
    dictionary: dict[str, Any],
    old_value: str,
    new_value: Union[str, list[str], dict[str, Any]],
) -> dict[str, Any]:
    """Helper function to replace a value in a dictionary."""
    updated_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(value)
            value = dict_replace_value(value, old_value, new_value)
        elif isinstance(value, list):
            value = list_replace_value(value, old_value, new_value)
        elif isinstance(value, str):
            if isinstance(new_value, str) and old_value in value:
                value = new_value
            elif isinstance(new_value, list) and old_value in value:
                value = new_value
            elif isinstance(new_value, dict) and old_value in value:
                value = new_value
        updated_dict[key] = value
    return updated_dict


def list_replace_value(
    lst: list[Any], old_value: str, new_value: Union[str, list[str], dict[str, Any]]
) -> list[Any]:
    """Helper function to replace a value in a list."""
    updated_lst = []
    for item in lst:
        if isinstance(item, list):
            item = list_replace_value(item, old_value, new_value)
        elif isinstance(item, dict):
            item = dict_replace_value(item, old_value, new_value)
        elif isinstance(item, str):
            if old_value in item:
                if isinstance(new_value, str):
                    item = new_value
                elif isinstance(new_value, list):
                    item = new_value
                elif isinstance(new_value, dict):
                    item = new_value
        updated_lst.append(item)
    return updated_lst


def setup_templated_modeller_from_config_file(
    path_to_config_yaml: Union[str, PathLike], defaults: Optional[list] = None
) -> tuple[_Modeller, list[str], Optional[str], bool, bool]:
    """Creates a modeller from a YAML config file.

    Args:
        path_to_config_yaml: the path to the config file
        defaults: list of default values to use for templating the config

    Returns:
        A tuple of the created Modeller and the list of pod identifiers to run
    """
    path_to_config_yaml = Path(path_to_config_yaml)

    with open(path_to_config_yaml) as f:
        config_yaml = yaml.safe_load(f)

    if "template" in config_yaml.keys():
        i = 0
        template = config_yaml["template"]
        del config_yaml["template"]
        for item_to_template, default_value in template.items():
            default = default_value.get("default")
            item_to_template = "{{ " + item_to_template + " }}"
            if default:
                config_yaml = dict_replace_value(
                    config_yaml, item_to_template, str(default)
                )
            elif defaults and i < len(defaults):
                config_yaml = dict_replace_value(
                    config_yaml, item_to_template, defaults[i]
                )
                i += 1
            else:
                raise ValueError("Need additional values to template config.")
    modeller_config_schema = desert.schema(ModellerConfig)
    modeller_config_schema.context["config_path"] = path_to_config_yaml

    config: ModellerConfig = modeller_config_schema.load(config_yaml)
    return setup_modeller_from_config(config)


def run(
    path_to_config_yaml: Union[str, PathLike],
    defaults: Optional[list] = None,
    require_all_pods: bool = False,
    model_out: Path = DEFAULT_MODEL_OUT,
) -> None:
    """Runs a modeller from a config file.

    Args:
        path_to_config_yaml: Path to the config YAML file.
        defaults: list of default values to use for templating the config.
        require_all_pods: Whether to require all pods to accept the task before
            continuing.
        model_out: Path to save the model to (if applicable).
    """
    log_pytorch_env_info_if_available()

    (
        modeller,
        pod_identifiers,
        project_id,
        run_on_new_datapoints,
        batched_execution,
    ) = setup_templated_modeller_from_config_file(path_to_config_yaml, defaults)

    run_modeller(
        modeller,
        pod_identifiers,
        require_all_pods,
        model_out,
        project_id,
        run_on_new_datapoints,
        batched_execution,
    )


if __name__ == "__main__":
    fire.Fire(run)
