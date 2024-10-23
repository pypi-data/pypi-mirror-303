from json import JSONDecodeError

from requests import request
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from chainalysis._exceptions import (
    BadRequest,
    DataSolutionsAPIException,
    ForbiddenException,
    NotFoundException,
    RateLimitExceededException,
    UnauthorizedException,
)


def get_headers(api_key: str) -> dict:
    """
    Generate headers for an HTTP request.

    This function creates a dictionary of headers required for an HTTP request,
    including the API key for authorization and JSON content-type headers which
    indicate what sort of information will be sent with the request.

    :param api_key: The API key used for authenticating the request.
    :type api_key: str
    :return: A dictionary containing the headers for the HTTP request.
    :rtype: dict
    """
    return {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Request-Source": "chainalysis-python-sdk",
    }


def retry_condition(exception):
    if isinstance(
        exception,
        (BadRequest, UnauthorizedException, ForbiddenException, NotFoundException),
    ):
        return False
    return True


@retry(
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception(retry_condition),
    stop=stop_after_attempt(10),
)
def issue_request(
    url: str,
    api_key: str,
    params: dict = {},
    body: dict = {},
    method: str = "GET",
) -> dict:
    """
    Helper method to issue a request to the Data Solutions API.
    This method will automatically retry the request, and handle
    basic error checking.

    :param url: The URL to send the request to.
    :type url: str
    :param api_key: The API key used for authenticating the request.
    :type api_key: str
    :param params: The parameters to send with the request.
    :type params: dict, optional
    :param body: The body of the request.
    :type body: dict, optional
    :param method: The HTTP method to use for the request.
    :type method: str, optional
    :return: The JSON response from the API.
    :rtype: dict
    """
    # Encode params and body into a single variable data
    data = {**(params or {}), **(body or {})}

    headers = get_headers(api_key)

    response = request(
        method,
        url,
        headers=headers,
        json=data,
    )

    if response.status_code >= 300:
        try:  # Try to decode the json response of the error
            json_output = response.json()
            error_message = json_output.get("message")

        except JSONDecodeError:
            raise DataSolutionsAPIException(
                message="Unexpected response from the API - response was not JSON",
            )
        if response.status_code == 400:
            raise BadRequest(
                message=error_message,
            )
        if response.status_code == 401:
            raise UnauthorizedException(
                message=error_message,
            )
        if response.status_code == 403:
            raise ForbiddenException(
                message=error_message,
            )
        if response.status_code == 404:
            raise NotFoundException(
                message=error_message,
            )
        if response.status_code == 429:
            raise RateLimitExceededException(
                message=error_message,
            )
        raise DataSolutionsAPIException(
            message=error_message,
        )

    try:  # Try to decode the json response of the successful request
        response_json = response.json()
    except JSONDecodeError:
        raise DataSolutionsAPIException(
            message="Unexpected response from the API - response was not JSON",
        )

    return response_json
