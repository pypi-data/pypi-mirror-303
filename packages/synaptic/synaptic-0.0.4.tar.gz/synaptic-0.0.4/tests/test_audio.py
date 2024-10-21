import soundfile as sf
import numpy as np
import logging
from synaptic.ipc import IPCConfig, IPCUrlConfig
from synaptic.state import State

logging.basicConfig(level=logging.CRITICAL)

def audio_file_stream(file_path, block_size=1024):
    """
    Generator that yields audio data from a file in chunks.

    Args:
        file_path (str): Path to the audio file.
        block_size (int): Number of samples per block.

    Yields:
        np.ndarray: A numpy array containing audio data.
    """
    # Load the entire audio file
    audio_data, sample_rate = sf.read(file_path, dtype='float32')
    
    # Split the audio file into chunks
    for start_idx in range(0, len(audio_data), block_size):
        end_idx = start_idx + block_size
        yield audio_data[start_idx:end_idx], sample_rate

# Define backend configuration for Zenoh
backend_kwargs = {
    "settings": IPCConfig(
        shared_memory_size_kb=1024,
        url=[
            IPCUrlConfig(connect="tcp/149.130.215.195:7448"),
        ],  
        ipc_kind="zenoh",
        serializer="msgpack",
    ),
    "root_key": "example/state",
}

if __name__ == "__main__":
    # Path to the audio file to send
    audio_file_path = "synaptic/tests/file_example_WAV_1MG.wav"

    # Get audio chunks from the file
    audio_gen = audio_file_stream(audio_file_path)

    with State(**backend_kwargs) as state:
        try:
            for audio_chunk, sample_rate in audio_gen:
                # Convert audio chunk to bytes and send it through Zenoh
                state.instruction = audio_chunk.tobytes()
                print(f"Sent audio chunk of size: {len(audio_chunk.tobytes())} bytes")
        except KeyboardInterrupt:
            print("Audio streaming stopped.")
