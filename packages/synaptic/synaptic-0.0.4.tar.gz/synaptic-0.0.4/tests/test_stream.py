import pytest
from synaptic.ipc import IPCConfig
from synaptic.state import State, MySpecialState

@pytest.fixture
def zeno_kwargs():
    config = IPCConfig(
            serializer="msgpack",
            url="localhost:7447",
            ipc_kind="zenoh",
    )
    return {"settings": config, "root_key": "example/state", "mode": "peer"}

def test_put_and_get(zenoh_protocol):
    key = "test/data"
    value = {"test": "data"}
    zenoh_protocol.put(key, value)
    retrieved_value = zenoh_protocol.get(key)
    assert retrieved_value == value

def test_update(zenoh_protocol):
    values = {
        "test/data1": {"test": "data1"},
        "test/data2": {"test": "data2"}
    }
    zenoh_protocol.update(values)
    for key, value in values.items():
        retrieved_value = zenoh_protocol.get(key)
        assert retrieved_value == value

def test_delete(zenoh_protocol):
    key = "test/data"
    value = {"test": "data"}
    zenoh_protocol.put(key, value)
    zenoh_protocol.delete(key)
    with pytest.raises(KeyError):
        zenoh_protocol.get(key)

from threading import Thread, Lock
import time

def test_stream(zeno_kwargs):
    key = "test/stream"
    values = [1, 2, 3, 4, 5]


    def publisher():
        with MySpecialState(**zeno_kwargs) as state:
            for value in values:
                state.b = value
                time.sleep(0.5)  # Small delay to ensure order

    # Start publishing in a separate thread
    publisher_thread = Thread(target=publisher, daemon=True)
    publisher_thread.start()
    received_values = []
    def consumer():
        with MySpecialState(**zeno_kwargs.copy()) as state2:
          
            start_time = time.time()
            for value in  state2.stream("b"):
                print(f"CONSUMED: {value}")
                received_values.append(value)
                if time.time() - start_time > 1:
                    break
            assert received_values == values, f"Expected {values}, but got {received_values}"
    consumer()
        # Ensure we received the expected values
    assert received_values == values, f"Expected {values}, but got {received_values}"
    publisher_thread.join(10)

        
        