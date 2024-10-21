from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Enum, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy.orm import Mapped, relationship, mapped_column

if TYPE_CHECKING:
    from .product_platform import ProductPlatform
    from .localization import Localization


class ProductPlatformName(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_name_product_platform_id", "product_platform_id"),
        Index("idx_product_platform_name_localization_id", "localization_id"),
        # TODO: Think about index for both foreign keys
    )

    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"),
                                                          nullable=False)
    # locale: Mapped[Locale] = mapped_column(Enum(Locale), nullable=False)
    localization_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("localization.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    value: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="names",
        foreign_keys="ProductPlatformName.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )

    locale: Mapped[Localization] = relationship(
        back_populates="product_platform_names",
        foreign_keys="ProductPlatformName.localization_id",
        innerjoin=True,
        uselist=False,
        lazy="joined"
    )
