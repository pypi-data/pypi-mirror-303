from contextlib import suppress

import pytest as pytest

from snowflake.core.database_role import DatabaseRole
from snowflake.core.exceptions import NotFoundError
from tests.integ.utils import random_string


@pytest.fixture
def test_database_role_name(database_roles):
    role_name = random_string(4, "test_grant_database_role_")
    test_role = DatabaseRole(name=role_name, comment="test_comment")
    try:
        database_roles.create(test_role)
        yield role_name
    finally:
        with suppress(NotFoundError):
            database_roles[role_name].drop()


@pytest.fixture
def test_database_role_name_2(database_roles):
    role_name = random_string(4, "test_grant_database_role_2_")
    test_role = DatabaseRole(name=role_name, comment="test_comment")
    try:
        database_roles.create(test_role)
        yield role_name
    finally:
        with suppress(NotFoundError):
            database_roles[role_name].drop()
