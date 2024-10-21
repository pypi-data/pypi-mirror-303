"""
This module provides the `SubpathClient` class, which serves as the base class for
API clients that interact with specific subpaths in the PulseChain API.

The `SubpathClient` class is responsible for handling HTTP requests to API endpoints
that belong to distinct subpath segments, such as 'addresses', 'tokens', or 'blocks'.
It utilizes the `APIRequestHandler` to manage GET requests and provides a reusable
structure for interacting with different sections of the API.
"""
from pulsechain.req_handler import APIRequestHandler


class SubpathClient:
    """
    Base class for API clients that interact with a specific subpath.

    Each subpath client is responsible for interacting with a distinct section of
    the PulseChain API, such as 'addresses', 'tokens', etc.

    Attributes:
        request_handler (APIRequestHandler): The handler for making HTTP requests.
        subpath (str): The specific subpath for this client.
    """

    def __init__(self, request_handler: APIRequestHandler, subpath: str):
        """
        Initialize the subpath client.

        :param request_handler: The handler for making HTTP requests.
        :param subpath: The specific subpath for this client.
        """
        self.request_handler = request_handler
        self.subpath = subpath

    def get(self, path: str | None = None, params: dict | None = None) -> dict:
        """
        Perform a GET request with the subpath.

        Sends a GET request to the specified path within this client's subpath.

        :param path: Optional additional path to append to the subpath.
        :param params: Optional query parameters.
        :return: The API response as a dictionary.
        """
        full_path = f"{self.subpath}/{path}" if path else self.subpath
        response = self.request_handler.get(full_path, params)
        return {"items": response} if isinstance(response, list) else response
