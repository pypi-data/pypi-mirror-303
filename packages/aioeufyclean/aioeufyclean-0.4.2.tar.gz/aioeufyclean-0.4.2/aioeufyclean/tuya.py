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

# Based on portions of https://github.com/codetheweb/tuyapi/
#
# MIT License
#
# Copyright (c) 2017 Max Isom
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import asyncio
import base64
import contextlib
import json
import logging
import struct
import time
from collections.abc import Callable
from typing import Any, Self

from cryptography.hazmat.backends.openssl import backend as openssl_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hashes import MD5, Hash
from cryptography.hazmat.primitives.padding import PKCS7

from .exceptions import (
    ConnectionException,
    ConnectionFailed,
    ConnectionTimeoutException,
    InvalidKey,
    InvalidMessage,
    MessageDecodeFailed,
)

_LOGGER = logging.getLogger(__name__)

MESSAGE_PREFIX_FORMAT = ">IIII"
MESSAGE_SUFFIX_FORMAT = ">II"
MAGIC_PREFIX = 0x000055AA
MAGIC_SUFFIX = 0x0000AA55
MAGIC_SUFFIX_BYTES = struct.pack(">I", MAGIC_SUFFIX)
CRC_32_TABLE = [
    0x00000000,
    0x77073096,
    0xEE0E612C,
    0x990951BA,
    0x076DC419,
    0x706AF48F,
    0xE963A535,
    0x9E6495A3,
    0x0EDB8832,
    0x79DCB8A4,
    0xE0D5E91E,
    0x97D2D988,
    0x09B64C2B,
    0x7EB17CBD,
    0xE7B82D07,
    0x90BF1D91,
    0x1DB71064,
    0x6AB020F2,
    0xF3B97148,
    0x84BE41DE,
    0x1ADAD47D,
    0x6DDDE4EB,
    0xF4D4B551,
    0x83D385C7,
    0x136C9856,
    0x646BA8C0,
    0xFD62F97A,
    0x8A65C9EC,
    0x14015C4F,
    0x63066CD9,
    0xFA0F3D63,
    0x8D080DF5,
    0x3B6E20C8,
    0x4C69105E,
    0xD56041E4,
    0xA2677172,
    0x3C03E4D1,
    0x4B04D447,
    0xD20D85FD,
    0xA50AB56B,
    0x35B5A8FA,
    0x42B2986C,
    0xDBBBC9D6,
    0xACBCF940,
    0x32D86CE3,
    0x45DF5C75,
    0xDCD60DCF,
    0xABD13D59,
    0x26D930AC,
    0x51DE003A,
    0xC8D75180,
    0xBFD06116,
    0x21B4F4B5,
    0x56B3C423,
    0xCFBA9599,
    0xB8BDA50F,
    0x2802B89E,
    0x5F058808,
    0xC60CD9B2,
    0xB10BE924,
    0x2F6F7C87,
    0x58684C11,
    0xC1611DAB,
    0xB6662D3D,
    0x76DC4190,
    0x01DB7106,
    0x98D220BC,
    0xEFD5102A,
    0x71B18589,
    0x06B6B51F,
    0x9FBFE4A5,
    0xE8B8D433,
    0x7807C9A2,
    0x0F00F934,
    0x9609A88E,
    0xE10E9818,
    0x7F6A0DBB,
    0x086D3D2D,
    0x91646C97,
    0xE6635C01,
    0x6B6B51F4,
    0x1C6C6162,
    0x856530D8,
    0xF262004E,
    0x6C0695ED,
    0x1B01A57B,
    0x8208F4C1,
    0xF50FC457,
    0x65B0D9C6,
    0x12B7E950,
    0x8BBEB8EA,
    0xFCB9887C,
    0x62DD1DDF,
    0x15DA2D49,
    0x8CD37CF3,
    0xFBD44C65,
    0x4DB26158,
    0x3AB551CE,
    0xA3BC0074,
    0xD4BB30E2,
    0x4ADFA541,
    0x3DD895D7,
    0xA4D1C46D,
    0xD3D6F4FB,
    0x4369E96A,
    0x346ED9FC,
    0xAD678846,
    0xDA60B8D0,
    0x44042D73,
    0x33031DE5,
    0xAA0A4C5F,
    0xDD0D7CC9,
    0x5005713C,
    0x270241AA,
    0xBE0B1010,
    0xC90C2086,
    0x5768B525,
    0x206F85B3,
    0xB966D409,
    0xCE61E49F,
    0x5EDEF90E,
    0x29D9C998,
    0xB0D09822,
    0xC7D7A8B4,
    0x59B33D17,
    0x2EB40D81,
    0xB7BD5C3B,
    0xC0BA6CAD,
    0xEDB88320,
    0x9ABFB3B6,
    0x03B6E20C,
    0x74B1D29A,
    0xEAD54739,
    0x9DD277AF,
    0x04DB2615,
    0x73DC1683,
    0xE3630B12,
    0x94643B84,
    0x0D6D6A3E,
    0x7A6A5AA8,
    0xE40ECF0B,
    0x9309FF9D,
    0x0A00AE27,
    0x7D079EB1,
    0xF00F9344,
    0x8708A3D2,
    0x1E01F268,
    0x6906C2FE,
    0xF762575D,
    0x806567CB,
    0x196C3671,
    0x6E6B06E7,
    0xFED41B76,
    0x89D32BE0,
    0x10DA7A5A,
    0x67DD4ACC,
    0xF9B9DF6F,
    0x8EBEEFF9,
    0x17B7BE43,
    0x60B08ED5,
    0xD6D6A3E8,
    0xA1D1937E,
    0x38D8C2C4,
    0x4FDFF252,
    0xD1BB67F1,
    0xA6BC5767,
    0x3FB506DD,
    0x48B2364B,
    0xD80D2BDA,
    0xAF0A1B4C,
    0x36034AF6,
    0x41047A60,
    0xDF60EFC3,
    0xA867DF55,
    0x316E8EEF,
    0x4669BE79,
    0xCB61B38C,
    0xBC66831A,
    0x256FD2A0,
    0x5268E236,
    0xCC0C7795,
    0xBB0B4703,
    0x220216B9,
    0x5505262F,
    0xC5BA3BBE,
    0xB2BD0B28,
    0x2BB45A92,
    0x5CB36A04,
    0xC2D7FFA7,
    0xB5D0CF31,
    0x2CD99E8B,
    0x5BDEAE1D,
    0x9B64C2B0,
    0xEC63F226,
    0x756AA39C,
    0x026D930A,
    0x9C0906A9,
    0xEB0E363F,
    0x72076785,
    0x05005713,
    0x95BF4A82,
    0xE2B87A14,
    0x7BB12BAE,
    0x0CB61B38,
    0x92D28E9B,
    0xE5D5BE0D,
    0x7CDCEFB7,
    0x0BDBDF21,
    0x86D3D2D4,
    0xF1D4E242,
    0x68DDB3F8,
    0x1FDA836E,
    0x81BE16CD,
    0xF6B9265B,
    0x6FB077E1,
    0x18B74777,
    0x88085AE6,
    0xFF0F6A70,
    0x66063BCA,
    0x11010B5C,
    0x8F659EFF,
    0xF862AE69,
    0x616BFFD3,
    0x166CCF45,
    0xA00AE278,
    0xD70DD2EE,
    0x4E048354,
    0x3903B3C2,
    0xA7672661,
    0xD06016F7,
    0x4969474D,
    0x3E6E77DB,
    0xAED16A4A,
    0xD9D65ADC,
    0x40DF0B66,
    0x37D83BF0,
    0xA9BCAE53,
    0xDEBB9EC5,
    0x47B2CF7F,
    0x30B5FFE9,
    0xBDBDF21C,
    0xCABAC28A,
    0x53B39330,
    0x24B4A3A6,
    0xBAD03605,
    0xCDD70693,
    0x54DE5729,
    0x23D967BF,
    0xB3667A2E,
    0xC4614AB8,
    0x5D681B02,
    0x2A6F2B94,
    0xB40BBE37,
    0xC30C8EA1,
    0x5A05DF1B,
    0x2D02EF8D,
]


