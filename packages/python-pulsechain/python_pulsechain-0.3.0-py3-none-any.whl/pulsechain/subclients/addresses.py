"""
Addresses subclient for the PulseChain API.
This client handles the endpoints related to addresses.
"""
from pulsechain.models import BaseResponse
from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.subpath_client import SubpathClient
from pulsechain.utils import paginated
from pulsechain.validators import validate_address_txn_filter, validate_token_type


class AddressesClient(SubpathClient):
    """
    Addresses subclient class for the PulseChain API.
    """

    def __init__(self, request_handler: APIRequestHandler):
        """
        Initialize the AddressesClient with the subpath 'addresses'.
        """
        super().__init__(subpath="addresses", request_handler=request_handler)

    def _get_address_txns(
        self,
        address: str,
        endpoint: str,
        params: dict,
        txn_filter: str | None = None,
    ) -> tuple[list, dict]:
        """
        Fetch transactions for a specific address based on the provided endpoint.

        :param str address: The address for which to fetch transactions.
        :param str endpoint: The endpoint to use for the request (e.g., 'transactions', 'internal-transactions').
        :param dict params: Additional parameters for the request.
        :param str txn_filter: A filter to apply on the transactions, such as filtering by transaction type
                               Valid options are 'to', 'from'.
                               Defaults to None.
        :returns: A tuple containing a list of transactions and the next page parameters.
        :raises PulseChainBadParamException: If an invalid `txn_filter` is provided.
        """
        if txn_filter is not None:
            txn_filter = validate_address_txn_filter(txn_filter)
            params["filter"] = txn_filter

        response = self.get(f"{address}/{endpoint}", params=params)
        return response["items"], response["next_page_params"]

    def get_pls_holders_list(self) -> BaseResponse:
        """
        Fetch the list of PLS holders.

        :returns: A response object containing a list of PLS holders.
        """
        return BaseResponse(items=self.get()["items"])

    def get_info(self, address: str) -> BaseResponse:
        """
        Fetch general information about a specific address.

        :param str address: The address to fetch information for.
        :returns: A response object containing general information about the address.
        """
        return BaseResponse(items=[self.get(address)])

    def get_counters(self, address: str) -> BaseResponse:
        """
        Fetch counters (e.g., transaction count) for a specific address.

        :param str address: The address to fetch counters for.
        :returns: A response object containing counters related to the address.
        """
        return BaseResponse(items=[self.get(f"{address}/counters")])

    @paginated
    def get_transactions(
        self,
        address: str,
        txn_filter: str | None = None,
        **kwargs,
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch transactions for a specific address with optional transaction filtering and pagination.

        :param str address: The address for which to fetch transactions.
        :param str txn_filter: A filter to apply on the transactions.
                               Defaults to None.
        :returns: A tuple containing a response object with the transactions and the next page parameters.
        """
        params = kwargs.pop("params", {})
        items, next_page_params = self._get_address_txns(
            address, "transactions", params, txn_filter
        )
        return BaseResponse(items=items), next_page_params

    @paginated
    def get_token_transfers(
        self,
        address: str,
        token_type: list[str] | None = None,
        txn_filter: str | None = None,
        token: str | None = None,
        **kwargs,
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch token transfers for a specific address with optional filters for token type, transaction type, and token.

        :param str address: The address for which to fetch token transfers.
        :param list[str] token_type: A list of token types to filter the transfers.
                                     Valid options are 'ERC-20', 'ERC-721', or 'ERC-1155'.
                                     Defaults to None.
        :param str txn_filter: A filter to apply on the transactions.
                               Defaults to None.
        :param str token: A specific token to filter the transfers by. Defaults to None.
        :returns: A tuple containing a response object with token transfers and the next page parameters.
        :raises PulseChainBadParamException: If an invalid `token_type` or `txn_filter` is provided.
        """
        params = kwargs.pop("params", {})
        if token_type:
            params["token_type"] = validate_token_type(token_type)

        if txn_filter:
            params["filter"] = validate_address_txn_filter(txn_filter)

        if token:
            params["token"] = token

        response = self.get(f"{address}/token-transfers", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_internal_transactions(
        self, address: str, txn_filter: str | None = None, **kwargs
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch internal transactions for a specific address.

        :param str address: The address for which to fetch internal transactions.
        :param str txn_filter: A filter to apply on the transactions.
                               Defaults to None.
        :returns: A tuple containing a response object with internal transactions and the next page parameters.
        """
        params = kwargs.pop("params", {})
        items, next_page_params = self._get_address_txns(
            address, "internal-transactions", params, txn_filter
        )
        return BaseResponse(items=items), next_page_params

    def get_logs(self, address: str) -> BaseResponse:
        """
        Fetch logs for the specified address. This is applicable to Smart Contract addresses.

        :param str address: The smart contract address to fetch logs for.
        :returns: A response object containing logs related to the smart contract.
        """
        return BaseResponse(items=self.get(f"{address}/logs")["items"])

    @paginated
    def get_blocks_validated(
        self, address: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch blocks validated by a specific address.

        :param str address: The address for which to fetch blocks validated.
        :param dict params: Additional parameters for the request.
        :returns: A tuple containing a response object with the blocks validated and the next page parameters.
        """
        response = self.get(f"{address}/blocks-validated", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_token_balances(self, address: str) -> BaseResponse:
        """
        Fetch all token balances for a specific address.

        :param str address: The address for which to fetch token balances.
        :returns: A response object containing token balances.
        """
        response = self.get(f"{address}/token-balances")
        return BaseResponse(items=response["items"])

    @paginated
    def get_tokens(
        self, address: str, token_type: list[str] | None = None, **kwargs
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch token balances for a specific address with optional filtering by token type and pagination.

        :param str address: The address for which to fetch token balances.
        :param list[str] token_type: A list of token types to filter the balances.
                                     Valid options are 'ERC-20', 'ERC-721', or 'ERC-1155'. Defaults to None.
        :returns: A tuple containing a response object with the token balances and the next page parameters.
        """
        params = kwargs.pop("params", {})
        if token_type:
            params["type"] = validate_token_type(token_type)
        response = self.get(f"{address}/tokens", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_coin_balance_history(
        self, address: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch PLS coin balance history for a specific address with pagination.

        :param str address: The address for which to fetch the coin balance history.
        :param dict params: Additional parameters for the request.
        :returns: A tuple containing a response object with the coin balance history and the next page parameters.
        """
        response = self.get(f"{address}/coin-balance-history", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_coin_balance_history_by_day(self, address: str) -> BaseResponse:
        """
        Fetch daily PLS balance history for a specific address.

        :param str address: The address for which to fetch the daily balance history.
        :returns: A response object containing the daily balance history.
        :rtype: BaseResponse
        """
        response = self.get(f"{address}/coin-balance-history-by-day")
        return BaseResponse(items=response["items"])

    @paginated
    def get_withdrawals(self, address: str, params: dict) -> tuple[BaseResponse, dict]:
        """
        Fetch withdrawals for a specific address.

        :param str address: The address for which to fetch withdrawals.
        :param dict params: Additional parameters for the request.
        :returns: A list of dictionaries containing withdrawal information.
        """
        response = self.get(f"{address}/withdrawals", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_nfts(self, address: str, params: dict) -> tuple[BaseResponse, dict]:
        """
        Fetch NFTs for a specific address.

        :param str address: The address for which to fetch NFTs.
        :param dict params: Additional parameters for the request.
        :returns: A list of dictionaries containing NFTs related to the address.
        """
        response = self.get(f"{address}/nft", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_nft_collections(
        self, address: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Fetch NFT collections for a specific address.

        :param str address: The address for which to fetch NFT collections.
        :param dict params: Additional parameters for the request.
        :returns: A list of dictionaries containing NFT collections related to the address.
        """
        response = self.get(f"{address}/nft/collections", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]
