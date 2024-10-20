# Copyright 2019 Richard Mitchell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import json
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from aioeufyclean.metadata import VACUUM_INFO

from .const import CleanSpeed, WorkMode
from .tuya import TuyaDevice


class ErrorCode(StrEnum):
    NO_ERROR = "no_error"
    WHEEL_STUCK = "Wheel_stuck"
    R_BRUSH_STUCK = "R_brush_stuck"
    CRASH_BAR_STUCK = "Crash_bar_stuck"
    SENSOR_DIRTY = "sensor_dirty"
    NOT_ENOUGH_POWER = "N_enough_pow"
    STUCK_5_MIN = "Stuck_5_min"
    FAN_STUCK = "Fan_stuck"
    S_BRUSH_STUCK = "S_brush_stuck"


class State(StrEnum):
    DOCKED = "docked"
    CLEANING = "cleaning"
    RETURNING = "returning"
    ERROR = "error"
    PAUSED = "paused"
    ON = "on"
    OFF = "off"
    IDLE = "idle"


class BinarySensor(StrEnum):
    pass


class Sensor(StrEnum):
    BATTERY = "battery"
    FILTER_LIFE = "filter_life"
    SIDE_BRUSH_LIFE = "side_brush_life"
    ROLLING_BRUSH_LIFE = "rolling_brush_life"
    SENSOR_CLEAN_LIFE = "sensor_clean_life"


class Switch(StrEnum):
    BOOST_IQ = "boost_iq"


@dataclass
class DataPoint:
    POWER = "1"
    PLAY_PAUSE = "2"
    DIRECTION = "3"
    WORK_MODE = "5"
    WORK_STATUS = "15"
    GO_HOME = "101"
    CLEAN_SPEED = "102"
    FIND_ROBOT = "103"
    BATTERY_LEVEL = "104"
    ERROR_CODE = "106"
    CONSUMABLE = "116"
    BOOST_IQ = "118"


@dataclass
class VacuumState:
    state: State
    clean_speed: CleanSpeed
    sensors: dict[Sensor, str | int | float]
    binary_sensors: dict[BinarySensor, bool]
    switches: dict[Switch, bool]


class VacuumDevice(TuyaDevice):
    """Represents a generic Eufy Robovac."""

    def __init__(
        self,
        unique_id: str,
        host: str,
        local_key: str,
        model_id: str,
        port: int = 6668,
        gateway_id: str | None = None,
        version: tuple[int, int] = (3, 3),
        timeout: int = 10,
    ):
        self.model_id = model_id
        self.device_info = VACUUM_INFO[model_id]

        super().__init__(unique_id, host, local_key, port, gateway_id, version, timeout)

    def _handle_state_update(self, payload: dict[str, Any]) -> VacuumState:
        if payload.get(DataPoint.ERROR_CODE) != 0:
            state = State.ERROR
        elif payload.get(DataPoint.POWER) == "1" or payload.get(DataPoint.WORK_STATUS) in (
            "Charging",
            "completed",
        ):
            state = State.DOCKED
        elif payload.get(DataPoint.WORK_STATUS) in ("Recharge",):
            state = State.RETURNING
        elif payload.get(DataPoint.WORK_STATUS) in ("Sleeping", "standby"):
            state = State.IDLE
        else:
            state = State.CLEANING

        clean_speed = CleanSpeed(payload[DataPoint.CLEAN_SPEED])

        vacuum_state = VacuumState(
            state=state,
            clean_speed=clean_speed,
            sensors={},
            binary_sensors={},
            switches={},
        )

        if DataPoint.BATTERY_LEVEL in payload:
            vacuum_state.sensors[Sensor.BATTERY] = payload[DataPoint.BATTERY_LEVEL]

        if consumable_json := payload.get(DataPoint.CONSUMABLE):
            if (
                duration := json.loads(base64.b64decode(consumable_json))
                .get("consumable", {})
                .get("duration", {})
            ):
                # TODO: What are SP, TR and BatteryStatus?
                if "FM" in duration:
                    vacuum_state.sensors[Sensor.FILTER_LIFE] = duration["FM"]
                if "RB" in duration:
                    vacuum_state.sensors[Sensor.ROLLING_BRUSH_LIFE] = duration["RB"]
                if "SB" in duration:
                    vacuum_state.sensors[Sensor.SIDE_BRUSH_LIFE] = duration["SB"]
                if "SS" in duration:
                    vacuum_state.sensors[Sensor.SENSOR_CLEAN_LIFE] = duration["SS"]

        if boost_iq := payload.get(DataPoint.BOOST_IQ):
            vacuum_state.switches[Switch.BOOST_IQ] = boost_iq

        return vacuum_state

    async def async_start(self) -> None:
        await self.async_set({DataPoint.WORK_MODE: str(WorkMode.AUTO)})

    async def async_pause(self) -> None:
        await self.async_set({DataPoint.PLAY_PAUSE: False})

    async def async_stop(self) -> None:
        await self.async_set({DataPoint.PLAY_PAUSE: False})

    async def async_return_to_base(self) -> None:
        await self.async_set({DataPoint.GO_HOME: True})

    async def async_locate(self) -> None:
        await self.async_set({DataPoint.FIND_ROBOT: True})

    async def async_set_fan_speed(self, clean_speed: CleanSpeed) -> None:
        await self.async_set({DataPoint.CLEAN_SPEED: str(clean_speed)})

    async def async_clean_spot(self) -> None:
        await self.async_set({DataPoint.WORK_MODE: WorkMode.SPOT})

    async def async_set_switch(self, switch: Switch, value: bool) -> None:
        if switch == Switch.BOOST_IQ:
            await self.async_set({DataPoint.BOOST_IQ: value})
