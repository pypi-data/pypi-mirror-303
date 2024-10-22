from decimal import Decimal
import functools
from importlib import resources
import os
from pathlib import Path
from typing import Any

from mach_client import ChainId
from mach_client.config import load_abi

# Only used for swaps between similar tokens (ie. WETH -> ETH, USDC -> USDT, etc.)
slippage_tolerance = Decimal(os.environ.get(
    "CCTT_SLIPPAGE_TOLERANCE", -0.0005))

# Relative to the root of the repository
abi_path = resources.files("abi")

# Time to wait between polls of the destination balance to check if the desired amount has been received
poll_timeout = 10

# Maximum number of polls
max_polls = 30

solidity_uint_max = 2**256 - 1

# Default logger
log_file = Path("logs") / "app.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

aave_symbols = frozenset(os.environ["CCTT_AAVE_SYMBOLS"].split(","))

# How many seconds for each Aave supply before rebalancing to highest interest pool
aave_supply_duration = int(os.environ.get("CCTT_AAVE_SUPPLY_DURATION", 300))

# Max interest rate difference between highest interest rate token and portfolio interest rate before forcing a rebalance
aave_rebalance_threshold = Decimal(0.003)

aave_pool_addresses = {
    ChainId.ETHEREUM: "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2",
    ChainId.OP: "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
    ChainId.BSC: "0x6807dc923806fE8Fd134338EABCA509979a7e0cB",
    ChainId.POLYGON: "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
    # ChainId.OPBNB
    # ChainId.MANTLE
    ChainId.BASE: "0xA238Dd80C259a72e81d7e4664a9801593F98d1c5",
    # ChainId.MODE
    ChainId.ARBITRUM: "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
    # ChainId.CELO
    ChainId.AVALANCHE_C_CHAIN: "0x794a61358D6845594F94dc1DB02A252b5b4814aD",
    # ChainId.BLAST
    ChainId.SCROLL: "0x11fCfe756c05AD438e312a7fd934381537D3cFfe",
}

aave_pool_data_provider_addresses = {
    ChainId.ETHEREUM: "0x7B4EB56E7CD4b454BA8ff71E4518426369a138a3",
    ChainId.OP: "0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654",
    ChainId.BSC: "0x23dF2a19384231aFD114b036C14b6b03324D79BC",
    ChainId.POLYGON: "0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654",
    # ChainId.OPBNB
    # ChainId.MANTLE
    ChainId.BASE: "0x2d8A3C5677189723C4cB8873CfC9C8976FDF38Ac",
    # ChainId.MODE
    ChainId.ARBITRUM: "0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654",
    # ChainId.CELO
    ChainId.AVALANCHE_C_CHAIN: "0x69FA688f1Dc47d4B5d8029D5a35FB7a548310654",
    # ChainId.BLAST
    ChainId.SCROLL: "0xa99F4E69acF23C6838DE90dD1B5c02EA928A53ee",
}

aave_pool_data_provider_abi = load_abi(
    abi_path / "aave" / "pool_data_provider.json")


@functools.cache
def aave_pool_abi(chain: ChainId) -> Any:
    """
    Load a JSON abi from a file.

    :param envvar: Environment variable pointing to the path.
    :param default_path: The path to check if environment var isn't set.
    """

    abi_path_full = abi_path / "aave" / "pool" / f"{chain}.json"

    return load_abi(abi_path_full)
