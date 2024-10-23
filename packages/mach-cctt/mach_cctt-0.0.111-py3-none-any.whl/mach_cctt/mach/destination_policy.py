from abc import ABC, abstractmethod
from collections import defaultdict
import pprint
import random
import typing
from typing import AbstractSet, Any, Optional, Iterator

from mach_client import ChainId, Token, client

from ..log import Logger, logger


def _get_tradeable_symbols(chain: ChainId, chain_info: dict[str, Any]) -> set[str]:
    result = set(chain_info["assets"].keys())

    if gas_token := client.gas_tokens.get(chain, None):
        result.remove(gas_token)

    return result


class DestinationPolicy(ABC):
    def __init__(
        self,
        initial_excluded_chains: AbstractSet[ChainId] = client.excluded_chains,
        log: Logger = logger,
    ):
        self.log = log

        # Maps chain -> set of tradeable symbols on that chain
        self.token_choices = defaultdict(
            set,
            {
                chain: _get_tradeable_symbols(chain, chain_info)
                for chain, chain_info in client.deployments.items()
                if chain not in initial_excluded_chains
            },
        )

        # Items from self.token_choices that have been removed because the chain was excluded
        self.tried_chains: list[tuple[ChainId, set[str]]] = []

        # Specific tokens that have been excluded
        self.tried_tokens: list[Token] = []

    # Produce the destination token for the next trade
    @abstractmethod
    def __call__(self) -> Optional[Token]:
        pass

    def __repr__(self) -> str:
        d = self.__dict__.copy()
        # This can be a huge dict and we don't want it to pollute logs
        token_choices = d["token_choices"]
        d["token_choices"] = f"({len(token_choices)} tokens)"
        d["tried_chains"] = [chain for chain, _ in d["tried_chains"]]
        return f"{self.__class__.__name__}{pprint.pformat(d)}"

    def permanently_exclude_chain(self, chain: ChainId) -> None:
        self.token_choices.pop(chain, None)

    def exclude_chain(self, chain: ChainId) -> None:
        if choices := self.token_choices.pop(chain, None):
            self.tried_chains.append((chain, choices))

    def exclude_token(self, token: Token) -> None:
        chain_id = token.chain.id

        self.token_choices[chain_id].remove(token.symbol)

        # Remove this chain if there are no tokens we can choose from it
        if not self.token_choices[chain_id]:
            self.token_choices.pop(chain_id)

        self.tried_tokens.append(token)

    # Reset for the next trade
    def reset(self) -> None:
        for chain, tokens in self.tried_chains:
            self.token_choices[chain] = tokens

        self.tried_chains.clear()

        for token in self.tried_tokens:
            self.token_choices[token.chain.id].add(token.symbol)

        self.tried_tokens.clear()


class RandomChainFixedSymbolPolicy(DestinationPolicy):
    def __init__(
        self,
        symbol: str,
        initial_excluded_chains: AbstractSet[ChainId] = client.excluded_chains,
    ):
        super().__init__(initial_excluded_chains)
        self.symbol = symbol

        for chain, tokens in self.token_choices.items():
            if symbol not in tokens:
                self.token_choices.pop(chain)
            else:
                self.token_choices[chain] = {symbol}

    @typing.override
    def __call__(self) -> Optional[Token]:
        try:
            chain = random.choice(tuple(self.token_choices.keys()))
            symbol = random.choice(
                tuple(self.token_choices[chain])
            )  # Should always be self.symbol, but this way respects token exclusions
        except IndexError:
            self.log.critical(
                "Unable to choose destination token - all choices have been excluded"
            )
            return None

        return Token(chain, symbol)


class CheapChainFixedSymbolPolicy(RandomChainFixedSymbolPolicy):
    cheap_chains = frozenset((ChainId.ARBITRUM, ChainId.OP))

    def __init__(self, symbol: str):
        assert len(self.cheap_chains.intersection(client.chains)) == len(
            self.cheap_chains
        ), "Not all cheap chains supported by client!"

        super().__init__(
            symbol,
            client.chains - self.cheap_chains,
        )


class RandomChainRandomSymbolPolicy(DestinationPolicy):
    def __init__(self):
        super().__init__()

    @typing.override
    def __call__(self) -> Optional[Token]:
        try:
            chain = random.choice(tuple(self.token_choices.keys()))
            symbol = random.choice(tuple(self.token_choices[chain]))
        except IndexError:
            self.log.critical(
                "Unable to choose destination token - all choices have been excluded"
            )
            return None

        return Token(chain, symbol)


class FixedTokenSingleTradePolicy(DestinationPolicy):
    def __init__(self, token: Token):
        super().__init__()
        self.token = token
        self.called = False

    @typing.override
    def __call__(self) -> Optional[Token]:
        if self.called:
            return None

        self.called = True
        return self.token

    @typing.override
    def permanently_exclude_chain(self, chain: ChainId) -> None:
        pass

    @typing.override
    def exclude_chain(self, chain: ChainId) -> None:
        pass

    @typing.override
    def exclude_token(self, token: Token) -> None:
        pass

    @typing.override
    def reset(self) -> None:
        pass


class TokenIteratorPolicy(DestinationPolicy):
    def __init__(self, tokens: Iterator[Token]):
        super().__init__()
        self.tokens = tokens

    @typing.override
    def __call__(self) -> Optional[Token]:
        try:
            while True:
                token = next(self.tokens)

                if token.chain.id not in self.token_choices:
                    continue
                elif token.symbol not in self.token_choices[token.chain.id]:
                    self.log.warning(
                        f"Token {token} in given list not a valid choice")
                    continue

                return token

        except StopIteration:
            return None
