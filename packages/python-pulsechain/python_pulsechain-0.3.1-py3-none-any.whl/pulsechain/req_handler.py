"""
This module provides the `APIRequestHandler` class, which is responsible for making HTTP GET
requests to the PulseChain API.

The `APIRequestHandler` manages sending GET requests, handles timeouts and errors, and checks
API response status codes to raise appropriate exceptions in case of failure.
"""
import httpx

from pulsechain.exceptions import (
    PulseChainBadRequestException,
    PulseChainServerError,
    PulseChainTimeoutException,
    PulseChainUnknownException,
    PulseChainUnprocessableEntityException,
)


class APIRequestHandler:
    """
    A handler for making HTTP GET requests to the PulseChain API.

    This class is used to send HTTP GET requests to the PulseChain API and handle various
    HTTP status codes, including timeouts and server errors. It parses the JSON response
    if the request is successful.

    Attributes:
        base_url (str): The base URL of the PulseChain API.
    """

    def __init__(self, base_url: str, timeout: float = 60):
        """
        Initialize the APIRequestHandler with the provided base URL.

        :param base_url: The base URL for the PulseChain API.
        :param timeout: The timeout for the HTTP requests in seconds.
        """
        self.base_url = base_url
        self.timeout = timeout

    def get(self, path: str, params: dict | None = None) -> dict | list:
        """
        Send a GET request to the PulseChain API.

        This method sends a GET request to the specified path and includes optional query
        parameters. It handles timeouts and checks the response status codes.

        :param path: The API path to send the request to.
        :param params: Optional query parameters for the request.
        :returns: The API response as a dictionary or list.
        :raises PulseChainTimeoutException: If the request times out.
        """
        try:
            response = httpx.get(f"{self.base_url}/{path}", params=params, timeout=self.timeout)
        except httpx.ReadTimeout as exc:
            raise PulseChainTimeoutException(exc.args[0]) from exc
        return self._check_result(response)

    @staticmethod
    def _check_result(response: httpx.Response) -> dict:
        """
        Check the result of the API response and handle errors.

        This method checks the HTTP status code of the response and raises an appropriate
        exception if the request was not successful. It returns the parsed JSON response
        if the request is successful.

        :param response: The HTTP response object from the PulseChain API.
        :returns: The parsed JSON response as a dictionary.
        :raises PulseChainServerError: If the response status code is 500 (Internal Server Error).
        :raises PulseChainUnprocessableEntityException: If the response status code is 422 (Unprocessable Entity).
        :raises PulseChainBadRequestException: If the response status code is 400 (Bad Request).
        :raises PulseChainUnknownException: If the response status code is not recognized.
        """
        if response.status_code == 200:
            return response.json()
        if response.status_code == 500:
            raise PulseChainServerError(response)
        if response.status_code == 422:
            raise PulseChainUnprocessableEntityException(response)
        if response.status_code == 400:
            raise PulseChainBadRequestException(response)
        raise PulseChainUnknownException(f"{response.status_code}: {response.text}")
