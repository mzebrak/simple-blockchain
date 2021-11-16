import datetime
from dataclasses import dataclass
from hashlib import sha256

from .Object import Object
from .Transaction import Transaction


@dataclass()
class Block(Object):
    timestamp: datetime.datetime = datetime.datetime.now()
    transactions: list[Transaction] = None
    previous_hash: str = ''
    hash: str = ''
    nonce: int = 0
    difficulty: int = 0

    def calculate_hash(self) -> str:
        return sha256(f'{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}'.encode(
            'utf-8')).hexdigest()

    def mine_block(self, difficulty: int):
        print(f'Please wait... mining block')
        if difficulty < 1:
            self.hash = self.calculate_hash()

        while self.hash[0:difficulty] != ['0' * difficulty][0] or self.hash != self.calculate_hash():
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f'Block mined in {self.nonce} iterations: {self.hash}')

    def has_valid_transactions(self) -> bool:
        for transaction in self.transactions:
            if not transaction.is_valid():
                return False
        return True
