# _base_url = r"https://api.4insight.io/v1/mlserve"
_base_url = r"http://127.0.0.1:8000"


_INDEX = {
    "models_url": f"{_base_url}/models{'{/id}'}",
}


_MODELS = [
    {
        "id": 1,
        "url": f"{_base_url}/models/1",
        "name": "Model A",
        "prediction_url": f"{_base_url}/models/1/prediction",
    },
    {
        "id": 2,
        "url": f"{_base_url}/models/2",
        "name": "Model B",
        "prediction_url": f"{_base_url}/models/2/prediction",
    },
]


def get_index() -> dict:
    """Retrieve the index."""
    return _INDEX


def get_models() -> list[dict]:
    """Retrieve the list of models."""
    return _MODELS


def get_model(id_) -> dict | None:
    """Retrieve the details for a specific model."""
    model = next((m for m in _MODELS if m["id"] == int(id_)), None)
    return model


def new_model(data: dict) -> dict:
    """Add a new model."""

    new_id = max(model["id"] for model in _MODELS) + 1 if _MODELS else 1
    new_model = {
        "id": new_id,
        "name": data.get("name"),
        "url": f"{_base_url}/models/{new_id}",
        "prediction_url": f"{_base_url}/models/{new_id}/prediction",
    }
    _MODELS.append(new_model)
    return new_model
