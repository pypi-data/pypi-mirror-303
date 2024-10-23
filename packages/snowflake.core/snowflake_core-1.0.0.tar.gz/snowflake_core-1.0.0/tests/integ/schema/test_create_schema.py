import copy

from time import sleep

import pytest

from snowflake.core import Clone, PointOfTimeOffset
from snowflake.core.exceptions import APIError, ConflictError
from snowflake.core.schema import Schema, SchemaCollection
from tests.utils import random_string


pytestmark = pytest.mark.usefixtures("backup_database_schema")


def test_create_schema(schemas: SchemaCollection):
    new_schema_def = Schema(
        name=random_string(10, "test_schema_int_test_"),
        kind="TRANSIENT",
    )
    new_schema_def.comment = "schema first"
    schema = schemas.create(new_schema_def)
    try:
        created_schema = schema.fetch()
        assert created_schema.name == new_schema_def.name.upper()
        assert created_schema.kind == "TRANSIENT"
        assert created_schema.comment == new_schema_def.comment
        assert created_schema.options != "MANAGED ACCESS"

        with pytest.raises(
            ConflictError,
        ):
            schemas.create(new_schema_def, mode="error_if_exists")

        new_schema_def_1 = copy.deepcopy(new_schema_def)
        new_schema_def_1.kind = None
        new_schema_def_1.comment = "schema second"
        schema = schemas.create(new_schema_def_1, mode="if_not_exists")

        created_schema = schema.fetch()
        assert created_schema.name == new_schema_def.name.upper()
        assert created_schema.kind == "TRANSIENT"
        assert created_schema.comment == new_schema_def.comment
        assert created_schema.options != "MANAGED ACCESS"
    finally:
        schema.drop()

    schema = schemas.create(new_schema_def_1, mode="or_replace")
    try:
        created_schema = schema.fetch()
        assert created_schema.name == new_schema_def_1.name.upper()
        assert created_schema.kind == "PERMANENT"
        assert created_schema.comment == new_schema_def_1.comment
    finally:
        schema.drop()

    schema_name = random_string(10, "test_schema_INT_test_")
    schema_name_case_sensitive = '"' + schema_name + '"'
    new_schema_def = Schema(name=schema_name_case_sensitive)
    schema = schemas.create(new_schema_def)
    try:
        # TODO(SNOW-1354988) - Please uncomment this once you have this bug resolved
        # created_schema = schema.fetch()
        # assert created_schema.name == new_schema_def.name
        pass
    finally:
        schema.drop()

def test_create_with_managed_access(schemas: SchemaCollection):
    new_schema_def = Schema(name=random_string(10, "test_schema_int_test_"), managed_access=True)
    try:
        schema = schemas.create(new_schema_def, mode="or_replace")

        created_schema = schema.fetch()
        assert created_schema.name == new_schema_def.name.upper()
        assert created_schema.managed_access is True
        assert created_schema.options == "MANAGED ACCESS"
    finally:
        schema.drop()


def test_create_clone(schemas: SchemaCollection):
    schema_name = random_string(10, "test_schema_")
    schema_def = Schema(name=schema_name, kind="TRANSIENT")

    new_schema_name = random_string(10, "test_schema_clone")
    new_schema_def = Schema(name=new_schema_name)

    # error because Schema does not exist
    with pytest.raises(APIError, match="does not exist"):
        schema = schemas.create(
            new_schema_def,
            clone=Clone(source=schema_name, point_of_time=PointOfTimeOffset(reference="at", when="-5")),
            mode="orreplace",
        )

    schemas.create(schema_def)
    sleep(2)
    # error because transient schema cannot be cloned to a permanent schema
    with pytest.raises(APIError, match="transient object cannot be cloned to a permanent object"):
        schema = schemas.create(
            new_schema_def,
            clone=Clone(source=schema_name, point_of_time=PointOfTimeOffset(reference="at", when="-1")),
            mode="orreplace",
        )

    # can clone transient to transient
    new_schema_def.kind = "TRANSIENT"
    schema = schemas.create(
        new_schema_def,
        clone=Clone(source=schema_name, point_of_time=PointOfTimeOffset(reference="at", when="-1")),
        mode="orreplace",
    )

    # replaced transient to permanent schema
    schema_def.kind = new_schema_def.kind = None
    schemas.create(schema_def, mode="or_replace")
    sleep(2)
    schema = schemas.create(
        new_schema_def,
        clone=Clone(source=schema_name, point_of_time=PointOfTimeOffset(reference="at", when="-1")),
        mode="orreplace",
    )
    try:
        schema.fetch()
    finally:
        schema.drop()

def test_create_clone_cross_database(schemas: SchemaCollection, temp_db):
    # clone temp_db.original_schema to <current database>.clone_schema
    original_schema_def = Schema(
        name=random_string(10, "test_schema_cross_database_"),
    )
    original_schema_def.comment = "original schema"

    original_schema = temp_db.schemas.create(original_schema_def)

    clone_of_schema_in_new_db = Clone(source=f"{temp_db.name}.{original_schema_def.name}")

    clone_schema = schemas.create(
        Schema(
            name=random_string(10, "test_schema_cross_database_"),
        ),
        clone=clone_of_schema_in_new_db
    )

    try:
        cloned_schema_def = clone_schema.fetch()
        original_schema_def = original_schema.fetch()

        assert original_schema_def.database_name.upper() == temp_db.name.upper()
        assert original_schema_def.comment.upper() == "original schema".upper()
        assert cloned_schema_def.database_name.upper() == schemas.database.name.upper()
        assert cloned_schema_def.comment.upper() == "original schema".upper()

        assert original_schema_def.name.upper() in [i.name.upper() for i in temp_db.schemas.iter()]
        assert cloned_schema_def.name.upper() in [i.name.upper() for i in schemas.iter()]
    finally:
        clone_schema.drop()
        original_schema.drop()

