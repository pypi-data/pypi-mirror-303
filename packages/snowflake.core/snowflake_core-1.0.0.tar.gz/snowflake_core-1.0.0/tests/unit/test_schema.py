from contextlib import suppress
from unittest import mock

from snowflake.core.schema import Schema
from snowflake.core.version import __version__ as VERSION


SNOWPY_USER_AGENT_VAL = "python_api/" + VERSION

def test_fetch(fake_root, schema):
    with suppress(Exception):
        with mock.patch("snowflake.core.schema._generated.api_client.ApiClient.request") as mocked_request:
            schema.fetch()
    mocked_request.assert_called_once_with(
        fake_root,
        "GET",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema",
        query_params=[],
        headers={"Accept": "application/json", "User-Agent": SNOWPY_USER_AGENT_VAL},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_drop(fake_root, schema):
    with mock.patch("snowflake.core.schema._generated.api_client.ApiClient.request") as mocked_request:
        schema.drop()
    mocked_request.assert_called_once_with(
        fake_root,
        "DELETE",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema",
        query_params=[],
        headers={"Accept": "application/json", "User-Agent": SNOWPY_USER_AGENT_VAL},
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_create(fake_root, schemas):
    with mock.patch("snowflake.core.schema._generated.api_client.ApiClient.request") as mocked_request:
        schemas.create(
            Schema(
                name="my_schema",
                kind="TRANSIENT",
                comment="my schema",
                trace_level="always",
            ),
        )
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas?createMode=errorIfExists",
        query_params=[
            ("createMode", "errorIfExists"),
        ],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={
            "name": "my_schema",
            "kind": "TRANSIENT",
            "comment": "my schema",
            "trace_level": "always",
            "dropped_on": None,
            "managed_access": False,
        },
        _preload_content=True,
        _request_timeout=None,
    )
