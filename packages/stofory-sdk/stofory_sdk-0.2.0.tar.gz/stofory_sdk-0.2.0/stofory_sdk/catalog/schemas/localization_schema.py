from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from stofory_sdk.catalog.models.enums import Locale


class LocalizationCreateRequest(Struct, forbid_unknown_fields=True):
    locale: Annotated[
        Locale,
        Parameter(
            title="Locale",
            description="The locale of the localization."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The enabled status of the localization."
        )
    ]


class LocalizationUpdateRequest(Struct, forbid_unknown_fields=True):
    locale: Annotated[
        Locale,
        Parameter(
            title="Locale",
            description="The locale of the localization."
        )
    ]
    is_enabled: Annotated[
        bool,
        Parameter(
            title="Is Enabled",
            description="The enabled status of the localization."
        )
    ]


class LocalizationResponse(Struct):
    id: int
    locale: Locale
    is_enabled: bool
    created_at: datetime
    updated_at: datetime
