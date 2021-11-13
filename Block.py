import datetime
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any
from typing import Optional


@dataclass(frozen=True, eq=True)
class Block:
    index: int
    timestamp: datetime.datetime
    data: Any
    previous_hash: Optional[str]
    hash: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'hash', self.calculate_hash())

    def calculate_hash(self) -> str:
        return sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8')).hexdigest()
