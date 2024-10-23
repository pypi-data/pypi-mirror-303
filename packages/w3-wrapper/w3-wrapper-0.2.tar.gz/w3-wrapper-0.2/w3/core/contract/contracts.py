import json
import logging

from eth_typing import ChecksumAddress, HexStr
from pydantic import BaseModel, ConfigDict, Field, validate_call
from web3.contract import AsyncContract

from ...utils.regex import ADDRESS_REGEX

erc20_abi = '[ { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "balance", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" }, { "name": "_spender", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "payable": true, "stateMutability": "payable", "type": "fallback" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "owner", "type": "address" }, { "indexed": true, "name": "spender", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" } ]'

logger = logging.getLogger(__name__)

class Contracts(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    _default_token_abi: list[object]
    _client: 'Client'

    def __init__(self, client: 'Client'):
        super().__init__()
        self._client = client
        self._default_token_abi = json.loads(erc20_abi)

    @validate_call
    def get_contract(self, abi: list, contract_address: ChecksumAddress = Field(pattern=ADDRESS_REGEX)) -> AsyncContract:
        return self._client.w3.async_w3.eth.contract(abi=abi, address=contract_address)

    @validate_call
    def get_erc20_contract(self, contract_address: ChecksumAddress = Field(pattern=ADDRESS_REGEX)) -> AsyncContract:
        return self._client.w3.async_w3.eth.contract(abi=self._default_token_abi, address=contract_address)

    @validate_call
    async def deploy(
            self,
            bytecode: HexStr,
            abi: list = None,
            constructor_args: list | None = None,
    ) -> AsyncContract | ChecksumAddress:
        logger.debug("Deploying contract")
        temp_contract = self._client.w3.async_w3.eth.contract(bytecode=bytecode, abi=abi) if abi else self._client.w3.async_w3.eth.contract(bytecode=bytecode)

        if abi and any(item["type"] == "constructor" for item in abi):
            constructor = temp_contract.constructor(
                *constructor_args) if constructor_args else temp_contract.constructor()
            encoded_data = constructor.data_in_transaction
        else:
            encoded_data = temp_contract.bytecode

        receipt = await self._client.transactions.send(
            encoded_data=encoded_data
        )

        if receipt.contractAddress is None:
            logger.error("Failed to get contract address after deployment.")
            raise Exception("It wasn't possible to get the address of the contract after deploy.")
        if abi:
            return self._client.contracts.get_contract(contract_address=receipt.contractAddress, abi=abi)
        else:
            return receipt

