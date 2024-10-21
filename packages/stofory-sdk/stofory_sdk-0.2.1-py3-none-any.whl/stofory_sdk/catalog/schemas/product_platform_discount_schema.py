from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


class ProductPlatformDiscountCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[
        int,
        Parameter(
            title="Product Platform ID",
            description="The ID of the product platform."
        )
    ]
    unit_for_discount: Annotated[
        int,
        Parameter(
            title="Unit For Discount",
            description="The unit for discount."
        )
    ]
    discount: Annotated[
        int,
        Parameter(
            title="Discount",
            description="The discount."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The is enabled."
        )
    ]


class ProductPlatformDiscountUpdateRequest(Struct, forbid_unknown_fields=True):
    unit_for_discount: Annotated[
        int,
        Parameter(
            title="Unit For Discount",
            description="The unit for discount."
        )
    ]
    discount: Annotated[
        int,
        Parameter(
            title="Discount",
            description="The discount."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The is enabled."
        )
    ]


class ProductPlatformDiscountResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    unit_for_discount: int
    discount: int
    is_enabled: bool
    created_at: datetime
    updated_at: datetime
