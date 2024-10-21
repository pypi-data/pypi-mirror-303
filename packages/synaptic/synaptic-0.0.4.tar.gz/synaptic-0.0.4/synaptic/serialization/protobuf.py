from synaptic.serialization.serializer import Serializer


class ProtobufSerializer(Serializer):
    def tobytes(self, data: dict) -> bytes:
        raise NotImplementedError
      
    def frombytes(self, data: bytes) -> dict:
        raise NotImplementedError