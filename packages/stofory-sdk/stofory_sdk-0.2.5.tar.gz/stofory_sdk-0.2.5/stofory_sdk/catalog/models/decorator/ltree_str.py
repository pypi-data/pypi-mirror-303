from typing import Any, Dict

from sqlalchemy_utils import LtreeType
from sqlalchemy_utils.types.ltree import Ltree
from sqlalchemy.types import TypeDecorator


class LtreeStr(TypeDecorator):
    impl = LtreeType

    def process_result_value(self, value: Any, dialect: Any) -> str:
        if value is None:
            return ""
        return str(value)

    def process_bind_param(self, value: Any, dialect: Any) -> Ltree:
        if value is None:
            return Ltree("")
        return Ltree(value)
