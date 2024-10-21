from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .localization_schema import LocalizationResponse


class ParameterOptionNameCreateRequest(Struct, forbid_unknown_fields=True):
    parameter_option_id: Annotated[int, Parameter(title="Parameter Option ID")]
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
            description="The value of the product parameter name."
        )
    ]


class ParameterOptionNameUpdateRequest(Struct, forbid_unknown_fields=True):
    # localization_id: Annotated[
    #     int,
    #     Parameter(
    #         title="Localization ID",
    #         description="The ID of the localization."
    #     )
    # ]
    value: Annotated[
        str,
        Parameter(
            title="Value",
            description="The value of the product parameter name."
        )
    ]


class ParameterOptionNameResponse(Struct):
    id: int
    parameter_option_id: int
    localization_id: int
    version: int
    value: str
    created_at: datetime
    updated_at: datetime

    locale: LocalizationResponse
