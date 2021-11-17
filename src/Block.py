import datetime
from dataclasses import dataclass, field
from hashlib import sha256

from .Object import Object
from .Transaction import Transaction


@dataclass()
class Block(Object):
    previous_hash: str
    timestamp: datetime.datetime = datetime.datetime.now()
    transactions: list[Transaction] = field(default_factory=lambda: [])
    nonce: int = 0
    hash: str = field(init=False)

    def calculate_hash(self) -> str:
        """
        Creates a SHA256 hash of the block
        :return: block hash
        """
        return sha256(f'{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}'.encode(
            'utf-8')).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Starts the mining process on the block. It changes the 'nonce' until the hash of the block
        starts with enough zeros(difficulty)
        :param difficulty: number of zeros
        """
        self.hash = self.calculate_hash()
        print(f'Please wait... mining block')
        while self.hash[0:difficulty] != ['0' * difficulty][0] or self.hash != self.calculate_hash():
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f'Block mined in {self.nonce} iterations: {self.hash}')

    def has_valid_transactions(self) -> bool:
        """
        Checks if all of the transactions stored in chain are valid (have a sender, signature and are signed properly
        so the signature is valid)
        :return: True if valid, False if not
        """
        for transaction in self.transactions:
            if not transaction.is_valid():
                return False
        return True
