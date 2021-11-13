import datetime
from typing import Any

from Block import Block
from Object import Object


class Blockchain(Object):
    def __init__(self, difficulty: int = 0):
        self.difficulty = difficulty if difficulty > 0 else 0
        self.chain = [self.create_genesis_block()]

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, timestamp: datetime = datetime.datetime.now(), data: Any = '', previous_hash: str = 'latest'):
        if previous_hash == 'latest':
            previous_hash = self.get_latest_block().hash
        block = Block(timestamp=timestamp, data=data, previous_hash=previous_hash, difficulty=self.difficulty)
        self.chain.append(block)

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):  # do not include genesis block
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash() \
                    or current_block.previous_hash != previous_block.calculate_hash():
                return False
        return True

    def create_genesis_block(self) -> Block:
        timestamp = datetime.datetime(2020, 1, 1, 12, 00)
        return Block(timestamp=timestamp, data='This is the genesis block', difficulty=self.difficulty)
