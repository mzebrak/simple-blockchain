from flask import Flask, jsonify
from src.api.prefix import prefix_api
app = Flask(__name__)
app.register_blueprint(prefix_api, url_prefix='/api')


def jsonify_error(error):
    return jsonify({"code": error.code, "name": error.name, "description": error.description})


@app.errorhandler(400)
@app.errorhandler(404)
def custom(error):
    return jsonify_error(error)
