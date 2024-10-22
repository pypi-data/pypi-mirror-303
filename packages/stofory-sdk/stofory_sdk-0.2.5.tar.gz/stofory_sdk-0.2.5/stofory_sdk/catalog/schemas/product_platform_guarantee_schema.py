from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


class ProductPlatformGuaranteeCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[
        int,
        Parameter(
            title="Product Platform ID",
            description="The product platform ID."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The is enabled."
        )
    ]
    value: Annotated[
        int,
        Parameter(
            title="Value",
            description="The value."
        )
    ]


class ProductPlatformGuaranteeUpdateRequest(Struct, forbid_unknown_fields=True):
    value: Annotated[
        int,
        Parameter(
            title="Value",
            description="The value."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The is enabled."
        )
    ]


class ProductPlatformGuaranteeResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    is_enabled: bool
    value: int
    created_at: datetime
    updated_at: datetime
