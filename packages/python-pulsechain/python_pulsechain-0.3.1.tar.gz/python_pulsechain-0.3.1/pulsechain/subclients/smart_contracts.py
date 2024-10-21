"""
This module provides the `SmartContractsClient` class, which interacts with the 'smart-contracts'
subpath of the PulseChain API.

The `SmartContractsClient` class provides methods to retrieve information about smart contracts,
including contract details, counters, and available read and write methods. It uses the
`APIRequestHandler` for making HTTP requests.
"""
from pulsechain.models import BaseResponse
from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.subpath_client import SubpathClient
from pulsechain.utils import paginated
from pulsechain.validators import validate_contract_filters


class SmartContractsClient(SubpathClient):
    """
    Client for interacting with the 'smart-contracts' subpath of the PulseChain API.

    The `SmartContractsClient` provides methods to interact with smart contract data,
    including retrieving contract counters, information, and the available read and write methods
    for verified smart contracts.

    :ivar request_handler: The handler for making HTTP requests.
    """

    def __init__(self, request_handler: APIRequestHandler):
        """
        Initialize the SmartContractsClient with the subpath 'smart-contracts'.

        :param request_handler: The handler for making HTTP requests.
        """
        super().__init__(subpath="smart-contracts", request_handler=request_handler)

    @paginated
    def get_smart_contracts(
        self, query: str, contract_filters: list[str] | None = None
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve a list of smart contracts based on a search query.

        :param query: The search query to filter smart contracts.
        :param contract_filters: A list of filters to apply to the contracts. Defaults to None.

        :return: A tuple containing the response object with smart contract details
                 and pagination information for the next page.
        """
        params = {"q": query}
        if contract_filters:
            params["filter"] = validate_contract_filters(contract_filters)

        response = self.get(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_info(self, address: str) -> BaseResponse:
        """
        Retrieve detailed information about a specific smart contract.

        :param address: The address of the smart contract.

        :return: A response object containing smart contract information.
        """
        response = self.get(address)
        return BaseResponse(items=[response])

    def get_counters(self) -> BaseResponse:
        """
        Retrieve counters for verified smart contracts.

        :return: A response object containing smart contracts counters.
        """
        response = self.get("counters")
        return BaseResponse(items=[response])

    def _get_methods(
        self, address: str, method_type: str, from_addr: str | None, is_custom_abi: bool
    ) -> BaseResponse:
        """
        Retrieve methods of a specific type for a smart contract.

        :param address: The address of the smart contract.
        :param method_type: The type of methods to retrieve ('read', 'write', 'read-proxy', or 'write-proxy').
        :param from_addr: The address to use for method invocation. Defaults to None.
        :param is_custom_abi: Whether to use a custom ABI. Defaults to False.

        :return: A response object containing smart contract methods.
        """
        params = {
            "is_custom_abi": "true" if is_custom_abi else "false",
        }
        if from_addr:
            params["from"] = from_addr
        response = self.get(f"{address}/methods-{method_type}", params)
        return BaseResponse(items=response["items"])

    def get_read_methods(
        self,
        address: str,
        from_addr: str | None = None,
        is_custom_abi: bool = False,
    ) -> BaseResponse:
        """
        Retrieve read methods for a smart contract.

        :param address: The address of the smart contract.
        :param from_addr: The address to use for method invocation. Defaults to None.
        :param is_custom_abi: Whether to use a custom ABI. Defaults to False.

        :return: A response object containing smart contract read methods.
        """
        return self._get_methods(address, "read", from_addr, is_custom_abi)

    def get_read_methods_proxy(
        self, address: str, from_addr: str | None = None, is_custom_abi: bool = False
    ) -> BaseResponse:
        """
        Retrieve read methods for a proxy smart contract.

        :param address: The address of the smart contract.
        :param from_addr: The address to use for method invocation. Defaults to None.
        :param is_custom_abi: Whether to use a custom ABI. Defaults to False.

        :return: A response object containing smart contract read methods for proxies.
        """
        return self._get_methods(address, "read-proxy", from_addr, is_custom_abi)

    def get_write_methods(
        self, address: str, from_addr: str | None = None, is_custom_abi: bool = False
    ) -> BaseResponse:
        """
        Retrieve write methods for a smart contract.

        :param address: The address of the smart contract.
        :param from_addr: The address to use for method invocation. Defaults to None.
        :param is_custom_abi: Whether to use a custom ABI. Defaults to False.

        :return: A response object containing smart contract write methods.
        """
        return self._get_methods(address, "write", from_addr, is_custom_abi)

    def get_write_methods_proxy(
        self,
        address: str,
        from_addr: str | None = None,
        is_custom_abi: bool = False,
    ) -> BaseResponse:
        """
        Retrieve write methods for a proxy smart contract.

        :param address: The address of the smart contract.
        :param from_addr: The address to use for method invocation. Defaults to None.
        :param is_custom_abi: Whether to use a custom ABI. Defaults to False.

        :return: A response object containing smart contract write methods for proxies.
        """
        return self._get_methods(address, "write-proxy", from_addr, is_custom_abi)
