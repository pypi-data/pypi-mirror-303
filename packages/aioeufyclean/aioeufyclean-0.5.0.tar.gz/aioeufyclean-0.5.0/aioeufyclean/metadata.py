"""Metadata about eufyClean vacuums."""

from dataclasses import dataclass

from .const import CleanSpeed, WorkMode

CLEAN_SPEEDS_C = (CleanSpeed.NO_SUCTION, CleanSpeed.STANDARD, CleanSpeed.BOOST_IQ, CleanSpeed.MAX)
CLEAN_SPEEDS_G = (CleanSpeed.STANDARD, CleanSpeed.TURBO, CleanSpeed.MAX, CleanSpeed.BOOST_IQ)
CLEAN_SPEEDS_L = (CleanSpeed.QUIET, CleanSpeed.STANDARD, CleanSpeed.TURBO, CleanSpeed.MAX)
CLEAN_SPEEDS_X = (CleanSpeed.PURE, CleanSpeed.STANDARD, CleanSpeed.TURBO, CleanSpeed.MAX)


@dataclass
class VacuumInfo:
    model: str

    work_mode: str = "5"
    work_mode_list: tuple[WorkMode, ...] = (
        WorkMode.AUTO,
        WorkMode.SMALL_ROOM,
        WorkMode.SPOT,
        WorkMode.EDGE,
        WorkMode.NO_SWEEP,
    )

    clean_speed: str = "102"
    clean_speed_list: tuple[CleanSpeed, ...] = CLEAN_SPEEDS_G

    power: str = "1"
    play_pause: str = "2"
    direction: str = "3"
    work_status: str = "15"
    go_home: str = "101"
    find_robot: str = "103"
    battery_level: str = "104"
    error_code: str = "106"
    consumable: str = "116"
    boost_iq: str | None = "118"


VACUUM_INFO = {
    "T1250": VacuumInfo(model="Robovac 35C"),
    "T2080": VacuumInfo(model="Robovac S1"),
    "T2103": VacuumInfo(
        model="Robovac 11C",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2117": VacuumInfo(
        model="Robovac 35C",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2118": VacuumInfo(
        model="Robovac 30C",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2119": VacuumInfo(
        model="Robovac 11S",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2120": VacuumInfo(
        model="Robovac 15C MAX",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2123": VacuumInfo(
        model="Robovac 25C",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2128": VacuumInfo(
        model="Robovac 15C MAX",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2130": VacuumInfo(
        model="Robovac 30C MAX",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2132": VacuumInfo(
        model="Robovac 25C MAX",
        clean_speed_list=CLEAN_SPEEDS_C,
    ),
    "T2150": VacuumInfo(model="Robovac G10 Hybrid"),
    "T2181": VacuumInfo(
        model="Robovac LR30 Hybrid+",
        clean_speed_list=CLEAN_SPEEDS_L,
    ),
    "T2182": VacuumInfo(
        model="Robovac L35 Hybrid+",
        clean_speed_list=CLEAN_SPEEDS_L,
    ),
    "T2190": VacuumInfo(
        model="Robovac L70 Hybrid",
        clean_speed_list=CLEAN_SPEEDS_L,
    ),
    "T2192": VacuumInfo(model="Robovac LR20"),
    "T2193": VacuumInfo(
        model="Robovac LR30",
        clean_speed_list=CLEAN_SPEEDS_L,
    ),
    "T2194": VacuumInfo(
        model="Robovac L35 Hybrid",
        clean_speed_list=CLEAN_SPEEDS_L,
    ),
    "T2250": VacuumInfo(model="Robovac G30"),
    "T2251": VacuumInfo(model="Robovac G30 Edge"),
    "T2252": VacuumInfo(model="Robovac G30 Verge"),
    "T2253": VacuumInfo(model="Robovac G30 Hybrid"),
    "T2254": VacuumInfo(model="Robovac G35"),
    "T2255": VacuumInfo(model="Robovac G40"),
    "T2256": VacuumInfo(model="Robovac G40 Hybrid"),
    "T2257": VacuumInfo(model="Robovac G20"),
    "T2258": VacuumInfo(model="Robovac G20 Hybrid"),
    "T2259": VacuumInfo(model="Robovac G32 Pro"),
    "T2261": VacuumInfo(
        model="Robovac X8 Hybrid",
        clean_speed_list=CLEAN_SPEEDS_X,
    ),
    "T2262": VacuumInfo(
        model="Robovac X8",
        clean_speed_list=CLEAN_SPEEDS_X,
    ),
    "T2266": VacuumInfo(
        model="Robovac X8 Pro",
        clean_speed_list=CLEAN_SPEEDS_X,
    ),
    "T2267": VacuumInfo(model="RoboVac L60"),
    "T2268": VacuumInfo(model="Robovac L60 Hybrid"),
    "T2270": VacuumInfo(model="RoboVac G35+"),
    "T2272": VacuumInfo(model="Robovac G30+ SES"),
    "T2273": VacuumInfo(model="RoboVac G40 Hybrid+"),
    "T2276": VacuumInfo(model="Robovac X8 Pro SES"),
    "T2277": VacuumInfo(model="Robovac L60 SES"),
    "T2278": VacuumInfo(model="Robovac L60 Hybrid SES"),
    "T2320": VacuumInfo(
        model="Robovac X9 Pro",
        clean_speed_list=CLEAN_SPEEDS_X,
    ),
    "T2351": VacuumInfo(
        model="Robovac X10 Pro Omni",
        clean_speed_list=CLEAN_SPEEDS_X,
    ),
}

_FRIENDLY_TO_MODEL = {vi.model: k for (k, vi) in VACUUM_INFO.items()}
VACUUM_MODEL_NAME_TO_ID = {k: _FRIENDLY_TO_MODEL[k] for k in sorted(_FRIENDLY_TO_MODEL.keys())}
