import asyncio
from pprint import pformat
import time
from typing import AsyncGenerator, Optional

from eth_account.signers.local import LocalAccount
from hexbytes import HexBytes
from mach_client import ChainId, Token, balances, client, config as client_config, utility
from web3 import AsyncWeb3
from web3.contract import AsyncContract

from .. import config
from ..amount_policy import AmountPolicy, max_amount_policy
from .destination_policy import DestinationPolicy
from ..log import LogContextAdapter, Logger
from ..safe_transactions import safe_build_and_send_tx
from ..utility import choose_source_token
from .event import *
from .risk_manager import RiskManager, SimilarTokenRiskManager


async def ensure_approval(
    w3: AsyncWeb3,
    account: LocalAccount,
    spender_address,
    src_address,
    amount: int,
    log: Logger,
) -> Optional[HexBytes]:
    log = LogContextAdapter(log, f"Approve")

    contract: AsyncContract = w3.eth.contract(
        address=src_address, abi=client_config.erc20_abi)

    try:
        allowance_func = contract.functions.allowance(
            account.address,
            spender_address,
        )
    except Exception as e:
        raise ValueError(f"failed to build allowance function: {e}") from e

    try:
        allowance: int = await allowance_func.call()
    except Exception as e:
        raise ConnectionError(f"failed to get allowance: {e}") from e

    log.debug(f"Allowance of {
              allowance=}/{amount=} ({100 * allowance / amount}%)")

    if allowance >= amount:
        return None

    try:
        approve_func = contract.functions.approve(
            spender_address,
            amount,
        )
    except Exception as e:
        raise ValueError(f"failed to build approve function: {e}") from e

    log.debug("Approving larger allowance")
    try:
        tx_hash = await safe_build_and_send_tx(
            w3,
            account,
            approve_func,
        )
    except Exception as e:
        raise ValueError(f"failed to send approve tx: {e}") from e

    log.debug(f"Approval transaction hash: {tx_hash.to_0x_hex()}")
    return tx_hash


