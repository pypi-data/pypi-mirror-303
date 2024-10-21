import time
import logging
from threading import Thread, Event
from typing import List
import zenoh
from zenoh import SampleKind
from synaptic.ipc.zenoh import ZenohIPC
from synaptic.ipc import IPCConfig, IPCUrlConfig

# Assuming ZenohIPC, IPCConfig, and URLConfig are already defined and imported
# from synaptic.ipc.zenoh import ZenohIPC, IPCConfig, URLConfig

# Configure logging for the test
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("ZenohQueueTest")

def test_queue_consumption():
    # Define IPC configuration with a unique root key for testing
    ipc_config = IPCConfig(
        url=[
            IPCUrlConfig(connect="tcp/149.130.215.195:7448"), 
            IPCUrlConfig(connect="tcp/0.0.0.0:7448"),
        ],
        serializer='msgpack'  # Ensure the serializer matches your setup
    )

    # Use a unique root key to prevent interference with ZenohIPC's internal subscriber
    test_root_key = "test/queue_consumption_unique"

    # Initialize ZenohIPC instance with the unique root key
    zenoh_ipc = ZenohIPC(settings=ipc_config, root_key=test_root_key)

    # Initialize the Zenoh session
    zenoh_ipc.initialize()

    # Define the key to use within the unique root key
    test_key = "consumption_test"

    # Define the data to publish before defining consume_data
    data_to_publish = [f"message_{i}" for i in range(1, 6)]  # Publish 5 messages

    # Function to consume data from the queue
    def consume_data(consume_event: Event, received_messages: List[str], data_to_publish: List[str]):
        queue = zenoh.Queue()
        subscription_key = f"{zenoh_ipc.root_key}/{test_key}"
        subscriber = zenoh_ipc.session.declare_subscriber(subscription_key, queue)
        logger.info("Subscriber declared for consumption test.")

        # Signal that subscriber is ready
        consume_event.set()

        try:
            while len(received_messages) < len(data_to_publish):  # Expecting 5 messages
                try:
                    # Attempt to get a sample from the queue with a timeout
                    sample = queue.get(timeout=5)  # Wait up to 5 seconds for data
                    if sample.kind == SampleKind.PUT():
                        # Deserialize the message directly as a string
                        message = zenoh_ipc.serializer.frombytes(sample.payload)
                        received_messages.append(message)
                        logger.info(f"Consumed: {message}")
                except StopIteration:
                    # Queue has been closed unexpectedly
                    logger.error("Queue closed unexpectedly: StopIteration raised")
                    break
                except Exception as e:
                    # Log any other exceptions with full stack trace
                    logger.exception("Error consuming data:")
                    break
        finally:
            # Clean up subscriber
            try:
                subscriber.undeclare()
                logger.info("Subscriber undeclared after consumption.")
            except Exception as e:
                logger.error(f"Error undeclaring subscriber: {e}")

    # Prepare for consumption
    consume_event = Event()
    received_messages = []

    # Start the consumer thread **before** publishing messages
    consumer_thread = Thread(target=consume_data, args=(consume_event, received_messages, data_to_publish))
    consumer_thread.start()

    # Wait until the consumer is ready
    consume_event.wait()

    # Now publish the messages
    for msg in data_to_publish:
        zenoh_ipc.put(test_key, msg)  # Publishing strings directly
        logger.info(f"Published: {msg}")
        time.sleep(0.1)  # Small delay to ensure messages are published in order

    # Wait for the consumer to finish
    consumer_thread.join()

    # Attempt to consume again to check if data persists
    logger.info("Attempting to consume data again to check persistence.")
    second_consumed_messages = []
    consume_event_second = Event()

    def consume_data_second(consume_event: Event, received_messages_second: List[str]):
        queue = zenoh.Queue()
        subscription_key = f"{zenoh_ipc.root_key}/{test_key}"
        subscriber = zenoh_ipc.session.declare_subscriber(subscription_key, queue)
        logger.info("Second subscriber declared for persistence check.")

        # Signal that subscriber is ready
        consume_event.set()

        try:
            # Attempt to get data without any new publications
            sample = queue.get(timeout=2)  # Wait up to 2 seconds
            if sample.kind == SampleKind.PUT():
                # Deserialize the message directly as a string
                message = zenoh_ipc.serializer.frombytes(sample.payload)
                received_messages_second.append(message)
                logger.info(f"Second consumption received: {message}")
        except Exception as e:
            # Log any exceptions, including timeout
            logger.info("No data received on second consumption attempt.")
        finally:
            # Clean up subscriber
            try:
                subscriber.undeclare()
                logger.info("Second subscriber undeclared after consumption attempt.")
            except Exception as e:
                logger.error(f"Error undeclaring second subscriber: {e}")

    # Start the second consumer thread
    second_consumer_thread = Thread(target=consume_data_second, args=(consume_event_second, second_consumed_messages))
    second_consumer_thread.start()

    # Wait until the second consumer is ready
    consume_event_second.wait()

    # Wait for the second consumer to finish
    second_consumer_thread.join()

    # Analyze the results
    logger.info(f"First consumption received messages: {received_messages}")
    logger.info(f"Second consumption received messages: {second_consumed_messages}")

    if not second_consumed_messages:
        logger.info("Data in the queue is consumed upon reading (Persistent=False).")
    else:
        logger.info("Data in the queue persists after reading (Persistent=True).")

    # Clean up
    zenoh_ipc.cleanup()


if __name__ == "__main__":
    test_queue_consumption()
