"""Additional functionality for DataFrame processing.

Provides functions that can be used for additional column generation.
"""

from __future__ import annotations

from collections.abc import Callable
from hashlib import md5
import re

from dateutil.parser import ParserError as DateUtilParserError
import pandas as pd
from pandas.errors import ParserError as PandasParserError
import text_unidecode

from bitfount.exceptions import BitfountError
from bitfount.federated.algorithms.ophthalmology.ophth_algo_types import (
    _BITFOUNT_PATIENT_ID_KEY,
    DOB_COL,
    NAME_COL,
)
from bitfount.federated.logging import _get_federated_logger

# Try to import the specific date parsing error from pandas, but if not possible,
# defer to the parent class of that exception
# mypy_reason: distinct paths through import
try:
    from pandas._libs.tslibs.parsing import DateParseError as PandasDateParseError
except ImportError:
    PandasDateParseError = ValueError  # type: ignore[misc,assignment] # Reason: see above # noqa: E501

DataFrameExtensionFunction = Callable[[pd.DataFrame], pd.DataFrame]

_logger = _get_federated_logger(f"bitfount.federated.algorithms.{__name__}")

extensions: dict[str, DataFrameExtensionFunction] = {}


def _register(
    register_name: str,
) -> Callable[[DataFrameExtensionFunction], DataFrameExtensionFunction]:
    """Decorate a function to register it as a DataFrame extension function.

    Args:
        register_name: The name to store the function against in the registry.
    """

    def _decorator(func: DataFrameExtensionFunction) -> DataFrameExtensionFunction:
        extensions[register_name] = func
        return func

    return _decorator


def id_safe_string(s: str) -> str:
    """Converts a string to a normalised version safe for use in IDs.

    In particular, converts accented/diacritic characters to their closest ASCII
    representation, ensures lowercase, and replaces any non-word characters with
    underscores.

    This allows us to map potentially different spellings (e.g. Francois John-Smith
    vs François John Smith) to the same string (francois_john_smith).
    """
    # First, ensure we are working in lower case.
    s = s.lower()

    # Next split and combine each "segment"
    # Here we split on any non-word characters (i.e. anything expect letters,
    # numbers, or underscore).
    s = "_".join(re.split(r"\W+", s))

    # Convert to a normalised unicode form, removing any combining characters (e.g.
    # accent modifiers, etc.).
    # This has the effect of converting things like 'ø' or 'é' to 'o' and 'e'
    # respectively.
    # `unidecode()` is relatively expensive, so we only do it if needed.
    if not s.isascii():
        s = text_unidecode.unidecode(s)

    return s


@_register(_BITFOUNT_PATIENT_ID_KEY)
def generate_bitfount_patient_id(
    df: pd.DataFrame, name_col: str = NAME_COL, dob_col: str = DOB_COL
) -> pd.DataFrame:
    """Adds a BitfountPatientID column to the provided DataFrame.

    This mutates the input dataframe with the new column.

    The generated IDs are the hash of the concatenated string of a Bitfount-specific
    key, full name, and date of birth.
    """
    try:
        # In order to get a consistent string representation of the dates, whilst
        # still maintaining nulls, we have to do this conversion via `.apply()` as
        # using just `.to_datetime()` and `astype(str)` converts nulls to "NaT"
        # strings.
        # See: https://github.com/pandas-dev/pandas/issues/31708
        dobs: pd.Series[str] = df[dob_col].apply(
            lambda x: pd.to_datetime(x).strftime("%Y-%m-%d") if pd.notnull(x) else pd.NA
        )

        # As above, need to use `apply()` to ensure that nulls are respected
        name_ids: pd.Series[str] = df[name_col].apply(
            lambda x: id_safe_string(x) if pd.notnull(x) else pd.NA
        )
    except KeyError as ke:
        raise DataFrameExtensionError(
            f"Unable to add BitfountPatientID column, missing base columns: {ke}"
        ) from ke
    except (DateUtilParserError, PandasDateParseError, PandasParserError) as dpe:
        # The error message may contain data information, so we want to ensure this
        # info is only logged locally, not potentially propagated back to the modeller
        # as part of the exception message.
        _logger.error(
            f"Parsing error whilst processing date of birth column, {dob_col}: {dpe}"
        )
        raise DataFrameExtensionError(
            f"Parsing error whilst processing date of birth column, {dob_col}."
            f" See Bitfount logs for details."
        ) from dpe

    # Concatenate the separate elements together, prepended with our key.
    # This concatenation respects null entries.
    patient_ids: pd.Series[str] = _BITFOUNT_PATIENT_ID_KEY + name_ids + dobs

    # Calculate the hash value of the generated key to ensure the IDs are obfuscated
    # We use md5 here, which is cryptographically broken but fine for our use-case as
    # it is not being used for security.
    # SHA-256 is ~20% slower than md5 which, for the scale of entries we are
    # considering, is a noticeable difference for no additional benefit.
    patient_ids = patient_ids.apply(
        lambda x: (
            md5(x.encode(), usedforsecurity=False).hexdigest()  # nosec[blacklist] md5 is not being used in a security context # noqa: E501
            if pd.notnull(x)
            else pd.NA
        )
    )

    # Add the new Bitfount patient ID column
    # This mutates the input dataframe, so returning it is slightly redundant but
    # we do so to ensure compatibility with other extensions.
    df[_BITFOUNT_PATIENT_ID_KEY] = patient_ids
    return df


class DataFrameExtensionError(BitfountError):
    """Indicates an error whilst trying to apply an extension function."""

    pass
