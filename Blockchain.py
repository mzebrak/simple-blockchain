import datetime
from typing import Any

from Block import Block
from Object import Object


class Blockchain(Object):
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, timestamp: datetime = datetime.datetime.now(), data: Any = '', previous_hash: str = 'latest'):
        if previous_hash == 'latest':
            previous_hash = self.get_latest_block().hash
        block = Block(timestamp=timestamp, data=data, previous_hash=previous_hash)
        self.chain.append(block)

    @staticmethod
    def create_genesis_block() -> Block:
        timestamp = datetime.datetime(2020, 1, 1, 12, 00)
        return Block(timestamp=timestamp, data='This is the genesis block')
