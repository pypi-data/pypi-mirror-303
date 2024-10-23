# Release History

## 1.0.0 (2024-10-10)

* Improved error messages: stack traces are shortened. The environment variable option `_SNOWFLAKE_PRINT_VERBOSE_STACK_TRACE` can be used to control this behavior.

### New Features

* Read-only properties are now by default included in dictionaries returned by `to_dict()` from models. This can be toggled by using `to_dict(hide_readonly_properties=True)`.
* The `if_exists` property, which toggles whether an action can be performed without erroring if the given resource does not exist, has been added to the following resources:
    * `drop()` for Database, NetworkPolicy, View, User, ComputePool, ImageRepository, Pipe, Role, Service, Stage, Table, Task, DynamicTable, Role, Alert, Procedure, Warehouse, Schema, Function.
    * `refresh()` for Database and DynamicTable.
    * `suspend()` and `resume()` for Service , DynamicTable, and Warehouse.
    * `suspendRecluster()` and `resumeRecluster()` for DynamicTable and Table
* Database
    * `undrop()` is now supported.
* Service
    * `from_name` is now supported in `iter()`.
* Table
    * `swap_with()` now supports `target_database` and `target_schema`.
* Procedure
    * `create()` now supports `copy_grants`.

### Bug Fixes

* Dynamic Table create now properly allows cloning source objects from different databases and schemas.
* Fixed an SSL connection issue for accounts and organizations with underscores when used in hostnames.

## 0.13.1 (2024-10-03)

* Logs are improved with secrets scrubbed

### New features

* Grant api are implemeneted in Role, User and Database Role

* New resources:
  * Database Role

## 0.13.0 (2024-09-26)

* API docs have been significantly improved
* `snowflake-snowpark-python` is no longer a dependency of `snowflake.core`. However, this package is still needed for certain features, such as when using DAG concepts; the check and requirement for these features is performed at runtime.
* All Python versions 3.8, or newer are supported.

### New features

