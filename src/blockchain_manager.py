from src.blockchain import Blockchain
from src.transaction import Transaction


class BlockchainManager:
    blockchain: Blockchain

    @classmethod
    def create_new_blockchain(cls):
        cls.blockchain = Blockchain(difficulty=4)
        public_key = '028932ef0ce3145fe17dd1d28c4b3ec40ccd8d5e32875f3f2fef8d4761ec6eb5fd'
        secret_key = '82605dccb6d509d60d4705b0399e6ab2aee6593a084585d41c63c6243fd9dda3'
        tx1 = Transaction(sender=public_key,
                          recipent='public key goes here',
                          description='test tx1',
                          amount=200)
        tx1.sign_transaction(sk_hex=secret_key)
        cls.blockchain.add_transaction(tx1)
        cls.blockchain.mine_pending_transactions(public_key)

    @classmethod
    def is_blockchain_valid(cls):
        return cls.blockchain.is_valid()

    @classmethod
    def get_blockchain(cls):
        return cls.blockchain

    @classmethod
    def get_chain(cls):
        return cls.blockchain.chain

    @classmethod
    def get_pending_transactions(cls):
        return cls.blockchain.pending_transactions
