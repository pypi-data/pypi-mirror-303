# import json
# import asyncio
# from typing import Any,

# from synaptic.ipc import ipcs, IPCConfig, IPC

# settings = {
#     "zenoh": {
#     "config": IPCConfig(
#         shared_memory_size_kb=1024,
#         url="localhost:7447",
#     ),
#     },
#     "root_key": "example/state",
# }

# # Configuration settings
# class State:
#     pass

# # Example of usage
# async def main() -> None:
#     async with State(**zenoh) as state:
#         # Update and retrieve state using attributes
#         await state.put("transcription", "This is a transcription example.")
#         assert await state.get("transcription") == "This is a transcription example.", "Transcription not set correctly."
#         await state.put("instruction", "Translate the transcription.")
#         assert await state.get("instruction") == "Translate the transcription.", "Instruction not set correctly."
#         await state.put("response", "Translation done.")
#         assert await state.get("response") == "Translation done.", "Response not set correctly."
#         await state.put("response_json", json.dumps({"translation": "Translation done."}))
#         assert await state.get("response_json") == json.dumps({"translation": "Translation done."}), "Response JSON not set correctly."
#         # Update state again
#         await state.put("additional_info", "This is some additional information.")
#         input("Press Enter to continue...")
#         async with State(settings) as state2:
#             assert await state2.get("additional_info") == "This is some additional information.", "Additional info not set correctly."

#         # Modify an existing state key
#         await state.put("transcription", "Updated transcription.")
#         assert await state.get("transcription") == "Updated transcription.", "Transcription not updated correctly."

# if __name__ == "__main__":
#     asyncio.run(main())
