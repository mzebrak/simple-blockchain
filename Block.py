from hashlib import sha256
from typing import Optional


class Block:
    def __init__(self, index: int, timestamp, data, previous_hash: Optional[str]):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        return sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8')).hexdigest()
