from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import ProductTypes

from .product_platform_schema import ProductPlatformResponse


class ProductCreateRequest(Struct, forbid_unknown_fields=True):
    name: Annotated[
        str,
        Parameter(
            title="Name",
            description="The name of the product."
        )
    ]
    description: Annotated[
        str,
        Parameter(
            title="Description",
            description="The description of the product."
        )
    ]
    product_type: Annotated[
        ProductTypes,
        Parameter(
            title="Product Type",
            description="The type of the product.",
            examples=[
                ProductTypes.STEAM_GIFT,
                ProductTypes.STEAM_TOPUP
            ]
        )
    ]
    slug: Annotated[
        str,
        Parameter(
            title="Slug",
            description="The slug of the product."
        )
    ]


class ProductUpdateRequest(Struct, forbid_unknown_fields=True):
    name: Annotated[
        str,
        Parameter(
            title="Name",
            description="The name of the product."
        )
    ]
    description: Annotated[
        str,
        Parameter(
            title="Description",
            description="The description of the product."
        )
    ]
    product_type: Annotated[
        ProductTypes,
        Parameter(
            title="Product Type",
            description="The type of the product.",
            examples=[
                ProductTypes.STEAM_GIFT,
                ProductTypes.STEAM_TOPUP
            ]
        )
    ]
    slug: Annotated[
        str,
        Parameter(
            title="Slug",
            description="The slug of the product."
        )
    ]


class ProductResponse(Struct):
    id: int
    name: str
    description: str
    product_type: ProductTypes
    status: bool
    slug: str
    created_at: datetime
    updated_at: datetime

    product_platforms: list[ProductPlatformResponse]
