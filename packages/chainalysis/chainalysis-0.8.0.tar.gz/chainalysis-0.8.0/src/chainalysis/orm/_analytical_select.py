from sqlalchemy import Column, MetaData, Table

from chainalysis._constants import ANALYTICAL_ENDPOINTS, BASE_URL
from chainalysis._exceptions import ValueException
from chainalysis._types import type_mapping
from chainalysis.orm._select import Select
from chainalysis.sql._analytical import AnalyticalQuery
from chainalysis.util_functions.requests import issue_request


class AnalyticalSelect(Select):
    """
    The AnalyticalSelect class implements the Select base class
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
            f"{BASE_URL['base_url']}/{ANALYTICAL_ENDPOINTS['get_schemas']}"
        )
        self.schemas: dict = issue_request(get_schemas_url, self.api_key)["results"]

        chain_schema: dict = self.schemas.get(chain)

        if not chain_schema:
            raise ValueException(
                f"Chain '{chain}' does not exist in the database. Check your input. If you believe the inputted chain should exist, contact Data Solutions."
            )

        # If the chain exists, get the schema for the table
        schema_table: dict = chain_schema.get(table)

        if not schema_table:
            raise ValueException(
                f"Table '{table}' does not exist in the database for chain '{chain}'. Check your input. If you believe the inputted table should exist, contact Data Solutions."
            )

        # If the table exists, return the table
        table_columns = [
            Column(
                col["name"],
                type_mapping[col["type"].lower()],
                comment=col["description"],
                nullable=col["nullable"],
            )
            for col in schema_table["columns"]
        ]
        return Table(f"{chain}.{table}", MetaData(), *table_columns)

    # pragma: no cover
    def execute(
        self,
        polling_interval_sec: int = 5,
        autopaginate: bool = True,
    ) -> AnalyticalQuery:
        """
        Execute the query and return an Analytical object.

        :param polling_interval_sec: The interval in seconds between status checks. The minimum value is 5 seconds.
        :type polling_interval_sec: int, optional
        :param autopaginate: Whether to automatically retrieve full results instead of individual pages.
        :type autopaginate: bool, optional
        :return: Analytical object.
        :rtype: Analytical
        """
        return AnalyticalQuery(self.api_key).__call__(
            self.sql().replace('"', ""),
            polling_interval_sec=polling_interval_sec,
            autopaginate=autopaginate,
        )
