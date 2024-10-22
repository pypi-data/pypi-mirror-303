from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Enum, Index
from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN, INTEGER, FLOAT
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .enums import ModifierOperator


if TYPE_CHECKING:
    from .product_platform_parameter import ProductPlatformParameter
    from .parameter_option_name import ParameterOptionName


class ParameterOption(BigIntAuditBase):
    __table_args__ = (
        Index("idx_parameter_option_parameter_id", "parameter_id"),
    )

    parameter_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform_parameter.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    modifier_operator: Mapped[ModifierOperator] = mapped_column(Enum(ModifierOperator), nullable=False)
    modifier_value: Mapped[float] = mapped_column(FLOAT, nullable=False)
    is_default: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    is_enabled: Mapped[bool] = mapped_column(BOOLEAN, default=True)
    order: Mapped[int] = mapped_column(INTEGER, nullable=False)

    parameter: Mapped[ProductPlatformParameter] = relationship(
        back_populates="options",
        foreign_keys="ParameterOption.parameter_id",
        innerjoin=True,
        uselist=False,
        lazy="noload"
    )

    names: Mapped[list[ParameterOptionName]] = relationship(
        back_populates="parameter_option",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )
