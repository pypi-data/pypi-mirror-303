# import time
# # Example of usage
# def main() -> None:
#     with State(**backend_kwargs) as state:
#         # Update and retrieve state using attributes
#         state.transcription = "This is a transcription example."
#         time.sleep(0.1)
#         assert (
#             state.transcription == "This is a transcription example."
#         ), f"Transcription not set correctly. Got: {state.transcription}"
#         state.instruction = "Translate the transcription."
#         time.sleep(0.1)
#         assert state.instruction == "Translate the transcription.", "Instruction not set correctly."
#         state.response = "Translation done."
#         time.sleep(0.1)
#         assert state.response == "Translation done.", "Response not set correctly."
#         state.response_json = json.dumps({"translation": "Translation done."})
#         time.sleep(0.1)
#         assert state.response_json == json.dumps(
#             {"translation": "Translation done."}
#         ), "Response JSON not set correctly."
#         # Update state again
#         state.additional_info = "This is some additional information."
#         time.sleep(0.2)
#         input("Press Enter to continue...")
#         with State(**backend_kwargs.copy()) as state2:
#             state2.transcription = "This is a transcription example."
#             time.sleep(0.1)
#             assert (
#                 state2.additional_info == "This is some additional information."
#             ), f"Additional info not set correctly. Got: {state2.additional_info}"

#         # Modify an existing state key
#         state.transcription = "Updated transcription."
#         time.sleep(0.1)
#         assert (
#             state.transcription == "Updated transcription."
#         ), f"Transcription not updated correctly. Got: {state.transcription}"


# def stream_example() -> None:
#     with State(**backend_kwargs) as state:
#         # Update and retrieve state using attributes
#         for word in ["This", "is", "a", "streaming", "example."]:
#             state.put("transcription", word)
#             with State(**backend_kwargs.copy()) as state2:
#                 assert state2.transcription == word, f"Transcription not set correctly. Got: {state2.transcription}"
#                 state2.transcription = "Updated transcription."
#             assert (
#                 state.transcription == "Updated transcription."
#             ), f"Transcription not updated correctly. Got: {state2.transcription}"
#             state.transcription = state.transcription
#             print(f"Transcription: {state.transcription}")
#             input("Press Enter to continue...")

#         state.transcription = "example."
#         assert state.transcription == "example.", f"Transcription not set correctly. Got: {state.transcription}"


# __all__ = ["State", "MySpecialState"]
# if __name__ == "__main__":
#     main()

# class MySpecialState(State):
#     a_list: list[str] = Field(default_factory=list)
#     a_dict: dict[str, str] = Field(default_factory=dict)
#     b: int = 0

