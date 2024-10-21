import enum


class PricingType(enum.StrEnum):
    FIXED = enum.auto()
    RATE = enum.auto()
