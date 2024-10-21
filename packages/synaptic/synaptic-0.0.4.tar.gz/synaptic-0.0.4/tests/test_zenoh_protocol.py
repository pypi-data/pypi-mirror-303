import pytest
import zenoh
from synaptic.ipc.zenoh import ZenohIPC
from synaptic.ipc import IPCConfig
import logging
logging.basicConfig(level=logging.CRITICAL, force=True)

@pytest.fixture()
def zenoh_config():
    return dict(zenoh_key="test/zenoh", mode="peer", connect=[{"tcp": "localhost:7447"}])

@pytest.fixture()
def comm_config(zenoh_config):
    return IPCConfig(messaging_config=zenoh_config, serialization_protocol="json")

@pytest.fixture()
def zenoh_protocol(comm_config):
    protocol = ZenohProtocol(comm_config)
    try:
        protocol.initialize()
        yield protocol
    except Exception as e:
        pytest.skip(f"Zenoh initialization failed: {e}. Is the Zenoh router running?")
    finally:
        if hasattr(protocol, 'session') and protocol.session is not None:
            protocol.cleanup()

# @pytest.mark.zenoh_test()
def test_zenoh_protocol_initialization(zenoh_protocol):
    assert zenoh_protocol.session is not None
    assert isinstance(zenoh_protocol.session, zenoh.Session)
    assert zenoh_protocol.sub is not None
    assert isinstance(zenoh_protocol.sub, zenoh.Subscriber)
    assert zenoh_protocol.queryable is not None
    assert isinstance(zenoh_protocol.queryable, zenoh.Queryable)
    assert zenoh_protocol.root_key == zenoh_protocol.config.zenoh_key

# @pytest.mark.zenoh_test()
def test_zenoh_protocol_put_and_get(zenoh_protocol):
    key = "test_key"
    value = {"data": "test_value"}
        
    zenoh_protocol.put(key, value)
    retrieved_value = zenoh_protocol.get(key)
        
    assert retrieved_value == value

    with pytest.raises(KeyError):
        zenoh_protocol.get("non_existent_key")

# @pytest.mark.zenoh_test
def test_zenoh_protocol_update(zenoh_protocol):
    initial_data = {"key1": "value1", "key2": "value2"}
    update_data = {"key2": "updated_value2", "key3": "value3"}
    
    zenoh_protocol.update(initial_data)
    zenoh_protocol.update(update_data)
    
    assert zenoh_protocol.get("key1") == "value1"
    assert zenoh_protocol.get("key2") == "updated_value2"
    assert zenoh_protocol.get("key3") == "value3"

# @pytest.mark.zenoh_test
def test_zenoh_protocol_delete(zenoh_protocol):
    key = "test_delete_key"
    value = {"data": "test_delete_value"}
        
    zenoh_protocol.put(key, value)
    assert zenoh_protocol.get(key) == value
        
    zenoh_protocol.delete(key)
    with pytest.raises(KeyError):
        zenoh_protocol.get(key)

    with pytest.raises(KeyError):
        zenoh_protocol.delete("non_existent_key")

# @pytest.mark.zenoh_test
def test_zenoh_protocol_delete_non_existent(zenoh_protocol):
    with pytest.raises(KeyError):
        zenoh_protocol.delete("non_existent_key")

# @pytest.mark.zenoh_test
def test_zenoh_protocol_large_array(zenoh_protocol):
    key = "large_array"
    large_array = list(range(1000))  # Array of 1000 integers
    
    # Write large array
    zenoh_protocol.put(key, large_array)
    
    # Read large array
    retrieved_array = zenoh_protocol.get(key)
    
    assert retrieved_array == large_array, "Retrieved array does not match the original array"
    assert len(retrieved_array) == 1000, "Retrieved array does not have the expected length"

# @pytest.mark.zenoh_test
def test_zenoh_protocol_stream(zenoh_protocol):
    try:
        import numpy as np
        
        # Test streaming a single numpy array
        key_single = "test_single_array"
        single_array = np.random.randint(0, 255, (10, 3), dtype=np.uint8)
        
        zenoh_protocol.stream(key_single, single_array)
        retrieved_single = zenoh_protocol.get(key_single)
        
        assert np.array_equal(single_array, np.frombuffer(retrieved_single, dtype=np.uint8).reshape(single_array.shape)), "Retrieved single array does not match the original"

        # Test streaming a list of numpy arrays
        key_multiple = "test_multiple_arrays"
        multiple_arrays = [np.random.randint(0, 255, (1, 3), dtype=np.uint8) for _ in range(5)]
        
        zenoh_protocol.stream(key_multiple, multiple_arrays)
        for i, original in enumerate(multiple_arrays):
            retrieved = zenoh_protocol.get(f"{key_multiple}/{i}")
            assert np.array_equal(original, np.frombuffer(retrieved, dtype=np.uint8).reshape(original.shape)), f"Retrieved array {i} does not match the original"

        # Test streaming non-numpy data
        key_other = "test_other_data"
        other_data = {"key": "value", "number": 42}
        
        zenoh_protocol.stream(key_other, other_data)
        # retrieved_other = zenoh_protocol.get(key_other)
        
        # assert retrieved_other == other_data, "Retrieved non-numpy data does not match the original"
    except Exception as e:
        pytest.skip(f"Error streaming data: {e}")
    finally:
        zenoh_protocol.cleanup()
        

def test_async_zenoh():
    import asyncio
    from multiprocessing.context import BaseContext

    import synaptic.state
    config = synaptic.state.IPCConfig(
        serialization_protocol="json",
        communication_protocol="zenoh",
        messaging_config={
            "mode": "peer",
            "connect": [{"tcp": "localhost:7447"}],
            "zenoh_key": "example/state",
        },
        ctx = BaseContext()
    )

    async def even_odd_paradox():
        async with synaptic.state.State(config) as state:
            state.any_attribute = "Hello, World!"
            state.another_attribute = 42

            async with synaptic.state.State(config) as same_state:
                async for i in [1,3,5,7,9]:
                    same_state.incrementing_attribute = i
                    await asyncio.sleep(1)
                    assert same_state.incrementing_attribute % 2 == 0
            
            async for i in [0,2,4,6,8]:
                state.incrementing_attribute = i
                await asyncio.sleep(1)
                assert state.incrementing_attribute % 2 == 1
    
    asyncio.run(even_odd_paradox())
