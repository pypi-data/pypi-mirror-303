import asyncio
import contextlib
import json
import logging
import socket
from collections.abc import AsyncGenerator
from dataclasses import dataclass
from hashlib import md5

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_LOGGER = logging.getLogger(__name__)

UDP_KEY = md5(b"yGAdlopoPVldABfn").digest()


@dataclass
class LocalDiscovery:
    device_id: str
    ip: str


def _payload_to_discovery(payload: bytes) -> LocalDiscovery | None:
    try:
        decoded = json.loads(payload.decode("utf-8"))
    except ValueError:
        return None

    if not isinstance(decoded, dict):
        return None

    if not (device_id := decoded.get("gwId")):
        return None

    if not (ip := decoded.get("ip")):
        return None

    return LocalDiscovery(
        device_id=device_id,
        ip=ip,
    )


async def discover() -> AsyncGenerator[LocalDiscovery, None]:
    loop = asyncio.get_running_loop()

    cipher = Cipher(algorithms.AES(UDP_KEY), modes.ECB(), default_backend())  # noqa: S305

    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.setblocking(False)
    listener.bind(("0.0.0.0", 6666))

    listener_aes = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener_aes.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener_aes.setblocking(False)
    listener_aes.bind(("0.0.0.0", 6667))

    try:
        datagram = asyncio.create_task(loop.sock_recvfrom(listener, 2048))
        datagram_aes = asyncio.create_task(loop.sock_recvfrom(listener_aes, 2048))

        while True:
            (done, _) = await asyncio.wait(
                (datagram, datagram_aes), return_when=asyncio.FIRST_COMPLETED
            )
            if datagram in done:
                data, _ = await datagram
                if discovery := _payload_to_discovery(data):
                    yield discovery
                datagram = asyncio.create_task(loop.sock_recvfrom(listener, 2048))

            if datagram_aes in done:
                data_aes, _ = await datagram_aes
                decryptor = cipher.decryptor()
                padded_data = decryptor.update(data_aes[20:-8]) + decryptor.finalize()
                data = padded_data[: -ord(padded_data[len(padded_data) - 1 :])]

                if discovery := _payload_to_discovery(data):
                    yield discovery

                datagram_aes = asyncio.create_task(loop.sock_recvfrom(listener_aes, 2048))

    finally:
        if not datagram.done():
            datagram.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await datagram

        if not datagram_aes.done():
            datagram_aes.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await datagram_aes


async def find(device_id: str, timeout: int = 10) -> LocalDiscovery | None:
    try:
        async with asyncio.timeout(timeout):
            async with contextlib.aclosing(discover()) as discoveries:
                async for discovery in discoveries:
                    if discovery.device_id == device_id:
                        return discovery

    except TimeoutError:
        pass

    return None
