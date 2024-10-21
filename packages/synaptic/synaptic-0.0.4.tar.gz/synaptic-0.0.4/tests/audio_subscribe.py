import logging
import time
import numpy as np
import soundfile as sf
import os

from synaptic.ipc import IPCConfig, IPCUrlConfig
from synaptic.state import State

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Define the logger
logger = logging.getLogger(__name__)

# Directory to save the audio files
save_directory = "zenoh/"

# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Audio configuration
sample_rate = 24000  # Assuming a sample rate of 24000 Hz
channels = 1         # Assuming mono audio (1 channel)
chunk_duration = 1   # 1 second of audio per file

# Accumulation buffer
audio_buffer = np.empty((0, channels), dtype=np.float32)

# Define backend configuration for Zenoh subscriber
backend_kwargs = {
    "settings": IPCConfig(
        shared_memory_size_kb=1024,
        url=[
            IPCUrlConfig(listen="tcp/0.0.0.0:7448")
        ],  
        ipc_kind="zenoh",
        serializer="msgpack",
    ),
    "root_key": "example/state",
}

def save_audio_to_wav(audio_data, file_index):
    """
    Save the accumulated audio data as a .wav file.

    Args:
        audio_data (np.ndarray): Audio data to save.
        file_index (int): File index for naming the output file.
    """
    # Save the NumPy array as a .wav file
    file_name = f"{save_directory}received_audio_{file_index}.wav"
    sf.write(file_name, audio_data, sample_rate)
    logger.info(f"Saved {file_name}")

if __name__ == "__main__":
    try:
        with State(**backend_kwargs) as state:
            file_count = 0
            while True:
                # Check if the instruction contains audio bytes
                if state.instruction is not None:
                    audio_bytes = state.instruction
                    
                    # Convert received bytes to NumPy array
                    audio_chunk = np.frombuffer(audio_bytes, dtype=np.float32).reshape(-1, channels)
                    
                    # Append the chunk to the buffer
                    audio_buffer = np.vstack((audio_buffer, audio_chunk))
                    
                    # Save the buffer to a .wav file when it accumulates enough data for `chunk_duration` seconds
                    if len(audio_buffer) >= sample_rate * chunk_duration:
                        save_audio_to_wav(audio_buffer, file_count)
                        file_count += 1
                        
                        # Clear the buffer after saving
                        audio_buffer = np.empty((0, channels), dtype=np.float32)
                
                time.sleep(0.1)  # Add a sleep to avoid a tight loop

    except KeyboardInterrupt:
        logger.info("Exiting...")
