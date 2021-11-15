import binascii
from dataclasses import dataclass
from hashlib import sha256
from typing import Optional

from coincurve import PrivateKey, PublicKey


@dataclass
class Transaction:
    sender: Optional[str]
    recipent: str
    amount: int
    description: Optional[str] = None
    hash: str = ''
    signature: str = ''

    def __post_init__(self):
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return sha256(f'{self.sender}{self.recipent}{self.amount}{self.description}'.encode('utf-8')).hexdigest()

    def sign_transaction(self, sk_hex):
        sk = PrivateKey().from_hex(sk_hex)
        pk_hex = sk.public_key.format().hex()

        if pk_hex != self.sender:
            raise ValueError(f'You cannot sign transactions that you havent sent!')

        sig = sk.sign(binascii.unhexlify(self.hash))
        self.signature = sig.hex()

    def is_valid(self):
        if self.sender is None:
            return True

        if not self.signature:
            raise ValueError(f'No signature in this transaction!')

        sender = PublicKey(binascii.unhexlify(self.sender))
        return sender.verify(binascii.unhexlify(self.signature), binascii.unhexlify(self.hash))
