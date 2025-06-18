import json

import numpy as np
from flask import Blueprint, abort, jsonify, request
import waveresponse as wr

from . import db

bp = Blueprint("models", __name__, url_prefix="/models")


@bp.get("/")
def get_models():
    return jsonify(db.get_models())


@bp.post("/")
def post_models():

    data = request.get_json()
    if "name" not in data:
        abort(400, description="Name is required")

    new_model = db.add_model(data)
    return jsonify(new_model), 201


@bp.get("/<int:model_id>")
def get_model(model_id):
    """Retrieve the details for a specific model."""
    return jsonify(db.get_model(model_id))


@bp.post("/<int:model_id>/prediction")
def prediction(model_id):
    """Predict operability using a specific ML model."""
    model = db.get_model(model_id)

    if not model:
        abort(404, description="Model not found")

    data = request.get_json()
    wave_data = data["wave"]
    heading = float(data["heading"])
    degrees = bool(data["degrees"])

    TYPE_MAP = {
        "WaveSpectrum": wr.WaveSpectrum,
        "WaveBinSpectrum": wr.WaveBinSpectrum,
    }

    wave = TYPE_MAP[wave_data["type"]](**wave_data["params"])

    pred = int(np.random.default_rng().choice([0, 1], p=[0.8, 0.2]))

    response_dict = {
        "model_id": model_id,
        "prediction": pred,
    }

    return jsonify(response_dict), 200
