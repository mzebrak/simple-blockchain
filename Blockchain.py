import datetime

from Block import Block
from Object import Object
from Transaction import Transaction


class Blockchain(Object):
    def __init__(self, difficulty: int = 0):
        self.difficulty = difficulty if difficulty > 0 else 2
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self) -> Block:
        timestamp = datetime.datetime(2020, 1, 1, 12, 00)
        block = Block(timestamp=timestamp,
                      transactions=[Transaction(sender='System',
                                                recipent='028932ef0ce3145fe17dd1d28c4b3ec40ccd8d5e32875f3f2fef8d4761ec6eb5fd',
                                                amount=1000,
                                                description='This is the genesis block')],
                      difficulty=self.difficulty)
        block.hash = block.calculate_hash()
        return block

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(transactions=self.pending_transactions, previous_hash=self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [Transaction(sender=None, recipent=miner_address, amount=self.mining_reward)]

    def add_transaction(self, transaction: Transaction):

        if not transaction.sender or not transaction.recipent:
            raise ValueError('Transaction must include sender and recipient address')

        if not transaction.is_valid():
            raise ValueError('Cannot add invalid transaction to chain')

        sender_balance = self.get_address_balance(transaction.sender)
        if sender_balance < transaction.amount:
            raise ValueError(f'{transaction.sender} balance is too low: {sender_balance}')
        self.pending_transactions.append(transaction)

    def get_address_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:

                if transaction.sender == address:
                    balance -= transaction.amount

                if transaction.recipent == address:
                    balance += transaction.amount

        return balance

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):  # do not include genesis block
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # if not current_block.has_valid_transactions()\
            if current_block.hash != current_block.calculate_hash() \
                    or current_block.previous_hash != previous_block.calculate_hash():
                return False
        return True
