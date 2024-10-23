import unittest
from unittest.mock import Mock, patch

from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table

from chainalysis._exceptions import ValueException
from chainalysis.orm._transactional_select import TransactionalSelect

schemas = {
    "schema": {
        "chain1": {
            "layer1": [
                {
                    "table1": {
                        "meta": {
                            "table": "table1",
                            "description": "table1 description",
                            "indexes": [
                                [
                                    "index1",
                                ],
                                [
                                    "index2",
                                    "index3",
                                ],
                                [
                                    "index4",
                                    "index5",
                                    "index6",
                                ],
                            ],
                        },
                        "schema": [
                            {
                                "column": "column1",
                                "type": "string",
                                "description": "column1 description",
                            },
                            {
                                "column": "column2",
                                "type": "integer",
                                "description": "column2 description",
                            },
                            {
                                "column": "column3",
                                "type": "boolean",
                                "description": "column3 description",
                            },
                        ],
                    }
                },
                {
                    "table2": {
                        "meta": {
                            "table": "table2",
                            "description": "table2 description",
                            "indexes": [
                                [
                                    "index7",
                                ],
                                [
                                    "index8",
                                    "index9",
                                ],
                                [
                                    "index10",
                                    "index11",
                                ],
                            ],
                        },
                        "schema": [
                            {
                                "column": "column4",
                                "type": "type4",
                                "description": "column4 description",
                            },
                        ],
                    }
                },
            ],
            "layer2": [
                {
                    "table3": {
                        "meta": {
                            "table": "table3",
                            "description": "table3 description",
                            "indexes": [
                                [
                                    "index12",
                                ],
                                [
                                    "index13",
                                    "index14",
                                ],
                                [
                                    "index15",
                                    "index16",
                                    "index17",
                                ],
                            ],
                        },
                        "schema": [
                            {
                                "column": "column4",
                                "type": "type4",
                                "description": "column4 description",
                            },
                        ],
                    },
                },
            ],
        },
        "chain2": {
            "layer1": [
                {
                    "table1": {
                        "meta": {
                            "table": "table1",
                            "description": "table1 description",
                            "indexes": [
                                [
                                    "index1",
                                ],
                                [
                                    "index2",
                                    "index3",
                                ],
                                [
                                    "index4",
                                    "index5",
                                    "index6",
                                ],
                            ],
                        },
                        "schema": [
                            {
                                "column": "column1",
                                "type": "type1",
                                "description": "column1 description",
                            },
                            {
                                "column": "column2",
                                "type": "type",
                                "description": "column2 description",
                            },
                            {
                                "column": "column3",
                                "type": "type",
                                "description": "column3 description",
                            },
                        ],
                    }
                },
                {
                    "table2": {
                        "meta": {
                            "table": "table2",
                            "description": "table2 description",
                            "indexes": [
                                [
                                    "index7",
                                ],
                                [
                                    "index8",
                                    "index9",
                                ],
                                [
                                    "index10",
                                    "index11",
                                ],
                            ],
                        },
                        "schema": [
                            {
                                "column": "column4",
                                "type": "type4",
                                "description": "column4 description",
                            },
                        ],
                    }
                },
            ],
            "layer2": [
                {
                    "table3": {
                        "meta": {
                            "table": "table3",
                            "description": "table3 description",
                            "indexes": [
                                [
                                    "index12",
                                ],
                                [
                                    "index13",
                                    "index14",
                                ],
                                [
                                    "index15",
                                    "index16",
                                    "index17",
                                ],
                            ],
                        },
                        "schema": [
                            {
                                "column": "column4",
                                "type": "type4",
                                "description": "column4 description",
                            },
                        ],
                    },
                },
            ],
        },
    }
}


class TransactionalSelectTests(unittest.TestCase):
    @patch("chainalysis.orm._transactional_select.issue_request")
    def test_get_table(self, mock_issue_request: Mock):
        """
        Test that get_table() returns a valid table object with columns correctly mapped.
        """

        mock_issue_request.return_value = schemas
        table = TransactionalSelect("api_key", "chain1.table1").table

        # Define the expected table
        expected_table = Table(
            "chain1.table1",
            MetaData(),
            Column("column1", String, comment="column1 description"),
            Column("column2", Integer, comment="column2 description"),
            Column("column3", Boolean, comment="column3 description"),
        )

        # Compare the names and columns of the tables
        self.assertEqual(table.name, expected_table.name)
        self.assertEqual(len(table.columns), len(expected_table.columns))

        for col in table.columns:
            expected_col = expected_table.columns[col.name]
            self.assertEqual(col.name, expected_col.name)
            self.assertIsInstance(col.type, type(expected_col.type))
            self.assertEqual(col.comment, expected_col.comment)

    @patch("chainalysis.orm._transactional_select.issue_request")
    def test_invalid_chain(self, mock_issue_request: Mock):
        """
        Test that an invalid chain raises a ValueException.
        """

        mock_issue_request.return_value = schemas
        with self.assertRaises(ValueException) as context:
            TransactionalSelect("api_key", "invalid_chain.table1")
        self.assertEqual(
            str(context.exception),
            "Chain 'invalid_chain' does not exist in the database. Check your input. If you believe the inputted chain should exist, contact Data Solutions.",
        )

    @patch("chainalysis.orm._transactional_select.issue_request")
    def test_invalid_table(self, mock_issue_request: Mock):
        """
        Test that an invalid chain raises a ValueException.
        """

        mock_issue_request.return_value = schemas
        with self.assertRaises(ValueException) as context:
            TransactionalSelect("api_key", "chain1.invalid_table")
        self.assertEqual(
            str(context.exception),
            "Table 'invalid_table' does not exist in the database for chain 'chain1'. Check your input. If you believe the inputted table should exist, contact Data Solutions.",
        )


if __name__ == "__main__":
    unittest.main()
