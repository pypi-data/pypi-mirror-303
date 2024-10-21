"""
This module provides the `BlocksClient` class, which interacts with the 'blocks' subpath
of the PulseChain API.

The `BlocksClient` class provides methods to retrieve information about blocks, including
block details, transactions, and withdrawals. It also allows filtering blocks by block type
and uses the `APIRequestHandler` for making HTTP requests.
"""
from pulsechain.models import BaseResponse
from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.subpath_client import SubpathClient
from pulsechain.utils import paginated
from pulsechain.validators import validate_block_type


class BlocksClient(SubpathClient):
    """
    Client for interacting with the 'blocks' subpath of the PulseChain API.

    The `BlocksClient` provides methods to interact with block data, including retrieving
    block details, transactions, and withdrawals for a specific block. It also supports
    filtering blocks by block type.

    Attributes:
        request_handler (APIRequestHandler): The handler for making HTTP requests.
    """

    def __init__(self, request_handler: APIRequestHandler):
        """
        Initialize the BlocksClient with the subpath 'blocks'.

        :param request_handler: The handler for making HTTP requests.
        """
        super().__init__(subpath="blocks", request_handler=request_handler)

    @paginated
    def get_blocks(
        self, block_type: list[str] | None = None, params: dict | None = None
    ) -> tuple[BaseResponse, dict]:
        """
        Get information about blocks.
        :return: BaseResponse containing information about the blocks.
        """
        params = params or {}
        if block_type:
            params["type"] = validate_block_type(block_type)
        response = self.get(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_block_info(self, block: str) -> BaseResponse:
        """
        Get information about a specific block.
        :param block: the hash or the number of the block
        :return: BaseResponse with information about the block
        """
        response = self.get(block)
        return BaseResponse(items=[response])

    @paginated
    def get_block_txns(
        self, block: str, params: dict | None = None
    ) -> tuple[BaseResponse, dict | None]:
        """
        Get transactions in a specific block.
        :param block: the hash or the number of the block
        :param params: Optional dictionary of additional parameters for pagination
        :return: A tuple containing a BaseResponse with block transactions
                 and a dict of next page parameters (or None if there are no more pages)
        """
        response = self.get(f"{block}/transactions", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_block_withdrawals(
        self, block: str, params: dict | None = None
    ) -> tuple[BaseResponse, dict]:
        """
        Get withdrawals in a specific block.
        :param block: the hash or the number of the block
        :param params: Optional dictionary of additional parameters for pagination
        :return: A tuple containing a BaseResponse with information about the block withdrawals
                 and a dict of next page parameters (or None if there are no more pages)
        """
        response = self.get(f"{block}/withdrawals", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]
