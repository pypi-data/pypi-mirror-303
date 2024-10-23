import pandas as pd

from chainalysis._constants import BASE_URL, TRANSACTIONAL_ENDPOINTS
from chainalysis._exceptions import (
    DataSolutionsSDKException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException,
    UnhandledException,
)
from chainalysis.util_functions.requests import issue_request


class TransactionalQuery:
    """
    The TransactionalQuery class provides methods to handle transactional queries.
    It supports fetching results as JSON or pandas DataFrame,
    and provides query execution statistics.
    """

    def __init__(self, api_key: str):
        """
        Initialize the Transactional Query object with an API key.

        :param api_key: API key for authenticating requests.
        :type api_key: str
        """
        self.api_key = api_key

    def __call__(
        self, query: str, parameters: dict[str, str] = {}, options: dict[str, str] = {}
    ) -> "TransactionalQuery":
        """
        Execute a SQL query using the provided parameters and options.

        :param query: SQL query template with placeholders for parameters.
        :type query: str
        :param parameters: Parameters to format the SQL query.
        :type parameters: dict[str, str], optional
        :param options: Additional options for query execution.
        :type options: dict[str, str], optional
        :return: An instance of the Transactional class with query results.
        :rtype: Transactional
        :raises UnauthorizedException: Raises an exception if the API key is invalid.
        :raises ForbiddenException: Raises an exception if the API key does not have access to the resource.
        :raises NotFoundException: Raises an exception if the resource is not found.
        :raises DataSolutionsSDKException: Raises an exception if the query execution results in an error.
        :raises UnhandledException: Raises an exception if an unhandled exception occurs.
        """
        self._status_code = 0
        self.results = {}
        self._stats = {}
        self.json_response = {}
        self._status = "error"
        self.dataframe_data = None

        query_execution_url = (
            f"{BASE_URL['base_url']}/{TRANSACTIONAL_ENDPOINTS['query_execution']}"
        )

        body = {
            "sql": query,
            "parameters": parameters,
            "options": options,
        }

        try:
            self.json_response = issue_request(
                api_key=self.api_key,
                url=query_execution_url,
                body=body,
                method="POST",
            )
            self._status = self.json_response["status"]
            if self._status == "error":
                self.error_message = self.json_response["message"]
                self.error_details = self.json_response.get("details")
                self.exception = DataSolutionsSDKException(self.error_message)
            else:
                self._stats = self.json_response["stats"]
                self.results = self.json_response["results"]
                self._status_code = 200
        except (UnauthorizedException, ForbiddenException, NotFoundException) as e:
            raise e
        except DataSolutionsSDKException as e:
            self.exception = e.get_exception()
            self._status_code = e.status_code
        except Exception as e:
            self.exception = UnhandledException(
                details=e,
            )
        return self

    def json(self) -> dict:
        """
        Return the JSON data of the results.

        :return: JSON results of the SQL query.
        :rtype: dict
        :raises Exception: Raises an exception if the query resulted in an error.
        """
        if self._status != "error":
            return self.results
        else:
            raise self.exception

    def df(self) -> pd.DataFrame:
        """
        Convert query results into a pandas DataFrame.

        :return: DataFrame containing the results of the SQL query.
        :rtype: pd.DataFrame
        :raises Exception: Raises an exception if the query resulted in an error.
        """
        if self._status != "error":
            if self.dataframe_data is None:
                self.dataframe_data = pd.DataFrame(self.results)
            return self.dataframe_data
        else:
            raise self.exception

    def stats(self) -> dict:
        """
        Get the statistics of the executed query.

        :return: Statistics of the query execution.
        :rtype: dict
        :raises Exception: Raises an exception if the query resulted in an error.
        """
        if self._status != "error":
            return self._stats
        else:
            raise self.exception

    def was_successful(self) -> bool:
        """
        Determine if the query executed successfully.

        :return: True if the query was successful, False otherwise.
        :rtype: bool
        """
        if self._status != "error":
            return True
        return False

    def status_code(self) -> int:
        """
        Return the status code of the query.

        :return: The status code of the query.
        :rtype: int
        """
        return self._status_code
