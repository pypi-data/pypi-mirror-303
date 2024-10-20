"""
For obtaining a list of keys for controlling eufy devices.

This is only needed once, to get the initial key.

See https://github.com/markbajaj/eufy-device-id-python/blob/main/eufy_local_id_grabber/crypto.py
"""

import json
import logging
from dataclasses import dataclass
from typing import Final

import aiohttp

from .countries import (
    phone_code_for_country,
    phone_code_for_region,
    region_for_country,
    region_for_phone_code,
)
from .exceptions import AuthenticationFailed, ConnectionFailed
from .tuya_cloud import TuyaAPISession

_LOGGER = logging.getLogger(__name__)

EUFY_HEADERS: Final[dict[str, str]] = {
    "User-Agent": "EufyHome-Android-2.4.0",
    "timezone": "Europe/London",
    "category": "Home",
    "token": "",
    "uid": "",
    "openudid": "sdk_gphone64_arm64",
    "clientType": "2",
    "language": "en",
    "country": "US",
    "Accept-Encoding": "gzip",
}


@dataclass
class VacuumCloudDiscovery:
    id: str
    name: str
    description: str
    model: str
    mac: str
    access_token: str


async def get_cloud_vacuums(
    session: aiohttp.ClientSession, username: str, password: str
) -> dict[str, VacuumCloudDiscovery]:
    """Login to Eufy and get the vacuum details."""
    user_info_resp = await session.post(
        "https://home-api.eufylife.com/v1/user/email/login",
        headers=EUFY_HEADERS,
        json={
            "client_Secret": "GQCpr9dSp3uQpsOMgJ4xQ",
            "client_id": "eufyhome-app",
            "email": username,
            "password": password,
        },
    )

    if user_info_resp.status != 200:
        raise ConnectionFailed

    user_info = await user_info_resp.json()

    if user_info["res_code"] != 1:
        raise AuthenticationFailed

    user_id = user_info["user_info"]["id"]
    host = user_info["user_info"]["request_host"]
    access_token = user_info["access_token"]

    device_info_resp = await session.get(
        host + "/v1/device/list/devices-and-groups",
        headers={**EUFY_HEADERS, "token": access_token, "id": user_id},
    )
    device_info = await device_info_resp.json()

    user_settings_resp = await session.get(
        host + "/v1/user/setting",
        headers={**EUFY_HEADERS, "token": access_token, "id": user_id},
    )
    user_settings = await user_settings_resp.json()

    if (
        "tuya_home" in user_settings["setting"]["home_setting"]
        and "tuya_region_code" in user_settings["setting"]["home_setting"]["tuya_home"]
    ):
        region = user_settings["setting"]["home_setting"]["tuya_home"]["tuya_region_code"]
        if user_info["user_info"]["phone_code"]:
            country_code = user_info["user_info"]["phone_code"]
        else:
            country_code = phone_code_for_region(region)
    elif user_info["user_info"]["phone_code"]:
        region = region_for_phone_code(user_info["user_info"]["phone_code"])
        country_code = user_info["user_info"]["phone_code"]
    elif user_info["user_info"]["country"]:
        region = region_for_country(user_info["user_info"]["country"])
        country_code = phone_code_for_country(user_info["user_info"]["country"])
    else:
        region = "EU"
        country_code = "44"

    time_zone = user_info["user_info"]["timezone"]

    tuya_client = TuyaAPISession(
        session,
        username="eh-" + user_id,
        region=region,
        timezone=time_zone,
        phone_code=country_code,
    )

    vacs = {}
    for item in device_info["items"]:
        if item["device"]["product"]["appliance"] != "Cleaning":
            continue

        try:
            device = await tuya_client.get_device(item["device"]["id"])
        except Exception:
            _LOGGER.debug(
                "Skipping vacuum %s: found on Eufy but not on Tuya. Eufy details:",
                item["device"]["id"],
            )
            _LOGGER.debug(json.dumps(item["device"], indent=2))
            continue

        vacs[item["device"]["id"]] = VacuumCloudDiscovery(
            id=item["device"]["id"],
            name=item["device"]["alias_name"],
            description=item["device"]["name"],
            model=item["device"]["product"]["product_code"],
            mac=item["device"]["wifi"]["mac"],
            access_token=device["localKey"],
        )

    return vacs
