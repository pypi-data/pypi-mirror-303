from warnings import warn

from chainalysis._data_solutions import DataSolutionsClient as new_client


class DataSolutionsClient(new_client):
    """
    .. warning::
        This import path has been deprecated. Please use the following import path instead:

        .. code-block:: python

            from chainalysis import DataSolutionsClient

    This class provides SDK functions for users to query
    Data Solutions databases.
    """

    def __init__(
        self,
        api_key: str,
    ):
        """
        Initialize the DataSolutionsClient class.

        :param api_key: The API key for the Data Solutions API
        :type api_key: str
        """
        warn(
            "Importing the `DataSolutionsClient` class from `data_solutions` has been deprecated. \nPlease use the following import path instead: `from chainalysis import DataSolutionsClient`.",
        )
        super().__init__(api_key)
