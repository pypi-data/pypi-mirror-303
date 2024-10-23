from chainalysis.orm._analytical_select import AnalyticalSelect
from chainalysis.orm._transactional_select import TransactionalSelect


class Orm:
    """
    The Orm class is used to query Database tables using Object Relational Mapping (ORM),
    which allows querying tables using Python methods rather than raw SQL.
    """

    def __init__(self, api_key: str):
        """
        Initialize the Orm class.

        :param api_key: The API key for the Data Solutions API
        :type api_key: str
        """
        self.api_key = api_key

    # pragma: no cover
    def TransactionalSelect(self, chain_table_name: str) -> TransactionalSelect:
        """
        Method to create a TransactionalSelect object.

        :param chain_table_name: The name of the chain table.
        :type chain_table_name: str
        :return: TransactionalSelect object.
        :rtype: TransactionalSelect
        """
        return TransactionalSelect(self.api_key, chain_table_name)

    # pragma: no cover
    def AnalyticalSelect(self, chain_table_name: str) -> AnalyticalSelect:
        """
        Method to create an AnalyticalSelect object.

        :param chain_table_name: The name of the chain table.
        :type chain_table_name: str
        :return: AnalyticalSelect object.
        :rtype: AnalyticalSelect
        """
        return AnalyticalSelect(self.api_key, chain_table_name)
