from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .decorator.jsonb_dict import JSONBDict

if TYPE_CHECKING:
    from .product import Product
    from .platform import Platform
    from .product_platform import ProductPlatform


class ProductPlatformExternalConnection(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_external_connection", "product_platform_id", "platform_id", "product_id"),
    )

    product_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product.id"), nullable=False)
    platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("platform.id"), nullable=False)
    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"), nullable=False, unique=True)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    external_id: Mapped[str] = Column(VARCHAR(255), nullable=False)
    external_meta: Mapped[dict] = Column(JSONBDict, default={})

    product: Mapped[Product] = relationship(
        back_populates="external_connections",
        foreign_keys="ProductPlatformExternalConnection.product_id",
        innerjoin=True,
        uselist=False,
        lazy="noload",
    )

    platform: Mapped[Platform] = relationship(
        back_populates="external_connections",
        foreign_keys="ProductPlatformExternalConnection.platform_id",
        innerjoin=True,
        uselist=False,
        lazy="noload",
    )

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="external_connections",
        foreign_keys="ProductPlatformExternalConnection.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="noload",
    )
