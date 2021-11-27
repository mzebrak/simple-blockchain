from flask import Blueprint, abort, request, jsonify

from src.key_generator import KeyGenerator

keys_api = Blueprint('keys_api', __name__)


@keys_api.route("/keys/", methods=['GET'])
def get_all_saved_keys():
    keys = KeyGenerator.keys
    return jsonify(keys) if keys else abort(404, 'No keys were saved. Use /keys/generate?save=true')


@keys_api.route("/keys/generate/", methods=['GET'])
def get_pending_transactions():
    save = request.args.get('save', default='false', type=str).lower()
    pair = KeyGenerator.generate_new_key_pair()

    if save == 'true':
        KeyGenerator.keys.append(pair)
    elif save != 'false':
        abort(400, 'Valid arguments are "true" or "false"')
    return jsonify(dict(pair, **{'saved': save}))
