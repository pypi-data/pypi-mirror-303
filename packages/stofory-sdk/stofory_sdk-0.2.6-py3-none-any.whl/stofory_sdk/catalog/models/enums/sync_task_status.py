import enum


class SyncTaskStatus(enum.StrEnum):
    PENDING = enum.auto()
    PROCESSING = enum.auto()
    COMPLETED = enum.auto()
    FAILED = enum.auto()
