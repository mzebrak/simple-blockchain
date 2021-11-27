from flask import Blueprint, jsonify, abort

from src.blockchain_manager import BlockchainManager

blocks_api = Blueprint('blocks_api', __name__)


@blocks_api.route("/blocks/", methods=['GET'])
def get_blocks():
    return jsonify(BlockchainManager.get_chain())


@blocks_api.route("/blocks/<hash>/", methods=['GET'])
def get_block(hash):
    block = next((b for b in BlockchainManager.get_chain() if b.hash == str(hash)), None)
    return jsonify(block if block else abort(404, f'No bock with given hash: {hash}'))