* `targetDatabase` and `targetSchema` are supported for cloning Tables.
* `targetDatabase` is supported for cloning Schemas.
* Type-definitions are now exposed.
* `ServiceCollection` now supports the `execute_job`.
* `ServiceResource` now supports `get_containers, get_instances, and get_roles.
* `create_or_update` is now supported for Service and ComputePool
* New resources:
  * Account
  * Alert
  * Catalog Integration
  * Event Table
  * External Volume
  * Managed Account
  * Network Policy
  * Notebook
  * Notification Integration
  * Pipe
  * Procedure
  * Stream
  * User Defined Functions
  * View

### Bug Fixes
* Fixed a bug relating to logging of URLs, where not all the URL pieces were injected into logging.


## 0.12.1 (2024-08-19)

### Bug fixes

* Various bug fixes related to large results handling.

## 0.12.0 (2024-08-06)

### New features

* Added `initially_suspended` support for creating `compute_pool` objects.
* `stage.upload_file()` and `stage.download_file()` have been deprecated. Please use `stage.put()` and `stage.get()` instead.
* Added client retry for retriable server error codes.

### Bug fixes

* Fixed an issue in long-running queries and large-results support when running in notebooks.

## 0.11.0 (2024-07-25)

(New features are dependent on Snowflake 8.27)

### New features

* Added client logging to the library to enhance debuggability
* Added `undrop` support to `Dynamic Table`, `Schema` and `Table`
* Enhanced `Grant` support
  * **Limitations**: We still don’t support `SHOW GRANTS ON`. Only `Grantees.role` is supported for grants.to (`SHOW GRANTS TO`)
* `create_or_update`, `delete`, and `undelete` are now deprecated and have been renamed to `create_or_alter`, `drop`, and `undrop`. This is done to match SQL syntax more consistently

### Bug fixes

* Fixed a bug in stored procedure generated code

## 0.10.1 (2024-06-26)

This version contains minor bug fixes.

## 0.10.0 (2024-06-24)

(New features are dependent on Snowflake 8.23)

### New features

* `Grant` APIs are now available
* `Dynamic Table` APIs are now available
* `Function` APIs are now available (only Service functions)
* Added support for Finalizers in DAG and tasks

## 0.9.0 (2024-06-10)

### New features

* `User` APIs are now available (experimental)
* `Role` APIs are now available (experimental)
* Management `Stage` APIs are now available (experimental)
* `create_or_update` is once against supported for `Warehouse` `Schema`, and `Database` resources

### Bug fixes

* `with_managed_access` is now properly returned as a property of `SchemaResource`

## 0.8.1 (2024-05-31)

### New features
* `with_managed_access` is now an available boolean option in `create_or_update` for `SchemaResource`. This is equivalent to the [WITH MANAGED ACCESS](https://docs.snowflake.com/en/sql-reference/sql/create-schema#optional-parameters) clause in `CREATE SCHEMA`.

    Usage example:

    ```schema.create_or_update(schema_def, with_managed_access = True)```

* Added a `get_endpoints` method for `Service` resources that returns a list of endpoints for a given `Service`.


## 0.8.0 (2024-04-30)

### Breaking changes
* The `deep` parameter is removed from `fetch()` on `TableResource` objects. `fetch()` will always return detailed columns and constraints information of a `TableResource`.
* `create_or_update()` for `Schema`, `Warehouse`, `Database`, `Compute Pool`, resources will (for the time being) not work. `create()` on these resources will still work.  
* Creating tables using `as_select` will no longer carry over information from any source tables used in the `as_select` query.
* `data_retention_time_in_days` and `max_data_extension_time_in_days` properties will be inherited from schema or database settings when not explicitly set in a `create_or_update` statement that alters an existing table.

### New features
* The Cortex Search API endpoint is now supported.
* Large results are now supported.
* Long-running queries are now supported.
* Added `ServiceSpec` helper to infer spec type from provided string in `Service` resources.
* Now uses the SnowAPI REST platform for all resources.
* `pip install snowflake[ml]` installs `snowflake-ml-python` v1.4.0.

### Bug fixes
* Various bug fixes

### 0.7.0 (2024-03-18)
* Task predecessors now return their fully qualified name.
* Fixed code generator and updated OpenAPI-spec driven models.
* Fixed Pydantic compatibility issues.
* Fixed bug in Task's `error_integration` property.
* Fixed bug in Task's `config` property when the REST property was missing.
* Make `DAGRun` notebook friendly by giving it `__str__()` and
  `__repr_html__()` methods.
* Documentation updated to refer to "task graphs" rather than "DAGs" to align
  with Snowflake documentation.

## 0.6.0 (2024-02-06)
* The `>>` and `<<` operators of `DATTask` now accept a function directly.
* `DAGTask` now uses the DAG's warehouse by default.
* `DAGTask` accepts a new parameter `session_parameters`.
* Updated `TaskContext`:
  * `get_predecessor_return_value` now works for both long and short names of a `DAGTask`.
  * Added the methods `get_current_task_short_name` and `get_task_graph_config_property`.
* Added support for pydantic 2.x.
* Added support for Python 3.11.
* Fixed a bug where `DAGOperation.run(dag)` raised an exception if the DAG doesn't have a schedule.
* Fixed a bug where deleting a `DAG` didn't delete all of its sub-tasks.
* Fixed a bug that raised an error when a DAG's `config` is set.

## 0.5.1 (2023-12-07)
*  Add urllib3 into dependencies.

## 0.5.0 (2023-12-06)
* Removed the experimental tags on all entities.
* Fixed a bug that raised an exception when listing Databases and Schemas.

## 0.4.0 (2023-12-04)
* Fixed a bug that had an exception when listing some entities that have non-alphanumeric characters in the names.
* Updated dependency on `snowflake-snowpark-python` to `1.5.0`.
* Added support for Python 3.11.
* Removed the Pydantic types from the model class.
* Renamed exception class names in `snowflake.core.exceptions`.

## 0.3.0 (2023-11-17)
* Initial pre-release.
