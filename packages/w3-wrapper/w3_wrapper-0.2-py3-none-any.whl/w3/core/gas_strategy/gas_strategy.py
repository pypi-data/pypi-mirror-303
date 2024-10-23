from abc import abstractmethod

from ..w3 import W3


class GasStrategy:
    def __init__(self, w3: W3):
        self._w3: W3 = w3

    @abstractmethod
    async def calculate_gas(self) -> dict:
        pass
