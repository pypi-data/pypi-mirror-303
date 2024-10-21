# PulseChain Scanner API Client

## Overview
This project is a Python client for interacting with the PulseChain Scanner API. It provides a main `Client` class along with several subclients that focus on specific areas of the PulseChain API, such as addresses, blocks, transactions, tokens, and more. This comprehensive client is designed to make it easy to perform various operations on the PulseChain blockchain, such as fetching block information, interacting with smart contracts, and retrieving token-related data.

### Features
- Unified API client for the PulseChain ecosystem.
- Modular architecture with individual subclients for different API endpoints.
- Supports paginated responses for large datasets.
- Custom exception handling for better error management.
- Easy configuration and usage.

## Documentation
Full documentation is available at [Read the Docs](https://python-pulsechain.readthedocs.io/en/latest/).

## Installation
To use the PulseChain API client, you need Python 3.10 or higher. You can install the necessary dependencies by running:

```sh
pip install python-pulsechain
```

## Usage
### Initializing the Client
To begin interacting with the PulseChain API, you first need to instantiate the main Client class:

```python
from pulsechain.client import Client
client = Client()
```

The Client class provides easy access to multiple subclients:

* stats: For interacting with statistics endpoints.
* addresses: For interacting with addresses and related data.
* transactions: For handling transaction-related queries.
* tokens: For working with tokens and NFTs.
* blocks: For retrieving block details.
* search: For performing search operations.
* smart_contracts: For interacting with smart contracts.

### Example Usage
Below are some examples of how to use the client to perform common tasks.

Fetch General Statistics

```python
response = client.stats.get_stats()
print(response.items)
```
Get Information About an Address

```python
response = client.addresses.get_info("0x123...")
print(response.items)
```
Search for Tokens by Name

```python
response = client.tokens.get_tokens(name_query="PLS")
print(response.items)
```

Fetch Transactions for a Specific Block
```python
response = client.blocks.get_block_txns("1234567")
print(response.items)
```

## Paginated Responses
To support paginated responses, the response contains field next_page_params that can be used to fetch the next page of results.
It needs to be passed as a named paramter to functions that fetch paginated responses.

Example:
```python
response = client.blocks.get_block_txns("1234567")
print(response.items)
next_page = client.blocks.get_block_txns("1234567", next_page_params=response.next_page_params)
```

## Custom Error Handling
This client raises custom exceptions defined in exceptions.py to make error handling more intuitive:

* PulseChainAPIException: Generic API error.
* PulseChainTimeoutException: Raised when a request to the API times out.
* PulseChainServerError: Raised when the API returns an internal server error (500).
* PulseChainBadRequestException: Raised when the client makes an invalid request (400).
* PulseChainUnprocessableEntityException: Raised when the server cannot process the request (422).

Example:
```python
try:
    stats = client.stats.get_stats()
except PulseChainAPIException as e:
    print(f"An error occurred: {e}")
```

## License
This project is licensed under the GPL-3.0 License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests to enhance the client.

## Contact
For questions or support, please open an issue on the repository or reach out to the maintainers.

## Support
If you find this project helpful and would like to support its development, consider sending PLS to the following address:
```sh
0xaC6f36D3B4B8aEA37D0B1363d35cb8D024deF1BC
```

