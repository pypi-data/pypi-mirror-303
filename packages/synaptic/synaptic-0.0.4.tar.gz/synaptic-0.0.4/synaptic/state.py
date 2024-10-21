import logging
from multiprocessing.managers import BaseManager, BaseProxy
from typing import Any, TypeVar

from mbodied.types.sample import Sample
from rich.console import Console

from synaptic.ipc import IPC, IPCConfig, ipcs

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Define the logger
logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Sample)


console = Console()

class _State:
    def __init__(self, settings: IPCConfig, **kwargs):
        self.settings = settings.config if isinstance(settings, IPC) else settings
        self.ipc: IPC = ipcs[self.settings.ipc_kind](settings, **kwargs)

    def initialize(self) -> None:
        self.ipc.initialize()

    def cleanup(self) -> None:
        if self.ipc is not None:
            try:
                self.ipc.cleanup()
            except Exception as e:
                logger.error(f"Error during protocol cleanup: {e}")

    def delete(self, key) -> None:
        try:
            self.ipc.delete(key)
        except Exception as e:
            logger.error(f"Error deleting state: {e}")

    def update(self, values: dict) -> None:
        self.ipc.update(values)

    def put(self, key: str, value: Any) -> None:
        try:
            self.ipc.put(key, value)
            logger.info(f"State updated: {key}")
        except Exception as e:
            logger.error(f"Error updating state: {e}")

    def get(self, key) -> Any:
        try:
            return self.ipc.get(key)
        except Exception as e:
            logger.error(f"Error getting state: {e}")
            return None




class StateProxy(BaseProxy):
    _exposed_ = ["initialize", "cleanup", "delete", "update", "put", "get"]

    def _make_callmethod(self, methodname: str) -> Any:
        """Make a call to the remote object."""

        def make_callmethod(*args, **kwds) -> Any:
            return self._callmethod(methodname, args, kwds)

        return make_callmethod

    def __getattr__(self, item: str) -> Any:
        """Get attribute from the remote object."""
        if item.startswith("_") and item not in self._exposed_:
            ret = object.__getattribute__(self, item)

        if item in self._exposed_:
            ret = self._make_callmethod(item)
            console.print(f"Getting {item}: {ret}", style="bold blue")
            return ret
        try:
            value = self._callmethod("get", (item,))
            if value is None:
                logger.warning(f"State for {item} is None")
            return value
        except Exception as e:
            logger.error(f"Error getting state for {item}: {e}")
            return None

    def __setattr__(self, key: str, value: Any) -> None:
        """Set attribute on the remote object."""
        if key.startswith("_") or key in self._exposed_:
            return object.__setattr__(self, key, value)
        try:
            self._callmethod("put", (key, value))
        except Exception as e:
            logger.error(f"Error setting state for {key}: {e}")

    def __delattr__(self, key: str) -> None:
        """Delete attribute on the remote object."""
        if key.startswith("_") or key in self._exposed_:
            return object.__delattr__(self, key)
        try:
            self._callmethod("delete", (key,))
        except Exception as e:
            logger.error(f"Error deleting state for {key}: {e}")

    def __getitem__(self, item) -> Any | None:  # noqa: D105
        return self.__getattr__(item)

    def __setitem__(self, key, value) -> None:  # noqa: D105
        return self.__setattr__(key, value)

    def initialize(self) -> None:
        return self._callmethod("initialize")

    def cleanup(self) -> None:
        return self._callmethod("cleanup")


class StateManager(BaseManager):
    pass


StateManager.register("State", _State, StateProxy, exposed=["initialize", "cleanup", "delete", "update", "put", "get"])


class State(Sample):
    def __init__(self, settings: IPCConfig, **kwargs):

        super().__init__(**kwargs)
        self.manager = StateManager()
        self.manager.start()
        self.state: StateProxy = self.manager.State(settings, **kwargs)

    def __del__(self) -> None:
        """Cleanup resources when the object is deleted."""
        try:
            self.cleanup()
        except Exception as e:
            logger.error(f"Error during Context.__del__: {e}")

    def __enter__(self) -> StateProxy:
        """Initialize the state object and return it."""
        self.state.initialize()
        return self.state

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Cleanup resources when exiting the context."""
        self.cleanup()
        if exc_type:
            logger.error(f"An error occurred: {exc_type}, {exc_tb}")
            raise exc_val

    def cleanup(self) -> None:
        try:
            if hasattr(self, "state") and self.state:
                try:
                    self.state.cleanup()
                    self.state = None
                except Exception as e:
                    logger.error(f"Error during state cleanup: {e}")

            if hasattr(self, "manager") and self.manager:
                try:
                    self.manager.shutdown()
                except Exception as e:
                    logger.error(f"Error shutting down manager: {e}")

            logger.info("Context cleanup completed")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")