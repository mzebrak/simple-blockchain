from flask import Blueprint, jsonify, abort
from src.transaction import Transaction

from src.api.transactions import get_transactions_list
from src.block import Block
from src.blockchain_manager import BlockchainManager

find_api = Blueprint('find_api', __name__)


def find_block(hash: str) -> Block:
    return next((b for b in BlockchainManager.get_chain() if b.hash == str(hash)), None)


def find_transaction(hash: str) -> Transaction:
    return next((t for t in get_transactions_list() if t.hash == str(hash)), None)


@find_api.route("/find/<hash>/", methods=['GET'])
def get_block_or_tx(hash: str):
    found = find_block(hash) or find_transaction(hash)
    return jsonify(found) if found else abort(404, f'No block or tx with given hash: {hash}')
