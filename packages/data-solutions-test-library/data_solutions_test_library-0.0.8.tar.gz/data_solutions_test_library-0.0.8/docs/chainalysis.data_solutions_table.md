# chainalysis.data_solutions_table package

## Submodules

## chainalysis.data_solutions_table.analytical_table module

### *class* chainalysis.data_solutions_table.analytical_table.AnalyticalTable(api_key: str, chain_table_name: str)

Bases: [`Select`](#chainalysis.data_solutions_table.data_solutions_table.Select)

#### execute() → [Analytical](chainalysis.sql.md#chainalysis.sql.analytical.Analytical)

Execute the query and return an Analytical object.

return: Analytical object.
rtype: Analytical

#### get_table(chain, table) → Table

Return a SQLAlchemy Table object for the given chain and table name.

* **Parameters:**
  * **chain** – The chain name.
  * **table** – The table name.
* **Returns:**
  A SQLAlchemy Table object.
* **Return type:**
  Table
* **Raises:**
  [**ValueException**](chainalysis.md#chainalysis.exceptions.ValueException) – If the chain or table does not exist in the database.

## chainalysis.data_solutions_table.data_solutions_table module

### *class* chainalysis.data_solutions_table.data_solutions_table.Select(api_key: str, chain_table_name: str)

Bases: `Select`, `ABC`

#### \_\_init_\_(api_key: str, chain_table_name: str)

Construct a new `_expression.Select`.

The public constructor for `_expression.Select` is the
`_sql.with_columns()` function.

#### *property* c

#### Deprecated
Deprecated since version 1.4: The `_expression.SelectBase.c` and `_expression.SelectBase.columns` attributes are deprecated and will be removed in a future release; these attributes implicitly create a subquery that should be explicit.  Please call `_expression.SelectBase.subquery()` first in order to create a subquery, which then contains this attribute.  To access the columns that this SELECT object SELECTs from, use the `_expression.SelectBase.selected_columns` attribute.

#### *abstract* execute() → [Transactional](chainalysis.sql.md#chainalysis.sql.transactional.Transactional) | [Analytical](chainalysis.sql.md#chainalysis.sql.analytical.Analytical)

Execute the query and return a Transactional or Analytical object.

return: Transactional or Analytical object.
rtype: Union[Transactional, Analytical]

#### *abstract* get_table(chain, table: str) → Table

Return a SQLAlchemy Table object for the given chain and table name.

* **Parameters:**
  * **chain** – The chain name.
  * **table** – The table name.
* **Returns:**
  A SQLAlchemy Table object.
* **Return type:**
  Table
* **Raises:**
  [**ValueException**](chainalysis.md#chainalysis.exceptions.ValueException) – If the chain or table does not exist in the database.

#### with_columns(\*columns) → [Select](#chainalysis.data_solutions_table.data_solutions_table.Select)

#### Deprecated
Deprecated since version 1.4: The `_expression.SelectBase.with_columns()` method is deprecated and will be removed in a future release; this method implicitly creates a subquery that should be explicit.  Please call `_expression.SelectBase.subquery()` first in order to create a subquery, which then can be selected.

#### sql() → str

## chainalysis.data_solutions_table.transactional_table module

### *class* chainalysis.data_solutions_table.transactional_table.TransactionalTable(api_key: str, chain_table_name: str)

Bases: [`Select`](#chainalysis.data_solutions_table.data_solutions_table.Select)

#### execute() → [Transactional](chainalysis.sql.md#chainalysis.sql.transactional.Transactional)

Execute the query and return a Transactional object.

return: Transactional object.
rtype: Transactional

#### get_table(chain, table) → None

Return a SQLAlchemy Table object for the given chain and table name.

* **Parameters:**
  * **chain** – The chain name.
  * **table** – The table name.
* **Returns:**
  A SQLAlchemy Table object.
* **Return type:**
  Table
* **Raises:**
  [**ValueException**](chainalysis.md#chainalysis.exceptions.ValueException) – If the chain or table does not exist in the database.

## Module contents
