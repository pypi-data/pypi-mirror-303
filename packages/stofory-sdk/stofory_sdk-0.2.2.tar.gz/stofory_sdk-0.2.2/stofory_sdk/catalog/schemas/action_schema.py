from datetime import datetime
from typing import Annotated, Any

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import SyncTaskStatus, SyncTaskType

from .product_platform_schema import ProductPlatformResponse

from .product_platform_sync_task_schema import ProductPlatformSyncTaskResponse
from .product_platform_external_connection_schema import ProductPlatformExternalConnectionResponse


class ValidateProductPlatfromEnablingResponse(Struct):
    result: Annotated[bool, Parameter(title="Result", description="The result of the operation.")]
    data: ProductPlatformResponse
    messages: Annotated[list[str], Parameter(title="Messages", description="Potential reasons for failure.")] = []


# class ProductPlatformSyncTaskResponse(Struct):
#     id: Annotated[int, Parameter(title="ID", description="The ID of the product platform sync task.")]
#     product_platform_id: Annotated[int, Parameter(title="Product Platform ID", description="The ID of the product platform.")]
#     task_type: Annotated[SyncTaskType, Parameter(title="Task Type", description="The type of the task.")]
#     task_meta: Annotated[dict, Parameter(title="Task Meta", description="The metadata of the task.")]
#     status: Annotated[SyncTaskStatus, Parameter(title="Status", description="The status of the task.")]
#     info: Annotated[str | None, Parameter(title="Info", description="Additional information about the task.")]
#
#     created_at: Annotated[datetime, Parameter(title="Created At", description="The timestamp of the creation of the task.")]
#     updated_at: Annotated[datetime, Parameter(title="Updated At", description="The timestamp of the last update of the task.")]
#
#
# class ProductPlatformExternalConnectionResponse(Struct):
#     id: Annotated[int, Parameter(title="ID", description="The ID of the product platform external connection.")]
#     product_id: Annotated[int, Parameter(title="Product ID", description="The ID of the product.")]
#     platform_id: Annotated[int, Parameter(title="Platform ID", description="The ID of the platform.")]
#     product_platform_id: Annotated[int, Parameter(title="Product Platform ID", description="The ID of the product platform.")]
#     version: Annotated[str, Parameter(title="Version", description="The version of the external connection.")]
#     external_id: Annotated[str, Parameter(title="External ID", description="The external ID of the external connection.")]
#     external_meta: Annotated[dict, Parameter(title="External Meta", description="The metadata of the external connection.")]
#
#     created_at: Annotated[datetime, Parameter(title="Created At", description="The timestamp of the creation of the external connection.")]
#     updated_at: Annotated[datetime, Parameter(title="Updated At", description="The timestamp of the last update of the external connection.")]


class CheckProductPlatformSyncResponse(Struct):
    result: Annotated[bool, Parameter(title="Result", description="The result of the operation.")]
    message: Annotated[str, Parameter(title="Message", description="Additional information about the task.")]
    external_connection: Annotated[ProductPlatformExternalConnectionResponse | None, Parameter(title="External Connection", description="The external connection of the product platform.")] = None
    sync_task: Annotated[ProductPlatformSyncTaskResponse | None, Parameter(title="Sync Task", description="The sync task of the product platform.")] = None


class SyncProductPlatformResponse(Struct):
    result: Annotated[bool, Parameter(title="Result", description="The result of the operation.")]
    message: Annotated[str, Parameter(title="Message", description="Additional information about the task.")]
    external_connection: Annotated[
        ProductPlatformExternalConnectionResponse | None, Parameter(title="External Connection",
                                                                    description="The external connection of the product platform.")] = None
    sync_task: Annotated[ProductPlatformSyncTaskResponse | None, Parameter(title="Sync Task", description="The sync task of the product platform.")] = None
