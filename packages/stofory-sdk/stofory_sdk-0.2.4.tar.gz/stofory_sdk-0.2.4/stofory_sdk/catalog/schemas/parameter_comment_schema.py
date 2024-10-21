from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from .localization_schema import LocalizationResponse


class ParameterCommentCreateRequest(Struct, forbid_unknown_fields=True):
    parameter_id: Annotated[int, Parameter(title="Parameter ID", description="The ID of the product parameter.")]
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
            description="The value of the product parameter comment."
        )
    ]


class ParameterCommentUpdateRequest(Struct, forbid_unknown_fields=True):
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
            description="The value of the product parameter comment."
        )
    ]


class ParameterCommentResponse(Struct):
    id: int
    parameter_id: int
    localization_id: int
    version: int
    value: str
    created_at: datetime
    updated_at: datetime

    locale: LocalizationResponse
