import logging
import time

import cv2
from embdata.sense.camera import Camera, Distortion, Extrinsics, Intrinsics
from embdata.sense.image import Image

from synaptic.ipc import IPCConfig, IPCUrlConfig
from synaptic.state import State

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Define the logger
logger = logging.getLogger(__name__)

# Define the camera configuration
camera = Camera(
    intrinsic=Intrinsics(fx=911.0, fy=911.0, cx=653.0, cy=371.0),
    distortion=Distortion(k1=0.0, k2=0.0, p1=0.0, p2=0.0, k3=0.0),
    extrinsic=Extrinsics(),
    depth_scale=0.001,
)

# Define backend configuration
backend_kwargs = {
    "settings": IPCConfig(
        shared_memory_size_kb=1024,
        url=[
            IPCUrlConfig(connect="tcp/149.130.215.195:7448")
        ], 
        ipc_kind="zenoh",
        serializer="msgpack",
    ),
    "root_key": "example/state",
}


if __name__ == "__main__":
    # Load the image using the EmbData Image class
    image = Image(path="resources/rgb_example.png", mode="RGB", encoding="PNG")

    with State(**backend_kwargs) as state:
        for _ in range(10):
            # Encode the image as PNG
            success, png_encoded = cv2.imencode('.png', image.array)

            if not success:
                logger.error("Failed to encode the image as PNG.")
                break  # Exit the loop or handle the error as needed

            # Convert the encoded image to bytes
            png_bytes = png_encoded.tobytes()

            # Publish the PNG image bytes
            # Assuming 'state.put' is the correct method to publish the data
            state.image = png_bytes

            logger.info("Published the image data.")

            # Wait for 1 second before the next iteration
            time.sleep(0.1)
