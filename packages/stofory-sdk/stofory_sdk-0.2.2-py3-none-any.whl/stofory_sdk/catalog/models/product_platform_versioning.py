from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, ARRAY
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .decorator.jsonb_dict import JSONBDict

if TYPE_CHECKING:
    from .product_platform import ProductPlatform


class ProductPlatformVersioning(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_versioning_product_platform_id", "product_platform_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    history: Mapped[list[ProductPlatform]] = Column(ARRAY(JSONBDict), default=[])

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="versions",
        foreign_keys="ProductPlatformVersioning.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="noload",
    )
