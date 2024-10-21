from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .platform_schema import PlatformResponse
from .product_platform_name_schema import ProductPlatformNameResponse
from .product_platform_description_schema import ProductPlatformDescriptionResponse
from .product_platform_category_schema import ProductPlatformCategoryResponse
from .product_platform_pricing_schema import ProductPlatformPricingResponse
from .product_platform_bonus_schema import ProductPlatformBonusResponse
from .product_platform_guarantee_schema import ProductPlatformGuaranteeResponse
from .product_platform_discount_schema import ProductPlatformDiscountResponse
from .product_platform_parameter_schema import ProductPlatformParameterResponse
from .product_platform_image_schema import ProductPlatformImageResponse
from .product_platform_video_schema import ProductPlatformVideoResponse


class ProductPlatformCreateRequest(Struct, forbid_unknown_fields=True):
    product_id: Annotated[
        int,
        Parameter(
            title="Product ID",
            description="The ID of the product."
        )
    ]
    platform_id: Annotated[
        int,
        Parameter(
            title="Platform ID",
            description="The ID of the platform."
        )
    ]
    custom_fields: Annotated[
        dict,
        Parameter(
            title="Custom Fields",
            description="The custom fields of the product."
        )
    ]


class ProductPlatformUpdateRequest(Struct, forbid_unknown_fields=True):
    custom_fields: Annotated[
        dict,
        Parameter(
            title="Custom Fields",
            description="The custom fields of the product."
        )
    ]


class ProductPlatformResponse(Struct):
    id: int
    product_id: int
    platform_id: int
    version: int
    is_enabled: bool
    custom_fields: dict
    created_at: datetime
    updated_at: datetime

    platform: PlatformResponse | None = None
    names: list[ProductPlatformNameResponse] = []
    descriptions: list[ProductPlatformDescriptionResponse] = []
    categories: list[ProductPlatformCategoryResponse] = []
    parameters: list[ProductPlatformParameterResponse] = []
    images: list[ProductPlatformImageResponse] = []
    videos: list[ProductPlatformVideoResponse] = []
    price: ProductPlatformPricingResponse | None = None
    bonus: ProductPlatformBonusResponse | None = None
    discount: ProductPlatformDiscountResponse | None = None
    guarantee: ProductPlatformGuaranteeResponse | None = None
