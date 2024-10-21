import inspect
import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, TypeVar
from collections import deque
import zenoh
from zenoh import Query, Queue, Reply, Sample, SampleKind, Session

from synaptic.ipc import IPC, IPCConfig
from synaptic.serialization import serializers
from synaptic.serialization.msgpack import UnpackException

T = TypeVar("T")

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Define the logger
logger = logging.getLogger(__name__)

class ZenohIPC(IPC):
    def __init__(self, settings: IPCConfig, *, root_key: str, mode: str = "peer", protocol: str = "tcp") -> None:
        self.settings = settings
        self.wire = protocol
        self.mode = mode
        self.serializer = serializers[settings.serializer]()
        self.root_key = root_key
        self.session: Session | None = None
        self._local_store: Dict[str, Any] = {}
        self.name = "ZenohProtocol" + time.strftime("%Y%m%d-%H%M%S")
        self._key_order = deque()  # A deque to keep track of the key insertion order

        # Separate the connect and listen URLs from the settings
        self.connection = []
        self.listen = []
        
        # Parse the URLs from settings
        if self.settings.url:
            for url_entry in self.settings.url:
                if url_entry.connect:
                    self.connection.append(url_entry.connect)
                if url_entry.listen:
                    self.listen.append(url_entry.listen)

        logger.info(f"Connection endpoints: {self.connection}")
        logger.info(f"Listen endpoints: {self.listen}")

    
    def initialize(self) -> None:
        if self.session is None:
            try:
                # Use zenoh.Config to configure the session
                conf = zenoh.Config()

                # Set mode
                if self.mode:
                    conf.insert_json5(zenoh.config.MODE_KEY, json.dumps(self.mode))

                # Prepare lists for connect and listen endpoints
                connect_endpoints = []
                listen_endpoints = []

                # Extract and categorize the URLs from the settings
                for url_config in self.settings.url:
                    if url_config.is_connect:
                        connect_endpoints.append(url_config.connect)
                    if url_config.is_listen:
                        listen_endpoints.append(url_config.listen)

                logger.info(f"Final connect endpoints being added to session: {connect_endpoints}")
                logger.info(f"Final listen endpoints being added to session: {listen_endpoints}")

                # Insert the connect endpoints into the Zenoh config
                if connect_endpoints:
                    conf.insert_json5(zenoh.config.CONNECT_KEY, json.dumps(connect_endpoints))

                # Insert the listen endpoints into the Zenoh config
                if listen_endpoints:
                    conf.insert_json5(zenoh.config.LISTEN_KEY, json.dumps(listen_endpoints))

                # Open the Zenoh session with the config
                self.session = zenoh.open(conf)

                # Declare a subscriber for the given root_key
                self.sub = self.session.declare_subscriber(self.root_key + "/**", self.listener)

                # Check if the root key exists, if not create it
                q = self.session.get(self.root_key, zenoh.Queue())
                if next(q, None) is None:
                    logger.info(f"Creating root key: {self.root_key}")
                    self.queryable = self.session.declare_queryable(
                        self.root_key + "/**", self.query_handler
                    )
            except Exception as e:
                logger.error(f"Error initializing Zenoh session: {e}")
                self.cleanup()
                raise e


    def __dict__(self) -> dict:
        """Return the object config as a dictionary."""
        return {
            "settings": self.settings,
            "mode": self.mode,
            "root_key": self.root_key,
        }


    def listener(self, sample: Sample) -> None:
        """Callback function for incoming samples."""
        # Use the full key instead of just the stem
        key = str(sample.key_expr)  # Use the full key, not just the stem
        logger.debug(f"Listener: Received sample for key: {key}")
        
        # Zenoh automatically assigns a timestamp to the sample
        zenoh_timestamp = sample.timestamp
        logger.debug(f"Received data with Zenoh timestamp: {zenoh_timestamp}")
        
        if sample.kind == SampleKind.DELETE():
            # Remove from _local_store and _key_order
            self._local_store.pop(key, None)
            if key in self._key_order:
                self._key_order.remove(key)
        else:
            try:
                deserialized_data = self.serializer(sample.payload)
                
                # Store both the data and Zenoh's timestamp in the local store
                self._local_store[key] = {
                    'value': deserialized_data,
                    'zenoh_timestamp': zenoh_timestamp  # Use Zenoh's assigned timestamp
                }
                logger.debug(f"Listener: Deserialized data for {key} with Zenoh timestamp {zenoh_timestamp}")

                # Ensure the key is in the deque and track its order
                if key in self._key_order:
                    self._key_order.remove(key)
                self._key_order.append(key)  # Add to the end to track the latest data
            except (json.JSONDecodeError, UnpackException) as e:
                logger.error(f"Error deserializing sample payload: {e}")

    
    def put(self, key: str, value: Any) -> None:
        """
        Store a value in Zenoh and save a timestamp of when it was added.

        Args:
            key (str): The key under which the value is stored.
            value (Any): The value to store.
        """
        if self.session is None:
            self.initialize()

        # Use the full key for consistency
        key = f"{self.root_key}/{key}"
        logger.debug(f"Putting key value for key: {key}")

        # Store the value with a timestamp in Zenoh
        self.session.put(key, self.serializer(value))

        # Ensure the key is in the deque, avoiding duplicates
        if key in self._key_order:
            self._key_order.remove(key)
        self._key_order.append(key)  # Add to the end to mark it as the latest



    def query_handler(self, query: Query) -> None:
        """Only runs if a queryable is declared by this node."""
        logger.debug(f">> [Queryable] Received Query '{query.selector.key_expr}'")
        key = str(Path(str(query.selector.key_expr)).stem)
        logger.debug(f"Query Handling Local store: using key: {key}")
        if key in self._local_store:
            value = self._local_store[key]
            reply_data = self.serializer(value)
            query.reply(Sample(query.selector.key_expr, reply_data))
            logger.debug(f"Replied to query: {query.selector.key_expr} ->")
        elif str(query.selector.key_expr) == self.root_key:
            response = list(self._local_store.keys())
            reply_data = self.serializer(response)
            query.reply(Sample(query.selector.key_expr, reply_data))
        else:
            logger.error(f"Query not found: {query.selector.key_expr} with key: {key}")


    def get(self, key: str) -> Any:
        try:
            if self.session is None:
                self.initialize()
            key = f"{self.root_key}/{key}"
            q: Queue[Reply] = self.session.get(key, zenoh.Queue())
            sample: Reply = next(q, None)
            if sample is not None and sample.ok is not None:
                logger.debug("Got value:")
                return self.serializer(sample.ok.payload)
            raise KeyError(f"Key not found: {key}")

        except Exception as e:
            logger.error(f"Error getting value from Zenoh: {e}")
            raise
    

    def get_latest(self) -> Any:
        """
        Get the most recently added value.

        Returns:
            Any: The value associated with the most recent key, or None if no keys are present.
        """
        if len(self._key_order) == 0:
            logger.info("No keys available in the store.")
            return None
        latest_key = self._key_order[-1]  # Get the last inserted key
        logger.info(f"Fetching latest key: {latest_key}")
        return self._local_store.get(latest_key, {}).get('value')  # Correctly fetch value from _local_store


    def get_earliest(self) -> Any:
        """
        Get the earliest added value.

        Returns:
            Any: The value associated with the earliest key, or None if no keys are present.
        """
        if len(self._key_order) == 0:
            logger.info("No keys available in the store.")
            return None
        earliest_key = self._key_order[0]  # Get the first inserted key
        logger.info(f"Fetching earliest key: {earliest_key}")
        return self._local_store.get(earliest_key, {}).get('value')  # Correctly fetch value from _local_store


    def update(self, values: dict) -> None:
        try:
            if self.session is None:
                self.initialize()
            for key, value in values.items():
                self.put(key, value)
        except Exception as e:
            logger.error(f"Error updating values in Zenoh: {e}")
            raise


    def delete(self, key: str) -> None:
        try:
            if self.session is None:
                self.initialize()
            key = f"{self.root_key}/{key}"
            q: Queue[zenoh.Reply] = self.session.get(key, zenoh.Queue())
            if next(q, None) is None:
                raise KeyError(f"Key not found: {key}")
            self.session.delete(key)
            logger.debug(f"Key removed: {key}")
        except KeyError:
            raise
        except Exception as e:
            logger.error(f"Error deleting key from Zenoh: {e}")
            raise KeyError(f"Key not found: {str(key)[:50] + '...'}") from e


    def cleanup(self) -> None:
        if self.session is not None:
            logger.info(inspect.currentframe().f_back.f_back)
            try:
                self.sub.undeclare()
                if hasattr(self, "queryable"):
                    self.queryable.undeclare()
                    self.session.delete(self.root_key)
                self.session.close()
                self.session = None
                logger.debug("Zenoh session closed successfully")
            except Exception as e:
                logger.error(f"Error closing Zenoh session: {e}")
            finally:
                if self.sub is not None:
                    self.sub.undeclare()
                    self.sub = None
                if hasattr(self, "queryable") and self.queryable is not None:
                    self.queryable.undeclare()
                    self.queryable = None
                if self.session is not None:
                    self.session.close()
                    self.session = None
                logger.debug("Cleanup completed")

