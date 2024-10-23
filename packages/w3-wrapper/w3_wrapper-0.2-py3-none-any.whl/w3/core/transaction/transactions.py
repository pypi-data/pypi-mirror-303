import logging

from eth_account.datastructures import SignedTransaction
from eth_typing import HexStr, ChecksumAddress
from hexbytes import HexBytes
from pydantic import validate_call
from web3.exceptions import Web3Exception
from web3.types import TxReceipt

from ..gas_strategy import OldGasStrategy, EIP1559GasStrategy, GasStrategy
from ..w3 import W3
from ..wallet import Wallet
from ...utils.exceptions import TransactionFailedException, InsufficientFundsException, \
    ReplacementTransactionUnderpricedException


logger = logging.getLogger(__name__)

class Transactions:
    def __init__(self, w3: W3, wallet: Wallet) -> None:
        self._w3: W3 = w3
        self._wallet: Wallet = wallet
        if self._w3.network.tx_type == 0:
            self._gas_strategy: GasStrategy = OldGasStrategy(self._w3)
            logger.debug("Using OldGasStrategy for gas calculation.")
        else:
            self._gas_strategy: GasStrategy = EIP1559GasStrategy(self._w3)
            logger.debug("Using EIP1559GasStrategy for gas calculation.")

    async def _create_transaction(
            self,
            contract_address: ChecksumAddress | None,
            encoded_data: HexStr,
            value: int,
    ) -> dict:
        logger.debug("Creating transaction with contract_address: %s, encoded_data: %s, value: %d", contract_address, encoded_data, value)
        gas_dict = await self._gas_strategy.calculate_gas()
        tx = {
            'chainId': self._w3.network.chain_id,
            'nonce': await self._wallet.get_nonce(),
            'from': self._wallet.public_key,
            'data': encoded_data,
            'value': value,
        }
        if contract_address:
            tx['to'] = contract_address
        tx.update(gas_dict)
        return tx

    async def _estimate_gas(self, tx: dict) -> dict:
        tx_copy = tx.copy()
        tx_copy['gas'] = await self._w3.async_w3.eth.estimate_gas(tx_copy)
        logger.debug("Estimated gas: %s", tx_copy['gas'])
        return tx_copy

    async def _wait_for_receipt(self, tx_hash) -> TxReceipt:
        logger.debug("Waiting for transaction receipt for tx_hash: %s", tx_hash.hex())
        tx_receipt = await self._w3.async_w3.eth.wait_for_transaction_receipt(tx_hash, 300)
        logger.debug("Transaction receipt received: %s", tx_receipt)
        return tx_receipt

    async def _send_raw_transaction(self, tx: SignedTransaction) -> HexBytes:
        logger.debug("Sending raw transaction: %s", tx.raw_transaction.hex())
        tx_hash = await self._w3.async_w3.eth.send_raw_transaction(tx.raw_transaction)
        logger.debug("Transaction sent with hash: %s", tx_hash.hex())
        return tx_hash

    @validate_call
    async def send(
            self,
            encoded_data: HexStr,
            contract_address: ChecksumAddress | None = None,
            tx_value: int = 0,
            retry_count: int = 5,
    ) -> TxReceipt:
        """
        Отправляет транзакцию в сеть, добавляя доп параметры (nonce и тд) и рассчитывая газ, а после ожидает ее выполнения.

        Args:
            encoded_data (HexStr): Данные транзакции (например, вызов функции или байт-код контракта).
            contract_address (ChecksumAddress | None): Адрес назначения. Если None, транзакция рассматривается как создание контракта.
            tx_value (int): Кол-во в wei.
            retry_count (int): Количество попыток отправки транзакции в случае неудачи.

        Returns:
            TxReceipt: Receipt подтверждающей транзакции.
        """
        logger.debug("Sending transaction with encoded_data: %s, contract_address: %s, tx_value: %d, retry_count: %d",
                    encoded_data, contract_address, tx_value, retry_count)
        tx = await self._create_transaction(
            contract_address=contract_address,
            encoded_data=encoded_data,
            value=tx_value,
        )
        for attempt in range(1, retry_count + 1):
            try:
                logger.debug("Attempt %d to send transaction.", attempt)
                tx = await self._estimate_gas(tx)
                signed_tx: SignedTransaction = self._wallet.sign_transaction(tx)
                tx_hash: HexBytes = await self._send_raw_transaction(signed_tx)
                res = await self._wait_for_receipt(tx_hash)

                if res.get('status') == 1:
                    logger.info("Transaction successful with receipt: %s", res)
                    return res
                else:
                    logger.error("Transaction failed with receipt: %s", res)
                    raise TransactionFailedException(f"Transaction failed with receipt: {res}")
            except Web3Exception as e:
                error_message = str(e)
                logger.warning("Web3Exception occurred: %s", error_message)

                if 'insufficient funds' in error_message:
                    logger.error("Insufficient funds for transaction.")
                    raise InsufficientFundsException(
                        f"Insufficient funds to complete the transaction: {error_message}"
                    )

                elif 'replacement transaction underpriced' in error_message:
                    if attempt == retry_count:
                        logger.error("Replacement transaction underpriced after %d attempts.", attempt)
                        raise ReplacementTransactionUnderpricedException(
                            f"Replacement transaction underpriced after {attempt} attempts."
                        )

                    gas_increase_factor = 1 + (5 + attempt) / 100
                    if 'gasPrice' in tx:
                        tx['gasPrice'] = int(tx['gasPrice'] * gas_increase_factor)
                    else:
                        # for EIP-1559
                        tx['maxFeePerGas'] = int(tx['maxFeePerGas'] * gas_increase_factor)
                        tx['maxPriorityFeePerGas'] = int(tx['maxPriorityFeePerGas'] * gas_increase_factor)
                    continue
                else:
                    if attempt == retry_count:
                        logger.error("Transaction failed with error: %s after %d attempts.", error_message, attempt)
                        raise TransactionFailedException(f"Transaction failed with receipt: {error_message} after {attempt} attempts")