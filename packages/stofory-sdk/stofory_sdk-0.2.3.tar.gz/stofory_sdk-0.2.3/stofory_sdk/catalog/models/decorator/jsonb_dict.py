from typing import Any, Dict

import msgspec.json
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.types import TypeDecorator
import base64


class JSONBDict(TypeDecorator):
    impl = JSONB

    def process_result_value(self, value: Any, dialect: Any) -> Dict[str, Any]:
        if value is None:
            return {}
        if isinstance(value, str):
            try:
                return msgspec.json.decode(value)
            except msgspec.DecodeError:
                try:
                    decoded = base64.b64decode(value).decode('utf-8')
                    return msgspec.json.decode(decoded)
                except Exception:
                    return {"value": value}
        return value
