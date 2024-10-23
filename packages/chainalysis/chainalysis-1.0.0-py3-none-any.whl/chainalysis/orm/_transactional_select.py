from sqlalchemy import Column, MetaData, Table

from chainalysis._constants import BASE_URL, TRANSACTIONAL_ENDPOINTS
from chainalysis._exceptions import ValueException
from chainalysis._types import type_mapping
from chainalysis.orm._select import Select
from chainalysis.sql._transactional import TransactionalQuery
from chainalysis.util_functions.requests import issue_request


class TransactionalSelect(Select):
    """
    The TransactionalSelect class implements the Select base class
    for querying a chain-specific table within the Data Solutions system.

    It provides the structure for constructing and executing SQL queries
    using ORM methods.
    """

    def _get_table(self, chain, table) -> Table:
        """
        Return a SQLAlchemy Table object for the given chain and table name.

        :param chain: The chain name.
        :type chain: str
        :param table: The table name.
        :type table: str
        :return: A SQLAlchemy Table object.
        :rtype: Table
        :raises ValueException: If the chain or table does not exist in the database.
        """
        get_schemas_url = (
            f"{BASE_URL['base_url']}/{TRANSACTIONAL_ENDPOINTS['get_schemas']}"
        )
        self.schemas: dict = issue_request(get_schemas_url, self.api_key)["schema"]

        chain_schema = self.schemas.get(chain)

        if not chain_schema:
            raise ValueException(
                f"Chain '{chain}' does not exist in the database. Check your input. "
                f"If you believe the inputted chain should exist, contact Data Solutions."
            )

        # If the chain exists, get the schema for the table
        for layer_tables in chain_schema.values():
            table_data = next(
                (_table for _table in layer_tables if table in _table), None
            )
            if table_data:

                # If the table exists, return the table
                columns = table_data[table]["schema"]

                table_columns = [
                    Column(
                        col["column"],
                        type_mapping[col["type"]],
                        comment=col["description"],
                    )
                    for col in columns
                ]

                return Table(f"{chain}.{table}", MetaData(), *table_columns)
        raise ValueException(
            f"Table '{table}' does not exist in the database for chain '{chain}'. Check your input. "
            f"If you believe the inputted table should exist, contact Data Solutions."
        )

    def execute(
        self,
        options: dict = {},
    ) -> TransactionalQuery:
        """
        Execute the query and return a TransactionalQuery object.

        :param options: The options for the query.
        :type options: dict
        :return: TransactionalQuery object.
        :rtype: TransactionalQuery
        """
        return TransactionalQuery(self.api_key).__call__(
            self.sql().replace('"', ""),
            options=options,
        )
