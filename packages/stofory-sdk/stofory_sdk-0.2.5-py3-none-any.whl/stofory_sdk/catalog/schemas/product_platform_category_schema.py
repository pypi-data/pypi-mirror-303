from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .category_schema import CategoryResponse


class ProductPlatformCategoryCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[
        int,
        Parameter(
            title="Product Platform ID",
            description="The ID of the product platform."
        )
    ]
    category_id: Annotated[
        int,
        Parameter(
            title="Category ID",
            description="The ID of the category."
        )
    ]


class ProductPlatformCategoryUpdateRequest(Struct, forbid_unknown_fields=True):
    category_id: Annotated[
        int,
        Parameter(
            title="Category ID",
            description="The ID of the category."
        )
    ]


class ProductPlatformCategoryResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    category_id: int
    created_at: datetime
    updated_at: datetime

    category: CategoryResponse
