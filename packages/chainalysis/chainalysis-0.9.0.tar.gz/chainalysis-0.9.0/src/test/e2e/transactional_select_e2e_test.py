import os
import unittest

from chainalysis._exceptions import ValueException
from chainalysis.orm._transactional_select import TransactionalSelect


class TransactionalSelectE2eTests(unittest.TestCase):
    def test_successful_inits(self):
        """
        Test that the TransactionalSelect class can be successfully initialized.
        """
        TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.accounts",
        )
        TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )
        TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="base.pool_liquidity_ohlc_1m",
        )
        TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="basegoerli.collections",
        )

    def test_incorrect_chain(self):
        """
        Test that the TransactionalSelect class raises an exception when an incorrect chain is provided.
        """
        with self.assertRaises(ValueException) as context:
            TransactionalSelect(
                api_key=os.getenv("API_KEY"),
                chain_table_name="incorrect_chain.accounts",
            )
        self.assertEqual(
            str(context.exception),
            "Chain 'incorrect_chain' does not exist in the database. Check your input. If you believe the inputted chain should exist, contact Data Solutions.",
        )

    def test_incorrect_table(self):
        """
        Test that the TransactionalSelect class raises an exception when an incorrect table is provided.
        """
        with self.assertRaises(ValueException) as context:
            TransactionalSelect(
                api_key=os.getenv("API_KEY"),
                chain_table_name="ethereum.incorrect_table",
            )
        self.assertEqual(
            str(context.exception),
            "Table 'incorrect_table' does not exist in the database for chain 'ethereum'. Check your input. If you believe the inputted table should exist, contact Data Solutions.",
        )

    def test_successful_execute_with_no_conditions(self):
        """
        Test that the TransactionalSelect class can successfully execute.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.accounts",
        )
        transactional_table.execute().json()

    def test_successful_execute_with_select_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with a select condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.accounts",
        )

        transactional_table.with_columns(
            transactional_table.c.address,
            transactional_table.c.created_timestamp,
            transactional_table.c.type,
        ).execute().json()

    def test_successful_execute_with_where_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with a where condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )

        transactional_table.where(
            transactional_table.c.block_number < 50
        ).execute().df()

    def test_successful_execute_with_select_and_where_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with select and where condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )

        transactional_table.with_columns(
            transactional_table.c.block_number, transactional_table.c.miner_address
        ).where(transactional_table.c.block_number < 50).execute().df()

    def test_successful_execute_with_group_by_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with a group_by condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )

        transactional_table.with_columns(
            transactional_table.c.base_fee_per_gas,
            transactional_table.c.block_hash,
        ).group_by(
            transactional_table.c.base_fee_per_gas, transactional_table.c.block_hash
        ).execute(
            options={"timeout": 500000}
        ).df()

    def test_successful_execute_with_order_by_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with an order_by condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )
        transactional_table.order_by(transactional_table.c.block_number).execute().df()

    def test_successful_execute_with_limit_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with a limit condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )
        transactional_table.limit(10).execute().df()

    def test_successful_execute_with_offset_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with an offset condition.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )
        transactional_table.limit(1).offset(10).execute().df()

    def test_successful_execute_with_join_condition(self):
        """
        Test that the TransactionalSelect class can successfully execute with a join condition.
        """
        ethereum_blocks_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )

        ethereum_accounts_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.accounts",
        )

        ethereum_blocks_table.join(
            ethereum_accounts_table.table,
            ethereum_blocks_table.c.miner_address == ethereum_accounts_table.c.address,
        ).execute().df()

    def test_successful_execute_with_multiple_conditions(self):
        """
        Test that the TransactionalSelect class can successfully execute with multiple conditions.
        """
        transactional_table = TransactionalSelect(
            api_key=os.getenv("API_KEY"),
            chain_table_name="ethereum.blocks",
        )
        transactional_table.with_columns(
            transactional_table.c.block_number, transactional_table.c.miner_address
        ).where(transactional_table.c.block_number < 50,).group_by(
            transactional_table.c.block_number, transactional_table.c.miner_address
        ).order_by(
            transactional_table.c.block_number
        ).limit(
            10
        ).offset(
            5
        ).execute().df()


if __name__ == "__main__":
    unittest.main()
