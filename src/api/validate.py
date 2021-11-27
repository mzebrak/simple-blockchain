from flask import Blueprint, jsonify, abort

from src.api.find import find_block, find_transaction
from src.blockchain_manager import BlockchainManager

validate_api = Blueprint('validate_api', __name__)


@validate_api.route("/validate/", methods=['GET'])
def get_validate_blockchain():
    return jsonify(BlockchainManager.is_blockchain_valid())


@validate_api.route("/validate/<hash>/", methods=['GET'])
def get_validate_block_or_tx(hash):
    if block := find_block(hash):
        return jsonify(block.is_valid())

    if tx := find_transaction(hash):
        return jsonify(tx.is_valid())

    abort(404, f'No block or tx with given hash: {hash}')
