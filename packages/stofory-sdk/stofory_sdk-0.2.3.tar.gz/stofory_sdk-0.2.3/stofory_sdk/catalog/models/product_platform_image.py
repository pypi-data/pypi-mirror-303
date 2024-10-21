from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Index
from sqlalchemy.dialects.postgresql import BOOLEAN, BIGINT, VARCHAR
from sqlalchemy.orm import Mapped, relationship, mapped_column


if TYPE_CHECKING:
    from .product_platform import ProductPlatform


class ProductPlatformImage(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_image_product_platform_id", "product_platform_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    relative_path: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    domain: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    is_enabled: Mapped[bool] = mapped_column(BOOLEAN, default=True)
    order: Mapped[int] = mapped_column(BIGINT, nullable=False)

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="images",
        foreign_keys="ProductPlatformImage.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
