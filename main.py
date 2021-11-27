from src.api.app import app
from src.blockchain_manager import BlockchainManager


def main():
    BlockchainManager.create_new_blockchain()
    app.run(debug=True)


if __name__ == '__main__':
    main()
