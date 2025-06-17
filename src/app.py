from flask import Flask, jsonify, request

from _db import INDEX, MODELS, MODEL

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(INDEX)


@app.get("/models")
def get_models():
    """
    Retrieve all models.
    """
    return jsonify(MODELS)


@app.get("/models/<model_id>")
def get_model(model_id):
    """Retrieve the details for a specific model."""
    return jsonify(MODEL[model_id])


# @app.post("/models/<model_id>")
# def post_model(model_id):
#     """Create a new prediction for a specific model."""
#     return jsonify(MODEL[model_id])


# @app.route("/test")
# def test():
#     return url_for("index")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