class TuyaCipher:
    """Tuya cryptographic helpers."""

    def __init__(self, key: str, version: tuple[int, int]):
        """Initialize the cipher."""
        self.version = version
        self.key = key
        self.cipher = Cipher(
            algorithms.AES(key.encode("ascii")),
            modes.ECB(),  # noqa: S305
            backend=openssl_backend,
        )

    def get_prefix_size_and_validate(self, command: Message, encrypted_data: bytes) -> int:
        try:
            version = tuple(map(int, encrypted_data[:3].decode("utf8").split(".")))
        except UnicodeDecodeError:
            version = (0, 0)
        if version != self.version:
            return 0
        if version < (3, 3):
            actual_hash = encrypted_data[3:19].decode("ascii")
            expected_hash = self.hash(encrypted_data[19:])
            if actual_hash != expected_hash:
                return 0
            return 19
        elif command in (Message.SET_COMMAND, Message.GRATUITOUS_UPDATE):
            _, sequence, __, ___ = struct.unpack_from(">IIIH", encrypted_data, 3)
            return 15
        return 0

    def decrypt(self, command: Message, data: bytes) -> bytes:
        prefix_size = self.get_prefix_size_and_validate(command, data)
        data = data[prefix_size:]
        decryptor = self.cipher.decryptor()
        if self.version < (3, 3):
            data = base64.b64decode(data)
        decrypted_data = decryptor.update(data)
        decrypted_data += decryptor.finalize()
        unpadder = PKCS7(128).unpadder()
        unpadded_data = unpadder.update(decrypted_data)
        unpadded_data += unpadder.finalize()

        return unpadded_data

    def encrypt(self, command: int, data: bytes) -> bytes:
        encrypted_data = b""
        if data:
            padder = PKCS7(128).padder()
            padded_data = padder.update(data)
            padded_data += padder.finalize()
            encryptor = self.cipher.encryptor()
            encrypted_data = encryptor.update(padded_data)
            encrypted_data += encryptor.finalize()

        prefix = ".".join(map(str, self.version)).encode("utf8")
        if self.version < (3, 3):
            payload = base64.b64encode(encrypted_data)
            payload_hash = self.hash(payload)
            prefix += payload_hash.encode("utf8")
        else:
            payload = encrypted_data
            if command in (Message.SET_COMMAND, Message.GRATUITOUS_UPDATE):
                prefix += b"\x00" * 12
            else:
                prefix = b""

        return prefix + payload

    def hash(self, data: bytes) -> str:
        digest = Hash(MD5(), backend=openssl_backend)  # noqa: S303
        to_hash = "data={}||lpv={}||{}".format(
            data.decode("ascii"), ".".join(map(str, self.version)), self.key
        )
        digest.update(to_hash.encode("utf8"))
        intermediate = digest.finalize().hex()
        return intermediate[8:24]


