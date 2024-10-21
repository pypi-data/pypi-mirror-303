import pytest
import time
from zenoh import Config, open as zenoh_open, SampleKind, Queue
from threading import Thread, Event
import logging

# Configure logging to INFO level to reduce verbosity
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Publisher function to publish numbers from 1 to 100
def publisher(session, root_key, ready_event):
    """
    Publishes numbers from 1 to 100 to the specified Zenoh key.

    Args:
        session (zenoh.session.Session): The Zenoh session.
        root_key (str): The root key for publishing.
        ready_event (threading.Event): Event to synchronize publisher start.
    """
    # Wait until the subscriber is ready
    ready_event.wait()
    for i in range(1, 101):
        session.put(f"{root_key}/numbers", str(i).encode())
        logger.info(f"Published number: {i}")
        time.sleep(0.01)  # Small delay to simulate publishing at intervals

# Subscriber function to receive numbers via a Queue
def subscriber(session, root_key, queue, ready_event, stop_event):
    """
    Declares a subscriber to the specified Zenoh key and manages its lifecycle.

    Args:
        session (zenoh.session.Session): The Zenoh session.
        root_key (str): The root key to subscribe to.
        queue (zenoh.closures.Queue): The Zenoh Queue to receive samples.
        ready_event (threading.Event): Event to signal subscriber readiness.
        stop_event (threading.Event): Event to signal subscriber to stop.
    """
    sub = session.declare_subscriber(f"{root_key}/numbers", queue)
    logger.info(f"Subscribed to {root_key}/numbers")
    # Signal that the subscriber is ready
    ready_event.set()
    # Keep the subscriber thread alive until stop_event is set
    while not stop_event.is_set():
        time.sleep(0.1)
    # Clean up the subscriber
    sub.undeclare()
    logger.info(f"Unsubscribed from {root_key}/numbers")

# Processing function to simulate time-consuming operations
def processing_function(number):
    """
    Simulates processing of a number by doubling it after a short delay.

    Args:
        number (int): The number to process.

    Returns:
        int: The processed number.
    """
    time.sleep(0.05)  # Simulate time-consuming processing
    return number * 2

@pytest.fixture
def zenoh_setup():
    """
    Pytest fixture to set up and tear down the Zenoh session.

    Yields:
        tuple: Zenoh session and root key.
    """
    config = Config()
    session = zenoh_open(config)
    root_key = "pytest/queue_test"  # Corrected key without leading slash
    yield session, root_key
    # Teardown the session after the test
    session.close()

def test_queue_subscription(zenoh_setup):
    """
    Tests the Zenoh Queue to ensure it behaves as FIFO by publishing and subscribing to numbers.

    Args:
        zenoh_setup (tuple): Zenoh session and root key.
    """
    session, root_key = zenoh_setup
    queue = Queue()
    ready_event = Event()
    stop_event = Event()

    # Start the subscriber in a separate thread
    subscriber_thread = Thread(target=subscriber, args=(session, root_key, queue, ready_event, stop_event))
    subscriber_thread.start()

    # Wait until the subscriber is ready
    ready_event.wait()

    # Start the publisher in a separate thread
    publisher_thread = Thread(target=publisher, args=(session, root_key, ready_event))
    publisher_thread.start()

    # Read numbers from the queue
    received_numbers = []
    try:
        # Collecting numbers from the queue
        while len(received_numbers) < 100:
            try:
                # Try getting the sample from the queue with a timeout
                sample = queue.get(timeout=10)  # Increased timeout to allow for data arrival
                if sample.kind == SampleKind.PUT():
                    number = int(sample.payload.decode())
                    received_numbers.append(number)
                    logger.info(f"Received number: {number}")
            except StopIteration:
                # StopIteration means the queue has been closed unexpectedly
                pytest.fail("Queue closed unexpectedly: StopIteration raised")
            except Exception as e:
                pytest.fail(f"Failed to read from queue: {e}")
    finally:
        # Signal the subscriber thread to stop and join the thread
        stop_event.set()
        subscriber_thread.join(timeout=1)
        if subscriber_thread.is_alive():
            logger.warning("Subscriber thread is still alive after test completion.")
        publisher_thread.join()

    # Assert that we received all 100 numbers
    assert len(received_numbers) == 100, f"Received {len(received_numbers)} instead of 100"

    # Assert the numbers are in order of arrival (FIFO)
    assert received_numbers == list(range(1, 101)), "Queue returned numbers out of order!"


