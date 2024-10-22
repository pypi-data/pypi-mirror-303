import abc
from abc import ABC
from decimal import Decimal
import typing

from mach_client import Token


class AmountPolicy(ABC):
    @abc.abstractmethod
    def __call__(self, src_token: Token, dest_token: Token, src_balance: int) -> int:
        pass


# Used primarily when placing a single trade
class FixedAmountPolicy(AmountPolicy):
    def __init__(self, amount: int):
        self.amount = amount

    @typing.override
    def __call__(self, src_token: Token, dest_token: Token, src_balance: int) -> int:
        assert self.amount <= src_balance
        return self.amount


class FixedPercentagePolicy(AmountPolicy):
    def __init__(self, percentage: Decimal):
        self.percentage = Decimal(percentage)
        assert 0.0 <= percentage <= 1.0

    @typing.override
    def __call__(self, src_token: Token, dest_token: Token, src_balance: int) -> int:
        return int(src_balance * self.percentage)


max_amount_policy = FixedPercentagePolicy(Decimal(1.0))
