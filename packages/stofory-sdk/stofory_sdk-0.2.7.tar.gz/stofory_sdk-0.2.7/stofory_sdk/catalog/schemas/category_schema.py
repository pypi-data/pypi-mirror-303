from datetime import datetime
from typing import Annotated, Any

from sqlalchemy_utils.types.ltree import Ltree
from litestar.params import Parameter
from msgspec import Struct


class CategoryCreateRequest(Struct, forbid_unknown_fields=True):
    platform_id: Annotated[
        int,
        Parameter(
            title="Platform ID",
            description="The ID of the platform."
        )
    ]
    name: Annotated[
        str,
        Parameter(
            title="Name",
            description="The name of the category."
        )
    ]
    slug: Annotated[
        str,
        Parameter(
            title="Slug",
            description="The slug of the category."
        )
    ]
    path: Annotated[
        Any,
        Parameter(
            title="Path",
            description="The path of the category."
        )
    ]
    parent_id: Annotated[
        int | None,
        Parameter(
            title="Parent ID",
            description="The ID of the parent category."
        )
    ] = None


class CategoryUpdateRequest(Struct, forbid_unknown_fields=True):
    platform_id: Annotated[
        int,
        Parameter(
            title="Platform ID",
            description="The ID of the platform."
        )
    ]
    parent_id: Annotated[
        int | None,
        Parameter(
            title="Parent ID",
            description="The ID of the parent category."
        )
    ]
    path: Annotated[
        Any,
        Parameter(
            title="Path",
            description="The path of the category."
        )
    ]
    name: Annotated[
        str,
        Parameter(
            title="Name",
            description="The name of the category."
        )
    ]
    slug: Annotated[
        str,
        Parameter(
            title="Slug",
            description="The slug of the category."
        )
    ]


class CategoryResponse(Struct):
    id: int
    platform_id: int
    parent_id: int | None
    path: Any
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
