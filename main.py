import json

from src.Blockchain import Blockchain
from src.Transaction import Transaction


def main():
    public_key = '028932ef0ce3145fe17dd1d28c4b3ec40ccd8d5e32875f3f2fef8d4761ec6eb5fd'
    secret_key = '82605dccb6d509d60d4705b0399e6ab2aee6593a084585d41c63c6243fd9dda3'

    blockchain = Blockchain(difficulty=4)

    # Create a new transaction
    tx1 = Transaction(sender=public_key,
                      recipent='public key goes here',
                      description='test tx1',
                      amount=200)
    print(tx1)

    tx1.sign_transaction(sk_hex=secret_key)  # Sign transaction with a secret key
    # print(f'tx1 signature: {tx1.signature}')
    print(f'Is transaction valid?: {tx1.is_valid()}\n')

    blockchain.add_transaction(tx1)  # Add transaction to the blockchain

    print(blockchain.get_address_balance(public_key))  # Miner balance before mining
    blockchain.mine_pending_transactions(public_key)  # Mining 1
    print(blockchain.get_address_balance(public_key))  # after mining - same because mining reward is in new transaction

    blockchain.mine_pending_transactions(public_key)  # Mining 2 - mining transaction with reward from Mining 1
    print(blockchain.get_address_balance(public_key))

    a = blockchain.get_wallet_transactions('SYSTEM')
    print(json.dumps(a, default=vars, indent=4))  # All transactions for single wallet

    print(f'\nIs chain valid?: {blockchain.is_chain_valid()}\n')

    # print(blockchain.to_json())


if __name__ == '__main__':
    main()
