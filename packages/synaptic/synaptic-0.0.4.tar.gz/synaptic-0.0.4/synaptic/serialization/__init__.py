from typing import Final, Generic, Type, TypeAlias, TypedDict, TypeVar

from .json import JSONSerializer, PydanticSerializer
from .msgpack import MsgPackSerializer
from .protobuf import ProtobufSerializer
from .serializer import Serializer


class SerializerMap(TypedDict):
    json: Type[JSONSerializer]
    pydantic: Type[PydanticSerializer] 
    msgpack: Type[MsgPackSerializer] 
    protobuf: Type[ProtobufSerializer] 


serializers: Final[SerializerMap[str, Serializer]] = {
    "json": JSONSerializer,
    "pydantic": PydanticSerializer,
    "msgpack": MsgPackSerializer,
    "protobuf": ProtobufSerializer,
}


SerializerType: Type = Serializer | JSONSerializer | PydanticSerializer | MsgPackSerializer | ProtobufSerializer 