def test_queue_subscription_with_delay(zenoh_setup):
    """
    Tests whether Zenoh retains published data when a subscriber joins late.
    Publisher starts first, and the subscriber joins after a delay to check
    if data published during the delay is still received.
    
    Args:
        zenoh_setup (tuple): Zenoh session and root key.
    """
    session, root_key = zenoh_setup
    queue = Queue()
    ready_event = Event()
    stop_event = Event()

    # Start the publisher in a separate thread
    publisher_thread = Thread(target=publisher, args=(session, root_key, ready_event))
    publisher_thread.start()

    # Introduce a delay before starting the subscriber (simulates late subscription)
    time.sleep(10)  # Wait 3 seconds before subscribing

    # Start the subscriber in a separate thread
    subscriber_thread = Thread(target=subscriber, args=(session, root_key, queue, ready_event, stop_event))
    subscriber_thread.start()

    # Wait until the subscriber is ready
    ready_event.wait()

    # Read numbers from the queue
    received_numbers = []
    try:
        # Collecting numbers from the queue
        while len(received_numbers) < 100:
            try:
                # Try getting the sample from the queue with a timeout
                sample = queue.get(timeout=10)  # Increased timeout to allow for data arrival
                if sample.kind == SampleKind.PUT():
                    number = int(sample.payload.decode())
                    received_numbers.append(number)
                    logger.info(f"Received number: {number}")
            except StopIteration:
                # StopIteration means the queue has been closed unexpectedly
                pytest.fail("Queue closed unexpectedly: StopIteration raised")
            except Exception as e:
                pytest.fail(f"Failed to read from queue: {e}")
    finally:
        # Signal the subscriber thread to stop and join the thread
        stop_event.set()
        subscriber_thread.join(timeout=1)
        if subscriber_thread.is_alive():
            logger.warning("Subscriber thread is still alive after test completion.")
        publisher_thread.join()

    # Assert that we received all 100 numbers
    if len(received_numbers) < 100:
        logger.warning(f"Received {len(received_numbers)} numbers. Missed some published data.")

    # Check if Zenoh is persistent or non-persistent based on when the subscriber started
    assert len(received_numbers) == 100, "Zenoh did not persist data for late subscribers."

    # Assert the numbers are in order of arrival (FIFO)
    assert received_numbers == list(range(1, 101)), "Queue returned numbers out of order!"


def test_queue_subscription_lifo(zenoh_setup):
    """
    Hypothetical test to verify LIFO behavior of Zenoh's Queue.

    Note: Zenoh's Queue is FIFO by design. This test is for educational purposes only.
    """
    session, root_key = zenoh_setup
    queue = Queue()
    ready_event = Event()
    stop_event = Event()

    # Start the subscriber in a separate thread
    subscriber_thread = Thread(target=subscriber, args=(session, root_key, queue, ready_event, stop_event))
    subscriber_thread.start()

    # Wait until the subscriber is ready
    ready_event.wait()

    # Start the publisher in a separate thread, passing the ready_event
    publisher_thread = Thread(target=publisher, args=(session, root_key, ready_event))
    publisher_thread.start()

    # Read numbers from the queue
    received_numbers = []
    try:
        # Collecting numbers from the queue
        while len(received_numbers) < 100:
            try:
                # Try getting the sample from the queue with a timeout
                sample = queue.get(timeout=10)  # Get the next sample from the queue
                if sample.kind == SampleKind.PUT():
                    number = int(sample.payload.decode())
                    received_numbers.append(number)
                    logger.info(f"Received number: {number}")
            except StopIteration:
                pytest.fail("Queue closed unexpectedly: StopIteration raised")
            except Exception as e:
                pytest.fail(f"Failed to read from queue: {e}")
    finally:
        # Signal the subscriber thread to stop and join the thread
        stop_event.set()
        subscriber_thread.join(timeout=1)
        if subscriber_thread.is_alive():
            logger.warning("Subscriber thread is still alive after test completion.")
        publisher_thread.join()

    # Assert that we received all 100 numbers
    assert len(received_numbers) == 100, f"Received {len(received_numbers)} instead of 100"

    # Hypothetical LIFO Assertion (This will fail since Queue is FIFO)
    expected_lifo = list(range(100, 0, -1))
    assert received_numbers != expected_lifo, "Queue is not LIFO as expected!"

def test_queue_fifo_with_processing(zenoh_setup):
    """
    Tests that the Zenoh Queue behaves as FIFO when a processing function operates on the numbers.
    Ensures that the earliest numbers are processed first.
    """
    session, root_key = zenoh_setup
    queue = Queue()
    ready_event = Event()
    stop_event = Event()

    # Start the subscriber in a separate thread
    subscriber_thread = Thread(target=subscriber, args=(session, root_key, queue, ready_event, stop_event))
    subscriber_thread.start()

    # Wait until the subscriber is ready
    ready_event.wait()

    # Start the publisher in a separate thread
    publisher_thread = Thread(target=publisher, args=(session, root_key, ready_event))
    publisher_thread.start()

    # Read and process numbers from the queue
    processed_numbers = []
    try:
        for _ in range(1, 101):
            try:
                # Try getting the sample from the queue with a timeout
                sample = queue.get(timeout=20)  # Increased timeout to allow for data arrival
                if sample.kind == SampleKind.PUT():
                    number = int(sample.payload.decode())
                    logger.info(f"Received number: {number}")
                    result = processing_function(number)
                    processed_numbers.append(result)
            except StopIteration:
                pytest.fail("Queue closed unexpectedly: StopIteration raised")
            except Exception as e:
                pytest.fail(f"Failed to read from queue: {e}")
    finally:
        # Signal the subscriber thread to stop and join the thread
        stop_event.set()
        subscriber_thread.join(timeout=1)
        if subscriber_thread.is_alive():
            logger.warning("Subscriber thread is still alive after test completion.")
        publisher_thread.join()

    # Assert that all numbers were processed
    assert len(processed_numbers) == 100, f"Processed {len(processed_numbers)} instead of 100"

    # Assert that processing was done in FIFO order
    expected_processed = [i * 2 for i in range(1, 101)]
    assert processed_numbers == expected_processed, "Processing did not occur in FIFO order!"
