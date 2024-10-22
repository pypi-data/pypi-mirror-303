from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import Mapped, relationship, mapped_column

if TYPE_CHECKING:
    from .category import Category
    from .product_platform import ProductPlatform


class ProductPlatformCategory(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_category_product_platform_id", "product_platform_id"),
        Index("idx_product_platform_category_category_id", "category_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"), nullable=False
    )
    category_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="categories",
        foreign_keys="ProductPlatformCategory.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )

    category: Mapped[Category] = relationship(
        back_populates="product_platform_info_categories",
        foreign_keys="ProductPlatformCategory.category_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
