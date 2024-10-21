from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


class ProductPlatformExternalConnectionCreateRequest(Struct, forbid_unknown_fields=True):
    product_id: Annotated[int, Parameter(title="Product ID")]
    platform_id: Annotated[int, Parameter(title="Platform ID")]
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    version: Annotated[int, Parameter(title="Version")]
    external_id: Annotated[str, Parameter(title="External ID")]
    external_meta: Annotated[dict, Parameter(title="External Meta")]


class ProductPlatformExternalConnectionUpdateRequest(Struct, forbid_unknown_fields=True):
    version: Annotated[int, Parameter(title="Version")]
    external_id: Annotated[str, Parameter(title="External ID")]
    external_meta: Annotated[dict, Parameter(title="External Meta")]


class ProductPlatformExternalConnectionResponse(Struct):
    id: Annotated[int, Parameter(title="ID")]
    product_id: Annotated[int, Parameter(title="Product ID")]
    platform_id: Annotated[int, Parameter(title="Platform ID")]
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    version: Annotated[int, Parameter(title="Version")]
    external_id: Annotated[str, Parameter(title="External ID")]
    external_meta: Annotated[dict, Parameter(title="External Meta")]

    created_at: Annotated[datetime, Parameter(title="Created At")]
    updated_at: Annotated[datetime, Parameter(title="Updated At")]
