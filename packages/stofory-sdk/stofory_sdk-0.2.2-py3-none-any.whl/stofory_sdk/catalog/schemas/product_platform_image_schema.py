from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


class ProductPlatformImageCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    relative_path: Annotated[
        str,
        Parameter(
            title="Relative Path",
            description="The relative path of the image."
        )
    ]
    domain: Annotated[
        str,
        Parameter(
            title="Domain",
            description="The domain of the image."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="Whether the image is enabled."
        )
    ]
    order: Annotated[
        int,
        Parameter(
            title="Order",
            description="The order of the image."
        )
    ]


class ProductPlatformImageUpdateRequest(Struct, forbid_unknown_fields=True):
    relative_path: Annotated[
        str,
        Parameter(
            title="Relative Path",
            description="The relative path of the image."
        )
    ]
    domain: Annotated[
        str,
        Parameter(
            title="Domain",
            description="The domain of the image."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="Whether the image is enabled."
        )
    ]
    order: Annotated[
        int,
        Parameter(
            title="Order",
            description="The order of the image."
        )
    ]


class ProductPlatformImageResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    relative_path: str
    domain: str
    is_enabled: bool
    order: int
    created_at: datetime
    updated_at: datetime


class ProductPlatformImageUploadResponse(Struct):
    relative_path: str
    domain: str
