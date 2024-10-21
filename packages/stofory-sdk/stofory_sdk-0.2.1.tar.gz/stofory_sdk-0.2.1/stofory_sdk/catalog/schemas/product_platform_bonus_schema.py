from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct


class ProductPlatformBonusCreateRequest(Struct, forbid_unknown_fields=True):
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
            description="The status of the bonus."
        )
    ]
    percent: Annotated[
        int,
        Parameter(
            title="Percent",
            description="The percent of the bonus."
        )
    ]


class ProductPlatformBonusUpdateRequest(Struct, forbid_unknown_fields=True):
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The status of the bonus."
        )
    ]
    percent: Annotated[
        int,
        Parameter(
            title="Percent",
            description="The percent of the bonus."
        )
    ]


class ProductPlatformBonusResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    is_enabled: bool
    percent: int
    created_at: datetime
    updated_at: datetime
