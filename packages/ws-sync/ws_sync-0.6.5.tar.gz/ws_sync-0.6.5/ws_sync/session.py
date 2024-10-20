from __future__ import annotations
from logging import Logger
import traceback
from typing import Callable
from contextvars import ContextVar

from starlette.websockets import WebSocket, WebSocketDisconnect

from .utils import nonblock_call

# session context
session_context: ContextVar[Session] = ContextVar("session_context")
"""Per-task session context. Within concurrent async tasks, this context variable can be used to access the current Session object."""


class Session:
    """
    This is a counter-part to the SessionManager in the frontend.
    There should be one instance of this class per user session, even across reconnects of the websocket. This means the states that belong to the user session should be subscribed to the events of this class.
    It defines a simple state-syncing protocol between the frontend and the backend, every event being of type {type: str, data: any}.
    """

    def __init__(self, logger: Logger = None):
        self.ws = None
        self.event_handlers: dict[str, Callable] = {}  # triggered on event
        self.init_handlers: list[Callable] = []  # triggered on connection init
        self.logger = logger
        self.state = None  # user-assigned state associated with the session

    @property
    def is_connected(self):
        return self.ws is not None

    # ===== Low-Level: Register Event Callbacks =====#
    def register_event(self, event: str, callback: Callable):
        if event in self.event_handlers:
            # raise Exception(f"Event {event} already has a subscriber.")
            if self.logger:
                self.logger.warning(f"Event {event} already has a subscriber.")
        self.event_handlers[event] = callback

    def deregister_event(self, event: str):
        if event not in self.event_handlers:
            raise Exception(f"Event {event} has no subscriber.")
        del self.event_handlers[event]

    def register_init(self, callback: Callable):
        self.init_handlers.append(callback)

    # ===== Low-Level: Networking =====#
    async def new_connection(self, ws: WebSocket):
        if self.ws is not None:
            if self.logger:
                self.logger.warning("Overwriting existing websocket.")
            await self.disconnect()
        self.ws = ws

        await self.init()

    async def disconnect(
        self,
        message="Seems like you're logged in somewhere else. If this is a mistake, please refresh the page.",
        ws: WebSocket = None,
    ):
        if ws:
            self.ws = ws
        await self.send("_DISCONNECT", message)
        await self.ws.close()
        self.ws = None

    async def init(self):
        for handler in self.init_handlers:
            await nonblock_call(handler)

    async def send(self, event: str, data: any):
        if self.ws is None:
            return
        try:
            await self.ws.send_json({"type": event, "data": data})
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error sending event {event}: {e}")

    async def send_binary(self, event: str, metadata: dict[str, any], data: bytes):
        if self.ws is None:
            return
        try:
            await self.ws.send_json(
                {"type": "_BIN_META", "data": {"type": event, "metadata": metadata}}
            )
            await self.ws.send_bytes(data)
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error sending binary event {event}: {e}")

    async def handle_connection(self):
        assert self.ws is not None
        try:
            while True:
                full_data = await self.ws.receive_json()
                event = full_data.get("type")
                data = full_data.get("data")

                if event == "_BIN_META":
                    # unwrap and construct the original event
                    event = data.get("type")
                    metadata = data.get("metadata")
                    bindata = await self.ws.receive_bytes()
                    data = {"data": bindata, **metadata}

                if event in self.event_handlers:
                    handler = self.event_handlers[event]
                    await nonblock_call(handler, data)
                else:
                    if self.logger:
                        self.logger.warning(
                            f"Received event {event} but no subscriber was found."
                        )
        except WebSocketDisconnect:
            if self.logger:
                self.logger.info("websocket disconnected")
        except Exception:
            if self.logger:
                self.logger.error(
                    f"Error while handling connection: {traceback.format_exc()}"
                )
        finally:
            try:
                ws = self.ws
                self.ws = None
                await ws.close()
            except:
                pass

    # ===== High-Level: Context Manager =====#
    def __enter__(self):
        self.token = session_context.set(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        session_context.reset(self.token)
        self.token = None
