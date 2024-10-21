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
    ProductPlatformVideoCreateRequest,
    ProductPlatformParameterCreateRequest,
    ParameterNameCreateRequest,
    ParameterCommentCreateRequest,
    ParameterOptionCreateRequest,
    ParameterOptionNameCreateRequest,
)


class GenericUpdateRequest[T](Struct, forbid_unknown_fields=True):
    id: int
    data: T


class BasicGroupCreateRequest(Struct, forbid_unknown_fields=True):
    names: list[ProductPlatformNameCreateRequest]
    descriptions: list[ProductPlatformDescriptionCreateRequest]
    categories: list[ProductPlatformCategoryCreateRequest]
    price: ProductPlatformPricingCreateRequest
    bonus: ProductPlatformBonusCreateRequest
    discount: ProductPlatformDiscountCreateRequest
    guarantee: ProductPlatformGuaranteeCreateRequest


class BasicGroupUpdateRequest(Struct, forbid_unknown_fields=True):
    names: list[GenericUpdateRequest[ProductPlatformNameUpdateRequest]]
    descriptions: list[GenericUpdateRequest[ProductPlatformDescriptionUpdateRequest]]
    categories: list[GenericUpdateRequest[ProductPlatformCategoryUpdateRequest]]
    price: GenericUpdateRequest[ProductPlatformPricingUpdateRequest]
    bonus: GenericUpdateRequest[ProductPlatformBonusUpdateRequest]
    discount: GenericUpdateRequest[ProductPlatformDiscountUpdateRequest]
    guarantee: GenericUpdateRequest[ProductPlatformGuaranteeUpdateRequest]


class GalleryGroupCreateRequest(Struct, forbid_unknown_fields=True):
    images: list[ProductPlatformImageCreateRequest]
    videos: list[ProductPlatformVideoCreateRequest]


class GalleryGroupUpdateRequest(Struct, forbid_unknown_fields=True):
    images: list[GenericUpdateRequest[ProductPlatformImageCreateRequest]]
    videos: list[GenericUpdateRequest[ProductPlatformVideoCreateRequest]]


class ParametersGroupCreateRequest(Struct, forbid_unknown_fields=True):
    parameters: list[ProductPlatformParameterCreateRequest]
    names: list[ParameterNameCreateRequest]
    comments: list[ParameterCommentCreateRequest]
    options: list[ParameterOptionCreateRequest]
    option_names: list[ParameterOptionNameCreateRequest]


class ParametersGroupUpdateRequest(Struct, forbid_unknown_fields=True):
    parameters: list[GenericUpdateRequest[ProductPlatformParameterCreateRequest]]
    names: list[GenericUpdateRequest[ParameterNameCreateRequest]]
    comments: list[GenericUpdateRequest[ParameterCommentCreateRequest]]
    options: list[GenericUpdateRequest[ParameterOptionCreateRequest]]
    option_names: list[GenericUpdateRequest[ParameterOptionNameCreateRequest]]

