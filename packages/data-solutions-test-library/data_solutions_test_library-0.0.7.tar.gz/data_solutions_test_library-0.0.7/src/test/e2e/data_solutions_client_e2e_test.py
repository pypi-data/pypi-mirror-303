import os
import unittest

from chainalysis import DataSolutionsClient


class DataSolutionsClientE2eTests(unittest.TestCase):
    """
    End-to-end tests for the DataSolutionsClient class.
    """

    def test_transactional_select_flow(self):
        """
        Test the transactional select flow.
        """
        ds = DataSolutionsClient(api_key=os.getenv("API_KEY"))
        transactional_select = ds.orm.TransactionalSelect("ethereum.blocks")

        query = transactional_select.with_columns(
            transactional_select.c.block_number, transactional_select.c.timestamp
        ).where(transactional_select.c.block_number == 10)

        print(query.sql())

        print(query.execute().df())

    def test_analytical_select_flow(self):
        """
        Test the analytical select flow.
        """
        ds = DataSolutionsClient(api_key=os.getenv("API_KEY"))
        analytical_select = ds.orm.AnalyticalSelect("cross_chain.clusters")

        query = (
            analytical_select.with_columns(
                analytical_select.c.cluster_id, analytical_select.c.entity_name
            )
            .where(analytical_select.c.entity_category == "exchange")
            .limit(5)
        )

        print(query.sql())

        print(query.execute().df())


if __name__ == "__main__":
    unittest.main()
