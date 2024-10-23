"Commands for VICI Universal Actuator"

from enum import Enum, IntEnum
try:
    from enum import StrEnum  # a 3.11+ feature.
except ImportError:
    class StrEnum(str, Enum):
        pass


class Cmds(StrEnum):
    CurrentPosition = "CP"
    MoveToPosition = "GO"
    MoveClockwiseToPosition = "CW"
    MoveCounterClockwiseToPosition = "CC"
    Home = "HM"
    Toggle = "TO"
    Learn = "LRN"
    InterfaceMode = "IFM"
    Mode = "AM"
