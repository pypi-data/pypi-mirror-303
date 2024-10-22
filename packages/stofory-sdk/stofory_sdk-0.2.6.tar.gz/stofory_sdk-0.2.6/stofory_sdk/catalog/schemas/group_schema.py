from datetime import datetime
from typing import Annotated

from litestar.params import Parameter
from msgspec import Struct

from . import (
    # ProductPlatformCreateRequest,     # base struct for create request schemas?

    ProductPlatformNameCreateRequest,
    ProductPlatformDescriptionCreateRequest,
    ProductPlatformCategoryCreateRequest,
    ProductPlatformPricingCreateRequest,
    ProductPlatformBonusCreateRequest,
    ProductPlatformDiscountCreateRequest,
    ProductPlatformGuaranteeCreateRequest,
    ProductPlatformNameUpdateRequest,
    ProductPlatformDescriptionUpdateRequest,
    ProductPlatformCategoryUpdateRequest,
    ProductPlatformPricingUpdateRequest,
    ProductPlatformBonusUpdateRequest,
    ProductPlatformDiscountUpdateRequest,
    ProductPlatformGuaranteeUpdateRequest,
    ProductPlatformImageCreateRequest,
    ProductPlatformImageUpdateRequest,
    ProductPlatformVideoCreateRequest,
    ProductPlatformVideoUpdateRequest,
    ProductPlatformParameterCreateRequest,
    ParameterNameCreateRequest,
    ParameterCommentCreateRequest,
    ParameterOptionCreateRequest,
    ParameterOptionNameCreateRequest,
    ProductPlatformParameterUpdateRequest,
    ParameterNameUpdateRequest,
    ParameterCommentUpdateRequest,
    ParameterOptionUpdateRequest,
    ParameterOptionNameUpdateRequest,
)


# Wrapper for all isolated update request schemas
class _GenericUpdateRequest[T](Struct, forbid_unknown_fields=True):
    id: int
    data: T


# Basic group
class BasicGroupCreateRequest(Struct, forbid_unknown_fields=True):
    names: list[ProductPlatformNameCreateRequest]
    descriptions: list[ProductPlatformDescriptionCreateRequest]
    categories: list[ProductPlatformCategoryCreateRequest]
    price: ProductPlatformPricingCreateRequest
    bonus: ProductPlatformBonusCreateRequest
    discount: ProductPlatformDiscountCreateRequest
    guarantee: ProductPlatformGuaranteeCreateRequest


class BasicGroupUpdateRequest(Struct, forbid_unknown_fields=True):
    names: list[_GenericUpdateRequest[ProductPlatformNameUpdateRequest]]
    descriptions: list[_GenericUpdateRequest[ProductPlatformDescriptionUpdateRequest]]
    categories: list[_GenericUpdateRequest[ProductPlatformCategoryUpdateRequest]]
    price: _GenericUpdateRequest[ProductPlatformPricingUpdateRequest]
    bonus: _GenericUpdateRequest[ProductPlatformBonusUpdateRequest]
    discount: _GenericUpdateRequest[ProductPlatformDiscountUpdateRequest]
    guarantee: _GenericUpdateRequest[ProductPlatformGuaranteeUpdateRequest]


# Gallery group
class GalleryGroupCreateRequest(Struct, forbid_unknown_fields=True):
    images: list[ProductPlatformImageCreateRequest]
    videos: list[ProductPlatformVideoCreateRequest]


class GalleryGroupUpdateRequest(Struct, forbid_unknown_fields=True):
    images: list[_GenericUpdateRequest[ProductPlatformImageUpdateRequest]]
    videos: list[_GenericUpdateRequest[ProductPlatformVideoUpdateRequest]]


# Parameters group
class _GroupParameterOptionCreateRequest(ParameterOptionCreateRequest, forbid_unknown_fields=True):
    names: list[ParameterOptionNameCreateRequest]


class _GroupParameterCreateRequest(ProductPlatformParameterCreateRequest, forbid_unknown_fields=True):
    names: list[ParameterNameCreateRequest]
    comments: list[ParameterCommentCreateRequest]
    options: list[_GroupParameterOptionCreateRequest]


class ParametersGroupCreateRequest(Struct, forbid_unknown_fields=True):
    parameters: list[_GroupParameterCreateRequest]


class _GroupParameterOptionUpdateRequest(ParameterOptionUpdateRequest, forbid_unknown_fields=True):
    names: list[_GenericUpdateRequest[ParameterOptionNameUpdateRequest]]


class _GroupParameterUpdateRequest(ProductPlatformParameterUpdateRequest, forbid_unknown_fields=True):
    names: list[_GenericUpdateRequest[ParameterNameUpdateRequest]]
    comments: list[_GenericUpdateRequest[ParameterCommentUpdateRequest]]
    options: list[_GenericUpdateRequest[_GroupParameterOptionUpdateRequest]]


class ParametersGroupUpdateRequest(Struct, forbid_unknown_fields=True):
    parameters: list[_GenericUpdateRequest[_GroupParameterUpdateRequest]]


