import logging
import time

from embdata.sense.image import Image

from synaptic.ipc import IPCConfig, IPCUrlConfig
from synaptic.state import State

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Define the logger
logger = logging.getLogger(__name__)

# backend_kwargs with proper list structure for 'url'
backend_kwargs = {
    "settings": IPCConfig(
        shared_memory_size_kb=1024,
        url=[
            IPCUrlConfig(listen="tcp/0.0.0.0:7448")
        ],  
        ipc_kind="zenoh",
        serializer="msgpack",
    ),
    "root_key": "example/state",
}

if __name__ == "__main__":
    
    try:
        with State(**backend_kwargs) as state:
            i = 0
            while True:
                if state.image is not None:
                    rgb = Image(bytes_obj=state.image, mode="RGB", encoding="png")
                    i += 1
                time.sleep(0.1)  # Add a sleep to avoid tight loop

    except KeyboardInterrupt:
        logger.info("Exiting...")