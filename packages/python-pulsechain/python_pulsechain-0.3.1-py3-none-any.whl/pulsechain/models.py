"""
Response models for the PulseChain API.

This module defines the BaseResponse and PaginatedResponse models, which are used
to structure the API responses. The models are designed to handle both regular
and paginated responses, making it easier to parse the data from the API.
"""

from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    Base response model for the PulseChain API.

    This model represents the basic structure of API responses, where the
    response contains a list of items, each represented as a dictionary
    with arbitrary key-value pairs.
    """

    items: list[dict[str, Any]]


class PaginatedResponse(BaseResponse):
    """
    Paginated response model for the PulseChain API.

    This model extends the BaseResponse to include pagination information
    via the 'next_page_params' attribute, which can be used to fetch the
    next set of results from the API.
    """

    next_page_params: dict[str, Any] | None
