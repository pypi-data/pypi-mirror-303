import base64
import logging
from abc import ABC, abstractmethod

import numpy as np


class UNSET(str):
    def __repr__(self):
        return "UNSET"
    def __bool__(self):
        return False
    def __eq__(self, other):
        return isinstance(other, UNSET)
    def __ne__(self, other):
        return not isinstance(other, UNSET)
        
# def is_utf8(data: bytes) -> bool:
#     if not isinstance(data, bytes):
#         return False
#     i = 0
#     length = len(data)
#     while i < length:
#         try:
#             # Attempt to decode a small chunk at a time (up to 4 bytes for UTF-8)
#             i += len(data[i:i+4].decode('utf-8'))
#         except UnicodeDecodeError:
#             return False
#     return True

class Serializer(ABC):
    name: str = UNSET
    @abstractmethod
    def tobytes(self, data):
        pass

    @abstractmethod
    def frombytes(self, data):
        pass

    def __call__(self, data, tobytes: bool | None = None, **kwargs):
        if tobytes is not None:
            if isinstance(data, np.ndarray):
                data = self.handle_numpy(data)
            return self.tobytes(data) if tobytes else self.frombytes(data)
        logging.debug(f"DATA {data}")
        data = self.frombytes(data) if isinstance(data, bytes)  else self.tobytes(data)
        try:
            data = self.handle_numpy(data)
        except Exception as e:
            if kwargs.get("type") == "numpy.ndarray":
                logging.warning(f"Error handling numpy data: {e}")
            return data
    
    def handle_numpy(self, data: dict | bytes) -> np.ndarray | dict | None:
        if isinstance(data, dict):
            return np.frombuffer(base64.b64decode(data['data']), dtype=data['dtype']).reshape(data['shape'])

        return  {
            'type': 'numpy.ndarray',
            'shape': data.shape,
            'dtype': str(data.dtype),
            'data': base64.b64encode(data.tobytes()).decode('ascii')
        }
