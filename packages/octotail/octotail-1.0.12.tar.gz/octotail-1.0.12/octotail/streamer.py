"""Streamer actor."""

import asyncio as aio
import json
import multiprocessing as mp
import typing as t

import websockets.client
from returns.result import Success, safe
from websockets.exceptions import ConnectionClosedError

from octotail.browser import RANDOM_UA
from octotail.mitm import WsSub
from octotail.utils import log

WS_HEADERS = {
    "User-Agent": RANDOM_UA,
    "Origin": "https://github.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "websocket",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}


class OutputItem(t.NamedTuple):
    """Holds an output item."""

    job_name: str
    lines: list[str]


class WebsocketClosed:
    """Indicates the closure of a websocket."""


def run_streamer(ws_sub: WsSub, queue: mp.Queue) -> mp.Process:
    process = mp.Process(target=_streamer, args=(ws_sub, queue))
    process.start()
    return process


def _streamer(ws_sub: WsSub, queue: mp.Queue) -> None:
    loop = aio.new_event_loop()
    aio.set_event_loop(loop)
    try:
        loop.run_until_complete(_stream_it(ws_sub, queue))
    except KeyboardInterrupt:
        loop.close()


async def _stream_it(ws_sub: WsSub, queue: mp.Queue) -> None:
    ws_url = "wss://" + ws_sub.url.removeprefix("https://")
    job_name = ws_sub.job_name or "unknown"

    async for websocket in websockets.client.connect(ws_url, extra_headers=WS_HEADERS):
        try:
            await websocket.send(ws_sub.subs)
            async for msg in websocket:
                _extract_lines(msg).apply(
                    Success(lambda _lines: queue.put(OutputItem(job_name, _lines)))
                )
        except aio.CancelledError:
            log("cancelled")
            if websocket:
                await websocket.close()
            return
        except ConnectionClosedError as e:
            log(f"fatal error during websockets connection: {e}")
            queue.put(WebsocketClosed())


@safe
def _extract_lines(msg: str | bytes) -> list[str]:
    _msg = msg.decode() if isinstance(msg, bytes) else msg
    return [line_obj["line"] for line_obj in json.loads(_msg)["data"]["data"]["lines"]]
