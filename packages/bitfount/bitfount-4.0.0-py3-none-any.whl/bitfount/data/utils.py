"""Utility functions concerning data."""

from __future__ import annotations

from collections.abc import Mapping
import enum
from enum import Enum
import hashlib
import json
import logging
from typing import TYPE_CHECKING, Any, Optional, Union

from bitfount.data.exceptions import (
    BitfountSchemaError,
)
from bitfount.data.types import SemanticType

if TYPE_CHECKING:
    from bitfount.data.datastructure import DataStructure
    from bitfount.data.schema import BitfountSchema, TableSchema

logger = logging.getLogger(__name__)


def _generate_dtypes_hash(dtypes: Mapping[str, Any]) -> str:
    """Generates a hash of a column name -> column type mapping.

    Uses column names and column dtypes to generate the hash. DataFrame contents
    is NOT used.

    SHA256 is used for hash generation.

    Args:
        dtypes: The mapping to hash.

    Returns:
        The hexdigest of the mapping hash.
    """
    dtypes = {k: str(v) for k, v in dtypes.items()}
    str_rep: str = json.dumps(dtypes, sort_keys=True)
    return _hash_str(str_rep)


def _hash_str(to_hash: str) -> str:
    """Generates a sha256 hash of a given string.

    Uses UTF-8 to encode the string before hashing.
    """
    return hashlib.sha256(to_hash.encode("utf-8")).hexdigest()


class DataStructureSchemaCompatibility(Enum):
    """The level of compatibility between a datastructure and a pod/table schema.

    Denotes 4 different levels of compatibility:
        - COMPATIBLE: Compatible to our knowledge.
        - WARNING: Might be compatible but there might still be runtime
                   incompatibility issues.
        - INCOMPATIBLE: Clearly incompatible.
        - ERROR: An error occurred whilst trying to check compatibility.
    """

    # Compatible to our knowledge
    COMPATIBLE = enum.auto()
    # Might be compatible but there might still be runtime incompatibility issues
    WARNING = enum.auto()
    # Clearly incompatible
    INCOMPATIBLE = enum.auto()
    # An error occurred whilst trying to check compatibility
    ERROR = enum.auto()


def check_datastructure_schema_compatibility(
    datastructure: DataStructure,
    schema: BitfountSchema,
    data_identifier: Optional[str] = None,
) -> tuple[DataStructureSchemaCompatibility, list[str]]:
    """Compare a datastructure from a task and a data schema for compatibility.

    Currently, this checks that requested columns exist in the target schema.

    Query-based datastructures are not supported.

    Args:
        datastructure: The datastructure for the task.
        schema: The overall schema for the pod in question.
        data_identifier: If the datastructure specifies multiple pods then the data
            identifier is needed to identify which part of the datastructure refers
            to the pod in question.

    Returns:
        A tuple of the compatibility level (DataStructureSchemaCompatibility value),
        and a list of strings which are all compatibility warnings/issues found.
    """
    curr_compat_level = DataStructureSchemaCompatibility.COMPATIBLE

    # If a query (or queries) are supplied, we cannot check this
    # TODO: [BIT-3099] Implement a way to check column names referenced in queries
    if datastructure.query:
        return DataStructureSchemaCompatibility.WARNING, [
            "Warning: Cannot check query compatibility."
        ]

    # Extract table name
    table_name: str
    try:
        # If the datastructure is for multiple pods and we've not been told which
        # one, or it's not in the mapping, error out
        table_name = datastructure.get_table_name(data_identifier)
    except (ValueError, KeyError):
        return DataStructureSchemaCompatibility.ERROR, [
            f"Error: Multiple pods are specified in the datastructure"
            f' but pod "{data_identifier}" was not one of them.'
        ]

    # Extract table schema
    table_schema: TableSchema
    try:
        table_schema = schema.table
        if table_name != table_schema.name:
            raise BitfountSchemaError(
                f"Table name mismatch: Expected table name '{table_name}'"
                f" but found '{table_schema.name}'."
            )
    except BitfountSchemaError:
        return DataStructureSchemaCompatibility.ERROR, [
            f"Error: Unable to find the table schema for"
            f' the table name "{table_name}".'
        ]

    # Extract column names from schema
    schema_columns: dict[Union[str, SemanticType], set[str]] = {
        st: set(table_schema.get_feature_names(st)) for st in SemanticType
    }
    schema_columns["ALL"] = set(table_schema.get_feature_names())

    # Collect any missing column details for which we consider the missing column
    # to be an WARNING:
    #   - ignored
    warning_cols: dict[str, list[str]] = {
        col_type: _find_missing_columns(req_cols, schema_columns["ALL"])
        for col_type, req_cols in (("ignore", datastructure.ignore_cols),)
    }
    warnings: list[str] = sorted(
        [
            f'Warning: Expected "{col_type}" column, "{col}",'
            f" but it could not be found in the data schema."
            for col_type, cols in warning_cols.items()
            for col in cols
        ]
    )
    if warnings:
        curr_compat_level = DataStructureSchemaCompatibility.WARNING

    # Collect any missing column details for which we consider the missing column
    # to indicate INCOMPATIBLE:
    #   - target
    #   - selected
    #   - image
    incompatible_cols = {
        col_type: _find_missing_columns(req_cols, schema_columns["ALL"])
        for col_type, req_cols in (
            ("target", datastructure.target),
            ("select", datastructure.selected_cols),
            ("image", datastructure.image_cols),
        )
    }
    incompatible: list[str] = sorted(
        [
            f'Incompatible: Expected "{col_type}" column, "{col}",'
            f" but it could not be found in the data schema."
            for col_type, cols in incompatible_cols.items()
            for col in cols
        ]
    )
    if incompatible:
        curr_compat_level = DataStructureSchemaCompatibility.INCOMPATIBLE

    # TODO: [BIT-3100] Add semantic type checks for additional compatibility
    #       constraints

    return curr_compat_level, incompatible + warnings


def _find_missing_columns(
    to_check: Optional[Union[str, list[str]]], check_against: set[str]
) -> list[str]:
    """Check if requested columns are missing from a set.

    Args:
        to_check: the column name(s) to check for inclusion.
        check_against: the set of columns to check against.

    Returns:
        A sorted list of all column names from `to_check` that _weren't_ found in
        `check_against`.
    """
    # If nothing to check, return empty list
    if to_check is None:
        return []

    # If only one to check, shortcut check it
    if isinstance(to_check, str):
        if to_check not in check_against:
            return [to_check]
        else:
            return []

    # Otherwise, perform full check
    to_check_set: set[str] = set(to_check)
    return sorted(to_check_set.difference(check_against))
