from abc import ABC, abstractmethod
import dataclasses
from decimal import Decimal
import typing

from mach_client import Token

from .. import config
from ..log import LogContextAdapter, Logger


@dataclasses.dataclass(kw_only=True)
class RebalanceAnalysis:
    rebalance: bool


class RebalanceManager(ABC):
    def __init__(self, log: Logger):
        self.log = log

    @abstractmethod
    def __call__(
        self,
        token_rates: dict[Token, Decimal],
        portfolio_balances: list[tuple[Token, Decimal]]
    ) -> RebalanceAnalysis:
        pass


class ProfitableRebalanceManager(RebalanceManager):
    def __init__(self, log: Logger):
        super().__init__(LogContextAdapter(log, "Profitable Rebalance Manager"))

    @dataclasses.dataclass(kw_only=True)
    class RebalanceAnalysis(RebalanceAnalysis):
        token_rates: dict[Token, Decimal]
        portfolio_interest_rate: Decimal
        portfolio_balances: list[tuple[Token, Decimal]]

    @typing.override
    def __call__(
        self,
        token_rates: dict[Token, Decimal],
        portfolio_balances: list[tuple[Token, Decimal]]
    ) -> RebalanceAnalysis:
        self.log.info("Checking for rebalance")

        portfolio_balance = sum(
            map(lambda balance: balance[1], portfolio_balances))

        portfolio_interest_rate = sum(
            balance * token_rates[token] / portfolio_balance
            for token, balance in portfolio_balances
        )

        self.log.info(f"Portfolio interest rate: {portfolio_interest_rate}")

        highest_rate = next(iter(token_rates.values()))

        return self.RebalanceAnalysis(
            rebalance=highest_rate - portfolio_interest_rate > config.aave_rebalance_threshold,
            token_rates=token_rates,
            portfolio_interest_rate=Decimal(portfolio_interest_rate),
            portfolio_balances=portfolio_balances,
        )

class FrequentRebalanceManager(RebalanceManager):
    def __init__(self, log: Logger):
        super().__init__(LogContextAdapter(log, "Frequent Rebalance Manager"))

    @dataclasses.dataclass(kw_only=True)
    class RebalanceAnalysis(RebalanceAnalysis):
        token_rates: dict[Token, Decimal]
        portfolio_balances: list[tuple[Token, Decimal]]

    @typing.override
    def __call__(
        self,
        token_rates: dict[Token, Decimal],
        portfolio_balances: list[tuple[Token, Decimal]]
    ) -> RebalanceAnalysis:
        self.log.info("Checking for rebalance")

        return self.RebalanceAnalysis(
            rebalance=True,
            token_rates=token_rates,
            portfolio_balances=portfolio_balances,
        )
