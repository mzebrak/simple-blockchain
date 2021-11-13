import datetime
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any, ClassVar

from Object import Object


@dataclass(frozen=True)
class Block(Object):
    class_index: ClassVar[int] = 0
    index: int = None  # calculated from class_index but initialized because of to_json order
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

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'(index={self.index}, ' \
               f'timestamp={self.timestamp}, ' \
               f'data={self.data}, ' \
               f'previous_hash={self.previous_hash}, ' \
               f'hash={self.hash})'
