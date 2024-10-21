import logging
import traceback
from multiprocessing.shared_memory import SharedMemory

from synaptic.ipc import IPC, IPCConfig
from synaptic.serialization import Serializer, serializers


class SHMIPC(IPC):
    def __init__(self, 
    settings: IPCConfig,/,*,
    shared_memory_size_kb):
        self.settings = settings
        self.root_key = settings.root_key
        self.shm_size = shared_memory_size_kb
        self.settings = settings
        self.serializer = serializers[settings.serializer]

    def initialize(self) -> None:
        try:
            self.shm = SharedMemory(
                name=self.root_key, create=True, size=self.shm_size * 1024
            )
            self._save_state({})
        
        except Exception as e:
            self.cleanup()
            raise

    def cleanup(self) -> None:
            if self.shm is not None:
                self.shm.close()
                self.shm.unlink()
                self.shm = None

    def _load_state(self) -> dict:
        try:
            data = bytes(self.shm.buf[: self.shm.size]).decode("utf-8").strip("\x00")
            serializer: Serializer = serializers[self.settings.serializer]()

            raise ValueError(f"Unsupported serialization protocol: {self.settings.serialization_protocol}")
        except Exception as e:
            raise

    def _save_state(self, state: dict) -> None:
        try:
            if self.settings.serializer not in serializers:
                raise ValueError(f"Unsupported serialization protocol: {self.settings.serialization_protocol}")
            serializer = serializers[self.settings.serializer]()
            serialized = serializer.tobytes(state)
            self.shm.buf[: self.shm.size] = b"\x00" * self.shm.size
            self.shm.buf[: len(serialized)] = serialized
        except Exception as e:
            logging.error(f"Failed to save state: {e}")
            traceback.print_exc()
            raise

    def publish_state(self, state: dict) -> None:
        self._save_state(state)