def crc(data: bytes) -> int:
    """Calculate the Tuya-flavored CRC of some data."""
    c = 0xFFFFFFFF
    for b in data:
        c = (c >> 8) ^ CRC_32_TABLE[(c ^ b) & 255]

    return c ^ 0xFFFFFFFF


class Message:
    PING_COMMAND = 0x09
    GET_COMMAND = 0x0A
    SET_COMMAND = 0x07
    GRATUITOUS_UPDATE = 0x08

    def __init__(
        self,
        command: int,
        payload: dict[str, Any] | bytes | None = None,
        sequence: int | None = None,
        encrypt_for: TuyaDevice | None = None,
    ):
        if payload is None:
            payload = b""
        self.payload = payload
        self.command = command
        if sequence is None:
            # Use millisecond process time as the sequence number. Not ideal,
            # but good for one month's continuous connection time though.
            sequence = int(time.perf_counter() * 1000) & 0xFFFFFFFF
        self.sequence = sequence
        self.encrypt = False
        self.device = None
        if encrypt_for is not None:
            self.device = encrypt_for
            self.encrypt = True

    def __repr__(self) -> str:
        return "{}({}, {!r}, {!r}, {})".format(
            self.__class__.__name__,
            hex(self.command),
            self.payload,
            self.sequence,
            f"<Device {self.device}>" if self.device else None,
        )

    def hex(self) -> str:
        return self.to_bytes().hex()

    def to_bytes(self) -> bytes:
        if isinstance(self.payload, dict):
            payload_data = json.dumps(self.payload, separators=(",", ":")).encode("utf-8")
        elif not isinstance(self.payload, bytes):
            payload_data = self.payload.encode("utf8")
        else:
            payload_data = self.payload

        if self.encrypt:
            assert self.device
            payload_data = self.device.cipher.encrypt(self.command, payload_data)

        payload_size = len(payload_data) + struct.calcsize(MESSAGE_SUFFIX_FORMAT)

        header = struct.pack(
            MESSAGE_PREFIX_FORMAT,
            MAGIC_PREFIX,
            self.sequence,
            self.command,
            payload_size,
        )
        if self.device and self.device.version >= (3, 3):
            checksum = crc(header + payload_data)
        else:
            checksum = crc(payload_data)
        footer = struct.pack(MESSAGE_SUFFIX_FORMAT, checksum, MAGIC_SUFFIX)
        return header + payload_data + footer

    __bytes__ = bytes

    @classmethod
    def from_bytes(cls, data: bytes, cipher: TuyaCipher) -> Self:
        try:
            prefix, sequence, command, payload_size = struct.unpack_from(
                MESSAGE_PREFIX_FORMAT, data
            )
        except struct.error as e:
            raise InvalidMessage("Invalid message header format.") from e
        if prefix != MAGIC_PREFIX:
            raise InvalidMessage("Magic prefix missing from message.")

        # check for an optional return code
        header_size = struct.calcsize(MESSAGE_PREFIX_FORMAT)
        try:
            (return_code,) = struct.unpack_from(">I", data, header_size)
        except struct.error as e:
            raise InvalidMessage("Unable to unpack return code.") from e
        if return_code >> 8:
            payload_data = data[
                header_size : header_size + payload_size - struct.calcsize(MESSAGE_SUFFIX_FORMAT)
            ]
            return_code = None
        else:
            payload_data = data[
                header_size + struct.calcsize(">I") : header_size
                + payload_size
                - struct.calcsize(MESSAGE_SUFFIX_FORMAT)
            ]

        try:
            expected_crc, suffix = struct.unpack_from(
                MESSAGE_SUFFIX_FORMAT,
                data,
                header_size + payload_size - struct.calcsize(MESSAGE_SUFFIX_FORMAT),
            )
        except struct.error as e:
            raise InvalidMessage("Invalid message suffix format.") from e
        if suffix != MAGIC_SUFFIX:
            raise InvalidMessage("Magic suffix missing from message")

        actual_crc = crc(
            data[: header_size + payload_size - struct.calcsize(MESSAGE_SUFFIX_FORMAT)]
        )
        if expected_crc != actual_crc:
            raise InvalidMessage("CRC check failed")

        payload = None
        if payload_data:
            with contextlib.suppress(ValueError):
                payload_data = cipher.decrypt(command, payload_data)
            try:
                payload_text = payload_data.decode("utf8")
            except UnicodeDecodeError as e:
                _LOGGER.debug(payload_data.hex())
                _LOGGER.error(e)
                raise MessageDecodeFailed from e
            try:
                payload = json.loads(payload_text)
            except json.decoder.JSONDecodeError as e:
                # data may be encrypted
                _LOGGER.debug(payload_data.hex())
                _LOGGER.error(e)
                raise MessageDecodeFailed from e

        return cls(command, payload, sequence)


