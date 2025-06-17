import json

from flask import Flask, url_for, jsonify

from _db import INDEX, MODELS, MODEL

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(INDEX)


@app.route("/models")
def list_models():
    return jsonify(MODELS)


@app.route("/models/<model_id>")
def get_model(model_id):
    return jsonify(MODEL[model_id])


# @app.route("/test")
# def test():
#     return url_for("index")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
