"""
Client for the PulseChain API.

This module provides the main `Client` class for interacting with
various subclients of the PulseChain API, such as stats, addresses,
transactions, tokens, blocks, search, and smart contracts.
"""

from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.addresses import AddressesClient
from pulsechain.subclients.blocks import BlocksClient
from pulsechain.subclients.search import SearchClient
from pulsechain.subclients.smart_contracts import SmartContractsClient
from pulsechain.subclients.stats import StatsClient
from pulsechain.subclients.tokens import TokensClient
from pulsechain.subclients.transactions import TransactionsClient


class Client:
    """
    Main client for interacting with the PulseChain API.

    This class provides access to multiple subclients, each of which is responsible for
    interacting with specific sections of the PulseChain API. It also provides methods
    to interact with generic API endpoints that do not belong to any subclient.

    Attributes:
        request_handler (APIRequestHandler): The handler for making HTTP requests.
        stats (StatsClient): Client for interacting with stats-related endpoints.
        addresses (AddressesClient): Client for interacting with address-related endpoints.
        transactions (TransactionsClient): Client for interacting with transactions.
        tokens (TokensClient): Client for interacting with tokens.
        blocks (BlocksClient): Client for interacting with blocks.
        search (SearchClient): Client for performing search operations.
        smart_contracts (SmartContractsClient): Client for interacting with smart contracts.
    """

    BASE_URL = "https://api.scan.pulsechain.com/api/v2"

    def __init__(self):
        """Initialize the client with its subclients and the request handler."""
        self.request_handler = APIRequestHandler(self.BASE_URL)
        self.stats = StatsClient(self.request_handler)
        self.addresses = AddressesClient(self.request_handler)
        self.transactions = TransactionsClient(self.request_handler)
        self.tokens = TokensClient(self.request_handler)
        self.blocks = BlocksClient(self.request_handler)
        self.search = SearchClient(self.request_handler)
        self.smart_contracts = SmartContractsClient(self.request_handler)

    def get_withdrawals(self, params: dict | None = None) -> dict:
        """
        Fetch withdrawal information.

        Sends a GET request to the 'withdrawals' endpoint to retrieve information about
        withdrawals on the PulseChain network.

        :param params: Optional query parameters for the request.
        :return: The API response as a dictionary.
        """
        return self.request_handler.get("withdrawals", params=params)

    def get_json_rpc_url(self) -> dict:
        """
        Fetch the JSON-RPC URL.

        Sends a GET request to the 'config/json-rpc-url' endpoint to retrieve the current
        JSON-RPC URL of the PulseChain network.

        :return: The API response containing the JSON-RPC URL.
        """
        return self.request_handler.get("config/json-rpc-url")