async def run(
    *,
    src_token: Token,
    destination_policy: DestinationPolicy,
    amount_policy: AmountPolicy = max_amount_policy,
    check_destination_gas: bool = True,
    account: LocalAccount,
    logger: Logger,
) -> AsyncGenerator[MachEvent, None]:
    src_w3 = await utility.make_w3(src_token.chain)
    src_order_book_contract = utility.make_order_book_contract(
        src_w3, src_token)

    risk_manager: RiskManager = SimilarTokenRiskManager(
        account.address, config.slippage_tolerance, logger
    )

    # Permanently exclude chains on which we have no gas
    permanently_excluded_chains: set[ChainId] = set()

    # Temporarily exclude the source chain since we don't support single chain swaps
    destination_policy.exclude_chain(src_token.chain.id)

    while True:
        log = LogContextAdapter(logger, f"{src_token} => (UNSELECTED)")

        initial_src_balance = await balances.get_balance(src_w3, src_token, account.address)
        log.debug(f"{initial_src_balance=}")

        # TODO: some pairs have trouble filling 1 tick, so treat it as 0
        if initial_src_balance <= 1:
            log.critical(f"Source balance empty. Cannot continue trading.")
            yield EmptySourceBalance(src_token, account.address)
            break

        if not (dest_token := destination_policy()):
            log.critical(f"No viable destination token")
            yield NoViableDestination(destination_policy)
            break

        log = LogContextAdapter(logger, f"{src_token} => {dest_token}")

        destination_policy.exclude_token(dest_token)
        dest_w3 = await utility.make_w3(dest_token.chain)

        if check_destination_gas:
            try:
                gas_estimate = await client.estimate_gas(dest_token.chain.id)
            except Exception as e:
                log.error("Gas estimate failed:", exc_info=e)
                yield GasEstimateFailed(dest_token.chain, e)
                continue

            log.debug(f"Gas estimate: {gas_estimate}")
            estimated_gas = gas_estimate["gas_estimate"] * \
                gas_estimate["gas_price"]
            log.debug(f"Estimated gas cost: {estimated_gas}")

            gas_available = await balances.get_gas_balance(dest_w3, account.address)
            log.debug(f"Available gas: {gas_available}")

            if gas_available < estimated_gas:
                log.info(
                    f"Insufficient gas on chain {
                        dest_token.chain.name}, will be excluded from future selection"
                )
                destination_policy.permanently_exclude_chain(
                    dest_token.chain.id)
                permanently_excluded_chains.add(dest_token.chain.id)
                yield InsufficientDestinationGas(
                    dest_token, gas_estimate, gas_available
                )
                continue

        desired_src_amount = amount_policy(
            src_token, dest_token, initial_src_balance)

        try:
            quote = await client.request_quote(
                src_token,
                dest_token,
                desired_src_amount,
                account.address,
            )
        except Exception as e:
            log.error("Quote request failed:", exc_info=e)
            yield QuoteFailed(
                (src_token, dest_token), desired_src_amount, account.address, e
            )
            continue

        log.debug(f"Quote:")
        log.debug(pformat(quote))

        if quote["invalid_amount"]:
            log.warning(f"Quote had invalid amount")
            yield QuoteInvalidAmount(
                (src_token, dest_token), desired_src_amount, account.address, quote
            )
            continue

        if quote["liquidity_source"] == "unavailable":
            log.warning(f"No liquidity source")
            yield QuoteLiquidityUnavailable(
                (src_token, dest_token), desired_src_amount, account.address, quote
            )
            continue

        if (risk_analyis := risk_manager(src_token, dest_token, quote)).reject:
            log.warning(f"Order rejected by risk manager")
            yield RiskManagerRejection(
                (src_token, dest_token), desired_src_amount, quote, risk_analyis
            )
            continue

        src_amount, dest_amount = quote["src_amount"], quote["dst_amount"]

        log.debug(
            f"Can fill {src_amount=}/{desired_src_amount=} ({
                100 * src_amount / desired_src_amount}%) through liquidity source {quote['liquidity_source']}"
        )

        assert src_amount <= desired_src_amount

        if src_amount < desired_src_amount:
            log.warning("Not enough liquidity to trade entire source balance")

            if src_amount <= 0:
                log.warning(
                    f"Cannot fill any amount, trying a different destination")
                yield CannotFill((src_token, dest_token), desired_src_amount, quote)
                continue

        # TODO: change
        try:
            approval_amount = max(src_amount, config.solidity_uint_max)

            await ensure_approval(
                src_w3,
                account,
                src_order_book_contract.address,
                src_token.contract_address,
                approval_amount,
                log,
            )
        except Exception as e:
            log.error(f"Failed to ensure approval:", exc_info=e)
            yield ApprovalFailed(
                src_token,
                approval_amount,
                account.address,
                src_order_book_contract.address,
                e,
            )
            raise e

        order_direction = (
            quote["src_asset_address"],  # srcAsset: address
            quote["dst_asset_address"],  # dstAsset: address
            dest_token.chain.lz_cid,  # dstLzc: uint32
        )

        order_funding = (
            src_amount,  # srcQuantity: uint96
            dest_amount,  # dstQuantity: uint96
            quote["bond_fee"],  # bondFee: uint16
            quote["bond_asset_address"],  # bondAsset: address
            quote["bond_amount"],  # bondAmount: uint96
        )

        # Note on why we aren't using quote["challenge_offset"] and quote["challenge_window"]:
        # https://tristeroworkspace.slack.com/archives/C07RJC68VD0/p1728678088837679
        order_expiration = (
            int(time.time()) + 3600,  # timestamp: uint32
            1,  # challengeOffset: uint16
            1,  # challengeWindow: uint16
        )

        is_maker = False

        place_order = src_order_book_contract.functions.placeOrder(
            order_direction,
            order_funding,
            order_expiration,
            is_maker,
        )

        try:
            tx_hash = await safe_build_and_send_tx(
                src_w3,
                account,
                place_order,
            )
            log.info(f"Placed order with hash: {tx_hash.to_0x_hex()}")

            tx_receipt = await src_w3.eth.wait_for_transaction_receipt(tx_hash)
            log.debug("Receipt:")
            log.debug(pformat(dict(tx_receipt)))

        except Exception as e:
            log.error(f"Failed to complete the transaction:", exc_info=e)
            yield PlaceOrderFailed(
                (src_token, dest_token),
                account.address,
                place_order,
                e,
            )
            continue

        # These need to be computed before the order has been submitted
        start_dest_balance = await balances.get_balance(dest_w3, dest_token, account.address)
        expected_src_balance = desired_src_amount - src_amount
        expected_dest_balance = start_dest_balance + dest_amount

        try:
            order_response = await client.submit_order(src_token.chain.id, tx_hash)

        except Exception as e:
            log.error(f"There was an error submitting this order:", exc_info=e)
            yield SubmitOrderFailed((src_token, dest_token), tx_hash, e)
            continue

        log.info("Submitted order")
        log.debug("Response:")
        log.debug(pformat(order_response))

        src_balance = await balances.get_balance(src_w3, src_token, account.address)
        log.info(
            "Waiting for source balance to be withdrawn "
            f"({src_balance=}, {expected_src_balance=})..."
        )
        prev_src_balance = src_balance

        count = 0

        while (
            src_balance := await balances.get_balance(src_w3, src_token, account.address)
        ) > expected_src_balance and count < config.max_polls:
            count += 1

            if (filled_amount := prev_src_balance - src_balance) > 0:
                log.warning(
                    f"Expected to fill {src_amount} ticks, actually filled {
                        filled_amount} ticks"
                )
                break

            prev_src_balance = src_balance

            await asyncio.sleep(config.poll_timeout)

        if count >= config.max_polls:
            log.warning("Source balance not withdrawn after max waiting time")
            yield SourceNotWithdrawn(
                (src_token, dest_token),
                order_response,
                config.max_polls * config.poll_timeout,
            )
            continue

        dest_balance = await balances.get_balance(dest_w3, dest_token, account.address)
        log.info(
            "Source balance withdrawn, waiting to receive destination token "
            f"({dest_balance=}, {expected_dest_balance=})..."
        )
        prev_dest_balance = dest_balance

        count = 0

        while (
            dest_balance := await balances.get_balance(dest_w3, dest_token, account.address)
        ) < expected_dest_balance and count < config.max_polls:

            count += 1

            if (received_amount := dest_balance - prev_dest_balance) > 0:
                log.warning(
                    f"Expected to receive {dest_amount} ticks, actually received {
                        received_amount} ticks"
                )
                break

            prev_dest_balance = dest_balance

            await asyncio.sleep(config.poll_timeout)

        if count >= config.max_polls:
            log.warning(
                "Exceeded max number of polls. Transaction possibly stuck.")
            yield DestinationNotReceived(
                (src_token, dest_token),
                order_response,
                config.max_polls * config.poll_timeout,
            )

            src_token = await choose_source_token(
                permanently_excluded_chains, account.address
            )
            src_w3 = await utility.make_w3(src_token.chain)
            src_order_book_contract = utility.make_order_book_contract(
                src_w3, src_token
            )

        else:
            log.info("Destination balance received - order complete")

            yield Trade((src_token, dest_token), quote, order_response)

            src_token, src_w3, src_order_book_contract = (
                dest_token,
                dest_w3,
                utility.make_order_book_contract(dest_w3, dest_token),
            )

        destination_policy.reset()
        destination_policy.exclude_chain(src_token.chain.id)
