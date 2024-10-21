from .core import get_chain_info, ChainInfo
from .exceptions import ChainNotFoundError

__all__ = ["get_chain_info", "ChainInfo", "ChainNotFoundError"]

__version__ = '0.1.0'
__author__ = 'gmatrix'
__license__ = 'MIT'

# You can add a brief description of the package
__doc__ = """
chainindex is a Python package for retrieving information about blockchain networks.
It provides easy access to details such as native currencies, RPC URLs, and more for various chains.
"""
