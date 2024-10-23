from web3 import types
from web3.contract import AsyncContract

Contract = str | types.Address | types.ChecksumAddress | AsyncContract
