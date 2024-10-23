from dataclasses import dataclass

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from mach_client import Chain, Token
from mach_client.client import GasEstimate, Order, Quote
from web3.contract.async_contract import AsyncContractFunction

from .destination_policy import DestinationPolicy
from .risk_manager import RiskAnalysis


@dataclass
class EmptySourceBalance:
    token: Token
    wallet: ChecksumAddress


@dataclass
class NoViableDestination:
    destination_policy: DestinationPolicy


@dataclass
class GasEstimateFailed:
    chain: Chain
    exception: Exception


@dataclass
class InsufficientDestinationGas:
    destination: Token
    gas_estimate: GasEstimate
    gas_available: int


@dataclass
class QuoteFailed:
    pair: tuple[Token, Token]
    amount: int
    wallet: ChecksumAddress
    exception: Exception


@dataclass
class QuoteInvalidAmount:
    pair: tuple[Token, Token]
    amount: int
    wallet: ChecksumAddress
    quote: Quote


@dataclass
class QuoteLiquidityUnavailable:
    pair: tuple[Token, Token]
    amount: int
    wallet: ChecksumAddress
    quote: Quote


@dataclass
class RiskManagerRejection:
    pair: tuple[Token, Token]
    amount: int
    quote: Quote
    risk_analysis: RiskAnalysis


@dataclass
class CannotFill:
    pair: tuple[Token, Token]
    amount: int
    quote: Quote


@dataclass
class ApprovalFailed:
    token: Token
    amount: int
    wallet: ChecksumAddress
    spender: ChecksumAddress
    exception: Exception


@dataclass
class PlaceOrderFailed:
    pair: tuple[Token, Token]
    wallet: ChecksumAddress
    place_order_function: AsyncContractFunction
    exception: Exception


@dataclass
class SubmitOrderFailed:
    pair: tuple[Token, Token]
    place_order_tx: HexBytes
    exception: Exception


@dataclass
class SourceNotWithdrawn:
    pair: tuple[Token, Token]
    order: Order
    wait_time: int


@dataclass
class DestinationNotReceived:
    pair: tuple[Token, Token]
    order: Order
    wait_time: int


TradeError = (
    EmptySourceBalance
    | NoViableDestination
    | GasEstimateFailed
    | InsufficientDestinationGas
    | QuoteFailed
    | QuoteInvalidAmount
    | QuoteLiquidityUnavailable
    | RiskManagerRejection
    | CannotFill
    | ApprovalFailed
    | PlaceOrderFailed
    | SubmitOrderFailed
    | SourceNotWithdrawn
    | DestinationNotReceived
)


@dataclass
class Trade:
    pair: tuple[Token, Token]
    quote: Quote
    order: Order


MachEvent = Trade | TradeError
