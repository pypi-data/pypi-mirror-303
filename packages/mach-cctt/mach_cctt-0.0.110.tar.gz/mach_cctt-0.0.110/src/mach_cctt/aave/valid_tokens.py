from typing import AbstractSet, Iterable

from mach_client import Chain, ChainId, Token, utility

from . import atoken


async def get_valid_aave_tokens(
    chains: Iterable[ChainId], symbols: AbstractSet[str]
) -> list[Token]:
    tokens: list[Token] = []

    for chain_id in chains:
        w3 = await utility.make_w3(Chain(chain_id))
        atokens = await atoken.get_all_atokens(w3, chain_id)

        tokens.extend(
            map(
                lambda symbol: Token(chain_id, symbol),
                frozenset(atokens.keys()).intersection(symbols),
            )
        )

    return tokens
