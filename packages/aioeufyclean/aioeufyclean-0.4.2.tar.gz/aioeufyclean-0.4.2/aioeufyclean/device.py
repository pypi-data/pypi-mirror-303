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

    def _handle_state_update(self, payload: dict[str, str | int | float]) -> VacuumState:
        if payload.get(self.device_info.error_code) != 0:
            state = State.ERROR
        elif payload.get(self.device_info.power) == "1" or payload.get(
            self.device_info.work_status
        ) in (
            "Charging",
            "completed",
        ):
            state = State.DOCKED
        elif payload.get(self.device_info.work_status) in ("Recharge",):
            state = State.RETURNING
        elif payload.get(self.device_info.work_status) in ("Sleeping", "standby"):
            state = State.IDLE
        else:
            state = State.CLEANING

        clean_speed = CleanSpeed(self.device_info.clean_speed)

        vacuum_state = VacuumState(
            state=state,
            clean_speed=clean_speed,
            sensors={},
            binary_sensors={},
            switches={},
        )

        if self.device_info.battery_level and self.device_info.battery_level in payload:
            if battery_level := payload.get(self.device_info.battery_level):
                vacuum_state.sensors[Sensor.BATTERY] = int(battery_level)

        if self.device_info.consumable:
            if consumable_json := payload.get(self.device_info.consumable):
                if (
                    duration := json.loads(base64.b64decode(str(consumable_json)))
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

        if self.device_info.boost_iq:
            if boost_iq := payload.get(self.device_info.boost_iq):
                vacuum_state.switches[Switch.BOOST_IQ] = bool(boost_iq)

        return vacuum_state

    async def async_start(self) -> None:
        await self.async_set({self.device_info.work_mode: str(WorkMode.AUTO)})

    async def async_pause(self) -> None:
        await self.async_set({self.device_info.play_pause: False})

    async def async_stop(self) -> None:
        await self.async_set({self.device_info.play_pause: False})

    async def async_return_to_base(self) -> None:
        await self.async_set({self.device_info.go_home: True})

    async def async_locate(self) -> None:
        await self.async_set({self.device_info.find_robot: True})

    async def async_set_fan_speed(self, clean_speed: CleanSpeed) -> None:
        await self.async_set({self.device_info.clean_speed: str(clean_speed)})

    async def async_clean_spot(self) -> None:
        await self.async_set({self.device_info.work_mode: WorkMode.SPOT})

    async def async_set_switch(self, switch: Switch, value: bool) -> None:
        if self.device_info.boost_iq and switch == Switch.BOOST_IQ:
            await self.async_set({self.device_info.boost_iq: value})