class TuyaDevice:
    """Represents a generic Tuya device."""

    PING_INTERVAL = 10

    def __init__(
        self,
        unique_id: str,
        host: str,
        local_key: str,
        port: int = 6668,
        gateway_id: str | None = None,
        version: tuple[int, int] = (3, 3),
        timeout: int = 10,
    ):
        """Initialize the device."""
        self.unique_id = unique_id
        self.host = host
        self.port = port
        if not gateway_id:
            gateway_id = self.unique_id
        self.gateway_id = gateway_id
        self.version = version
        self.timeout = timeout
        self.last_pong = 0.0

        if len(local_key) != 16:
            raise InvalidKey("Local key should be a 16-character string")

        self.cipher = TuyaCipher(local_key, self.version)
        self.writer: asyncio.StreamWriter | None = None
        self._futures: dict[int, asyncio.Future[Message]] = {}
        self._dps: dict[str, str | int | float] = {}
        self._connected = False
        self._connecting_lock = asyncio.Lock()
        self._availability_callbacks: set[Callable[[bool], None]] = set()
        self._state_callbacks: set[Callable[[Any], None]] = set()

    def __str__(self) -> str:
        return f"{self.unique_id} ({self.host}:{self.port})"

    def async_add_availability_callback(
        self, callback: Callable[[Any], None]
    ) -> Callable[[], None]:
        self._availability_callbacks.add(callback)

        def _() -> None:
            self._availability_callbacks.discard(callback)

        return _

    def async_add_state_callback(self, callback: Callable[[Any], None]) -> Callable[[], None]:
        self._state_callbacks.add(callback)

        def _() -> None:
            self._state_callbacks.discard(callback)

        return _

    async def async_connect(self) -> None:
        async with self._connecting_lock:
            if self._connected:
                return

            _LOGGER.debug("Starting connection to %s:%s", self.host, self.port)

            try:
                self.reader, self.writer = await asyncio.wait_for(
                    asyncio.open_connection(host=self.host, port=self.port), self.timeout
                )
            except ConnectionRefusedError as e:
                raise ConnectionFailed(
                    f"Could not start connection to {self.host}:{self.port} - "
                    "device is offline or ip is incorrect"
                ) from e
            except TimeoutError as e:
                raise ConnectionTimeoutException("Connection timed out") from e

            self._connected = True
            for callback in self._availability_callbacks:
                callback(True)

        await self._async_ping()

    def _async_disconnect(self) -> None:
        _LOGGER.debug(f"Disconnected from {self}")
        self._connected = False
        for callback in self._availability_callbacks:
            callback(False)
        self.last_pong = 0
        if self.writer is not None:
            self.writer.close()
            self.writer = None

    async def async_poll(self) -> None:
        payload = {"gwId": self.gateway_id, "devId": self.unique_id}
        maybe_self = None if self.version < (3, 3) else self
        message = Message(Message.GET_COMMAND, payload, encrypt_for=maybe_self)
        await self.async_call(message)

    async def async_set(self, dps: dict[str, Any]) -> Message:
        t = int(time.time())
        payload = {"devId": self.unique_id, "uid": "", "t": t, "dps": dps}
        message = Message(Message.SET_COMMAND, payload, encrypt_for=self)
        return await self.async_call(message)

    async def _async_ping(self) -> None:
        self.last_ping = time.time()
        maybe_self = None if self.version < (3, 3) else self
        message = Message(Message.PING_COMMAND, sequence=0, encrypt_for=maybe_self)
        await self.async_send(message)

    async def async_update_state(self, state_message: Message) -> None:
        _LOGGER.debug("Received updated state %s: %s", self, state_message)
        assert isinstance(state_message.payload, dict)
        self._dps.update(state_message.payload["dps"])
        self.state = self._handle_state_update(self._dps)
        _LOGGER.debug("New vacuum state %s: %s", self, self.state)
        for callback in self._state_callbacks:
            callback(self.state)

    def _handle_state_update(self, dps: dict[str, Any]) -> Any:
        raise NotImplementedError

    async def _async_read_message(self) -> Message | None:
        try:
            response_data = await self.reader.readuntil(MAGIC_SUFFIX_BYTES)
        except OSError as e:
            _LOGGER.error(f"Connection to {self} failed: {e}")
            self._async_disconnect()
            return None

        try:
            message = Message.from_bytes(response_data, self.cipher)

        except InvalidMessage as e:
            _LOGGER.error(f"Invalid message from {self}: {e}")
            self._async_disconnect()
            return None

        except MessageDecodeFailed:
            _LOGGER.error(f"Failed to decrypt message from {self}")
            self._async_disconnect()
            return None

        _LOGGER.debug(f"Received message from {self}: {message}")
        return message

    async def async_process_messages(self) -> None:
        while True:
            try:
                await self.async_connect()
            except ConnectionFailed:
                _LOGGER.debug("Could not connect to %s:%s", self.host, self.port)
                await asyncio.sleep(10)

            sleep_fut = asyncio.create_task(asyncio.sleep(self.PING_INTERVAL))
            message_fut = asyncio.create_task(self._async_read_message())

            try:
                while self._connected:
                    (done, pending) = await asyncio.wait(
                        [message_fut, sleep_fut], return_when=asyncio.FIRST_COMPLETED
                    )

                    if message_fut in done:
                        message = await message_fut

                        if not message:
                            break

                        if message.command in (Message.GET_COMMAND, Message.GRATUITOUS_UPDATE):
                            await self.async_update_state(message)

                        elif message.command == Message.PING_COMMAND:
                            self.last_pong = time.time()

                        if future := self._futures.pop(message.sequence, None):
                            future.set_result(message)

                        message_fut = asyncio.create_task(self._async_read_message())

                    if sleep_fut in done:
                        if self.last_pong < self.last_ping:
                            self._async_disconnect()
                            break
                        await sleep_fut
                        await self._async_ping()
                        sleep_fut = asyncio.create_task(asyncio.sleep(self.PING_INTERVAL))
            finally:
                if not message_fut.done():
                    message_fut.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await message_fut

                if not sleep_fut.done():
                    sleep_fut.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await message_fut

    async def async_send(self, message: Message, retries: int = 4) -> None:
        await self.async_connect()
        _LOGGER.debug(f"Sending to {self}: {message}")
        try:
            assert self.writer
            self.writer.write(message.to_bytes())
        except (TimeoutError, OSError) as e:
            if retries == 0:
                raise ConnectionException(f"Failed to send data to {self}") from e
            await self.async_connect()
            await self.async_send(message, retries=retries - 1)

    async def async_call(self, message: Message, retries: int = 4) -> Message:
        fut = self._futures[message.sequence] = asyncio.Future()

        try:
            await self.async_send(message, retries=retries)
        except ConnectionException:
            self._futures.pop(message.sequence, None)

        try:
            return await asyncio.wait_for(fut, 10)
        except TimeoutError:
            self._futures.pop(message.sequence, None)
            raise
