import math
import unittest
from unittest.mock import Mock, patch

import pandas as pd
import pandas.testing as pdt

from chainalysis._exceptions import (
    BadRequest,
    DataSolutionsAPIException,
    InternalServerException,
    UnhandledException,
)
from chainalysis.data_solutions import DataSolutionsClient

mocked_async_query_id_response = {
    "status": "pending",
    "query_id": "01ef5a51-0e7c-13d6-9383-6412bf7b03cc",
}

mocked_async_query_id_response_no_query_id = {
    "status": "pending",
}

mocked_async_query_response_1 = {
    "status": "pending",
    "message": "Query is in a pending state",
}

mocked_async_query_response_2 = {
    "status": "success",
    "results": [{"chain_id": "bip122:000000000019d6689c085ae165831e93"}],
    "stats": {
        "truncated": "false",
        "time": 2317.030191421509,
        "size": 45,
        "total_size": 45,
        "count": 1,
        "starting_row_offset": 0,
        "last_processed_row_offset": 0,
        "total_count": 1,
        "starting_page_index": 0,
        "last_processed_page_index": 0,
        "total_pages": 1,
    },
    "next": "next_url",
}

mocked_async_query_response_3 = {
    "status": "success",
    "results": [{"chain_id": "bip122:333"}],
    "stats": {
        "truncated": "false",
        "time": 2317.030191421509,
        "size": 45,
        "total_size": 45,
        "count": 1,
        "starting_row_offset": 0,
        "last_processed_row_offset": 0,
        "total_count": 1,
        "starting_page_index": 0,
        "last_processed_page_index": 0,
        "total_pages": 1,
    },
    "next": "next_url",
}

mocked_async_query_response_no_next_page = {
    "status": "success",
    "results": [{"chain_id": "bip122:111"}],
    "stats": {
        "truncated": "false",
        "time": 2317.030191421509,
        "size": 45,
        "total_size": 45,
        "count": 1,
        "starting_row_offset": 0,
        "last_processed_row_offset": 0,
        "total_count": 1,
        "starting_page_index": 0,
        "last_processed_page_index": 0,
        "total_pages": 1,
    },
    "next": None,
}

mocked_async_query_response = {
    "status": "success",
    "results": [{"chain_id": "bip122:000000000019d6689c085ae165831e93"}],
    "stats": {
        "truncated": "false",
        "time": 2317.030191421509,
        "size": 45,
        "total_size": 45,
        "count": 1,
        "starting_row_offset": 0,
        "last_processed_row_offset": 0,
        "total_count": 1,
        "starting_page_index": 0,
        "last_processed_page_index": 0,
        "total_pages": 1,
    },
    "next": "next_url",
}

mocked_async_query_response_no_next_url = {
    "status": "success",
    "results": [{"chain_id": "bip122:000000000019d6689c085ae165831e93"}],
    "stats": {
        "truncated": "false",
        "time": 2317.030191421509,
        "size": 45,
        "total_size": 45,
        "count": 1,
        "starting_row_offset": 0,
        "last_processed_row_offset": 0,
        "total_count": 1,
        "starting_page_index": 0,
        "last_processed_page_index": 0,
        "total_pages": 1,
    },
    "next": None,
}

mocked_async_query_error_status = {
    "status": "error",
    "details": "error",
    "message": "error",
}


