import os
import unittest

from chainalysis._exceptions import ValueException
from chainalysis.orm import AnalyticalSelect


class AnalyticalSelectE2eTests(unittest.TestCase):
    def test_successful_inits(self):
        """
        Test that the AnalyticalSelect class can be successfully initialized.
        """
        AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.category_signals",
        )
        AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )
        AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="arbitrum_one.category_signals",
        )
        AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="arbitrum_one.clusters",
        )

    def test_incorrect_chain(self):
        """
        Test that the AnalyticalSelect class raises an exception when an incorrect chain is provided.
        """
        with self.assertRaises(ValueException) as context:
            AnalyticalSelect(
                api_key=os.getenv("API_KEY"),
                chain_table_name="incorrect_chain.clusters",
            )
        self.assertEqual(
            str(context.exception),
            "Chain 'incorrect_chain' does not exist in the database. Check your input. If you believe the inputted chain should exist, contact Data Solutions.",
        )

    def test_incorrect_table(self):
        """
        Test that the AnalyticalSelect class raises an exception when an incorrect table is provided.
        """
        with self.assertRaises(ValueException) as context:
            AnalyticalSelect(
                api_key=os.getenv("API_KEY"),
                chain_table_name="ethereum.incorrect_table",
            )
        self.assertEqual(
            str(context.exception),
            "Table 'incorrect_table' does not exist in the database for chain 'ethereum'. Check your input. If you believe the inputted table should exist, contact Data Solutions.",
        )

    def test_successful_execute_with_no_conditions(self):
        """
        Test that the AnalyticalSelect class can successfully execute.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )
        analytical_table.execute(autopaginate=False).json()

    def test_successful_execute_with_select_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with a select condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )

        analytical_table.with_columns(
            analytical_table.c.chain_id,
            analytical_table.c.address,
            analytical_table.c.cluster_id,
        ).execute(autopaginate=False).json()

    def test_successful_execute_with_where_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with a where condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )

        analytical_table.where(
            analytical_table.c.address == "0xe801a7ba92dfef5092c69f70f1d1a5ba066e01b6"
        ).execute(autopaginate=False).df()

    def test_successful_execute_with_select_and_where_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with select and where condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )

        analytical_table.with_columns(
            analytical_table.c.chain_id,
            analytical_table.c.address,
            analytical_table.c.cluster_id,
        ).where(
            analytical_table.c.address == "0xe801a7ba92dfef5092c69f70f1d1a5ba066e01b6"
        ).execute(
            autopaginate=False
        ).df()

    def test_successful_execute_with_group_by_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with a group_by condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="bitcoin.sending_exposure_by_transfer",
        )

        analytical_table.with_columns(
            analytical_table.c.transaction_time,
            analytical_table.c.transfer_amount_usd,
            analytical_table.c.transfer_sender_cluster_id,
            analytical_table.c.transfer_receiver_category,
        ).group_by(
            analytical_table.c.transaction_hash,
            analytical_table.c.transaction_time,
            analytical_table.c.transfer_amount_usd,
            analytical_table.c.transfer_sender_cluster_id,
            analytical_table.c.transfer_receiver_category,
        ).execute(
            autopaginate=False
        ).df()

    def test_successful_execute_with_order_by_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with an order_by condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.receiving_exposure_aggregation_alltime",
        )
        analytical_table.order_by(analytical_table.c.amount_usd_total).execute(
            autopaginate=False
        ).df()

    def test_successful_execute_with_limit_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with a limit condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )
        analytical_table.limit(10).execute(autopaginate=False).df()

    def test_successful_execute_with_offset_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with an offset condition.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )
        analytical_table.limit(1).offset(10).execute(autopaginate=False).df()

    def test_successful_execute_with_join_condition(self):
        """
        Test that the AnalyticalSelect class can successfully execute with a join condition.
        """
        ethereum_clusters_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )

        ethereum_receiving_exposure_aggregation_alltime_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.receiving_exposure_aggregation_alltime",
        )

        ethereum_clusters_table.join(
            ethereum_receiving_exposure_aggregation_alltime_table.table,
            ethereum_clusters_table.c.cluster_id
            == ethereum_receiving_exposure_aggregation_alltime_table.c.receiver_cluster_id,
        ).execute(autopaginate=False).df()

    def test_successful_execute_with_multiple_conditions(self):
        """
        Test that the AnalyticalSelect class can successfully execute with multiple conditions.
        """
        analytical_table = AnalyticalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.clusters",
        )
        analytical_table.with_columns(
            analytical_table.c.chain_id, analytical_table.c.address
        ).where(
            analytical_table.c.address == "0xe801a7ba92dfef5092c69f70f1d1a5ba066e01b6"
        ).group_by(
            analytical_table.c.chain_id, analytical_table.c.address
        ).limit(
            10
        ).execute(
            autopaginate=False
        ).df()


if __name__ == "__main__":
    unittest.main()
