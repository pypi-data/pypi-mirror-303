import logging

from eth_account.datastructures import SignedTransaction
from eth_account.messages import encode_defunct
from eth_typing import ChecksumAddress
from pydantic import BaseModel, Field, ConfigDict
from web3.contract import AsyncContract

from ..contract import Contracts
from ..token_amount import TokenAmount
from ..w3 import W3
from ...utils.regex import PRIVATE_KEY_REGEX, ADDRESS_REGEX
from ...utils.types import Contract


logger = logging.getLogger(__name__)

class Wallet(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    private_key: str = Field(pattern=PRIVATE_KEY_REGEX)
    public_key: ChecksumAddress = Field(pattern=ADDRESS_REGEX)
    _w3: W3
    _contracts: Contracts

    def __init__(self, private_key: str, public_key: ChecksumAddress, w3: W3, contracts: Contracts):
        super().__init__(
            private_key=private_key,
            public_key=public_key,
        )
        self._w3 = w3
        self._contracts = contracts

    #todo реализовать transfer

    def sign_message(self, message: str) -> str:
        logger.debug("Signing message: %s", message)
        message_encoded = encode_defunct(text=message)
        signed_message = self._w3.async_w3.eth.account.sign_message(message_encoded, private_key=self.private_key)
        signature = signed_message.signature.hex()
        logger.debug("Message signed. Signature: %s", signature)
        return signature

    def sign_transaction(self, tx: dict) -> SignedTransaction:
        logger.debug("Signing transaction: %s", tx)
        signed_tx = self._w3.async_w3.eth.account.sign_transaction(tx, private_key=self.private_key)
        logger.debug("Transaction signed. SignedTransaction: %s", signed_tx)
        return signed_tx

    async def get_nonce(self) -> int:
        logger.debug("Getting nonce for public_key: %s", self.public_key)
        nonce = await self._w3.async_w3.eth.get_transaction_count(self.public_key)
        logger.debug("Nonce obtained: %d", nonce)
        return nonce

    async def get_balance(self, token: Contract = None) -> TokenAmount:
        if token is None:
            return TokenAmount(
                await self._w3.async_w3.eth.get_balance(
                    account=self.public_key
                ),
                18
            )
        token_address = self._w3.async_w3.to_checksum_address(token)
        if isinstance(token, AsyncContract):
            token_address = token.address

        contract = self._contracts.get_erc20_contract(token_address)
        return TokenAmount(
            int(await contract.functions.balanceOf(self.public_key).call()),
            int(await contract.functions.decimals().call())
        )
