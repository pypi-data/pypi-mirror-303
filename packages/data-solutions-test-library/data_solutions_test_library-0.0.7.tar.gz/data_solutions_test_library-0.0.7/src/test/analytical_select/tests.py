import unittest
from unittest.mock import Mock, patch

from sqlalchemy import Column, MetaData, String, Table

from chainalysis._exceptions import ValueException
from chainalysis.orm._analytical_select import AnalyticalSelect

schemas = {
    "status": "success",
    "stats": {},
    "results": {
        "chain1": {
            "table1": {
                "description": "table_1_description",
                "full_name": "chain1.table1",
                "columns": [
                    {
                        "name": "column1",
                        "type": "STRING",
                        "description": "column_description1",
                        "nullable": True,
                        "full_name": "chain1.table1.column1",
                    },
                    {
                        "name": "column2",
                        "type": "STRING",
                        "description": "column_description2",
                        "nullable": True,
                        "full_name": "chain1.table1.column2",
                    },
                    {
                        "name": "column3",
                        "type": "STRING",
                        "description": "column_description3",
                        "nullable": False,
                        "full_name": "chain1.table1.column3",
                    },
                ],
            },
            "table2": {
                "description": "table_2_description",
                "full_name": "chain1.table2",
                "columns": [
                    {
                        "name": "column1",
                        "type": "STRING",
                        "description": "column_description1",
                        "nullable": True,
                        "full_name": "chain1.table2.column1",
                    },
                    {
                        "name": "column2",
                        "type": "STRING",
                        "description": "column_description2",
                        "nullable": True,
                        "full_name": "chain1.table2.column2",
                    },
                    {
                        "name": "column3",
                        "type": "STRING",
                        "description": "column_description3",
                        "nullable": True,
                        "full_name": "chain1.table2.column3",
                    },
                ],
            },
        },
        "chain2": {
            "table1": {
                "description": "table_1_description",
                "full_name": "chain2.table1",
                "columns": [
                    {
                        "name": "column1",
                        "type": "STRING",
                        "description": "column_description1",
                        "nullable": True,
                        "full_name": "chain2.table1.column1",
                    },
                    {
                        "name": "column2",
                        "type": "STRING",
                        "description": "column_description2",
                        "nullable": True,
                        "full_name": "chain2.table1.column2",
                    },
                    {
                        "name": "column3",
                        "type": "STRING",
                        "description": "column_description3",
                        "nullable": True,
                        "full_name": "chain2.table1.column3",
                    },
                ],
            },
            "table2": {
                "description": "table_2_description",
                "full_name": "chain2.table2",
                "columns": [
                    {
                        "name": "column1",
                        "type": "STRING",
                        "description": "column_description1",
                        "nullable": True,
                        "full_name": "chain2.table2.column1",
                    },
                    {
                        "name": "column2",
                        "type": "STRING",
                        "description": "column_description2",
                        "nullable": True,
                        "full_name": "chain2.table2.column2",
                    },
                    {
                        "name": "column3",
                        "type": "STRING",
                        "description": "column_description3",
                        "nullable": True,
                        "full_name": "chain2.table2.column3",
                    },
                ],
            },
        },
    },
}


class AnalyticalSelectTests(unittest.TestCase):
    @patch("chainalysis.orm._analytical_select.issue_request")
    def test_get_table(self, mock_issue_request: Mock):
        """
        Test that get_table() returns a valid table object with columns correctly mapped.
        """

        mock_issue_request.return_value = schemas
        table = AnalyticalSelect("api_key", "chain1.table1").table

        expected_table = Table(
            "chain1.table1",
            MetaData(),
            Column(
                "column1",
                String,
                comment="column_description1",
                nullable=True,
            ),
            Column(
                "column2",
                String,
                comment="column_description2",
                nullable=True,
            ),
            Column(
                "column3",
                String,
                comment="column_description3",
                nullable=False,
            ),
        )

        # Compare the names and columns of the tables
        self.assertEqual(table.name, expected_table.name)
        self.assertEqual(len(table.columns), len(expected_table.columns))

        for col in table.columns:
            expected_col = expected_table.columns[col.name]
            self.assertEqual(col.name, expected_col.name)
            self.assertIsInstance(col.type, type(expected_col.type))
            self.assertEqual(col.comment, expected_col.comment)
            self.assertEqual(col.nullable, expected_col.nullable)

    @patch("chainalysis.orm._analytical_select.issue_request")
    def test_invalid_chain(self, mock_issue_request: Mock):
        """
        Test that an invalid chain raises a ValueException.
        """

        mock_issue_request.return_value = schemas
        with self.assertRaises(ValueException) as context:
            AnalyticalSelect("api_key", "invalid_chain.table1")
        self.assertEqual(
            str(context.exception),
            "Chain 'invalid_chain' does not exist in the database. Check your input. If you believe the inputted chain should exist, contact Data Solutions.",
        )

    @patch("chainalysis.orm._analytical_select.issue_request")
    def test_invalid_table(self, mock_issue_request: Mock):
        """
        Test that an invalid chain raises a ValueException.
        """

        mock_issue_request.return_value = schemas
        with self.assertRaises(ValueException) as context:
            AnalyticalSelect("api_key", "chain1.invalid_table")
        self.assertEqual(
            str(context.exception),
            "Table 'invalid_table' does not exist in the database for chain 'chain1'. Check your input. If you believe the inputted table should exist, contact Data Solutions.",
        )


if __name__ == "__main__":
    unittest.main()
