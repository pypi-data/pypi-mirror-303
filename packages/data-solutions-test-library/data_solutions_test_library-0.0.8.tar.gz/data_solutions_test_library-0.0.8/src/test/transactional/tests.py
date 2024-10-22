import unittest
from unittest.mock import Mock, patch

import pandas as pd
import pandas.testing as pdt

from chainalysis._exceptions import (
    BadRequest,
    DataSolutionsAPIException,
    DataSolutionsSDKException,
    ForbiddenException,
    InternalServerException,
    NotFoundException,
    UnauthorizedException,
    UnhandledException,
)
from chainalysis.data_solutions import DataSolutionsClient

mocked_result = {
    "status": "success",
    "stats": {"count": 1, "size": 657, "time": 2, "truncated": "false"},
    "results": [
        {
            "block_number": 142572,
            "block_hash": "000000000000057d13a731f556c24a1318bcbb4df7d537ef07c8c813c0dc1b37",
            "timestamp": "2011-08-25T22:07:41Z",
            "median_timestamp": "2011-08-25T21:28:01Z",
            "parent_blockhash": "000000000000048edbb6c004b3fce541b5004fee9729a8b1710cb488a974d959",
            "merkleroot": "fbcf9d2616f5b8beebb21eff7186a1acc31c1bf25a71e61e2d989d2394c4d2bb",
            "version": 1,
            "version_hex": "00000001",
            "size": 44437,
            "stripped_size": 44437,
            "weight": 177748,
            "bits": "1a094a86",
            "transaction_count": 99,
            "chainwork": "0000000000000000000000000000000000000000000000050db82b769ce8b7f0",
            "nonce": 897686037.0,
            "difficulty": 1805700.836193673,
            "__confirmed": "true",
        }
    ],
}


class TransactionalTests(unittest.TestCase):
    """
    This test suite ensures that the Transactional class runs appropriatel
    """

    @patch("chainalysis.sql._transactional.issue_request")
    def test_successful_query(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.return_value = mocked_result

        query_result = ds.sql.transactional_query("")

        self.assertEqual(query_result.json(), mocked_result["results"])
        pdt.assert_frame_equal(
            query_result.df(), pd.DataFrame(mocked_result["results"])
        )
        self.assertEqual(query_result.stats(), mocked_result["stats"])
        self.assertEqual(query_result.was_successful(), True)
        self.assertEqual(query_result.status_code(), 200)

    @patch("chainalysis.sql._transactional.issue_request")
    def test_api_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = DataSolutionsAPIException()

        query_result = ds.sql.transactional_query("")

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 501)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(DataSolutionsAPIException):
            query_result.json()

        with self.assertRaises(DataSolutionsAPIException):
            query_result.df()

        with self.assertRaises(DataSolutionsAPIException):
            query_result.stats()

    @patch("chainalysis.sql._transactional.issue_request")
    def test_bad_request_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = BadRequest()

        query_result = ds.sql.transactional_query("")

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 400)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(BadRequest):
            query_result.json()

        with self.assertRaises(BadRequest):
            query_result.df()

        with self.assertRaises(BadRequest):
            query_result.stats()

    @patch("chainalysis.sql._transactional.issue_request")
    def test_unauthorized_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = UnauthorizedException()

        with self.assertRaises(UnauthorizedException):
            ds.sql.transactional_query("")

    @patch("chainalysis.sql._transactional.issue_request")
    def test_forbidden_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = ForbiddenException()

        with self.assertRaises(ForbiddenException):
            ds.sql.transactional_query("")

    @patch("chainalysis.sql._transactional.issue_request")
    def test_not_found_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = NotFoundException()

        with self.assertRaises(NotFoundException):
            ds.sql.transactional_query("")

    @patch("chainalysis.sql._transactional.issue_request")
    def test_internal_server_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = InternalServerException()

        query_result = ds.sql.transactional_query("")

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 500)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(InternalServerException):
            query_result.json()

        with self.assertRaises(InternalServerException):
            query_result.df()

        with self.assertRaises(InternalServerException):
            query_result.stats()

    @patch("chainalysis.sql._transactional.issue_request")
    def test_unhandled_exception(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_issue_request.side_effect = Exception()

        query_result = ds.sql.transactional_query("")

        self.assertEqual(query_result._status, "error")
        self.assertEqual(query_result._status_code, 0)
        self.assertEqual(query_result.was_successful(), False)

        with self.assertRaises(UnhandledException):
            query_result.json()

        with self.assertRaises(UnhandledException):
            query_result.df()

        with self.assertRaises(UnhandledException):
            query_result.stats()

    @patch("chainalysis.sql._transactional.issue_request")
    def test_incorrect_parameters(self, mocked_issue_request: Mock):
        ds = DataSolutionsClient(
            api_key="",
        )

        mocked_result = {
            "status": "error",
            "message": "Invalid query: Missing parameter value (chain)",
        }
        mocked_issue_request.return_value = mocked_result

        query_result = ds.sql.transactional_query("")

        with self.assertRaises(DataSolutionsSDKException):
            query_result.df()

        with self.assertRaises(DataSolutionsSDKException):
            query_result.stats()


if __name__ == "__main__":
    unittest.main()
