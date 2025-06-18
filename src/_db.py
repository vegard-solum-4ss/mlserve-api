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
