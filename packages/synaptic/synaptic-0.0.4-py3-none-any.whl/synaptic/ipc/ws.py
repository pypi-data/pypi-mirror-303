from typing import Dict

import websockets
import logging  as log

from synaptic.ipc import IPC, BaseConfig, IPCConfig
from synaptic.serialization import serializers as SERIALIZATION_MAP


class WebSocketConfig(BaseConfig):
    url: str
    sse: bool


class WSIPC(IPC):
    def __init__(self, settings: IPCConfig) -> None:
        self.settings = settings
        self.websocket = None
        self._local_store: Dict[str, any] = {}
        self.host, self.port = self.settings.url.host, self.settings.url.port

    async def handler(self, ws: websockets.WebSocketServerProtocol, path: str) -> None:
        """Callback function for incoming samples."""
        log.info(f"Received message: {await ws.recv()}")
        self._local_store[path] = await self._load_state()
        await ws.send("Message received")

    async def initialize(self) -> None:
        try:
            self.websocket: websockets.WebSocketClientProtocol = await websockets.connect(str(self.settings.url))
            log.info("WebSocket connection established successfully")
        except Exception as e:
            log.error(f"Error establishing WebSocket connection: {e}")
            self.listener = websockets.serve(self.handler, self.host, self.port)
            log.info(f"WebSocket server started at {self.host}:{self.port}")
            

    async def cleanup(self) -> None:
        try:
            if self.websocket is not None:
                await self.websocket.close()
                self.websocket = None
            log.info("WebSocket cleanup completed successfully")
        except Exception as e:
            log.error(f"Error during WebSocket cleanup: {e}")

    async def publish_state(self, state: Dict) -> None:
        try:
            serializer = SERIALIZATION_MAP[self.settings.serialization_protocol]()
            serialized = serializer.tobytes(state)
            await self.websocket.send(serialized)
            log.info("State published to WebSocket")
        except Exception as e:
            log.error(f"Error publishing state to WebSocket: {e}")

    async def _load_state(self) -> Dict:
        try:
            data = await self.websocket.recv()
            if self.settings.serialization_protocol not in SERIALIZATION_MAP:
                raise ValueError(f"Unsupported serialization protocol: {self.settings.serialization_protocol}")
            serializer = SERIALIZATION_MAP[self.settings.serialization_protocol]()
            return serializer.frombytes(data)
        except Exception as e:
            log.error(f"Error loading state: {e}")
            raise
