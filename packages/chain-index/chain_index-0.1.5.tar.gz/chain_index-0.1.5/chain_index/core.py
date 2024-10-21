import json
from pathlib import Path
import logging
from typing import Union, Optional
from pydantic import BaseModel, Field
from .exceptions import ChainNotFoundError
import numpy as np

logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG level
logger = logging.getLogger(__name__)

class NativeCurrency(BaseModel):
    name: str
    symbol: str
    decimals: int

class WrapperNativeCurrency(BaseModel):
    name: str
    symbol: str
    decimals: int
    contract: str

class Explorer(BaseModel):
    name: str
    url: str
    standard: Optional[str] = None

class ChainInfo(BaseModel):
    name: str
    chain: Optional[str] = None
    chainId: int
    networkId: Optional[int] = None
    rpc: list[str] = []
    faucets: list[str] = []
    nativeCurrency: NativeCurrency
    wrapperNativeCurrency: Optional[WrapperNativeCurrency] = None
    infoURL: Optional[str] = None
    shortName: str
    icon: Optional[str] = None
    explorers: Optional[list[Explorer]] = None
    ens: Optional[dict] = None
    slip44: Optional[int] = None

def load_chains():
    json_path = Path(__file__).parent / 'data' / 'chains.json'
    with open(json_path, 'r') as f:
        return json.load(f)

CHAINS = load_chains()

def get_chain_info(chain_identifier: Union[int, str]) -> ChainInfo:
    # logger.debug(f"Searching for chain: {chain_identifier}")
    for chain in CHAINS:
        if isinstance(chain_identifier, (int, np.integer)):
            if chain_identifier == chain['chainId']:
                # logger.debug(f"Found chain by ID: {chain_identifier}")
                return ChainInfo(**chain)
        elif isinstance(chain_identifier, str):
            if (chain_identifier.lower() == chain['name'].lower() or
                chain_identifier.lower() in [alias.lower() for alias in chain.get('alias', [])] or
                chain_identifier.lower() == chain.get('shortName', '').lower()):
                # logger.debug(f"Found chain by name or alias: {chain_identifier}")
                return ChainInfo(**chain)
            try:
                if int(chain_identifier) == chain['chainId']:
                    # logger.debug(f"Found chain by ID (string): {chain_identifier}")
                    return ChainInfo(**chain)
            except ValueError:
                pass
    # logger.debug(f"Chain not found: {chain_identifier}")
    raise ChainNotFoundError(f"Chain not found: {chain_identifier}")
