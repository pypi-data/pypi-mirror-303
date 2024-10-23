from typing import AsyncGenerator

from .aave.event import AaveEvent
from .mach.event import MachEvent


Runner = AsyncGenerator[AaveEvent | MachEvent, None]
