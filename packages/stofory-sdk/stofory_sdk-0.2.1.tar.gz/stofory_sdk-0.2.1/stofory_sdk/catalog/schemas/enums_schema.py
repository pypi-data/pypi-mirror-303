from litestar.params import Parameter
from msgspec import Struct


class EnumsListResponse(Struct):
    items: list[str]


class EnumListResponse(Struct):
    enum: str
    items: list[str]
