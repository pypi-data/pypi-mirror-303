from typing import Any, Dict

from sqlalchemy_utils import LtreeType
from sqlalchemy_utils.types.ltree import Ltree
from sqlalchemy.types import TypeDecorator


class LtreeStr(TypeDecorator):
    impl = LtreeType

    def process_result_value(self, value: Any, dialect: Any) -> str:
        if isinstance(value, Ltree):
            return str(value)
        elif isinstance(value, str):
            return Ltree(value)

        return value
