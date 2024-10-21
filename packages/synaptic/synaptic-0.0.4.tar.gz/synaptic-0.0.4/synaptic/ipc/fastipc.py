import logging
import time
from threading import Thread
from typing import Any, Dict

import requests
import uvicorn
from fastapi import FastAPI, HTTPException

from synaptic.ipc import IPC, IPCConfig
from synaptic.serialization import serializers


class FastIPC(IPC):
    def __init__(self, settings: IPCConfig) -> None:
        self.settings = settings
        self.local_store: Dict[str, Any] = {}
        self.session = requests.Session()  # For persistent connections
        self.server_thread = None
        self.app = None
        self.host, self.port = self.settings.url.host, self.settings.url.port
        self.serializer = serializers[self.settings.serializer]()

    def start_server(self) -> None:
        self.app = FastAPI()

        @self.app.get("/state/check")
        async def check():
            return {"status": "ok"}

        @self.app.put("/state/{key}")
        async def put_state(key: str, value: Any):
            self.local_store[key] = value
            # Propagate the change to other servers
            await self.propagate_state("put", key, value)
            return {"status": "success", "key": key}

        @self.app.get("/state/{key}")
        async def get_state(key: str):
            if key in self.local_store:
                return self.local_store[key]
            raise HTTPException(status_code=404, detail="Key not found")

        @self.app.delete("/state/{key}")
        async def delete_state(key: str):
            if key in self.local_store:
                del self.local_store[key]
                # Propagate the deletion to other servers
                await self.propagate_state("delete", key)
                return {"status": "success", "key": key}
            raise HTTPException(status_code=404, detail="Key not found")

        port = int(self.config.url.split(":")[-1])
        uvicorn.run(self.app, host="0.0.0.0", port=port, log_level="info")

    # async def propagate_state(self, action: str, key: str, value: Any = None) -> None:
    #     """Propagate state changes to other servers in the network."""
    #     for url in self.config.other_server_urls:
    #         try:  # noqa: ERA001
    #             if action == "put":
    #                 response = self.session.put(f"{url}/state/{key}", json=value, timeout=self.config.timeout)
    #             elif action == "delete":
    #                 response = self.session.delete(f"{url}/state/{key}", timeout=self.config.timeout)
    #             response.raise_for_status()
    #             logging.info(f"Successfully propagated {action} for key '{key}' to {url}")
    #         except requests.RequestException as e:
    #             logging.error(f"Failed to propagate {action} for key '{key}' to {url}: {e}")

    def initialize(self) -> None:
        """Initialize the FastAPI protocol, either starting a server or checking server connectivity."""
        if self.config.start_server:
            # Start the FastAPI server in a separate thread
            self.server_thread = Thread(target=self.start_server, daemon=True)
            self.server_thread.start()
            logging.info("FastAPI server starting...")

            # Wait for the server to start
            server_ready = False
            for _ in range(10):  # Retry up to 10 times
                try:
                    response = self.session.get(f"{self.config.url}/state/check")
                    if response.status_code == 200:
                        logging.info(f"Connected to FastAPI server at {self.config.server_url}.")
                        server_ready = True
                        break
                except requests.RequestException:
                    time.sleep(1)  # Wait 1 second before retrying
            if not server_ready:
                raise RuntimeError(
                    f"Failed to connect to FastAPI server at {self.config.server_url} after 10 attempts."
                )
        else:
            # Check connectivity to the existing FastAPI server
            try:
                response = self.session.get(f"{self.config.server_url}/state/check")
                if response.status_code == 200:
                    logging.info(f"Connected to FastAPI server at {self.config.server_url}.")
                else:
                    raise RuntimeError(f"Unable to connect to FastAPI server: {response.status_code}")
            except requests.RequestException as e:
                msg = f"Failed to connect to FastAPI server: {e}"
                raise RuntimeError(msg) from e

    def put(self, key: str, value: Any) -> None:
        """Put a key-value pair into the FastAPI server and propagate it to other servers."""
        url = f"{self.config.server_url}/state/{key}"
        try:
            response = self.session.put(url, json=value, timeout=self.config.timeout)
            response.raise_for_status()
            logging.info(f"Put value for key '{key}' successfully.")
        except requests.RequestException as e:
            logging.error(f"Failed to PUT value to FastAPI server: {e}")
            raise

    def get(self, key: str) -> Any:
        """Get a value by key from the FastAPI server."""
        url = f"{self.config.server_url}/state/{key}"
        try:
            response = self.session.get(url, timeout=self.config.timeout)
            response.raise_for_status()
            logging.info(f"Got value for key '{key}' successfully.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Failed to GET value from FastAPI server: {e}")
            raise

    def delete(self, key: str) -> None:
        """Delete a key-value pair from the FastAPI server and propagate it to other servers."""
        url = f"{self.config.server_url}/state/{key}"
        try:
            response = self.session.delete(url, timeout=self.config.timeout)
            response.raise_for_status()
            logging.info(f"Deleted key '{key}' successfully.")
        except requests.RequestException as e:
            logging.error(f"Failed to DELETE value from FastAPI server: {e}")
            raise 

    def update(self, values: dict) -> None:
        """Update multiple key-value pairs in the FastAPI server."""
        for key, value in values.items():
            try:
                self.put(key, value)
                logging.info(f"Updated key '{key}' successfully.")
            except Exception as e:
                logging.error(f"Failed to update key '{key}': {e}")
                raise

    def cleanup(self) -> None:
        """Cleanup resources and shut down the FastAPI server if started."""
        if self.server_thread is not None:
            logging.info("Attempting to shut down FastAPI server...")
            self.server_thread.join(timeout=1)
            logging.info("FastAPI server shut down.")
        self.session.close()
        logging.info("Session closed.")
