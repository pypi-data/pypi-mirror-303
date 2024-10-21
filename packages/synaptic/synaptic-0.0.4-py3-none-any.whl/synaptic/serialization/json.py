import json

from pydantic import BaseModel
from pydantic.config import JsonDict

from synaptic.serialization.serializer import Serializer


class JSONSerializer(Serializer):
    def tobytes(self, data: JsonDict) -> bytes:
        print(f"tobytes ", data)
        return json.dumps(data).encode('utf-8')

    def frombytes(self, data: bytes) -> JsonDict:
        print(f"frombytes ", data)
        try:
            return json.loads(data.decode('utf-8'))
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {data}")
            try:
                return self.tobytes(data)
            except Exception as e:
                raise json.JSONDecodeError(f"Error decoding JSON: {e}")

class PydanticSerializer(Serializer):
    model: type[BaseModel]
    def tobytes(self, data: BaseModel) -> bytes:
        return data.model_dump_json().encode('utf-8')

    def frombytes(self, data: bytes) -> JsonDict:
        return self.model.model_validate_json(data)