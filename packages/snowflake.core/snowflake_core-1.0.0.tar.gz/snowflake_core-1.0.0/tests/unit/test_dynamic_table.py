from unittest import mock

from snowflake.core.dynamic_table import DownstreamLag, DynamicTable, DynamicTableColumn
from snowflake.core.version import __version__ as VERSION


SNOWPY_USER_AGENT_VAL = "python_api/" + VERSION

def test_create_dynamic_table(fake_root, dynamic_tables):
    dynamic_table = DynamicTable(
        name="my_table",
        target_lag=DownstreamLag(),
        warehouse='wh',
        columns=[
            DynamicTableColumn(name="c1", datatype="int"),
        ],
        query='SELECT * FROM foo',
    )

    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_tables.create(dynamic_table)
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables?createMode=errorIfExists",
        query_params=[("createMode", "errorIfExists")],
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body={
            "name": "my_table",
            "kind": "PERMANENT",
            "target_lag": {"type": "DOWNSTREAM"},
            "warehouse": "wh",
            "columns": [{"name": "c1", "datatype": "int"}],
            "query": "SELECT * FROM foo",
        },
        _preload_content=True,
        _request_timeout=None,
    )


def test_create_dynamic_table_clone(fake_root, dynamic_tables):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_tables.create("my_table", clone_table="temp_clone_table")
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/temp_clone_table:clone?" +\
            "createMode=errorIfExists&copyGrants=False&targetDatabase=my_db&targetSchema=my_schema",
        query_params=[("createMode", "errorIfExists"), ("copyGrants", False), ('targetDatabase', 'my_db'),
                      ('targetSchema', 'my_schema')],
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


def test_drop_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.drop()
    mocked_request.assert_called_once_with(
        fake_root,
        "DELETE",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_undrop_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.undelete()
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:undrop",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_suspend_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.suspend()
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:suspend",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_resume_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.resume()
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:resume",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_refresh_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.refresh()
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:refresh",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_swap_with_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.swap_with("other_db.other_schema.other_table")
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:swap-with?targetName=other_db.other_schema.other_table",
        query_params=[('targetName', 'other_db.other_schema.other_table')],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_suspend_recluster_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.suspend_recluster()
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:suspend-recluster",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )


def test_resume_recluster_dynamic_table(fake_root, dynamic_table):
    with mock.patch("snowflake.core.dynamic_table._generated.api_client.ApiClient.request") as mocked_request:
        dynamic_table.resume_recluster()
    mocked_request.assert_called_once_with(
        fake_root,
        "POST",
        "http://localhost:80/api/v2/databases/my_db/schemas/my_schema/dynamic-tables/my_table:resume-recluster",
        query_params=[],
        headers={
            "Accept": "application/json",
            "User-Agent": SNOWPY_USER_AGENT_VAL,
        },
        post_params=[],
        body=None,
        _preload_content=True,
        _request_timeout=None,
    )
