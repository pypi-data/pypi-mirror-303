from __future__ import annotations

import logging

from ..async_mixin import AsyncMixin
from ..contract import Contracts
from ..network import Network
from ..transaction import Transactions
from ..w3 import W3
from ..wallet import Wallet


logger = logging.getLogger(__name__)

class Client(AsyncMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def __ainit__(self, private_key: str, network: Network, proxy: str) -> None:
        logger.debug("Initializing Client with network: %s and proxy: %s", network, proxy)
        self.w3 = await W3(
            network,
            proxy
        )

        self.contracts = Contracts(self)

        self.wallet = Wallet(
            private_key,
            self.w3.async_w3.eth.account.from_key(private_key).address,
            self.w3,
            self.contracts
        )
        self.transactions = Transactions(self.w3, self.wallet)

    async def switch_network(self, network: Network) -> Client:
        logger.debug("Switching network to: %s", network)
        return await Client(self.wallet.private_key, network, self.w3.proxy)

