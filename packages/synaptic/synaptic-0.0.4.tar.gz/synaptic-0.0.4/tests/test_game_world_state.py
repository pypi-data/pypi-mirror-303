import pytest
import logging
from synaptic.ipc import IPCConfig, ipcs
from synaptic.serialization.json import JSONSerializer

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def ipc_protocol():
    config = IPCConfig(
        ipc_kind="zenoh",
        serializer="json",
        url="tcp://localhost:7447",
    )
    IPCClass = ipcs[config.ipc_kind]
    protocol = IPCClass(config)
    protocol.serializer = JSONSerializer()
    protocol.initialize()
    yield protocol
    protocol.cleanup()

def test_game_world_state_update(ipc_protocol):
    # Initial game world state
    initial_state = {
        "players": {
            "player1": {"position": [0, 0], "health": 100, "inventory": ["sword"]},
            "player2": {"position": [10, 10], "health": 100, "inventory": ["bow"]}
        },
        "enemies": {
            "enemy1": {"position": [5, 5], "health": 50, "type": "goblin"},
            "enemy2": {"position": [15, 15], "health": 75, "type": "orc"}
        },
        "items": {
            "item1": {"position": [3, 3], "type": "health_potion"},
            "item2": {"position": [7, 7], "type": "gold_coin"}
        }
    }

    # Set initial state
    ipc_protocol.put("game/world_state", initial_state)

    # Simulate world state update
    updated_state = ipc_protocol.get("game/world_state")
    updated_state["players"]["player1"]["position"][0] += 1
    updated_state["players"]["player2"]["position"][1] -= 1
    updated_state["enemies"]["enemy1"]["position"][0] -= 1
    updated_state["enemies"]["enemy2"]["position"][1] += 1

    # Player1 picks up the health potion
    if updated_state["players"]["player1"]["position"] == updated_state["items"]["item1"]["position"]:
        updated_state["players"]["player1"]["inventory"].append("health_potion")
        del updated_state["items"]["item1"]

    # Update the world state in the IPC
    ipc_protocol.put("game/world_state", updated_state)

    # Retrieve the updated state
    final_state = ipc_protocol.get("game/world_state")

    # Assertions
    assert final_state["players"]["player1"]["position"] == [1, 0]
    assert final_state["players"]["player2"]["position"] == [10, 9]
    assert final_state["enemies"]["enemy1"]["position"] == [4, 5]
    assert final_state["enemies"]["enemy2"]["position"] == [15, 16]
    assert "health_potion" not in final_state["players"]["player1"]["inventory"]
    assert "item1" in final_state["items"]
