from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, ENUM
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .enums import PricingType, Currency

if TYPE_CHECKING:
    from .product_platform import ProductPlatform


class ProductPlatformPricing(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_pricing_product_platform_id", "product_platform_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"),
                                                          nullable=False, unique=True)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    pricing_type: Mapped[PricingType] = mapped_column(ENUM(PricingType), nullable=False)
    price: Mapped[int] = mapped_column(BIGINT, nullable=True)
    price_per_unit: Mapped[int] = mapped_column(BIGINT, nullable=True)
    min_quantity: Mapped[int] = mapped_column(BIGINT, nullable=True)
    max_quantity: Mapped[int] = mapped_column(BIGINT, nullable=True)
    unit_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    currency: Mapped[Currency] = mapped_column(ENUM(Currency), nullable=False)

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="price",
        foreign_keys="ProductPlatformPricing.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="joined"
    )
