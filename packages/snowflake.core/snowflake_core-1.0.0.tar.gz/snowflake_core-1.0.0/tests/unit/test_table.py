from contextlib import suppress
from unittest import mock

from snowflake.core.table import Table, TableColumn
from snowflake.core.version import __version__ as VERSION


SNOWPY_USER_AGENT_VAL = "python_api/" + VERSION

def test_create_table(fake_root, tables, table):
    with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
        tables.create(table)
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables?createMode=errorIfExists&copyGrants=False",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False)],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={
            "name": "my_table",
            "kind": "PERMANENT",
            "columns": [{"name": "c1", "datatype": "int", "nullable": True}],
        },
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_table_deprecated(fake_root, tables):
    table = Table(
        name="my_table",
        kind="transient",
        columns=[
            TableColumn(name="c1", datatype="int"),
        ],
    )

    with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
        tables.create(table)
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables?createMode=errorIfExists&copyGrants=False",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False)],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={
            "name": "my_table",
            "kind": "TRANSIENT",
            "columns": [{"name": "c1", "datatype": "int", "nullable": True}],
        },
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_table_as_select_with_table_as_str(fake_root, tables):
    with suppress(Exception):
        with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
            tables.create("my_table", as_select="SELECT 1")
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables:as-select?"
        "createMode=errorIfExists&copyGrants=False&query=SELECT 1",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False), ("query", "SELECT 1")],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={"name": "my_table"},
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_table_as_select_with_table_module(fake_root, tables, table):
    with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
        tables.create(table, as_select="SELECT 1")
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables:as-select?"
        "createMode=errorIfExists&copyGrants=False&query=SELECT 1",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False), ("query", "SELECT 1")],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={"name": "my_table", "columns": [{"name": "c1", "datatype": "int", "nullable": True}]},
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_table_using_template(fake_root, tables):
    with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
        tables.create(
            "my_table",
            template="select array_agg(object_construct(*)) "
            "from table(infer_schema(location=>'@table_test_stage', "
            "file_format=>'table_test_csv_format', "
            "files=>'testCSVheader.csv'))",
        )
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables:using-template?"
        "createMode=errorIfExists&copyGrants=False&query=select array_agg(object_construct(*)) from "
        "table(infer_schema(location=>'@table_test_stage', file_format=>'table_test_csv_format', "
        "files=>'testCSVheader.csv'))",
        query_params=[
            ("createMode", "errorIfExists"),
            ("copyGrants", False),
            (
                "query",
                "select array_agg(object_construct(*)) from table(infer_schema(location=>"
                "'@table_test_stage', file_format=>'table_test_csv_format', files=>'testCSVheader.csv'))",
            ),
        ],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={"name": "my_table"},
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_table_as_like(fake_root, tables):
    with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
        tables.create("my_table", like_table="temp_table")
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables/temp_table:create-like?"
        "createMode=errorIfExists&copyGrants=False",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False)],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={"name": "my_table"},
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_table_clone(fake_root, tables):
    with mock.patch("snowflake.core.table._generated.api_client.ApiClient.request") as mocked_request:
        tables.create("my_table", clone_table="temp_clone_table")
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/tables/temp_clone_table:clone?createMode=errorIfExists&copyGrants=False&targetDatabase=my_db&targetSchema=my_schema",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False), ('targetDatabase', 'my_db'),
                      ('targetSchema', 'my_schema')],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={"name": "my_table", "kind": "PERMANENT"},
        _preload_content=True,
        _request_timeout=None,
    )
