#
# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
#

from operator import attrgetter

import pytest

from pydantic_core._pydantic_core import ValidationError


pytestmark = [
    pytest.mark.usefixtures("backup_database_schema"),
]


def test_iter(databases, temp_db, temp_db_case_sensitive):
    database_names = tuple(
        map(
            attrgetter("name"),
            databases.iter(),
        )
    )
    assert any(
        map(
            lambda e: e in database_names,
            (
                temp_db.name.upper(),  # for upper/lower case names
            ),
        )
    )

    # TODO(SNOW-1354988) - Please uncomment this once you have this bug resolved
    # assert any(
    #     map(
    #         lambda e: e in database_names,
    #         (
    #             temp_db_case_sensitive.name,  # for mixed case names
    #         ),
    #     )
    # )


def test_iter_like(databases, temp_db, temp_db_case_sensitive):
    database_names = tuple(
        map(
            attrgetter("name"),
            databases.iter(like="test_database%"),
        )
    )
    assert any(
        map(
            lambda e: e in database_names,
            (
                temp_db.name.upper(),  # for upper/lower case names
            ),
        )
    )

    # TODO(SNOW-1354988) - Please uncomment this once you have this bug resolved
    # assert any(
    #     map(
    #         lambda e: e in database_names,
    #         (
    #             temp_db_case_sensitive.name,  # for mixed case names
    #         ),
    #     )
    # )


def test_iter_starts_with(databases, temp_db, temp_db_case_sensitive):
    database_names = tuple(
        map(
            attrgetter("name"),
            databases.iter(starts_with="Test_database"),
        )
    )
    assert not any(
        map(
            lambda e: e in database_names,
            (
                temp_db.name.upper(),  # for upper/lower case names
            ),
        )
    )

    assert not any(
        map(
            lambda e: e in database_names,
            (
                temp_db_case_sensitive.name,  # for mixed case names
            ),
        )
    )

    database_names = tuple(
        map(
            attrgetter("name"),
            databases.iter(starts_with="TEST_DATABASE"),
        )
    )
    assert any(
        map(
            lambda e: e in database_names,
            (
                temp_db.name.upper(),  # for upper/lower case names
            ),
        )
    )

    assert not any(
        map(
            lambda e: e in database_names,
            (
                temp_db_case_sensitive.name,  # for mixed case names
            ),
        )
    )


# TODO(SNOW-1355013) - Please uncomment this once you have this bug resolved
# def test_iter_from_name(databases, temp_db, temp_db_case_sensitive):
#     database_names = tuple(
#         map(
#             attrgetter("name"),
#             databases.iter(from_name="test_schema"),
#         )
#     )
#     assert not any(
#         map(
#             lambda e: e in database_names,
#             (
#                 temp_db.name.upper(),  # for upper/lower case names
#             ),
#         )
#     )
#     # TODO(SNOW-1354988) - Please uncomment this once you have this bug resolved
#     # assert any(
#     #     map(
#     #         lambda e: e in database_names,
#     #         (
#     #             temp_db_case_sensitive.name,  # for mixed case names
#     #         ),
#     #     )
#     # )


def test_iter_limit(databases):
    data = list(databases.iter())
    initial_length = len(data)

    data = list(databases.iter(limit=initial_length))
    assert len(data) <= initial_length

    data = list(databases.iter(limit=initial_length - 1))
    assert len(data) <= initial_length - 1

    data = list(databases.iter(limit=10000))
    assert len(data) <= 10000

    with pytest.raises(
        ValidationError,
    ):
        data = list(databases.iter(limit=10001))
