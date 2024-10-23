from eth_typing import ChecksumAddress
from web3 import Web3


def to_checksum_address(address: str) -> ChecksumAddress:
    return Web3().to_checksum_address(address)