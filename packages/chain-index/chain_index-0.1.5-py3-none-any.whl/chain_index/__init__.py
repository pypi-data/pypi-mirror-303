from .core import get_chain_info, ChainInfo
from .exceptions import ChainNotFoundError

__all__ = ["get_chain_info", "ChainInfo", "ChainNotFoundError"]

__version__ = '0.1.5'
__author__ = 'gmatrix'
__license__ = 'MIT'

__doc__ = """
Chain Index is a Python package for retrieving information about blockchain networks.

It provides easy access to details such as native currencies, RPC URLs, and more for various chains.
The package supports querying by chain ID, name, or alias, and includes robust error handling.

Quick example:
    from chain_index import get_chain_info, ChainNotFoundError

    try:
        ethereum = get_chain_info(1)
        print(f"Ethereum native currency: {ethereum.nativeCurrency.symbol}")

        polygon = get_chain_info("Polygon Mainnet")
        print(f"Polygon chain ID: {polygon.chainId}")
    except ChainNotFoundError as e:
        print(f"Error: {e}")

For more information, visit: https://github.com/gmatrixuniverse/chain-index
"""
