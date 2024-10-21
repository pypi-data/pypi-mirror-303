"""
utils.py

Module provides helper functions.
"""
from functools import wraps

from pulsechain.models import PaginatedResponse


def add_decimal_sign(string: str, decimal_places: int = 18) -> str:
    """
    Insert a dot into a string at a specific position from the right.

    :param string: The string to insert the dot into.
    :type string: str
    :param decimal_places: The number of decimal places to separate from the right.
    :type decimal_places: int
    :return: The string with the dot inserted.
    :rtype: str
    """
    return string[:-decimal_places] + "." + string[-decimal_places:]


def paginated(func):
    """
    A decorator that handles pagination for API endpoints.

    This decorator automatically manages pagination by passing `next_page_params`
    to the decorated function. It expects the decorated function to return a
    `BaseResponse` containing the items and a dictionary with `next_page_params`.
    The decorator then wraps the result in a `PaginatedResponse`.

    :param func: The function to be decorated, which should return a tuple of `BaseResponse`
                 and `next_page_params`.
    :type func: callable
    :return: A `PaginatedResponse` containing all items and the final `next_page_params`.
    :rtype: PaginatedResponse
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        params = kwargs.pop("next_page_params", {})
        base_response, next_page_params = func(self, *args, params=params)
        return PaginatedResponse(
            items=base_response.items, next_page_params=next_page_params
        )

    return wrapper
