import os
import unittest

from chainalysis.sql._analytical import AnalyticalQuery


class AnalyticalQueryE2eTest(unittest.TestCase):
    def test_execution_without_autopagination(self):
        """
        Test that the Analytical class can execute a query without autopagination.
        """

        query = """
            SELECT * FROM ethereum.category_signals LIMIT 1000000
        """

        analytical_result = AnalyticalQuery(os.getenv("API_KEY")).__call__(
            query=query,
            autopaginate=False,
        )

        analytical_result.json()
        analytical_result.df()

    def test_execution_with_autopagination(self):
        """
        Test that the Analytical class can execute a query with autopagination.
        """

        query = """
            SELECT * FROM ethereum.category_signals LIMIT 500000
        """

        analytical_result = AnalyticalQuery(os.getenv("API_KEY")).__call__(
            query=query,
            autopaginate=True,
        )

        analytical_result.json()
        analytical_result.df()

    def test_execution_with_autopagination_with_one_page(self):
        """
        Test that the Analytical class can execute a query with autopagination.
        """

        query = """
            SELECT * FROM ethereum.category_signals LIMIT 5
        """

        analytical_result = AnalyticalQuery(os.getenv("API_KEY")).__call__(
            query=query,
            autopaginate=True,
        )

        analytical_result.json()
        analytical_result.df()

    def test_autopagination_with_very_large_query(self):
        """
        Test that the Analytical class can handle a query with autopagination when the query is very large.
        """

        query = """
            SELECT * FROM ethereum.receiving_exposure_aggregation_daily LIMIT 10000000
        """

        analytical_result = AnalyticalQuery(os.getenv("API_KEY")).__call__(
            query=query,
            autopaginate=True,
            polling_interval_sec=10,
        )

        # Ensure that the full dataset has been fetched
        self.assertEqual(len(analytical_result.json()), 10000000)
        analytical_result.json()

    def test_autopagination_with_very_large_query_with_free_tier_api_key(self):
        """
        Test that the Analytical class can handle a query with autopagination when the query is very large.
        """

        query = """
            SELECT * FROM ethereum.receiving_exposure_aggregation_daily LIMIT 10000000
        """

        analytical_result = AnalyticalQuery(os.getenv("FREE_TIER_API_KEY")).__call__(
            query=query,
            autopaginate=True,
            polling_interval_sec=10,
        )

        # Ensure that the full dataset has been fetched
        self.assertEqual(len(analytical_result.json()), 10000000)
        analytical_result.json()

    def test_multiple_api_calls(self):
        """
        Test that the Analytical class can handle multiple API calls and return the correct results.
        """

        query = """
            SELECT * FROM ethereum.category_signals LIMIT 10
        """

        analytical_result = AnalyticalQuery(os.getenv("API_KEY")).__call__(
            query=query,
            autopaginate=True,
        )

        self.assertEqual(
            len(analytical_result.json()),
            10,
        )

        print(analytical_result.df())

        query = """
            SELECT * FROM ethereum.category_signals LIMIT 20
        """

        analytical_result = AnalyticalQuery(os.getenv("API_KEY")).__call__(
            query=query,
            autopaginate=True,
        )

        self.assertEqual(
            len(analytical_result.json()),
            20,
        )

        print(analytical_result.df())


if __name__ == "__main__":
    unittest.main()
