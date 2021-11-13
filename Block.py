import datetime
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any, ClassVar, Optional

from Object import Object


@dataclass(frozen=False)  # should be True but if we want to check if is_chain_valid() works - set to False
class Block(Object):
    class_index: ClassVar[int] = 0
    index: Optional[int] = None  # calculated from class_index but initialized because of to_json order
    timestamp: datetime.datetime = datetime.datetime.now()
    data: Any = ''
    previous_hash: str = None
    hash: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'index', self.__class__.class_index)
        object.__setattr__(self, 'hash', self.calculate_hash())
        self.__class__.class_index += 1

    def calculate_hash(self) -> str:
        return sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8')).hexdigest()
