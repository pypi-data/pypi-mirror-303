from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import BOOLEAN, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .enums import Locale

if TYPE_CHECKING:
    from .product_platform_name import ProductPlatformName
    from .product_platform_description import ProductPlatformDescription
    from .parameter_name import ParameterName
    from .parameter_comment import ParameterComment
    from .parameter_option_name import ParameterOptionName


class Localization(BigIntAuditBase):
    locale: Mapped[Locale] = mapped_column(ENUM(Locale), nullable=False, unique=True)
    is_enabled: Mapped[bool] = mapped_column(BOOLEAN, default=True)

    product_platform_names: Mapped[list[ProductPlatformName]] = relationship(
        back_populates="locale",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    product_platform_descriptions: Mapped[list[ProductPlatformDescription]] = relationship(
        back_populates="locale",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    parameter_names: Mapped[list[ParameterName]] = relationship(
        back_populates="locale",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    parameter_comments: Mapped[list[ParameterComment]] = relationship(
        back_populates="locale",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    parameter_option_names: Mapped[list[ParameterOptionName]] = relationship(
        back_populates="locale",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )
