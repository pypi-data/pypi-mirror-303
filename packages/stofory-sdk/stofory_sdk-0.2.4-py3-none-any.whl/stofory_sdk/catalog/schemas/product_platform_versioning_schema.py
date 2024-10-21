from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


from .product_platform_schema import ProductPlatformResponse


class ProductPlatformVersioningCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    version: Annotated[int, Parameter(title="Version")]
    history: Annotated[list[ProductPlatformResponse], Parameter(title="History")]


class ProductPlatformVersioningUpdateRequest(Struct, forbid_unknown_fields=True):
    version: Annotated[int, Parameter(title="Version")]
    history: Annotated[list[ProductPlatformResponse], Parameter(title="History")]


class ProductPlatformVersioningResponse(Struct):
    id: Annotated[int, Parameter(title="ID")]
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    version: Annotated[int, Parameter(title="Version")]
    history: Annotated[list[ProductPlatformResponse], Parameter(title="History")]

    created_at: Annotated[datetime, Parameter(title="Created At")]
    updated_at: Annotated[datetime, Parameter(title="Updated At")]
