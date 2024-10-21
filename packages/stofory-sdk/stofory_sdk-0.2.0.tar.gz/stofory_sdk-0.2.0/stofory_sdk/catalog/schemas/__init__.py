from .product_schema import ProductResponse, ProductUpdateRequest, ProductCreateRequest
from .category_schema import CategoryResponse, CategoryUpdateRequest, CategoryCreateRequest
from .localization_schema import LocalizationResponse, LocalizationUpdateRequest, LocalizationCreateRequest
from .platform_schema import PlatformResponse, PlatformUpdateRequest, PlatformCreateRequest

from .product_platform_schema import ProductPlatformResponse, ProductPlatformUpdateRequest, ProductPlatformCreateRequest
from .product_platform_parameter_schema import ProductPlatformParameterResponse, ProductPlatformParameterUpdateRequest, ProductPlatformParameterCreateRequest
from .product_platform_image_schema import ProductPlatformImageResponse, ProductPlatformImageUpdateRequest, ProductPlatformImageCreateRequest
from .product_platform_video_schema import ProductPlatformVideoResponse, ProductPlatformVideoUpdateRequest, ProductPlatformVideoCreateRequest

from .product_platform_category_schema import ProductPlatformCategoryResponse, ProductPlatformCategoryUpdateRequest, ProductPlatformCategoryCreateRequest
from .product_platform_name_schema import ProductPlatformNameResponse, ProductPlatformNameUpdateRequest, ProductPlatformNameCreateRequest
from .product_platform_description_schema import ProductPlatformDescriptionResponse, ProductPlatformDescriptionUpdateRequest, ProductPlatformDescriptionCreateRequest
from .product_platform_discount_schema import ProductPlatformDiscountResponse, ProductPlatformDiscountUpdateRequest, ProductPlatformDiscountCreateRequest
from .product_platform_bonus_schema import ProductPlatformBonusResponse, ProductPlatformBonusUpdateRequest, ProductPlatformBonusCreateRequest
from .product_platform_guarantee_schema import ProductPlatformGuaranteeResponse, ProductPlatformGuaranteeUpdateRequest, ProductPlatformGuaranteeCreateRequest
from .product_platform_pricing_schema import ProductPlatformPricingResponse, ProductPlatformPricingUpdateRequest, ProductPlatformPricingCreateRequest

from .parameter_name_schema import ParameterNameResponse, ParameterNameUpdateRequest, ParameterNameCreateRequest
from .parameter_comment_schema import ParameterCommentResponse, ParameterCommentUpdateRequest, ParameterCommentCreateRequest
from .parameter_option_schema import ParameterOptionResponse, ParameterOptionUpdateRequest, ParameterOptionCreateRequest
from .parameter_option_name_schema import ParameterOptionNameResponse, ParameterOptionNameUpdateRequest, ParameterOptionNameCreateRequest

# ProductResponse.__annotations__["platform_infos"] = list[ProductPlatformResponse]
# ProductResponse.__annotations__["parameters"] = list[ProductPlatformParameterResponse]
# ProductResponse.__annotations__["images"] = list[ProductPlatformImageResponse]
# ProductResponse.__annotations__["videos"] = list[ProductPlatformVideoResponse]

# ProductPlatformInfoResponse.__annotations__["product"] = ProductResponse
# ProductPlatformResponse.__annotations__["platform"] = PlatformResponse
# ProductPlatformResponse.__annotations__["categories"] = list[ProductPlatformCategoryResponse]
# ProductPlatformResponse.__annotations__["names"] = list[ProductPlatformNameResponse]
# ProductPlatformResponse.__annotations__["descriptions"] = list[ProductPlatformDescriptionResponse]
# ProductPlatformResponse.__annotations__["discount"] = list[ProductPlatformDiscountResponse]
# ProductPlatformResponse.__annotations__["bonuse"] = list[ProductPlatformBonusResponse]
# ProductPlatformResponse.__annotations__["guarantee"] = list[ProductPlatformGuaranteeResponse]
# ProductPlatformResponse.__annotations__["pricing"] = list[ProductPlatformPricingResponse]

__all__ = (
    "ProductResponse",
    "ProductUpdateRequest",
    "ProductCreateRequest",

    "CategoryResponse",
    "CategoryUpdateRequest",
    "CategoryCreateRequest",

    "LocalizationResponse",
    "LocalizationUpdateRequest",
    "LocalizationCreateRequest",

    "PlatformResponse",
    "PlatformUpdateRequest",
    "PlatformCreateRequest",

    "ProductPlatformResponse",
    "ProductPlatformUpdateRequest",
    "ProductPlatformCreateRequest",

    "ProductPlatformParameterResponse",
    "ProductPlatformParameterUpdateRequest",
    "ProductParameterCreateRequest",

    "ProductPlatformImageResponse",
    "ProductPlatformImageUpdateRequest",
    "ProductPlatformImageCreateRequest",

    "ProductPlatformVideoResponse",
    "ProductPlatformVideoUpdateRequest",
    "ProductPlatformVideoCreateRequest",

    "ProductPlatformCategoryResponse",
    "ProductPlatformCategoryUpdateRequest",
    "ProductPlatformCategoryCreateRequest",

    "ProductPlatformNameResponse",
    "ProductPlatformNameUpdateRequest",
    "ProductPlatformNameCreateRequest",

    "ProductPlatformDescriptionResponse",
    "ProductPlatformDescriptionUpdateRequest",
    "ProductPlatformDescriptionCreateRequest",

    "ProductPlatformDiscountResponse",
    "ProductPlatformDiscountUpdateRequest",
    "ProductPlatformDiscountCreateRequest",

    "ProductPlatformBonusResponse",
    "ProductPlatformBonusUpdateRequest",
    "ProductPlatformBonusCreateRequest",

    "ProductPlatformGuaranteeResponse",
    "ProductPlatformGuaranteeUpdateRequest",
    "ProductPlatformGuaranteeCreateRequest",

    "ProductPlatformPricingResponse",
    "ProductPlatformPricingUpdateRequest",
    "ProductPlatformPricingCreateRequest",

    "ParameterNameResponse",
    "ParameterNameUpdateRequest",
    "ParameterNameCreateRequest",

    "ParameterCommentResponse",
    "ParameterCommentUpdateRequest",
    "ParameterCommentCreateRequest",

    "ParameterOptionResponse",
    "ParameterOptionUpdateRequest",
    "ParameterOptionCreateRequest",

    "ParameterOptionNameResponse",
    "ParameterOptionNameUpdateRequest",
    "ParameterOptionNameCreateRequest",
)
