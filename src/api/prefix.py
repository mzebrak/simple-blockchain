from flask import Blueprint

from src.api.blocks import blocks_api
from src.api.find import find_api
from src.api.keys import keys_api
from src.api.transactions import transactions_api
from src.api.validate import validate_api

prefix_api = Blueprint('prefix_api', __name__)
prefix_api.register_blueprint(blocks_api)
prefix_api.register_blueprint(transactions_api)
prefix_api.register_blueprint(keys_api)
prefix_api.register_blueprint(find_api)
prefix_api.register_blueprint(validate_api)


@prefix_api.route('/')
def index():
    return "Hi!"
