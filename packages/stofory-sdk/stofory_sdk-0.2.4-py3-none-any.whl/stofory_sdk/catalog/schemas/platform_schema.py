from datetime import datetime
from typing import Annotated, Dict, Any

from litestar.params import Parameter
from msgspec import Struct


class PlatformCreateRequest(Struct, forbid_unknown_fields=True):
    name: Annotated[
        str,
        Parameter(
            title="Name",
            description="The name of the platform."
        )
    ]
    description: Annotated[
        str,
        Parameter(
            title="Description",
            description="The description of the platform."
        )
    ]
    custom_fields_template: Annotated[
        Dict[str, Any],
        Parameter(
            title="Custom Fields Template",
            description="The custom fields template of the platform."
        )
    ]
    slug: Annotated[
        str,
        Parameter(
            title="Slug",
            description="The slug of the platform."
        )
    ]
    is_external: Annotated[
        bool,
        Parameter(
            title="Is External",
            description="Whether the platform is external."
        )
    ]


class PlatformUpdateRequest(Struct, forbid_unknown_fields=True):
    name: str
    description: str
    custom_fields_template: Dict[str, Any]
    slug: str
    is_external: bool


class PlatformResponse(Struct):
    id: int
    name: str
    description: str
    custom_fields_template: Dict[str, Any]
    slug: str
    is_external: bool
    created_at: datetime
    updated_at: datetime
