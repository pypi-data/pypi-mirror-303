from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import SyncTaskStatus, SyncTaskType


class ProductPlatformSyncTaskCreateRequest(Struct, forbid_unknown_fields=True):
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    task_type: Annotated[
        SyncTaskType,
        Parameter(
            title="Task Type",
            description="The task type."
        )
    ]
    task_meta: Annotated[
        dict,
        Parameter(
            required=False,
            title="Task Meta",
            description="The task meta."
        )
    ]
    status: Annotated[
        SyncTaskStatus,
        Parameter(
            title="Status",
            description="The status."
        )
    ]
    info: Annotated[
        str | None,
        Parameter(
            required=False,
            title="Info",
            description="The info."
        )
    ] = None


class ProductPlatformSyncTaskUpdateRequest(Struct, forbid_unknown_fields=True):
    task_type: Annotated[
        SyncTaskType,
        Parameter(
            title="Task Type",
            description="The task type."
        )
    ]
    task_meta: Annotated[
        dict,
        Parameter(
            title="Task Meta",
            description="The task meta."
        )
    ]
    status: Annotated[
        SyncTaskStatus,
        Parameter(
            title="Status",
            description="The status."
        )
    ]
    info: Annotated[
        str | None,
        Parameter(
            title="Info",
            description="The info."
        )
    ]


class ProductPlatformSyncTaskResponse(Struct):
    id: Annotated[int, Parameter(title="ID")]
    product_platform_id: Annotated[int, Parameter(title="Product Platform ID")]
    task_type: Annotated[
        SyncTaskType,
        Parameter(
            title="Task Type",
            description="The task type."
        )
    ]
    task_meta: Annotated[
        dict,
        Parameter(
            title="Task Meta",
            description="The task meta."
        )
    ]
    status: Annotated[
        SyncTaskStatus,
        Parameter(
            title="Status",
            description="The status."
        )
    ]
    info: Annotated[
        str | None,
        Parameter(
            required=False,
            title="Info",
            description="The info."
        )
    ]

    created_at: Annotated[datetime, Parameter(title="Created At")]
    updated_at: Annotated[datetime, Parameter(title="Updated At")]
