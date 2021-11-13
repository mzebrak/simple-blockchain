import datetime
from dataclasses import FrozenInstanceError

from Blockchain import Blockchain


def print_blockchain(blockchain: Blockchain, additional: bool = False):
    print("This blockchain in JSON:")
    print(blockchain.to_json())
    if additional:
        print(f'Second last block in chain: {blockchain.chain[-2]}')
        print(f'Latest block in chain: {blockchain.get_latest_block()}')
        print(f'Latest block in chain printed as json:\n{blockchain.get_latest_block().to_json()}')
    print(f'Is blockchain valid?: {blockchain.is_chain_valid()}')


def show_valid_blockchain(additional: bool = False):
    print('\n----------------------------------\nshow_valid_blockchain()\n----------------------------------')
    blockchain = Blockchain()
    blockchain.add_block(timestamp=datetime.datetime(2021, 11, 13, 12),
                         data={'amount': 200},
                         previous_hash='latest')
    blockchain.add_block(timestamp=datetime.datetime.now(),
                         data={'amount': 100},
                         previous_hash='latest')

    print_blockchain(blockchain, additional)


def show_invalid_blockchain(additional: bool = False):
    print('\n----------------------------------\nshow_invalid_blockchain()\n----------------------------------')
    blockchain = Blockchain()
    blockchain.add_block(timestamp=datetime.datetime(2021, 11, 13, 12),
                         data={'amount': 200},
                         previous_hash='latest')

    try:
        obj = blockchain.chain[1]
        obj.data = "newdata"
        # obj.hash = obj.calculate_hash() # to make it valid again
    except FrozenInstanceError:
        raise SystemExit("block is immutable, change its frozen attribute")

    print_blockchain(blockchain, additional)


def main():
    # show_valid_blockchain(additional=False)
    show_invalid_blockchain(additional=False)


if __name__ == '__main__':
    main()
