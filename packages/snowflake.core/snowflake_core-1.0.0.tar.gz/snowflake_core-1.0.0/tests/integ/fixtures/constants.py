import uuid

from typing import Dict, NamedTuple, Set, TypedDict


TEST_DATABASE = "TESTDB_PYTHON_AUTO"
TEST_SCHEMA = "GH_JOB_{}".format(str(uuid.uuid4()).replace("-", "_"))
TEST_WAREHOUSE = 'TESTWH_PYTHON'
TEST_COMPUTE_POOL = "test_compute_pool"
TEST_IMAGE_REPO = "test_image_repo_auto"
DEFAULT_IR_URL = (
    "sfengineering-ss-lprpr-test2.registry.snowflakecomputing.com/"
    + "testdb_python_auto/testschema_auto/test_image_repo_auto"
)

class Tuple_database(NamedTuple):
    name: str
    param: str


class DatabaseDict(TypedDict):
    params: str
    schemas: Set[str]

class SpcsSetupTuple(NamedTuple):
    instance_family: str
    compute_pool: str


objects_to_setup: Dict[str, DatabaseDict] = {
    TEST_DATABASE: {
        "schemas": {
            TEST_SCHEMA,
        },
        "params": "DATA_RETENTION_TIME_IN_DAYS=1",
    },
}
