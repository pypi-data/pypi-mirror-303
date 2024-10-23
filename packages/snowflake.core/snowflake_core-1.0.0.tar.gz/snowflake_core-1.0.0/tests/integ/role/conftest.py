from contextlib import suppress

import pytest as pytest

from tests.integ.utils import random_string

from snowflake.core.role import Role


@pytest.fixture
def test_database_role_name(connection):
    database_role_name = random_string(4, "test_database_grant_role_")
    with connection.cursor() as cursor:
        cursor.execute(f"create database role if not exists {database_role_name}")
        try:
            yield database_role_name
        finally:
            cursor.execute(f"drop database role if exists {database_role_name}")


@pytest.fixture
def test_role_name(roles):
    role_name = random_string(4, "test_grant_role_")
    test_role = Role(name=role_name, comment="test_comment")
    try:
        roles.create(test_role)
        yield role_name
    finally:
        with suppress(Exception):
            roles[role_name].drop()


@pytest.fixture
def test_role_name_2(roles):
    role_name = random_string(4, "test_grant_role_2_")
    test_role = Role(name=role_name, comment="test_comment")
    try:
        roles.create(test_role)
        yield role_name
    finally:
        with suppress(Exception):
            roles[role_name].drop()
