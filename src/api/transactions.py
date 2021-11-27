from flask import Blueprint, jsonify, abort

from src.blockchain_manager import BlockchainManager
from src.transaction import Transaction

transactions_api = Blueprint('transactions_api', __name__)


def get_transactions_list() -> list[Transaction]:
    txs_lists = [block.transactions for block in BlockchainManager.get_chain()]
    return [item for sublist in txs_lists for item in sublist]


@transactions_api.route("/transactions/", methods=['GET'])
def get_transactions():
    return jsonify(get_transactions_list())


@transactions_api.route("/transactions/<hash>/", methods=['GET'])
def get_transaction(hash):
    tx = next((t for t in get_transactions_list() if t.hash == str(hash)), None)
    return jsonify(tx if tx else abort(404, f'No transaction with given hash: {hash}'))


@transactions_api.route("/transactions/pending/", methods=['GET'])
def get_pending_transactions():
    return jsonify(BlockchainManager.get_pending_transactions())
