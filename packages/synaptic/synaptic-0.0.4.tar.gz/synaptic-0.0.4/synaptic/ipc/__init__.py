from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Final, List, Type, TypedDict

from pydantic import AnyUrl, BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_root(key: str) -> str:
    """Return the root key for the IPC protocol."""
    return str(Path(str(key)).parents[0])


def get_stem(key: str) -> str:
    return str(Path(str(key)).stem)


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(cli_parse_args=False, extra="ignore")

class IPCUrlConfig(BaseModel):
    """URL configuration for Zenoh, supporting 'connect' and 'listen'."""
    connect: AnyUrl | str = None
    listen: AnyUrl | str = None

    @property
    def is_connect(self) -> bool:
        return self.connect is not None

    @property
    def is_listen(self) -> bool:
        return self.listen is not None

class IPCConfig(BaseSettings):
    """The configuration of an IPC peer."""

    model_config = SettingsConfigDict(cli_parse_args=False, extra="allow")
    url: List[IPCUrlConfig] = Field(default_factory=list, description="List of connect/listen URLs for Zenoh")
    auth_token: str | None = None
    serializer: str = Field(default="msgpack", description="Serialization protocol")
    timeout: int = Field(default=10, description="Request timeout in seconds")
    ipc_kind: str = "zenoh"
    root_key: str = Field(default="example/state", description="Root key for the distributed state")


class IPC(ABC):
    """Inter-process communication interface."""

    def copy(self) -> "IPC":
        """Return a copy of this IPC object."""
        return self.__class__(self.config, **self.__dict__)

    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass

    @abstractmethod
    def get(self, key, value) -> Any:
        pass

    @abstractmethod
    def put(self, key, value) -> None:
        pass

    @abstractmethod
    def update(self, values: dict) -> None:
        pass

    @abstractmethod
    def delete(self, key) -> None:
        pass

class IPCs(TypedDict):
    fastipc: Type[IPC]
    shm: Type[IPC]
    ws: Type[IPC]
    zenoh: Type[IPC]

    key_map = {
        "fastipc": "FastIPC",
        "shm": "SHMIPC",
        "ws": "WSIPC",
        "zenoh": "ZenohIPC",
    }


    
def load_ipcs() -> IPCs[str, IPC]:
    from .fastipc import FastIPC
    from .shm import SHMIPC
    from .ws import WSIPC
    from .zenoh import ZenohIPC
    return {
        "fastipc": FastIPC,
        "shm": SHMIPC,
        "ws": WSIPC,
        "zenoh": ZenohIPC,
    }


ipcs: Final[IPCs] = load_ipcs()



__all__ = ["IPC", "BaseConfig", "IPCConfig", "ipcs"]
