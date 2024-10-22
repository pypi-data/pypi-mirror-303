from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any


from advanced_alchemy.base import BigIntAuditBase, SlugKey
from sqlalchemy.dialects.postgresql import VARCHAR, TEXT, JSONB, BOOLEAN
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .decorator.jsonb_dict import JSONBDict

if TYPE_CHECKING:
    from .product_platform import ProductPlatform
    from .product_platform_external_connection import ProductPlatformExternalConnection


class Platform(BigIntAuditBase, SlugKey):
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    description: Mapped[str] = mapped_column(TEXT(), nullable=False)
    custom_fields_template: Mapped[Dict[str, Any]] = mapped_column(JSONBDict, default={})
    is_external: Mapped[bool] = mapped_column(BOOLEAN, default=False)

    product_platforms: Mapped[list[ProductPlatform]] = relationship(
        back_populates="platform",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    external_connections: Mapped[list[ProductPlatformExternalConnection]] = relationship(
        back_populates="platform",
        lazy="selectin",
        uselist=True,
        # cascade="all, delete"
    )
