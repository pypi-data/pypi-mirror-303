from typing import Literal

from pydantic import BaseModel, Field

from ...utils.regex import RPC_REGEX, COIN_SYMBOL_REGEX


class Network(BaseModel):
    name: str = Field(min_length=1)
    rpc: str = Field(pattern=RPC_REGEX)
    chain_id: int = Field(gt=0)
    tx_type: Literal[0, 2]

    def __init__(self, name: str, rpc: str, chain_id: int, tx_type: Literal[0, 2]):
        super().__init__(
            name=name,
            rpc=rpc,
            chain_id=chain_id,
            tx_type=tx_type
        )
