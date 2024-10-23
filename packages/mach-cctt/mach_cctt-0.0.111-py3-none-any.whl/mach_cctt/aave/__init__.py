import asyncio
from decimal import Decimal
import itertools
from pprint import pformat
from typing import AsyncGenerator, Sequence

from eth_account.signers.local import LocalAccount
from mach_client import ChainId, Token, client, utility

from .. import config, mach
from ..mach.destination_policy import TokenIteratorPolicy
from ..log import Logger
from ..mach.event import EmptySourceBalance, Trade
from . import atoken
from .event import *
from .rebalance_manager import RebalanceManager
from .supply import supply
from . import valid_tokens
from .withdraw import withdraw


scaling_factor = 10**27


async def get_liquidity_rate(token: Token) -> Decimal:
    asset_info = client.deployments[token.chain.id]["assets"][token.symbol]

    w3 = await utility.make_w3(token.chain)

    aave_pool_address = config.aave_pool_addresses[token.chain.id]
    pool_contract = w3.eth.contract(
        address=aave_pool_address,  # type: ignore
        abi=config.aave_pool_abi(token.chain.id),
    )

    reserve_data = await pool_contract.functions.getReserveData(
        asset_info["address"]
    ).call()

    return Decimal(reserve_data[2]) / scaling_factor


# Returned dict is ordered by liquidity rate, descending
async def get_liquidity_rates(
    tokens: Sequence[Token],
) -> dict[Token, Decimal]:
    liquidity_rates = await asyncio.gather(
        *(get_liquidity_rate(token) for token in tokens)
    )

    result = list(zip(tokens, liquidity_rates))
    result.sort(key=lambda x: x[1], reverse=True)

    return dict(result)


async def run(
    *,
    account: LocalAccount,
    rebalance_manager: RebalanceManager,
    # When rebalancing, if swapping to higher rate tokens fails, should we try swapping to a lower rate token or keep what we have?
    filter_lower_rate_tokens: bool,
    logger: Logger,
) -> AsyncGenerator[AaveEvent, None]:
    chains = client.chains - frozenset(
        (ChainId.AVALANCHE_C_CHAIN, ChainId.BSC, ChainId.POLYGON)
    )
    tokens = await valid_tokens.get_valid_aave_tokens(chains, config.aave_symbols)

    logger.info(f"Tokens:")
    logger.info(pformat(tokens))

    while True:

        # Inner loop determines when to rebalance portfolio
        while True:
            try:
                token_rates = await get_liquidity_rates(tokens)
            except Exception as e:
                logger.error(
                    "An exception was thrown while fetching liquidity rates from Aave:",
                    exc_info=e
                )
                yield LiquidityRateError(tokens, e)
                continue

            logger.info("Liquidity rates:")
            logger.info(pformat(token_rates))

            portfolio_balances = await asyncio.gather(*[
                atoken.get_token_balance(
                    token,
                    account.address
                )
                for token in tokens
            ])

            portfolio_balance_pairs = list(zip(tokens, portfolio_balances))

            logger.info("Portfolio balances:")
            logger.info(pformat(portfolio_balance_pairs))

            rebalance_analysis = rebalance_manager(
                token_rates, portfolio_balance_pairs)

            yield RebalanceEvaluation(
                rebalance_analysis
            )

            if rebalance_analysis.rebalance:
                break

            logger.info("Not rebalancing portfolio")
            await asyncio.sleep(config.aave_supply_duration)

        logger.info("Rebalancing portfolio")

        logger.info(f"Withdrawing funds from Aave")

        withdrawn = []

        for token in tokens:
            amount, exception = await withdraw(token, account, logger)

            if exception:
                logger.error(
                    "An exception was thrown while withdrawing "
                    f"{token} from Aave:",
                    exc_info=exception
                )
                yield WithdrawError(
                    token,
                    Decimal(amount) / 10 ** token.decimals,
                    exception
                )
            elif amount <= 0:
                continue

            withdrawn.append((token, Decimal(amount) / 10**token.decimals))

        yield Withdraw(withdrawn)

        logger.info(f"Swapping funds in wallet")

        for src_token, rate in token_rates.items():
            if filter_lower_rate_tokens:
                next_tokens = itertools.takewhile(
                    lambda item: item[1] > rate,
                    token_rates.items()
                )
            else:
                next_tokens = token_rates.items()

            if not next_tokens:
                continue

            destination_policy = TokenIteratorPolicy(
                map(lambda item: item[0], next_tokens)
            )

            runner = mach.run(
                src_token=src_token,
                destination_policy=destination_policy,
                account=account,
                logger=logger,
            )

            try:
                async for event in runner:
                    # Only 2 successful cases are expected: either the trade goes through, or we never had any of the source token in the first place
                    if isinstance(event, (Trade, EmptySourceBalance)):
                        break

                    logger.error(
                        f"Unexpected event while swapping {token}:"
                    )
                    logger.error(pformat(event))

                    yield ConvertError(token, event)

            except Exception as e:
                logger.error(
                    f"An exception was thrown while swapping {token}:",
                    exc_info=e
                )
                yield ConvertError(token, e)

        supplied = []

        for token in tokens:
            amount, exception = await supply(token, account, logger)

            if exception:
                logger.error(
                    "An exception was thrown while supplying "
                    f"{token} to Aave:",
                    exc_info=exception
                )
                yield SupplyError(token, Decimal(amount) / 10**token.decimals, e)
            elif amount <= 0:
                continue

            supplied.append((token, Decimal(amount) / 10**token.decimals))

        yield Supply(supplied)

        logger.info("Sleeping...")
        await asyncio.sleep(config.aave_supply_duration)
