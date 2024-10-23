import pytest


pytestmark = pytest.mark.usefixtures("backup_database_schema")


def test_fetch(temp_schema, temp_schema_case_sensitive):
    schema = temp_schema.fetch()
    assert schema.name.upper() == temp_schema.name.upper()

    schema = temp_schema_case_sensitive.fetch()
    assert f'"{schema.name}"' == temp_schema_case_sensitive.name
    assert schema.comment == "created by temp_schema_case_sensitive"
