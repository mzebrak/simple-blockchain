import datetime
import json
from typing import Any


class Object:
    def to_json(self, sort_keys: bool = False, indent: int = 4) -> str:
        return json.dumps(self, default=self.json_default, sort_keys=sort_keys, indent=indent)

    @staticmethod
    def json_default(value: Any) -> dict:
        if isinstance(value, datetime.date):
            return dict(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute,
                        second=value.second, microsecond=value.microsecond)
        else:
            return value.__dict__
