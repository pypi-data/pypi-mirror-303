import datetime
from typing import Union

from pandas import DataFrame, Series

from chainalysis._exceptions import BadRequest
from chainalysis.util_functions.check_list_type import get_list_type


class Stringify:
    """
    This class contains functions to transform python objects
    into formatted string params so they can be used to query
    Data Solutions' databases without needing to be transformed
    manually by the user.
    """

    def lists(self, data: Union[Series, list]) -> str:
        """
        Convert a list or pandas Series to a formatted string param.

        :param data: The list to be converted.
        :type data: Union[Series, list]

        :return: The converted list.
        :rtype: str
        """

        if isinstance(data, Series):
            data = data.tolist()
        return "(" + ", ".join(["'" + str(x) + "'" for x in data]) + ")"

    def columns(self, columns: list) -> str:
        """
        Convert a column select list to a formatted string param.

        :param columns: The column select list object to be converted.
        :type columns: list

        :return: The converted column select list.
        :rtype: str
        """
        type = get_list_type(columns)
        if type != str:
            raise BadRequest("Columns must be a string list")
        return ", ".join(columns)

    def datetimes(self, _datetime: datetime.datetime) -> str:
        """
        Convert a datetime object to a formatted string param.

        :param list: The datetime object to be converted.
        :type list: list

        :return: The converted datetime object.
        :rtype: str
        """
        if not isinstance(_datetime, datetime.datetime):
            raise BadRequest("Incorrect type. Supply a datetime.datetime object.")

        return f"'{_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')}'"

    def dataframes(self, df: DataFrame) -> str:
        """
        Convert a pandas DataFrame to a SQL CTE

        :param df: The DataFrame to be converted.
        :type df: DataFrame
        :return: The converted DataFrame.
        :rtype: str
        """
        tuples = list(df.itertuples(index=False, name=None))
        values = "".join([str(t) for t in tuples])
        return values
