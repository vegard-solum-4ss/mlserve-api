import numpy as np
from flask import Blueprint, abort, jsonify, request

from ._db import MODELS, base_url

bp = Blueprint("models", __name__, url_prefix="/models")


@bp.get("/")
def get_models():
    return jsonify(MODELS)


@bp.post("/")
def post_models():

    data = request.get_json()
    if "name" not in data:
        abort(400, description="Name is required")

    new_id = max(model["id"] for model in MODELS) + 1 if MODELS else 1
    new_model = {
        "id": new_id,
        "name": data["name"],
        "url": f"{base_url}/models/{new_id}",
        "prediction_url": f"{base_url}/models/{new_id}/prediction",
    }
    MODELS.append(new_model)
    return jsonify(new_model), 201


@bp.get("/<int:model_id>")
def get_model(model_id):
    """Retrieve the details for a specific model."""
    model = next((m for m in MODELS if m["id"] == int(model_id)), None)
    return jsonify(model)


@bp.post("/<int:model_id>/prediction")
def prediction(model_id):
    """Predict operability using a specific ML model."""
    model = next((m for m in MODELS if m["id"] == model_id), None)
    if not model:
        abort(404, description="Model not found")

    pred = int(np.random.default_rng().choice([0, 1], p=[0.9, 0.1]))

    response_dict = {
        "model_id": model_id,
        "prediction": pred,
    }

    return jsonify(response_dict), 200
