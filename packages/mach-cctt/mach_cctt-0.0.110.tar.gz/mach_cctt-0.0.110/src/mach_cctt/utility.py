from typing import AbstractSet, Optional

from eth_typing import ChecksumAddress
from mach_client import ChainId, Token, client


async def choose_source_token(
    excluded_chains: AbstractSet[ChainId], wallet_address: ChecksumAddress
) -> Token:
    balances = await client.get_token_balances(wallet_address)

    token: Optional[tuple[int, ChainId, str]] = None

    # Choose the token with the greatest balance (regardless of denomination) that is not the gas token
    for chain, chain_balances in filter(
        lambda item: item[0] not in excluded_chains, balances.items()
    ):
        for symbol, balance in chain_balances.items():
            if client.gas_tokens.get(chain, None) != symbol and (
                not token or token[0] < balance
            ):
                token = (balance, chain, symbol)

    if not token:
        raise RuntimeError("No viable source tokens to choose from")

    return Token(token[1], token[2])
