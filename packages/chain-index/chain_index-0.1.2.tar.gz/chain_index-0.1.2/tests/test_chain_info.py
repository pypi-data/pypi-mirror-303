import pytest
import logging
from chain_index import get_chain_info, ChainInfo, ChainNotFoundError
from chain_index.core import CHAINS  # Import CHAINS to check for non-existent IDs

logger = logging.getLogger(__name__)

def test_get_chain_info_by_id():
    ethereum = get_chain_info(1)
    assert isinstance(ethereum, ChainInfo)
    assert ethereum.name == "Ethereum Mainnet"
    assert ethereum.chainId == 1
    assert ethereum.nativeCurrency.symbol == "ETH"

def test_get_chain_info_by_name():
    polygon = get_chain_info("Polygon Mainnet")
    assert isinstance(polygon, ChainInfo)
    assert polygon.chainId == 137
    assert polygon.nativeCurrency.symbol == "MATIC"

def test_get_chain_info_case_insensitive():
    bsc = get_chain_info("binance smart chain")
    assert isinstance(bsc, ChainInfo)
    assert bsc.chainId == 56

def test_chain_not_found():
    # Find a chain ID that doesn't exist
    non_existent_id = max(chain['chainId'] for chain in CHAINS) + 1
    
    logger.info(f"Testing non-existent chain ID: {non_existent_id}")
    with pytest.raises(ChainNotFoundError):
        get_chain_info(non_existent_id)

    logger.info("Testing non-existent chain name")
    with pytest.raises(ChainNotFoundError):
        get_chain_info("NonexistentChain")

def test_chain_info_attributes():
    ethereum = get_chain_info(1)
    expected_attributes = [
        'name', 'chain', 'chainId', 'networkId', 'rpc', 'faucets',
        'nativeCurrency', 'infoURL', 'shortName', 'explorers', 'icon'
    ]
    for attr in expected_attributes:
        assert hasattr(ethereum, attr)

def test_get_chain_by_short_name():
    ethereum = get_chain_info("eth")
    assert isinstance(ethereum, ChainInfo)
    assert ethereum.chainId == 1

def test_incomplete_chain_info():
    # Test a chain that might have incomplete information
    chain = get_chain_info(8217)  # Klaytn Mainnet Cypress
    assert isinstance(chain, ChainInfo)
    assert chain.name == "Klaytn Mainnet Cypress"
    assert chain.chainId == 8217
    assert chain.nativeCurrency.symbol == "KLAY"
