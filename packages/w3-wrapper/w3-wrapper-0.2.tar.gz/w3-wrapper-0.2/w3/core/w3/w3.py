import logging

from pydantic import validate_call, Field
from web3 import AsyncWeb3, AsyncHTTPProvider

from ..async_mixin import AsyncMixin
from ..network import Network
from ...utils.exceptions import RPCException
from ...utils.regex import PROXY_REGEX


logger = logging.getLogger(__name__)

class W3(AsyncMixin):

    @validate_call
    async def __ainit__(
            self,
            network: Network,
            proxy: str = Field(pattern=PROXY_REGEX)
    ):
        logger.debug("Initializing W3 with network: %s and proxy: %s", network, proxy)
        async_w3: AsyncWeb3 = AsyncWeb3(
            AsyncHTTPProvider(
                endpoint_uri=network.rpc,
                request_kwargs={"proxy": proxy},
            )
        )
        is_connected = await async_w3.is_connected()
        if is_connected:
            self.async_w3: AsyncWeb3 = async_w3
            self.network: Network = network
            self.proxy: str = proxy
            logger.debug("W3 connected to network: %s", network)
        else:
            logger.error("RPC %s not working", network.rpc)
            raise RPCException(f'RPC {network.rpc} not working')
