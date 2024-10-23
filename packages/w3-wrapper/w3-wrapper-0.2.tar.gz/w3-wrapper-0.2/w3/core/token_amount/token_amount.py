from pydantic import BaseModel, Field


class TokenAmount(BaseModel):
    amount: int = Field(gt=-1)
    decimals: int = Field(gt=0)

    def __init__(self, amount: int, decimals: int):
        super().__init__(amount=amount, decimals=decimals)

    def get_converted_amount(self) -> float:
        return self.amount / 10 ** self.decimals
