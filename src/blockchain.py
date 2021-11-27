import datetime
from typing import Union

from .block import Block
from .object import Object
from .transaction import Transaction, TransactionType as tt


class Blockchain(Object):
    def __init__(self, difficulty: int = 2):
        self.difficulty = difficulty if difficulty > 0 else 2
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self) -> Block:
        """
        Creates the first block in the blockchain. It has to be created manually, because first block
        did not contains the hash of previous block (previous_hash)
        :return: Block object of the genesis block
        """
        timestamp = datetime.datetime(2020, 1, 1, 12, 00)
        block = Block(previous_hash='0',
                      timestamp=timestamp,
                      transactions=[Transaction(tx_type=tt.SYSTEM,
                                                timestamp=timestamp,
                                                recipent='028932ef0ce3145fe17dd1d28c4b3ec40ccd8d5e32875f3f2fef8d4761ec6eb5fd',
                                                amount=1000,
                                                description='FIRST, GENESIS BLOCK')])
        block.hash = block.calculate_hash()
        return block

    def get_latest_block(self) -> Block:
        """
        Useful when you are creating a new block and need the hash of the previous block
        :return: Latest Block object in the chain
        """
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address: str):
        """
        Takes all the pending transactions, puts them in a Block and starts the mining process.
        It also adds a transaction to send the mining reward to the given miner address.
        :param miner_address:
        """
        block = Block(transactions=self.pending_transactions, previous_hash=self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [Transaction(sender='SYSTEM', recipent=miner_address, amount=self.mining_reward,
                                                 description='MINING REWARD')]

    def add_transaction(self, transaction: Transaction):
        """
        Adds a new transaction to the list of pending transactions (would be mined next time the mining process starts).
        Also verifies that the given transaction is properly signed (is valid).
        :param transaction:
        """
        if not transaction.sender or not transaction.recipent:
            raise ValueError('Transaction must include sender and recipient address')

        if not transaction.is_valid():
            raise ValueError('Cannot add invalid transaction to chain')

        sender_balance = self.get_address_balance(transaction.sender)
        if sender_balance < transaction.amount:
            raise ValueError(f'{transaction.sender} balance is too low: {sender_balance}')
        self.pending_transactions.append(transaction)

    def get_address_balance(self, address: str) -> float:
        """
        Returns the balance of the provided wallet address. It is computed by checking all transactions stored in chain
        :param address: public wallet key
        :return: balance of the given address
        """
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:

                if transaction.sender == address:
                    balance -= transaction.amount

                if transaction.recipent == address:
                    balance += transaction.amount

        return balance

    def get_wallet_transactions(self, address: str, tx_type: tt = tt.BOTH) -> Union[dict, list[Transaction]]:
        """
        Returns list of all wallet transactions stored in the blockchain, which contains given address as sender or
        recipient.
        :param kind: INCOMING, OUTGOING or BOTH
        :param address: public wallet key
        :return: list of transactions of the provided address
        """
        transactions = {'incoming': [], 'outgoing': []}
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    transactions['outgoing'].append(tx)
                if tx.recipent == address:
                    transactions['incoming'].append(tx)

        if tx_type == tt.INCOMING:
            return transactions['incoming']
        if tx_type == tt.OUTGOING:
            return transactions['outgoing']
        return transactions

    def is_valid(self) -> bool:
        """
        Loops over all the blocks in the chain and verify if they are properly linked together and nobody has tampered
        with the hashes. By checking the blocks it also verifies the transactions inside of them
        :return: bool
        """
        for i in range(1, len(self.chain)):  # do not include genesis block
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if not current_block.is_valid():
                return False

            if current_block.hash != current_block.calculate_hash() \
                    or current_block.previous_hash != previous_block.calculate_hash():
                return False

            return True
