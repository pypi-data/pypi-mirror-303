import random
import string
import time

from typing import Sequence

import pytest

from snowflake.core._utils import check_version_gte


def is_prod_version(version_str) -> bool:
    # Check if version string is all digits or decimals, because non-prod versions contain
    # letters or other symbols.
    return version_str and all(character.isdigit() or character == '.' for character in version_str)


def ensure_snowflake_version(current_version, requested_version):
    # Check if current version of Snowflake used for testing meets the minimum requested version
    if is_prod_version(current_version):
        if not check_version_gte(current_version, requested_version):
            pytest.skip(
                f"Skipping test because the current server version {current_version} "
                f"is older than the minimum version {requested_version}"
            )


def random_string(
    length: int,
    prefix: str = "",
    suffix: str = "",
    choices: Sequence[str] = string.ascii_lowercase,
) -> str:
    """Our convenience function to generate random string for object names.

    Args:
        length: How many random characters to choose from choices.
            length would be at least 6 for avoiding collision
        prefix: Prefix to add to random string generated.
        suffix: Suffix to add to random string generated.
        choices: A generator of things to choose from.
    """
    random_part = "".join([random.choice(choices) for _ in range(length)]) + str(time.time_ns())

    return "".join([prefix, random_part, suffix])
