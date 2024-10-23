from warnings import warn

from chainalysis.sql._analytical import AnalyticalQuery
from chainalysis.sql._transactional import TransactionalQuery


class Sql:
    """
    The SQL class is used to query Database tables using SQL queries.
    """

    def __init__(self, api_key: str):
        """
        Initialize the SQL class.

        :param api_key: The API key for the Data Solutions API
        :type api_key: str
        """
        self.t = TransactionalQuery(api_key)
        self.a = AnalyticalQuery(api_key)

    @property
    def transactional_query(self) -> TransactionalQuery:
        """
        Call the transactional_query property to query transactional tables.
        """
        return self.t

    @property
    def analytical_query(self) -> AnalyticalQuery:
        """
        Call the analytical_query property to query analytical tables.
        """
        return self.a

    @property
    def transactional(self) -> TransactionalQuery:
        """
        The transactional property is deprecated. Use `transactional_query` instead.
        """
        warn(
            "The `transactional` property is deprecated. Use `transactional_query` instead."
        )
        return self.transactional_query

    @property
    def analytical(self) -> AnalyticalQuery:
        """
        The `analytical` property is deprecated. Use `analytical_query` instead.
        """
        warn("The analytical property is deprecated. Use `analytical_query` instead.")
        return self.analytical_query
