from abc import abstractmethod, ABC


class AsyncMixin(ABC):
    """
            use with await\n
            don't override __init__ method, override __ainit__ instead
            Example:
                class Wallet(AsyncMixin):
                    async def __ainit__(self, *args, **kwargs):
                        ...your code goes here.

                wallet = await Wallet(*your_args)
    """

    def __init__(self, *args, **kwargs):
        self.__storedargs = args, kwargs

    @abstractmethod
    async def __ainit__(self, *args, **kwargs) -> None:
        """Async constructor, you should implement this"""

    async def __initobj(self):
        await self.__ainit__(*self.__storedargs[0], **self.__storedargs[1])
        return self

    def __await__(self):
        return self.__initobj().__await__()
