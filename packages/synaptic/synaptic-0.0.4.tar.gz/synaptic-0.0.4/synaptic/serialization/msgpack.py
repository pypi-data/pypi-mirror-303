import logging
import traceback
from typing import Any

import msgpack
from msgpack.exceptions import PackException, UnpackException

from synaptic.serialization.serializer import Serializer

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Define the logger
logger = logging.getLogger(__name__)

class MsgPackSerializer(Serializer):
    def tobytes(self, data: Any) -> bytes:
        """Serialize Python data into MessagePack format (bytes)."""
        # logger.info("serializing data ")
        try:
            # Ensure strings are encoded as UTF-8, not binary
            out = msgpack.packb(data, use_bin_type=True)
            # logger.info("Serialized data")
            return out
        except PackException as e:
            traceback.print_exc()
            msg = f"Error packing data: {e}"
            raise ValueError(msg) from e

    def frombytes(self, data: bytes) -> Any:
        """Deserialize MessagePack bytes back into Python objects, ensuring correct handling of strings."""
        try:
            # logger.info("deserializing data")
            out = msgpack.unpackb(data, raw=False) 
            # logger.info("deserialized data")
            return out
            # Ensure that binary data is decoded back into strings
        # raw=False ensures binary strings are decoded to UTF-8 strings
        except UnpackException as e:
            traceback.print_exc()
            msg = f"Error unpacking data: {e}"
            raise ValueError(msg) from e
