from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Enum, Index
from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN, INTEGER
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .enums import ParameterType


if TYPE_CHECKING:
    from .product_platform import ProductPlatform
    from .parameter_name import ParameterName
    from .parameter_comment import ParameterComment
    from .parameter_option import ParameterOption


class ProductPlatformParameter(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_parameter_product_platform_id", "product_platform_id"),
    )

    product_platform_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    parameter_type: Mapped[ParameterType] = mapped_column(Enum(ParameterType), nullable=False)
    is_required: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    order: Mapped[int] = mapped_column(INTEGER, nullable=False)

    product_platform: Mapped[list[ProductPlatform]] = relationship(
        back_populates="parameters",
        foreign_keys="ProductPlatformParameter.product_platform_id",
        innerjoin=True,
        uselist=False,
        lazy="noload"   # select/noload?
    )

    names: Mapped[list[ParameterName]] = relationship(
        back_populates="parameter",
        lazy="noload",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    comments: Mapped[list[ParameterComment]] = relationship(
        back_populates="parameter",
        lazy="noload",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    options: Mapped[list[ParameterOption]] = relationship(
        back_populates="parameter",
        lazy="noload",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )
