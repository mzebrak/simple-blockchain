import datetime

from Blockchain import Blockchain


def main():
    blockchain = Blockchain()

    blockchain.add_block(timestamp=datetime.datetime(2021, 11, 13, 12, 00),
                         data={'amount': 200},
                         previous_hash='latest')

    print(blockchain.to_json())

    print(blockchain.get_latest_block())
    # print(blockchain.get_latest_block().to_json())


if __name__ == '__main__':
    main()
