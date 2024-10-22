import unittest

from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table

from chainalysis._exceptions import ValueException
from chainalysis.orm import (
    Select,
    and_,
    between,
    case,
    distinct,
    except_,
    except_all,
    exists,
    func,
    intersect,
    intersect_all,
    join,
    lateral,
    literal,
    not_,
    or_,
    outerjoin,
    union,
    union_all,
)

table = Table(
    "chain.table",
    MetaData(),
    Column("column1", Integer),
    Column("column2", String),
    Column("column3", Boolean),
)

table2 = Table(
    "chain.table2",
    MetaData(),
    Column("column1", Integer),
    Column("column2", String),
    Column("column3", Boolean),
)


class BasicSelect(Select):
    def _get_table(self, chain: str, table: str):
        return Table(
            f"{chain}.{table}",
            MetaData(),
            Column("column1", Integer),
            Column("column2", String),
            Column("column3", Boolean),
        )

    def execute(self):
        pass


class SelectTests(unittest.TestCase):
    """
    Test suite for the Select class.
    """

    def test_incorrect_table_name_format(self):
        """
        Test that an error is raised when an incorrect table name format is provided.
        """
        with self.assertRaises(ValueException) as context:
            BasicSelect("api_key", "incorrect_format")
        self.assertEqual(
            str(context.exception),
            "Table must be formatted as 'chain.table'. Check your input.",
        )

    def test_empty_with_columns(self):
        """
        Test that sql() returns a valid SQL SELECT statement when no selections have been made.
        """
        query = BasicSelect("api_key", "chain.table")
        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table"',
        )

    def test_with_columns(self):
        """
        Test that sql() returns a valid SQL SELECT statement when selections have been made.
        """
        # Select(table.c.column1, table.c.column2)
        table = BasicSelect("api_key", "chain.table")
        query = table.with_columns(table.c.column1, table.c.column2)

        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, "chain.table".column2 \nFROM "chain.table"',
        )

    def test_invalid_columns(self):
        """
        Test that an error is raised when invalid columns are selected.
        """
        query = BasicSelect("api_key", "chain.table")
        with self.assertRaises(AttributeError) as context:
            query.with_columns(query.c.column4)

        self.assertEqual(
            str(context.exception),
            "column4",
        )

    def test_where(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a WHERE clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.where(table.c.column1 == 1)
        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1',
        )

    def test_with_columns_and_where(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a SELECT and WHERE clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.with_columns(table.c.column1, table.c.column2).where(
            table.c.column1 == 1
        )
        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, "chain.table".column2 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1',
        )

    def test_complex_query(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a complex query is built.
        """
        table = BasicSelect("api_key", "chain.table")
        query = (
            table.with_columns(table.c.column1, table.c.column2)
            .where(table.c.column1 == 1)
            .group_by(table.c.column1)
            .order_by(table.c.column1.desc())
            .limit(10)
        )

        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, "chain.table".column2 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1 GROUP BY "chain.table".column1 ORDER BY "chain.table".column1 DESC\n LIMIT 10',
        )

    def test_group_by(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a GROUP BY clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query1 = table.group_by(table.c.column1)
        query2 = table.group_by(table.c.column1).having(table.c.column1 > 1)

        self.assertEqual(
            query1.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" GROUP BY "chain.table".column1',
        )

        self.assertEqual(
            query2.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" GROUP BY "chain.table".column1 \nHAVING "chain.table".column1 > 1',
        )

    def test_join(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a JOIN clause is added.
        """

        table1 = BasicSelect("api_key", "chain.table1")
        table2 = BasicSelect("api_key", "chain.table2")

        query1 = table1.join(table2.table, table1.c.column1 == table2.c.column1)
        query2 = table1.with_columns(
            join(table1.table, table2.table, table1.c.column1 == table2.c.column1)
        )

        self.assertEqual(
            query1.sql(),
            'SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3 \nFROM "chain.table1" JOIN "chain.table2" ON "chain.table1".column1 = "chain.table2".column1',
        )

        self.assertEqual(
            query2.sql(),
            'SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3, "chain.table2".column1 AS column1_1, "chain.table2".column2 AS column2_1, "chain.table2".column3 AS column3_1 \nFROM "chain.table1" JOIN "chain.table2" ON "chain.table1".column1 = "chain.table2".column1',
        )

    def test_outerjoin(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an OUTER JOIN clause is added.
        """
        table1 = BasicSelect("api_key", "chain.table1")
        table2 = BasicSelect("api_key", "chain.table2")

        query1 = table1.outerjoin(table2.table, table1.c.column1 == table2.c.column1)
        query2 = table1.with_columns(
            outerjoin(
                table1.table,
                table2.table,
                table1.c.column1 == table2.c.column1,
            )
        )

        self.assertEqual(
            query1.sql(),
            'SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3 \nFROM "chain.table1" LEFT OUTER JOIN "chain.table2" ON "chain.table1".column1 = "chain.table2".column1',
        )

        self.assertEqual(
            query2.sql(),
            'SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3, "chain.table2".column1 AS column1_1, "chain.table2".column2 AS column2_1, "chain.table2".column3 AS column3_1 \nFROM "chain.table1" LEFT OUTER JOIN "chain.table2" ON "chain.table1".column1 = "chain.table2".column1',
        )

    def test_outerjoin_from(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an OUTER JOIN FROM clause is added.
        """
        table1 = BasicSelect("api_key", "chain.table1")
        table2 = BasicSelect("api_key", "chain.table2")

        query1 = table1.outerjoin_from(
            table1.table, table2.table, table1.c.column1 == table2.c.column1
        )

        self.assertEqual(
            query1.sql(),
            'SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3 \nFROM "chain.table1" LEFT OUTER JOIN "chain.table2" ON "chain.table1".column1 = "chain.table2".column1',
        )

    def test_and(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an AND clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.where(and_(table.c.column1 == 1, table.c.column2 == "test"))
        query_2 = table.where((table.c.column1 == 1) & (table.c.column2 == "test"))

        self.assertEqual(
            query.sql(),
            query_2.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1 AND "chain.table".column2 = \'test\'',
        )

    def test_or(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an OR clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.where(or_(table.c.column1 == 1, table.c.column2 == "test"))
        query_2 = table.where((table.c.column1 == 1) | (table.c.column2 == "test"))

        self.assertEqual(
            query.sql(),
            query_2.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1 OR "chain.table".column2 = \'test\'',
        )

    def test_nested_and_or(self):
        """
        Test that sql() returns a valid SQL SELECT statement when nested AND and OR clauses are added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.where(
            and_(
                table.c.column1 == 1,
                or_(table.c.column2 == "test", table.c.column3 == True),
            )
        )
        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1 AND ("chain.table".column2 = \'test\' OR "chain.table".column3 = true)',
        )

    def test_not(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a NOT clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.where(not_(table.c.column1 == 1))
        query_2 = table.where(~(table.c.column1 == 1))

        self.assertEqual(
            query.sql(),
            query_2.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" \nWHERE "chain.table".column1 != 1',
        )

    def test_func(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a function is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.with_columns(func.count(table.c.column1))

        self.assertEqual(
            query.sql(),
            'SELECT count("chain.table".column1) AS count_1 \nFROM "chain.table"',
        )

    def test_case(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a CASE clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.with_columns(
            case(
                (table.c.column1 == 1, "one"),
                (table.c.column1 == 2, "two"),
                else_="other",
            )
        )

        self.assertEqual(
            query.sql(),
            "SELECT CASE WHEN (\"chain.table\".column1 = 1) THEN 'one' WHEN (\"chain.table\".column1 = 2) THEN 'two' ELSE 'other' END AS anon_1 \nFROM \"chain.table\"",
        )

    def test_literal(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a literal is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.with_columns(table.c.column1, literal(1).label("one"))
        self.assertEqual(
            query.sql(),
            'SELECT "chain.table".column1, 1 AS one \nFROM "chain.table"',
        )

    def test_alias(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an alias is added.
        """

        table = BasicSelect("api_key", "chain.table")
        alias_table = table.alias("alias_table")

        self.assertEqual(
            str(alias_table),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table"',
        )

    def test_between(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a BETWEEN clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query = table.where(table.c.column1.between(5, 10))
        query2 = table.where(between(table.c.column1, 5, 10))

        self.assertEqual(
            query.sql(),
            query2.sql(),
            'SELECT "chain.table".column1, "chain.table".column2, "chain.table".column3 \nFROM "chain.table" \nWHERE "chain.table".column1 BETWEEN 5 AND 10',
        )

    def test_distinct(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a DISTINCT clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query1 = table.with_columns(distinct(table.c.column1))
        query2 = table.with_columns(table.c.column1).distinct()
        self.assertEqual(
            query1.sql(),
            query2.sql(),
            'SELECT DISTINCT "chain.table".column1 \nFROM "chain.table"',
        )

    def test_exists(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an EXISTS clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        subquery = table.with_columns(table.c.column1).where(table.c.column1 == 1)
        query1 = table.where(exists(subquery))
        query2 = table.where(subquery.exists())

        self.assertEqual(
            query1.sql(),
            query2.sql(),
            'SELECT "chain.table".column1 \nFROM "chain.table" \nWHERE EXISTS (SELECT "chain.table".column1 \nFROM "chain.table" \nWHERE "chain.table".column1 = 1)',
        )

    def test_except_(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an EXCEPT clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query1 = table.with_columns(table.c.column1)
        query2 = table.with_columns(table.c.column2)
        query3 = query1.except_(query2)
        query4 = table.with_columns(except_(query1, query2).alias())

        self.assertEqual(
            query3.sql(),
            query4.sql(),
            'SELECT anon_1.column1 \nFROM (SELECT "chain.table".column1 AS column1 \nFROM "chain.table" EXCEPT SELECT "chain.table".column1 AS column1 \nFROM "chain.table" EXCEPT SELECT "chain.table".column2 AS column2 \nFROM "chain.table") AS anon_1',
        )

    def test_except_all(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an EXCEPT ALL clause is added.
        """
        table = BasicSelect("api_key", "chain.name")
        query1 = table.with_columns(table.c.column1)
        query2 = table.with_columns(table.c.column2)
        query3 = query1.except_all(query2)
        query4 = table.with_columns(except_all(query1, query2).alias())

        self.assertEqual(
            query3.sql(),
            query4.sql(),
            'SELECT anon_1.column2 \nFROM (SELECT "chain.name".column2 AS column2 \nFROM "chain.name" EXCEPT ALL SELECT "chain.name".column1 AS column1 \nFROM "chain.name") AS anon_1',
        )

    def test_intersect(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an INTERSECT clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        table2 = BasicSelect("api_key", "chain.table2")
        query1 = table.with_columns(table.c.column1)
        query2 = table2.with_columns(table2.c.column1)
        query3 = query1.intersect(query2)
        query4 = table.with_columns(intersect(query1, query2).alias())

        self.assertEqual(
            query3.sql(),
            query4.sql(),
            'SELECT anon_1.column1 \nFROM (SELECT "chain.table".column1 AS column1 \nFROM "chain.table" INTERSECT SELECT "chain.table".column1 AS column1 \nFROM "chain.table" INTERSECT SELECT "chain.table2".column1 AS column1 \nFROM "chain.table2") AS anon_1',
        )

    def test_intersect_all(self):
        """
        Test that sql() returns a valid SQL SELECT statement when an INTERSECT ALL clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        table2 = BasicSelect("api_key", "chain.table2")
        query1 = table.with_columns(table.c.column1)
        query2 = table2.with_columns(table2.c.column1)
        query3 = query1.intersect_all(query2)
        query4 = table.with_columns(intersect_all(query1, query2).alias())

        self.assertEqual(
            query3.sql(),
            query4.sql(),
            'SELECT anon_1.column1 \nFROM (SELECT "chain.table".column1 AS column1 \nFROM "chain.table" INTERSECT ALL SELECT "chain.table".column1 AS column1 \nFROM "chain.table" INTERSECT ALL SELECT "chain.table2".column1 AS column1 \nFROM "chain.table2") AS anon_1',
        )

    def test_lateral(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a LATERAL clause is added.
        """
        table = BasicSelect("api_key", "chain.table")
        query1 = table.with_columns(table.c.column1)
        query2 = query1.lateral()
        query3 = table.with_columns(lateral(query1))

        self.assertEqual(
            query2.sql(),
            query3.sql(),
            'SELECT alias.column1 \nFROM LATERAL (SELECT "chain.table".column1 AS column1 \nFROM "chain.table") AS alias',
        )

    def test_union(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a UNION clause is added.
        """
        table1 = BasicSelect("api_key", "chain.table1")
        table2 = BasicSelect("api_key", "chain.table2")
        query1 = table1.with_columns(table1.c.column1)
        query2 = table2.with_columns(table2.c.column1)
        query3 = query1.union(query2)
        query4 = table1.with_columns(union(query1, query2).alias())

        self.assertEqual(
            query3.sql(),
            query4.sql(),
            'SELECT anon_1.column1 \nFROM (SELECT "chain.table1".column1 AS column1 \nFROM "chain.table1" UNION SELECT "chain.table2".column1 AS column1 \nFROM "chain.table2") AS anon_1',
        )

    def test_union_all(self):
        """
        Test that sql() returns a valid SQL SELECT statement when a UNION ALL clause is added.
        """
        table1 = BasicSelect("api_key", "chain.table1")
        table2 = BasicSelect("api_key", "chain.table2")
        query1 = table1.with_columns(table1.c.column1)
        query2 = table2.with_columns(table2.c.column1)
        query3 = query1.union_all(query2)
        query4 = table1.with_columns(union_all(query1, query2).alias())

        self.assertEqual(
            query3.sql(),
            query4.sql(),
            'SELECT anon_1.column1 \nFROM (SELECT "chain.table2".column1 AS column1 \nFROM "chain.table2" UNION ALL SELECT "chain.table1".column1 AS column1 \nFROM "chain.table1") AS anon_1',
        )


if __name__ == "__main__":
    unittest.main()
