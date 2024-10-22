from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, Enum, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy.orm import Mapped, relationship, mapped_column

if TYPE_CHECKING:
    from .product_platform_parameter import ProductPlatformParameter
    from .localization import Localization


class ParameterName(BigIntAuditBase):
    __table_args__ = (
        Index("idx_product_platform_parameter_name_parameter_id", "parameter_id"),
        Index("idx_product_platform_parameter_name_localization_id", "localization_id"),
        # TODO: Think about index for both foreign keys
    )

    parameter_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("product_platform_parameter.id", ondelete="CASCADE"), nullable=False)
    # locale: Mapped[Locale] = mapped_column(Enum(Locale), nullable=False)
    localization_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("localization.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[int] = mapped_column(BIGINT, default=1)
    value: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)

    parameter: Mapped[ProductPlatformParameter] = relationship(
        back_populates="names",
        foreign_keys="ParameterName.parameter_id",
        innerjoin=True,
        uselist=False,
        lazy="noload"
    )

    locale: Mapped[Localization] = relationship(
        back_populates="parameter_names",
        foreign_keys="ParameterName.localization_id",
        innerjoin=True,
        uselist=False,
        lazy="joined"
    )
