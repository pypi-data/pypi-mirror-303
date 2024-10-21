from typing import Any, Dict

from sqlalchemy_utils import LtreeType
from sqlalchemy.types import TypeDecorator


class LtreeStr(TypeDecorator):
    impl = LtreeType

    def process_result_value(self, value: Any, dialect: Any) -> str:
        if value is None:
            return ""
        return str(value)