class AnalyticalTests(unittest.TestCase):
    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_successful_query(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        first_successful_response = mocked_async_query_id_response
        second_successful_response = mocked_async_query_response_1
        third_successful_response = mocked_async_query_response_2

        mocked_issue_request.side_effect = (
            first_successful_response,
            second_successful_response,
            third_successful_response,
        )

        query_result = ds.sql.analytical(
            "", polling_interval_sec=10, autopaginate=False
        )

        self.assertEqual(
            query_result.query_id,
            "01ef5a51-0e7c-13d6-9383-6412bf7b03cc",
        )
        self.assertEqual(
            query_result.json(),
            mocked_async_query_response_2["results"],
        )
        pdt.assert_frame_equal(
            query_result.df(), pd.DataFrame(mocked_async_query_response_2["results"])
        )
        pdt.assert_frame_equal(
            query_result.df(), pd.DataFrame(mocked_async_query_response_2["results"])
        )
        self.assertEqual(
            query_result.stats(),
            mocked_async_query_response_2["stats"],
        )
        self.assertEqual(
            query_result.was_successful(),
            True,
        )
        self.assertEqual(
            query_result.total_pages(),
            1,
        )
        self.assertEqual(
            query_result.has_next(),
            True,
        )
        self.assertEqual(
            query_result.status_code(),
            200,
        )

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_missing_query_id(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        mocked_issue_request.return_value = mocked_async_query_id_response_no_query_id

        with self.assertRaises(DataSolutionsAPIException):
            ds.sql.analytical("", polling_interval_sec=0)

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_first_api_exception(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        mocked_issue_request.side_effect = DataSolutionsAPIException()

        with self.assertRaises(DataSolutionsAPIException):
            ds.sql.analytical(
                "",
                polling_interval_sec=0,
            )

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_second_api_exception(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        mocked_issue_request.side_effect = (
            mocked_async_query_id_response,
            DataSolutionsAPIException(),
        )

        query_result = ds.sql.analytical("", polling_interval_sec=0, autopaginate=False)

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 501)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(DataSolutionsAPIException):
            query_result.json()

        with self.assertRaises(DataSolutionsAPIException):
            query_result.df()

        with self.assertRaises(DataSolutionsAPIException):
            query_result.stats()

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_interval_server_exception(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        mocked_issue_request.side_effect = (
            mocked_async_query_id_response,
            InternalServerException(),
        )

        query_result = ds.sql.analytical("", polling_interval_sec=0, autopaginate=False)

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 500)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(InternalServerException):
            query_result.json()

        with self.assertRaises(InternalServerException):
            query_result.df()

        with self.assertRaises(InternalServerException):
            query_result.stats()

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_unhandled_exception(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        mocked_issue_request.side_effect = (
            mocked_async_query_id_response,
            Exception(),
        )

        query_result = ds.sql.analytical("", polling_interval_sec=0, autopaginate=False)

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 0)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(UnhandledException):
            query_result.json()

        with self.assertRaises(UnhandledException):
            query_result.df()

        with self.assertRaises(UnhandledException):
            query_result.stats()

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_get_next_page_successful(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        first_successful_response = mocked_async_query_id_response
        second_successful_response = mocked_async_query_response_1
        third_successful_response = mocked_async_query_response_2
        final_successful_response = mocked_async_query_response_2

        mocked_issue_request.side_effect = (
            first_successful_response,
            second_successful_response,
            third_successful_response,
            final_successful_response,
        )

        first_query_result = ds.sql.analytical(
            "", polling_interval_sec=0, autopaginate=False
        )

        second_query_result = first_query_result.next_page()

        self.assertEqual(
            second_query_result._status,
            "success",
        )
        self.assertEqual(
            second_query_result.stats(),
            final_successful_response["stats"],
        )
        self.assertEqual(
            second_query_result.json(),
            final_successful_response["results"],
        )
        self.assertEqual(
            second_query_result.next_url,
            final_successful_response["next"],
        )

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_get_next_page_error(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        first_response = mocked_async_query_id_response
        second_response = mocked_async_query_response_1
        third_response = mocked_async_query_response_2

        mocked_issue_request.side_effect = (
            first_response,
            second_response,
            third_response,
            mocked_async_query_error_status,
        )

        first_query_result = ds.sql.analytical(
            "", polling_interval_sec=0, autopaginate=False
        )
        query_result = first_query_result.next_page()

        self.assertEqual(
            query_result._status,
            "error",
        )
        self.assertEqual(
            query_result.error_message,
            "error",
        )
        self.assertEqual(
            query_result.error_details,
            "error",
        )

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_get_next_page_with_no_next_page_error(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        first_response = mocked_async_query_id_response
        second_response = mocked_async_query_response_1
        third_response = mocked_async_query_response_no_next_url

        mocked_issue_request.side_effect = (
            first_response,
            second_response,
            third_response,
        )

        first_query_result = ds.sql.analytical("", polling_interval_sec=0)

        self.assertEqual(
            first_query_result.has_next(),
            False,
        )

        with self.assertRaises(BadRequest):
            first_query_result.next_page()

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_auto_pagination(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        """
        Test that the Analytical class can execute a query with autopagination.
        """
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        first_successful_response = mocked_async_query_id_response
        second_successful_response = mocked_async_query_response_1
        third_successful_response = mocked_async_query_response_2
        fourth_successful_response = mocked_async_query_response_3
        final_successful_response = mocked_async_query_response_no_next_page

        mocked_issue_request.side_effect = (
            first_successful_response,
            second_successful_response,
            third_successful_response,
            fourth_successful_response,
            final_successful_response,
        )

        query_result = ds.sql.analytical("", polling_interval_sec=0, autopaginate=True)

        expected_results = []
        expected_results.extend(mocked_async_query_response_2["results"])
        expected_results.extend(mocked_async_query_response_3["results"])
        expected_results.extend(mocked_async_query_response_no_next_page["results"])

        self.assertEqual(query_result.json(), expected_results)

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_status_error(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        mocked_issue_request.side_effect = (
            mocked_async_query_id_response,
            mocked_async_query_error_status,
        )

        query_result = ds.sql.analytical("", polling_interval_sec=0, autopaginate=False)

        self.assertEqual(
            query_result._status,
            "error",
        )
        self.assertEqual(
            query_result.error_message,
            "error",
        )
        self.assertEqual(
            query_result.error_details,
            "error",
        )

    @patch("chainalysis.sql._analytical.time")
    @patch("chainalysis.sql._analytical.sleep", return_value=None)
    @patch("chainalysis.sql._analytical.issue_request")
    def test_auto_pagination_errors_if_issue_request_errors(
        self, mocked_issue_request: Mock, mocked_sleep: Mock, mocked_time: Mock
    ):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_time.side_effect = (0, math.inf)

        first_successful_response = mocked_async_query_id_response
        second_successful_response = mocked_async_query_response_1
        third_successful_response = mocked_async_query_response_2

        mocked_issue_request.side_effect = (
            first_successful_response,
            second_successful_response,
            third_successful_response,
            Exception(),
        )

        query_result = ds.sql.analytical(
            "",
            polling_interval_sec=0,
            autopaginate=True,
        )
        with self.assertRaises(Exception):
            query_result.json()


if __name__ == "__main__":
    unittest.main()
