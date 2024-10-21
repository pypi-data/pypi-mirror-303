# Synaptic IPC

This project implements inter-process communication (IPC) using various protocols, including Zenoh.

## Installation

To install Synaptic and its dependencies, run:

```bash
pip install synaptic
```

## Subclassing IPC and Configuring Serializers

### Subclassing IPC

To create a custom IPC implementation:

1. Import the necessary modules:
   ```python
   from synaptic.ipc.base import IPC, IPCConfig
   ```

2. Create a new class that inherits from IPC:
   ```python
   class CustomIPC(IPC):
       def __init__(self, config: IPCConfig):
           super().__init__(config)
           # Add any custom initialization here

       def initialize(self) -> None:
           # Implement initialization logic

       def cleanup(self) -> None:
           # Implement cleanup logic

       def get(self, key, value) -> Dict:
           # Implement get logic

       def put(self, key, value) -> None:
           # Implement put logic

       def update(self, values: dict) -> None:
           # Implement update logic

       def delete(self, key) -> None:
           # Implement delete logic
   ```

### Configuring a Serializer

To configure a serializer for your IPC:

1. Import the Serializer base class:
   ```python
   from synaptic.serialization.base import Serializer
   ```

2. Create a custom serializer:
   ```python
   class CustomSerializer(Serializer):
       def tobytes(self, data):
           # Implement serialization logic

       def frombytes(self, data):
           # Implement deserialization logic
   ```

3. Use the serializer in your IPC configuration:
   ```python
   from synaptic.ipc.base import IPCConfig

   config = IPCConfig(
       serialization_protocol="custom",
       communication_protocol="your_protocol",
       # Other configuration options
   )
   custom_ipc = CustomIPC(config)
   custom_ipc.serializer = CustomSerializer()
   ```

## Using Multiprocessing Manager

For more detailed information on multiprocessing and managers, refer to the [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html#managers).

## Example Usage

Here's an example of how to use the ZenohProtocol with msgpack serialization:

```python
from synaptic.ipc.base import IPCConfig
from synaptic.synapse import State
# Configure Zenoh with msgpack serialization
config = IPCConfig(
    serialization_protocol="json",
    communication_protocol="zenoh",
    messaging_config=ZenohConfig(
        mode="peer",
        connect=[{"tcp": "localhost:7447"}],
        zenoh_key="example/state",
    )
)

with State(config) as state:
    # Put a state
    state.any_attribute = "Hello, World!"
    state.another_attribute = 42

    with State(config) as same_state:
        assert same_state.any_attribute == "Hello, World!"
        assert same_state.another_attribute == 42
            

```

# Now For A Fun Example

```python
from synaptic.synapse import State, IPCConfig
import asyncio

config = IPCConfig(
        serialization_protocol="json",
        communication_protocol="zenoh",
        messaging_config=ZenohConfig(
            mode="peer",
            connect=[{"tcp": "localhost:7447"}],
            zenoh_key="example/state",
        )
    )

async def main():
    async with State(config) as state:
        state.any_attribute = "Hello, World!"
        state.another_attribute = 42

        async with State(config) as same_state:
            async for i in range(10):
                same_state.incrementing_attribute = i
                await asyncio.sleep(1)
        
        async for i in range(10):
            print(state.incrementing_attribute)
            await asyncio.sleep(1)

asyncio.run(main())
````