"""
Exception classes for the PulseChain API client.

This module defines a hierarchy of custom exceptions used to handle various
error scenarios when interacting with the PulseChain API. These exceptions
provide more specific context to the types of errors encountered, such as
server errors, timeouts, or invalid requests.
"""
import httpx


class PulsechainException(Exception):
    """
    Base exception for the PulseChain client.

    All custom exceptions for the PulseChain API inherit from this class.
    """


class PulseChainAPIException(PulsechainException):
    """
    Exception raised for API-related errors.

    This class is a generic exception for errors that occur when interacting
    with the PulseChain API.
    """


class PulseChainTimeoutException(PulseChainAPIException):
    """
    Exception raised when a request to the PulseChain API times out.

    This error occurs when the API takes too long to respond.
    """


class PulseChainServerError(PulseChainAPIException):
    """
    Exception raised for server errors (HTTP 500).

    This error is triggered when the PulseChain API returns a 500 status code,
    indicating an internal server error.
    """


class PulseChainUnprocessableEntityException(PulseChainAPIException):
    """
    Exception raised for unprocessable entity errors (HTTP 422).

    This error occurs when the PulseChain API cannot process the request, such as
    when the request contains invalid data. The error message from the API is
    passed into the exception.
    """

    def __init__(self, response: httpx.Response):
        super().__init__(response.json()["message"])


class PulseChainBadRequestException(PulseChainAPIException):
    """
    Exception raised for bad request errors (HTTP 400).

    This error occurs when the PulseChain API returns a 400 status code, indicating
    an invalid request. The error message from the API is passed into the exception.
    """

    def __init__(self, response: httpx.Response):
        super().__init__(response.json()["message"])


class PulseChainUnknownException(PulseChainAPIException):
    """
    Exception raised for unknown errors.

    This error is used when the PulseChain API returns an unexpected status code.
    """


class PulseChainBadParamException(PulsechainException):
    """
    Exception raised for invalid parameters.

    This error occurs when the client code passes invalid parameters to an API request.
    """
