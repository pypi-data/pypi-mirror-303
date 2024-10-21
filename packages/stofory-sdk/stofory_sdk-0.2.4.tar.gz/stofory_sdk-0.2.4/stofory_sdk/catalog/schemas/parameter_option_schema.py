from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import ModifierOperator

from .parameter_option_name_schema import ParameterOptionNameResponse


class ParameterOptionCreateRequest(Struct, forbid_unknown_fields=True):
    parameter_id: Annotated[int, Parameter(title="Parameter ID")]
    modifier_operator: Annotated[
        ModifierOperator,
        Parameter(
            title="Modifier Operator",
            description="The modifier operator of the product parameter option."
        )
    ]
    modifier_value: Annotated[
        float,
        Parameter(
            title="Modifier Value",
            description="The modifier value of the product parameter option."
        )
    ]
    is_default: Annotated[
        bool,
        Parameter(
            title="Is Default",
            description="The default status of the product parameter option."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The enabled status of the product parameter option."
        )
    ]
    order: Annotated[
        int,
        Parameter(
            title="Order",
            description="The order of the product parameter option."
        )
    ]


class ParameterOptionUpdateRequest(Struct, forbid_unknown_fields=True):
    modifier_operator: Annotated[
        ModifierOperator,
        Parameter(
            title="Modifier Operator",
            description="The modifier operator of the product parameter option."
        )
    ]
    modifier_value: Annotated[
        float,
        Parameter(
            title="Modifier Value",
            description="The modifier value of the product parameter option."
        )
    ]
    is_default: Annotated[
        bool,
        Parameter(
            title="Is Default",
            description="The default status of the product parameter option."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The enabled status of the product parameter option."
        )
    ]
    order: Annotated[
        int,
        Parameter(
            title="Order",
            description="The order of the product parameter option."
        )
    ]


class ParameterOptionResponse(Struct):
    id: int
    parameter_id: int
    version: int
    modifier_operator: ModifierOperator
    modifier_value: float
    is_default: bool
    is_enabled: bool
    order: int
    created_at: datetime
    updated_at: datetime

    names: list[ParameterOptionNameResponse]
