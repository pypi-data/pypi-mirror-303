from contextlib import suppress

import pytest

from snowflake.core.role import Role
from snowflake.core.user import User
from tests.utils import random_string


@pytest.fixture
def test_user_name(users):
    user_name = random_string(4, "test_grant_user_")
    test_user = User(
        name=user_name,
        password="test",
        display_name="test_name",
        first_name="firstname",
        last_name="lastname",
        email="test@snowflake.com",
        must_change_password=False,
        disabled=False,
        days_to_expiry=1,
        mins_to_unlock=10,
        mins_to_bypass_mfa=60,
        default_warehouse="test",
        default_namespace="test",
        default_role="public",
        default_secondary_roles="ALL",
        comment="test_comment",
    )
    try:
        users.create(test_user)
        yield user_name
    finally:
        with suppress(Exception):
            users[user_name].drop()


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
