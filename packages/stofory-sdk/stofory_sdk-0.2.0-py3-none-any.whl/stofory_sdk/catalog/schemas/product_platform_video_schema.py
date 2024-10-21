from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


class ProductPlatformVideoCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    url: Annotated[
        str,
        Parameter(
            title="Video URL",
            description="The URL of the video."
        )
    ]
    platform: Annotated[
        str,
        Parameter(
            title="Platform",
            description="The platform of the video."
        )
    ]


class ProductPlatformVideoUpdateRequest(Struct, forbid_unknown_fields=True):
    url: Annotated[
        str,
        Parameter(
            title="Video URL",
            description="The URL of the video."
        )
    ]
    platform: Annotated[
        str,
        Parameter(
            title="Platform",
            description="The platform of the video."
        )
    ]


class ProductPlatformVideoResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    url: str
    platform: str
    created_at: datetime
    updated_at: datetime
