import datetime
from dataclasses import dataclass
from hashlib import sha256
from typing import Any, ClassVar, Optional

from Object import Object


@dataclass(frozen=False)  # should be True but if we want to check if is_chain_valid() works - set to False
class Block(Object):
    class_index: ClassVar[int] = 0
    index: Optional[int] = None  # calculated from class_index but initialized because of to_json order
    timestamp: datetime.datetime = datetime.datetime.now()
    data: Any = ''
    previous_hash: str = ''
    hash: str = ''
    nonce: int = 0
    difficulty: int = 0

    def __post_init__(self):
        object.__setattr__(self, 'index', self.__class__.class_index)
        self.__class__.class_index += 1
        self.mine_block(self.difficulty)

    def calculate_hash(self) -> str:
        return sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}'.encode(
            'utf-8')).hexdigest()

    def mine_block(self, difficulty: int):
        print(f'Please wait... mining block: {self.index}')

        if difficulty < 1:
            object.__setattr__(self, 'hash', self.calculate_hash())  # self.hash = self.calculate_hash()

        while self.hash[0:difficulty] != ['0' * difficulty][0]:
            object.__setattr__(self, 'nonce', self.nonce + 1)  # self.nonce += 1
            object.__setattr__(self, 'hash', self.calculate_hash())  # self.hash = self.calculate_hash()

        print(f'Block mined in {self.nonce} iterations: {self.hash}')
