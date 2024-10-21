"""
This module provides the `TransactionsClient` class,
which interacts with the 'transactions' subpath of the PulseChain API.

The `TransactionsClient` class provides methods to retrieve detailed transaction information,
including token transfers, internal transactions, logs, and state changes. It utilizes the
`APIRequestHandler` for making HTTP requests and includes pagination support for methods that
return large datasets.
"""
from pulsechain.models import BaseResponse
from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.subpath_client import SubpathClient
from pulsechain.utils import paginated
from pulsechain.validators import (
    validate_method,
    validate_txn_filter,
    validate_txn_type,
)


class TransactionsClient(SubpathClient):
    """
    Client for interacting with the 'transactions' subpath of the PulseChain API.

    The `TransactionsClient` provides methods to retrieve information about transactions,
    including transaction details, token transfers, internal transactions, logs, and state
    changes. It also handles validation of transaction filters and methods.

    Attributes:
        request_handler (APIRequestHandler): The handler for making HTTP requests.
    """

    def __init__(self, request_handler: APIRequestHandler):
        """
        Initialize the TransactionsClient with the subpath 'transactions'.
        """
        super().__init__(subpath="transactions", request_handler=request_handler)

    @paginated
    def get_transactions(
        self,
        txn_filter: list[str] | None = None,
        txn_type: list[str] | None = None,
        method: list[str] | None = None,
        params: dict | None = None,
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve a list of transactions based on filters.

        This method allows for filtering transactions based on filter, transaction type, and method.
        Validates the provided filters and returns a paginated response.

        :param txn_filter: List of transaction filters (e.g., 'pending', 'validated').
        :param txn_type: List of transaction types (e.g., 'token_transfer', 'contract_creation').
        :param method: List of methods (e.g., 'approve', 'transfer').
        :param params: Additional query parameters for the request.
        :return: A tuple containing a `BaseResponse` object with the transaction data and
                 the next page parameters for pagination.
        """
        if params:
            if txn_filter:
                params["filter"] = validate_txn_filter(txn_filter)
            if txn_type:
                params["tx_type"] = validate_txn_type(txn_type)
            if method:
                params["method"] = validate_method(method)

        response = self.get(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_transaction_info(self, transaction_hash: str) -> BaseResponse:
        """
        Get detailed information about a specific transaction.

        :param transaction_hash: The hash of the transaction.
        :return: A `BaseResponse` object containing detailed information about the transaction.
        """
        return BaseResponse(items=[self.get(transaction_hash)])

    @paginated
    def get_token_transfers(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve token transfers for a specific transaction.

        :param transaction_hash: The hash of the transaction.
        :param params: Additional parameters for the request.
        :return: A tuple containing a `BaseResponse` object with token transfer data and
                 the next page parameters for pagination.
        """
        response = self.get(f"{transaction_hash}/token-transfers", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_internal_transactions(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve internal transactions for a specific transaction.

        :param transaction_hash: The hash of the transaction.
        :param params: Additional parameters for the request.
        :return: A tuple containing a `BaseResponse` object with internal transaction data and
                 the next page parameters for pagination.
        """
        response = self.get(f"{transaction_hash}/internal-transactions", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_logs(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve logs for a specific transaction.

        :param transaction_hash: The hash of the transaction.
        :param params: Additional parameters for the request.
        :return: A tuple containing a `BaseResponse` object with log data and
                 the next page parameters for pagination.
        """
        response = self.get(f"{transaction_hash}/logs", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_raw_trace(self, transaction_hash: str) -> BaseResponse:
        """
        Retrieve raw trace information for a specific transaction.

        :param transaction_hash: The hash of the transaction.
        :return: A `BaseResponse` object containing raw trace information about the transaction.
        """
        return BaseResponse(items=[self.get(f"{transaction_hash}/raw-trace")])

    @paginated
    def get_state_changes(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve state changes for a specific transaction.

        :param transaction_hash: The hash of the transaction.
        :param params: Additional parameters for the request.
        :return: A tuple containing a `BaseResponse` object with state change data and
                 the next page parameters for pagination.
        """
        response = self.get(f"{transaction_hash}/state-changes", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]
