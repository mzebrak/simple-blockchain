import binascii
import datetime
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Optional

from coincurve import PrivateKey, PublicKey

from .object import Object


class TransactionType(str, Enum):
    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'
    BOTH = 'BOTH'
    SYSTEM = 'SYSTEM'
    USER_DEFINED = 'USER_DEFINED'


@dataclass
class Transaction(Object):
    amount: float
    recipent: str
    sender: str
    tx_type: TransactionType = TransactionType.USER_DEFINED
    description: Optional[str] = None
    timestamp: int = int(datetime.datetime.now().timestamp() * 1000)
    hash: str = field(init=False)

    # signature: str = field(repr=False, init=False)

    def __post_init__(self):
        """
        After creating and initiating a transaction - add timestamp and calculate its hash
        """
        self.description = '' if self.description is None else self.description
        # self.timestamp = self.json_default(datetime.datetime.now())
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Creates a SHA256 hash of the transaction
        :return: block hash
        """
        return sha256(f'{self.amount}{self.recipent}{self.sender}{self.description}{self.timestamp}'.encode(
            'utf-8')).hexdigest()

    def sign_transaction(self, sk_hex: str):
        """
        Sign a transaction using sender's secret key
        """
        sk = PrivateKey().from_hex(sk_hex)
        pk_hex = sk.public_key.format().hex()

        if pk_hex != self.sender:
            raise ValueError(f'You cannot sign transactions that you havent sent!')

        sig = sk.sign(binascii.unhexlify(self.hash))
        self.signature = sig.hex()

    def is_valid(self) -> bool:
        """
        Check if transaction is valid (have a sender, signature and is signed properly so the signature is valid)
        :return: True if valid, False if not
        """
        if self.sender is 'SYSTEM':
            return True

        if not self.signature:
            raise ValueError(f'No signature in this transaction!')

        sender = PublicKey(binascii.unhexlify(self.sender))
        return sender.verify(binascii.unhexlify(self.signature), binascii.unhexlify(self.hash))
