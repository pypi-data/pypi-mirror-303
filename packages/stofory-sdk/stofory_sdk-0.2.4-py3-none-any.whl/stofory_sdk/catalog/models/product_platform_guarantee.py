from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN, INTEGER
from sqlalchemy.orm import Mapped, relationship, mapped_column

if TYPE_CHECKING:
    from .product_platform import ProductPlatform


class ProductPlatformGuarantee(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_guarantee_product_platform_id", "product_platform_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"),
                                                          nullable=False, unique=True)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    is_enabled: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    value: Mapped[int] = mapped_column(INTEGER, nullable=False)

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="guarantee",
        foreign_keys="ProductPlatformGuarantee.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="noload"
    )
