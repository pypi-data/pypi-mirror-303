from dataclasses import dataclass
from decimal import Decimal

from mach_client import Token

from .rebalance_manager import RebalanceAnalysis


@dataclass
class RebalanceEvaluation:
    rebalance_analysis: RebalanceAnalysis


@dataclass
class Withdraw:
    amounts: list[tuple[Token, Decimal]]


@dataclass
class Supply:
    amounts: list[tuple[Token, Decimal]]


@dataclass
class LiquidityRateError:
    tokens: list[Token]
    exception: Exception


@dataclass
class WithdrawError:
    token: Token
    amount: Decimal
    exception: Exception


@dataclass
class ConvertError:
    src_token: Token
    error: object


@dataclass
class SupplyError:
    token: Token
    amount: Decimal
    exception: Exception


AaveError = LiquidityRateError | WithdrawError | ConvertError | SupplyError

AaveEvent = RebalanceEvaluation | Withdraw | Supply | AaveError
