#
# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
#


import pytest


pytestmark = pytest.mark.usefixtures("backup_database_schema")


def test_fetch(databases, temp_db):
    database = databases[temp_db.name].fetch()
    assert database.name.upper() == temp_db.name.upper()
    assert database.comment == "created by temp_db"
