from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import Currency, PricingType


class ProductPlatformPricingCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    pricing_type: Annotated[
        PricingType,
        Parameter(
            title="Pricing Type",
            description="The pricing type."
        )
    ]
    currency: Annotated[
        Currency,
        Parameter(
            title="Currency",
            description="The currency."
        )
    ]
    price: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Price",
            description="The price."
        )
    ] = None
    price_per_unit: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Price Per Unit",
            description="The price per unit."
        )
    ] = None
    min_quantity: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Min Quantity",
            description="The min quantity."
        )
    ] = None
    max_quantity: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Max Quantity",
            description="The max quantity."
        )
    ] = None
    unit_name: Annotated[
        str | None,
        Parameter(
            required=False,
            title="Unit Name",
            description="The unit name."
        )
    ] = None


class ProductPlatformPricingUpdateRequest(Struct, forbid_unknown_fields=True):
    pricing_type: Annotated[
        PricingType,
        Parameter(
            title="Pricing Type",
            description="The pricing type."
        )
    ]
    currency: Annotated[
        Currency,
        Parameter(
            title="Currency",
            description="The currency."
        )
    ]
    price: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Price",
            description="The price."
        )
    ] = None
    price_per_unit: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Price Per Unit",
            description="The price per unit."
        )
    ] = None
    min_quantity: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Min Quantity",
            description="The min quantity."
        )
    ] = None
    max_quantity: Annotated[
        int | None,
        Parameter(
            required=False,
            title="Max Quantity",
            description="The max quantity."
        )
    ] = None
    unit_name: Annotated[
        str | None,
        Parameter(
            required=False,
            title="Unit Name",
            description="The unit name."
        )
    ] = None


class ProductPlatformPricingResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    pricing_type: PricingType
    currency: Currency
    price: int | None
    price_per_unit: int | None
    min_quantity: int | None
    max_quantity: int | None
    unit_name: str | None
    created_at: datetime
    updated_at: datetime
