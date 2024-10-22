from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .localization_schema import LocalizationResponse


class ProductPlatformNameCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID", description="The ID of the product platform.")]
    localization_id: Annotated[int, Parameter(title="Localization ID", description="The ID of the localization.")]
    value: Annotated[str, Parameter(title="Value", description="The value.")]


class ProductPlatformNameUpdateRequest(Struct, forbid_unknown_fields=True):
    # localization_id: Annotated[
    #     int | None,
    #     Parameter(
    #         required=False,
    #         title="Localization ID",
    #         description="The ID of the localization."
    #     )
    # ] = None
    value: Annotated[
        str,
        Parameter(
            title="Value",
            description="The value."
        )
    ]


class ProductPlatformNameResponse(Struct):
    id: int
    product_platform_id: int
    localization_id: int
    version: int
    value: str
    created_at: datetime
    updated_at: datetime

    locale: LocalizationResponse
