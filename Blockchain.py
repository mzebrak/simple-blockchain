import datetime
import json
from typing import Any

from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def to_json(self, sort_keys: bool = False, indent: int = 4) -> str:
        return json.dumps(self, default=self.json_default, sort_keys=sort_keys, indent=indent)

    @staticmethod
    def json_default(value: Any) -> dict:
        if isinstance(value, datetime.date):
            return dict(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute,
                        second=value.second)
        else:
            return value.__dict__

    @staticmethod
    def create_genesis_block() -> Block:
        timestamp = datetime.datetime(2020, 1, 1, 12, 00)
        return Block(0, timestamp, 'This is the genesis block', None)
