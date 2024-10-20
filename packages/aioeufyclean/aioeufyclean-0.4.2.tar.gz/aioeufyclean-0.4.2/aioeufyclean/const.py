from enum import StrEnum


class WorkMode(StrEnum):
    AUTO = "auto"
    NO_SWEEP = "Nosweep"
    SMALL_ROOM = "SmallRoom"
    EDGE = "Edge"
    SPOT = "Spot"


class Direction(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"
    BACKWARD = "backward"


class CleanSpeed(StrEnum):
    NO_SUCTION = "No_suction"
    QUIET = "Quiet"
    PURE = "Pure"
    STANDARD = "Standard"
    BOOST_IQ = "Boost_IQ"
    TURBO = "Turbo"
    MAX = "Max"
