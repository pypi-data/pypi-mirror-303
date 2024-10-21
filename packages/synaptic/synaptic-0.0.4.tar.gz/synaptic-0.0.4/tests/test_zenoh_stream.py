from asyncio import Queue
from typing import Optional, Generator, Dict, Any
import logging
import zenoh

import logging
from typing import Any, Dict, Generator

import zenoh
from zenoh import Queue, Sample, SampleKind

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

def stream(self, key_pattern: Optional[str] = None, timeout: Optional[float] = None) -> Generator[Dict[str, Any], None, None]:
    """
    Stream data from the Zenoh Queue using a generator.

    Args:
        key_pattern (str, optional): Specific key pattern to subscribe to.
            Defaults to None, which subscribes to all keys under the root_key.
        timeout (float, optional): Timeout in seconds for yielding data.
            Defaults to None, which blocks indefinitely until data is available.

    Yields:
        dict: A dictionary containing the data, UUID, and timestamp.
    """
    if self.session is None:
        self.initialize()

    # Define the subscription key pattern
    subscription_key = self.root_key + "/**" if not key_pattern else f"{self.root_key}/{key_pattern}/**"

    # Create a new Queue for this stream
    stream_queue: Queue = Queue()
    self._active_streams.append(stream_queue)

    try:
        # Declare a new subscriber with the stream_queue as the closure
        subscriber = self.session.declare_subscriber(subscription_key, stream_queue)
        logger.info(f"Started streaming on key pattern: {subscription_key}")

        while True:
            try:
                # Attempt to get a sample from the queue
                sample: Sample = stream_queue.get(timeout=timeout) if timeout else stream_queue.get()

                if sample.kind == SampleKind.PUT():
                    # Deserialize the payload
                    deserialized_data = self.serializer.frombytes(sample.payload)
                    # Yield the data along with metadata
                    yield {
                        'data': deserialized_data.get('data'),
                        'uuid': deserialized_data.get('uuid'),
                        'timestamp': sample.timestamp
                    }
                elif sample.kind == SampleKind.DELETE():
                    # Handle deletion if necessary
                    yield {
                        'data': None,
                        'uuid': None,
                        'timestamp': sample.timestamp,
                        'deleted': True,
                        'key': str(sample.key_expr)
                    }
            except zenoh.Error as e:
                logger.error(f"Zenoh error while streaming: {e}")
                break
            except StopIteration:
                logger.info("Stream terminated: Queue closed.")
                break
            except Exception as e:
                logger.error(f"Unexpected error while streaming: {e}")
                break
    finally:
        # Clean up: undeclare the subscriber and remove the queue from active streams
        try:
            subscriber.undeclare()
            logger.info(f"Stopped streaming on key pattern: {subscription_key}")
        except Exception as e:
            logger.error(f"Error undeclaring subscriber: {e}")
        self._active_streams.remove(stream_queue)
