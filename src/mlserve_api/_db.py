# base_url = r"https://api.mlserve.com"
base_url = r"http://127.0.0.1:8000"


INDEX = {
    "models_url": f"{base_url}/models{'{/id}'}",
}


MODELS = [
    {
        "id": 1,
        "url": f"{base_url}/models/1",
        "name": "Model A",
        "prediction_url": f"{base_url}/models/1/prediction",
    },
    {
        "id": 2,
        "url": f"{base_url}/models/2",
        "name": "Model B",
        "prediction_url": f"{base_url}/models/2/prediction",
    },
]


def get_index():
    """Retrieve the index."""
    return INDEX


def get_models():
    """Retrieve the list of models."""
    return MODELS


def get_model(id_):
    """Retrieve the details for a specific model."""
    model = next((m for m in MODELS if m["id"] == int(id_)), None)
    return model

def add_model(data):
    """Add a new model."""

    new_id = max(model["id"] for model in MODELS) + 1 if MODELS else 1
    new_model = {
        "id": new_id,
        "name": data.get("name"),
        "url": f"{base_url}/models/{new_id}",
        "prediction_url": f"{base_url}/models/{new_id}/prediction",
    }
    MODELS.append(new_model)
    return new_model
