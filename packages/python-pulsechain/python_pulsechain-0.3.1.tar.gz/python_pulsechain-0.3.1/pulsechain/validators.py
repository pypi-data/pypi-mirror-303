"""
This module provides validation functions for various filters used in the PulseChain API.

Each validator function ensures that input values conform to the expected types and
formats required by the API, and raises `PulseChainBadParamException` for invalid inputs.
"""

from pulsechain.exceptions import PulseChainBadParamException


def validate_block_type(block_type: list[str]) -> str:
    """
    Validate the block type filter.

    :param block_type: A list of block types to validate. Valid options are 'block', 'uncle', or 'reorg'.
    :returns: A string of comma-separated block types if valid.
    :raises PulseChainBadParamException: If any `block_type` is not a valid type.
    """
    valid_block_types = {"block", "uncle", "reorg"}
    for b_type in block_type:
        if b_type not in valid_block_types:
            raise PulseChainBadParamException(
                "block_type must be one of 'block', 'uncle', or 'reorg'"
            )
    return ",".join(block_type)


def validate_txn_type(txn_type: list[str]) -> str:
    """
    Validate the transaction (txn) type filter.

    :param txn_type: A list of transaction types to validate. Valid options are:
                     'token_transfer', 'contract_creation', 'contract_call', 'coin_transfer', or 'token_creation'.
    :returns: A string of comma-separated transaction types if valid.
    :raises PulseChainBadParamException: If any `txn_type` is not a valid type.
    """
    valid_txn_types = {
        "token_transfer",
        "contract_creation",
        "contract_call",
        "coin_transfer",
        "token_creation",
    }
    for t_type in txn_type:
        if t_type not in valid_txn_types:
            raise PulseChainBadParamException(
                "txn_type must be one of 'token_transfer', 'contract_creation', 'contract_call', 'coin_transfer', "
                "or 'token_creation'"
            )
    return ",".join(txn_type)


def validate_txn_filter(txn_filter: list[str]) -> str:
    """
    Validate the transaction status filter.

    :param txn_filter: A list of transaction filters to validate. Valid options are 'pending' or 'validated'.
    :returns: A string of pipe-separated transaction filters if valid.
    :raises PulseChainBadParamException: If any `txn_filter` is not 'pending' or 'validated'.
    """
    valid_txn_filters = {"pending", "validated"}
    for t_filter in txn_filter:
        if t_filter not in valid_txn_filters:
            raise PulseChainBadParamException(
                "txn_filter must be either 'pending' or 'validated'"
            )
    return " | ".join(txn_filter)


def validate_address_txn_filter(txn_filter: str) -> str:
    """
    Validate the address transaction filter.

    :param txn_filter: The transaction filter to validate. Valid options are 'to' or 'from'.
    :returns: The validated transaction filter.
    :raises PulseChainBadParamException: If `txn_filter` is not 'to' or 'from'.
    """
    if txn_filter not in {"to", "from"}:
        raise PulseChainBadParamException("txn_filter must be either 'to' or 'from'")
    return txn_filter


def validate_method(method: list[str]) -> str:
    """
    Validate the method filter.

    :param method: A list of methods to validate. Valid options are 'approve', 'transfer',
                   'multicall', 'mint', or 'commit'.
    :returns: A string of comma-separated methods if valid.
    :raises PulseChainBadParamException: If any `method` is not 'approve', 'transfer', 'multicall', 'mint', or 'commit'.
    """
    valid_methods = {"approve", "transfer", "multicall", "mint", "commit"}
    for m in method:
        if m not in valid_methods:
            raise PulseChainBadParamException(
                "method must be either 'approve', 'transfer', 'multicall', 'mint', or 'commit'"
            )
    return ",".join(method)


def validate_token_type(token_type: list[str]) -> str:
    """
    Validate the token type filter.

    :param token_type: A list of token types to validate. Valid options are 'ERC-20', 'ERC-721', or 'ERC-1155'.
    :returns: A string of comma-separated token types if valid.
    :raises PulseChainBadParamException: If any `token_type` is not a valid type.
    """
    valid_token_types = {"ERC-20", "ERC-721", "ERC-1155"}
    for t_type in token_type:
        if t_type not in valid_token_types:
            raise PulseChainBadParamException(
                "token_type must be one of 'ERC-20', 'ERC-721', or 'ERC-1155'"
            )
    return ",".join(token_type)


def validate_contract_filters(contract_filters: list[str]) -> str:
    """
    Validate the smart contract type filter.

    :param contract_filters: A list of token types to validate.
           Valid options are 'vyper', 'solidity', or 'yul'.
    :returns: A string of comma-separated smart contract filters if valid.
    :raises PulseChainBadParamException: If any of `contract_filters` is not a valid type.
    """
    valid_contract_filters = {"vyper", "solidity", "yul"}
    for contract_filter in contract_filters:
        if contract_filter not in valid_contract_filters:
            raise PulseChainBadParamException(
                "contract_filter must be one of 'vyper', 'solidity' or 'yul'"
            )
    return " | ".join(contract_filters)
