from Blockchain import Blockchain
import datetime
from Block import Block
def main():
    blockchain = Blockchain()

    print(blockchain.to_json())


if __name__ == '__main__':
    main()
