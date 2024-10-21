from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .localization_schema import LocalizationResponse


class ProductPlatformDescriptionCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    localization_id: Annotated[
        int,
        Parameter(
            title="Localization ID",
            description="The ID of the localization."
        )
    ]
    value: Annotated[
        str,
        Parameter(
            title="Value",
            description="The value of the description."
        )
    ]


class ProductPlatformDescriptionUpdateRequest(Struct, forbid_unknown_fields=True):
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
            description="The value of the description."
        )
    ]


class ProductPlatformDescriptionResponse(Struct):
    id: int
    product_platform_id: int
    localization_id: int
    version: int
    value: str
    created_at: datetime
    updated_at: datetime

    locale: LocalizationResponse
