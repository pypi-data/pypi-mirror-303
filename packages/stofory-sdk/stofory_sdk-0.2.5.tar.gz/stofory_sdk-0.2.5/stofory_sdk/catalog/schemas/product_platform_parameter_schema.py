from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import ParameterType

from .parameter_name_schema import ParameterNameResponse
from .parameter_comment_schema import ParameterCommentResponse
from .parameter_option_schema import ParameterOptionResponse


class ProductPlatformParameterCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    parameter_type: Annotated[
        ParameterType,
        Parameter(
            title="Parameter Type",
            description="The type of the parameter to create."
        )
    ]
    is_required: Annotated[
        bool,
        Parameter(
            title="Is Required",
            description="Whether the parameter is required."
        )
    ]
    order: Annotated[
        int,
        Parameter(
            title="Order",
            description="The order of the parameter."
        )
    ]


class ProductPlatformParameterUpdateRequest(Struct, forbid_unknown_fields=True):
    parameter_type: Annotated[
        ParameterType,
        Parameter(
            title="Parameter Type",
            description="The type of the parameter to update.",
        )
    ]
    is_required: Annotated[
        bool,
        Parameter(
            title="Is Required",
            description="Whether the parameter is required.",
        )
    ]
    order: Annotated[
        int,
        Parameter(
            title="Order",
            description="The order of the parameter.",
        )
    ]


class ProductPlatformParameterResponse(Struct):
    id: int
    product_platform_id: int
    version: int
    parameter_type: ParameterType
    is_required: bool
    order: int
    created_at: datetime
    updated_at: datetime

    names: list[ParameterNameResponse]
    comments: list[ParameterCommentResponse]
    options: list[ParameterOptionResponse]
