import time
import pytest
from synaptic.ipc import IPCConfig, IPCUrlConfig
from synaptic.ipc.zenoh import ZenohIPC

# Pytest fixture to set up the ZenohIPC instance and tear it down after the test
@pytest.fixture
def zenoh_ipc_setup():
    """
    Fixture to set up ZenohIPC with the required configuration and yield it for testing.

    Yields:
        ZenohIPC: The ZenohIPC instance.
    """
    ipc_config = IPCConfig(
        url=[
            IPCUrlConfig(connect="tcp/149.130.215.195:7448"), 
            IPCUrlConfig(connect="tcp/0.0.0.0:7448"),
        ],
        serializer='msgpack'  # Ensure the serializer matches your setup
    )
    test_root_key = "test/zenoh_ipc_test"
    zenoh_ipc = ZenohIPC(settings=ipc_config, root_key=test_root_key)
    zenoh_ipc.initialize()

    yield zenoh_ipc  # Yield the ZenohIPC instance for use in the test

    zenoh_ipc.cleanup()  # Cleanup after the test is done

# Test for put, get_latest, and get_earliest methods
def test_zenoh_ipc_put_and_get(zenoh_ipc_setup):
    """
    Test that verifies the 'put', 'get_latest', and 'get_earliest' methods of ZenohIPC.

    Args:
        zenoh_ipc_setup (ZenohIPC): The ZenohIPC instance set up for testing.
    """
    zenoh_ipc = zenoh_ipc_setup

    # Putting some values
    zenoh_ipc.put("sensor_data_1", {"temp": 25})
    time.sleep(0.1)  # Allow listener to process
    zenoh_ipc.put("sensor_data_2", {"temp": 30})
    time.sleep(0.1)  # Allow listener to process
    zenoh_ipc.put("sensor_data_3", {"temp": 35})
    time.sleep(0.1)  # Allow listener to process

    # Get the latest added value
    latest_value = zenoh_ipc.get_latest()
    assert latest_value == {"temp": 35}, f"Expected latest value to be {{'temp': 35}}, but got {latest_value}"

    # Get the earliest added value
    earliest_value = zenoh_ipc.get_earliest()
    assert earliest_value == {"temp": 25}, f"Expected earliest value to be {{'temp': 25}}, but got {earliest_value}"


# Example of how you would run this as a pytest
if __name__ == "__main__":
    pytest.main(["-v", __file__])
