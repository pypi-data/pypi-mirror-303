from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy.orm import Mapped, relationship, mapped_column

if TYPE_CHECKING:
    from .product_platform import ProductPlatform


class ProductPlatformVideo(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_video_product_platform_id", "product_platform_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    url: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    platform: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)

    product_platform: Mapped[ProductPlatform] = relationship(
        back_populates="videos",
        foreign_keys="ProductPlatformVideo.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="joined"
    )
