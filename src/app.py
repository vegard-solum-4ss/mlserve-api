from flask import Flask, jsonify, request, abort

from _db import base_url, INDEX, MODELS, MODEL

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(INDEX)


@app.get("/models")
def get_models():
    return jsonify(MODELS)


@app.post("/models")
def post_models():

    data = request.get_json()
    if "name" not in data:
        abort(400, description="Name is required")

    new_id = max(model["id"] for model in MODELS) + 1 if MODELS else 1
    new_model = {
        "id": new_id,
        "name": data["name"],
        "url": base_url + f"/models/{new_id}",
    }
    MODELS.append(new_model)
    return jsonify(new_model), 201


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
