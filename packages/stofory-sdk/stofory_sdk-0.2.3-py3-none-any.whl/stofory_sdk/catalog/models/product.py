from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase, SlugKey
from sqlalchemy import Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import VARCHAR, ENUM, TEXT, BOOLEAN
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr

from .enums import ProductTypes


if TYPE_CHECKING:
    from .product_platform import ProductPlatform
    from .product_platform_external_connection import ProductPlatformExternalConnection


class Product(BigIntAuditBase, SlugKey):
    @declared_attr.directive
    @classmethod
    def __table_args__(cls):
        return (
            Index("idx_product_name", "name"),
            UniqueConstraint(
                cls.slug,
                name=f"uq_{cls.__tablename__}_slug",
            ).ddl_if(callable_=cls._create_unique_slug_constraint),
            Index(
                f"ix_{cls.__tablename__}_slug_unique",
                cls.slug,
                unique=True,
            ).ddl_if(callable_=cls._create_unique_slug_index),
        )
    # __table_args__ = (
    #     Index("idx_product_name", "name"),
    # )

    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    description: Mapped[str] = mapped_column(TEXT(), nullable=False)
    product_type: Mapped[ProductTypes] = mapped_column(ENUM(ProductTypes), nullable=False)
    status: Mapped[bool] = mapped_column(BOOLEAN(), default=False)

    product_platforms: Mapped[list[ProductPlatform]] = relationship(
        back_populates="product",
        lazy="selectin",
        uselist=True,
        passive_deletes=True,
        cascade="all, delete-orphan"
    )

    external_connections: Mapped[list[ProductPlatformExternalConnection]] = relationship(
        back_populates="product",
        lazy="selectin",
        uselist=True,
        # cascade="all, delete-orphan"
    )
