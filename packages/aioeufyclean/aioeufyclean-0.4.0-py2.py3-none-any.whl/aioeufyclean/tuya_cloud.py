"""
For obtaining a list of keys for controlling eufy devices.

This is only needed once, to get the initial key.

See https://github.com/markbajaj/eufy-device-id-python/blob/main/eufy_local_id_grabber/crypto.py
"""

import hmac
import json
import math
import random
import string
import time
import uuid
from hashlib import md5, sha256
from typing import Any

import aiohttp
from cryptography.hazmat.backends.openssl import backend as openssl_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

EUFY_HMAC_KEY = b"A_cepev5pfnhua4dkqkdpmnrdxx378mpjr_s8x78u7xwymasd9kqa7a73pjhxqsedaj"


def unpadded_rsa(key_exponent: int, key_n: int, plaintext: bytes) -> bytes:
    keylength = math.ceil(key_n.bit_length() / 8)
    input_nr = int.from_bytes(plaintext, byteorder="big")
    crypted_nr = pow(input_nr, key_exponent, key_n)
    return crypted_nr.to_bytes(keylength, byteorder="big")


def shuffled_md5(value: str) -> str:
    _hash = md5(value.encode("utf-8")).hexdigest()
    return _hash[8:16] + _hash[0:8] + _hash[24:32] + _hash[16:24]


TUYA_PASSWORD_INNER_CIPHER = Cipher(
    algorithms.AES(
        bytearray([36, 78, 109, 138, 86, 172, 135, 145, 36, 67, 45, 139, 108, 188, 162, 196])
    ),
    modes.CBC(bytearray([119, 36, 86, 242, 167, 102, 76, 243, 57, 44, 53, 151, 233, 62, 87, 71])),
    backend=openssl_backend,
)

DEFAULT_TUYA_HEADERS = {"User-Agent": "TY-UA=APP/Android/2.4.0/SDK/null"}

SIGNATURE_RELEVANT_PARAMETERS = {
    "a",
    "v",
    "lat",
    "lon",
    "lang",
    "deviceId",
    "appVersion",
    "ttid",
    "isH5",
    "h5Token",
    "os",
    "clientId",
    "postData",
    "time",
    "requestId",
    "et",
    "n4h5",
    "sid",
    "sp",
}

DEFAULT_TUYA_QUERY_PARAMS = {
    "appVersion": "2.4.0",
    "deviceId": "",
    "platform": "sdk_gphone64_arm64",
    "clientId": "yx5v9uc3ef9wg3v9atje",
    "lang": "en",
    "osSystem": "12",
    "os": "Android",
    "timeZoneId": "Europe/London",
    "ttid": "android",
    "et": "0.0.1",
    "sdkVersion": "3.0.8cAnker",
}


class TuyaAPISession:
    session_id = None

    def __init__(
        self,
        session: aiohttp.ClientSession,
        username: str,
        region: str,
        timezone: str,
        phone_code: str,
    ):
        self.session = session
        self.headers = DEFAULT_TUYA_HEADERS.copy()
        self.default_query_params = DEFAULT_TUYA_QUERY_PARAMS.copy()
        self.default_query_params["deviceId"] = self.generate_new_device_id()
        self.default_query_params["timeZoneId"] = timezone
        self.username = username
        self.country_code = phone_code
        self.base_url = {
            "AZ": "https://a1.tuyaus.com",
            "AY": "https://a1.tuyacn.com",
            "IN": "https://a1.tuyain.com",
            "EU": "https://a1.tuyaeu.com",
        }.get(region, "https://a1.tuyaeu.com")

    @staticmethod
    def generate_new_device_id() -> str:
        expected_length = 44
        base64_characters = string.ascii_letters + string.digits
        device_id_dependent_part = "8534c8ec0ed0"
        return device_id_dependent_part + "".join(
            random.choice(base64_characters)
            for _ in range(expected_length - len(device_id_dependent_part))
        )

    @staticmethod
    def get_signature(query_params: dict[str, str], encoded_post_data: str) -> str:
        query_params = query_params.copy()
        if encoded_post_data:
            query_params["postData"] = encoded_post_data
        sorted_pairs = sorted(query_params.items())
        filtered_pairs = filter(
            lambda p: p[0] and p[0] in SIGNATURE_RELEVANT_PARAMETERS, sorted_pairs
        )
        mapped_pairs = (
            p[0] + "=" + (shuffled_md5(p[1]) if p[0] == "postData" else p[1])
            for p in filtered_pairs
        )
        message = "||".join(mapped_pairs)
        return hmac.HMAC(
            key=EUFY_HMAC_KEY, msg=message.encode("utf-8"), digestmod=sha256
        ).hexdigest()

    async def _request(
        self,
        action: str,
        version: str = "1.0",
        data: dict[str, str] | None = None,
        query_params: dict[str, str] | None = None,
        _requires_session: bool = True,
    ) -> Any:
        if not self.session_id and _requires_session:
            await self.acquire_session()

        current_time = time.time()
        request_id = uuid.uuid4()
        extra_query_params = {
            "time": str(int(current_time)),
            "requestId": str(request_id),
            "a": action,
            "v": version,
            **(query_params or {}),
        }
        query_params = {**self.default_query_params, **extra_query_params}
        encoded_post_data = json.dumps(data, separators=(",", ":")) if data else ""
        resp = await self.session.post(
            self.base_url + "/api.json",
            headers=self.headers,
            params={
                **query_params,
                "sign": self.get_signature(query_params, encoded_post_data),
            },
            data={"postData": encoded_post_data} if encoded_post_data else None,
            raise_for_status=True,
        )
        resp_json = await resp.json()
        if "result" not in resp_json:
            raise Exception(
                f"No 'result' key in the response - the entire response is {resp_json}."
            )
        return resp_json["result"]

    async def request_token(self, username: str, country_code: str) -> Any:
        return await self._request(
            action="tuya.m.user.uid.token.create",
            data={"uid": username, "countryCode": country_code},
            _requires_session=False,
        )

    def determine_password(self, username: str) -> str:
        new_uid = username
        padded_size = 16 * math.ceil(len(new_uid) / 16)
        password_uid = new_uid.zfill(padded_size)
        encryptor = TUYA_PASSWORD_INNER_CIPHER.encryptor()
        encrypted_uid = encryptor.update(password_uid.encode("utf8"))
        encrypted_uid += encryptor.finalize()
        return md5(encrypted_uid.hex().upper().encode("utf-8")).hexdigest()

    async def request_session(self, username: str, country_code: str) -> Any:
        password = self.determine_password(username)
        token_response = await self.request_token(username, country_code)
        encrypted_password = unpadded_rsa(
            key_exponent=int(token_response["exponent"]),
            key_n=int(token_response["publicKey"]),
            plaintext=password.encode("utf-8"),
        )
        data = {
            "uid": username,
            "createGroup": True,
            "ifencrypt": 1,
            "passwd": encrypted_password.hex(),
            "countryCode": country_code,
            "options": '{"group": 1}',
            "token": token_response["token"],
        }
        return await self._request(
            action="tuya.m.user.uid.password.login.reg",
            data=data,
            _requires_session=False,
        )

    async def acquire_session(self) -> None:
        session_response = await self.request_session(self.username, self.country_code)
        self.session_id = self.default_query_params["sid"] = session_response["sid"]
        self.base_url = session_response["domain"]["mobileApiUrl"]

    def get_device(self, device_id: str) -> Any:
        return self._request(action="tuya.m.device.get", version="1.0", data={"devId": device_id})
