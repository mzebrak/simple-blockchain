from flask import Flask, jsonify

from src.api.blocks import blocks_api
from src.api.keys import keys_api
from src.api.transactions import transactions_api
from src.api.find import find_api
from src.api.validate import validate_api

app = Flask(__name__)


def jsonify_error(error):
    return jsonify({"code": error.code, "name": error.name, "description": error.description})


@app.errorhandler(400)
@app.errorhandler(404)
def custom(error):
    return jsonify_error(error)


app.register_blueprint(blocks_api)
app.register_blueprint(transactions_api)
app.register_blueprint(keys_api)
app.register_blueprint(find_api)
app.register_blueprint(validate_api)


@app.route("/")
def homepage():
    return "simple-blockchain api"
