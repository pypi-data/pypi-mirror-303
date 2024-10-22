import datetime
import unittest

from pandas import DataFrame, Series

from chainalysis._exceptions import BadRequest
from chainalysis.data_solutions import DataSolutionsClient

ds = DataSolutionsClient(
    api_key="",
)


class utils(unittest.TestCase):
    """
    Unit tests for various utility functions in the DataSolutions API.

    This test suite covers stringifying lists and datetime objects,
    as well as validating the correct execution of SQL queries using these utilities.
    """

    def test_list_stringify(self):
        """
        Test that a list of integers is correctly stringified.

        Verifies that a list of integers is converted to a string format
        that can be used in an SQL query.
        """

        blocks = [1, 2]
        stringified_blocks = ds.utils.stringify.lists(
            blocks,
        )
        assert stringified_blocks == "('1', '2')"

    def test_list_stringified_string(self):
        """
        Test that a list of strings (block hashes) is correctly stringified.

        Ensures that a list of block hashes is formatted into a string suitable
        for use in an SQL query.
        """

        block_hashes = [
            "000000000000057d13a731f556c24a1318bcbb4df7d537ef07c8c813c0dc1b37",
            "00000000000005b71bc4c0cf24a6f00e04980c627e9409266983bd37acbe14d3",
        ]

        stringified_block_hashes = (
            ds.utils.stringify.lists(
                block_hashes,
            ),
        )

        assert stringified_block_hashes == (
            "('000000000000057d13a731f556c24a1318bcbb4df7d537ef07c8c813c0dc1b37', '00000000000005b71bc4c0cf24a6f00e04980c627e9409266983bd37acbe14d3')",
        )

    def test_datetime_stringify(self):
        """
        Test that a datetime object is correctly stringified.

        Ensures that a datetime object is formatted into a string suitable
        for use in an SQL query.
        """

        timestamp = "2011-08-25T22:07:41Z"
        dt_object = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")

        stringified_timestamp = ds.utils.stringify.datetimes(
            dt_object,
        )
        assert stringified_timestamp == "'2011-08-25T22:07:41Z'"

    def test_incorrect_datetime(self):
        """
        Test that an incorrect type raises the correct exception for datetime stringification.

        Ensures that passing a non-datetime object to the datetime stringification utility
        raises a BadRequest exception with the expected message.
        """

        with self.assertRaises(BadRequest) as context:
            ds.utils.stringify.datetimes(3)
        self.assertEqual(
            str(context.exception),
            "Incorrect type. Supply a datetime.datetime object.",
        )

    def test_correct_columns(self):
        """
        Test that an column list is correctly converted.

        Ensures that a list with different data types raises an exception
        with the expected error message.
        """

        columns = ["column1", "column2"]

        stringified_columns = ds.utils.stringify.columns(columns)

        assert stringified_columns == "column1, column2"

    def test_pandas_series(self):
        """
        Test that a pandas Series is correctly converted to a string.
        """
        series = Series([1, 2, 3])

        stringified_series = ds.utils.stringify.lists(series)

        assert stringified_series == "('1', '2', '3')"

    def test_stringify_dataframe(self):
        """
        Test that a pandas DataFrame is correctly converted to a CTE.
        """

        df = DataFrame(
            {
                "column1": [1, 2, 3],
                "column2": ["a", "b", "c"],
            }
        )

        stringified_df = ds.utils.stringify.dataframes(df)

        assert stringified_df == "(1, 'a')(2, 'b')(3, 'c')"


if __name__ == "__main__":
    unittest.main()
