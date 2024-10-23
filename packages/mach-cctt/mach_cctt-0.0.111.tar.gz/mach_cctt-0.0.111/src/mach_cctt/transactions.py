# Unsafe transactions without nonce management

from pprint import pformat

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress
from mach_client import Token, client, utility
from web3 import AsyncWeb3
from web3.contract.async_contract import AsyncContract, AsyncContractFunction
from web3.types import TxParams

from . import config
from .log import LogContextAdapter, Logger, logger


async def fill_transaction_defaults(
    w3: AsyncWeb3, address: ChecksumAddress
) -> TxParams:
    params: TxParams = {
        "from": address,
        "nonce": await w3.eth.get_transaction_count(
            address, "latest"
        ),
    }
    return params


async def send_transaction(
    w3: AsyncWeb3,
    account: LocalAccount,
    params: TxParams,
    log: Logger = logger,
) -> None:
    log.debug("Sending transaction with params:")
    log.debug(pformat(params))

    signed_transaction = account.sign_transaction(params)  # type: ignore

    log.debug(f"Sending raw transaction: {pformat(signed_transaction)}")

    transaction_hash = await w3.eth.send_raw_transaction(
        signed_transaction.raw_transaction
    )

    log.debug(f"Transaction hash: {transaction_hash.to_0x_hex()}")

    transaction_receipt = await w3.eth.wait_for_transaction_receipt(transaction_hash)

    log.debug("Received receipt:")
    log.debug(pformat(dict(transaction_receipt)))

    assert transaction_receipt["status"] == 0x1, "Transaction failed"

    log.debug("Transaction success")


async def approve(
    account: LocalAccount,
    spender: ChecksumAddress,
    token_contract: AsyncContract,
    amount: int,
    log: Logger = logger,
) -> None:
    log = LogContextAdapter(log, f"Approve")

    # Warning: this could be dangerous if we don't trust the contract
    approve_function = token_contract.functions.approve(
        spender, max(amount, config.solidity_uint_max)
    )

    params = await fill_transaction_defaults(token_contract.w3, account.address)
    params = await approve_function.build_transaction(params)

    log.debug("Sending approve transaction")
    await send_transaction(token_contract.w3, account, params, log)


async def send_contract_function_transaction(
    contract_function: AsyncContractFunction,
    account: LocalAccount,
    log: Logger = logger,
) -> None:
    log.debug(f"{contract_function=}")
    params = await fill_transaction_defaults(contract_function.w3, account.address)
    params = await contract_function.build_transaction(params)
    params["gas"] = int(1.5 * params["gas"])  # type: ignore

    await send_transaction(contract_function.w3, account, params, log)


async def approve_send_contract_function_transaction(
    contract_function: AsyncContractFunction,
    account: LocalAccount,
    token_contract: AsyncContract,
    amount: int,
    log: Logger = logger,
) -> None:
    await approve(account, contract_function.address, token_contract, amount, log)
    await send_contract_function_transaction(contract_function, account, log)


async def transfer_token(
    w3: AsyncWeb3, token: Token, amount: int, account: LocalAccount, wallet
) -> None:
    assert (
        client.gas_tokens[token.chain.id] != token.symbol
    ), "Token must be ERC-20 token, not gas token"

    log = LogContextAdapter(logger, f"Transfer {token}")

    if amount <= 0:
        log.info(f"Skipping {token} - balance empty")
        return

    log.info(f"Transferring {amount} units of {token}")

    contract = utility.make_token_contract(w3, token)

    params = await fill_transaction_defaults(w3, account.address)
    params["chainId"] = token.chain.id

    params = await contract.functions.transfer(wallet, amount).build_transaction(params)

    await send_transaction(w3, account, params, log)
