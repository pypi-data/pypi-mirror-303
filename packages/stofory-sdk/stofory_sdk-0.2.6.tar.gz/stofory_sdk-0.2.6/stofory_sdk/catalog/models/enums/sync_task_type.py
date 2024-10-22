import enum


class SyncTaskType(enum.StrEnum):
    CREATE = enum.auto()
    UPDATE = enum.auto()
    DELETE = enum.auto()
