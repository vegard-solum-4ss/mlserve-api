# base_url = r"https://api.mlserve.com"
base_url = r"http://127.0.0.1:8000"



INDEX = {
    "models_url": base_url + r"/models{/id}",
}


MODELS = [
    {
        "id": 1234,
        "url": base_url + "/models/1234",
        "name": "Model A",
    },
    {
        "id": 5678,
        "url": base_url + "/models/5678",
        "name": "Model B",
    }
]


MODEL = {
    "1234": {
        "id": 1234,
        "name": "Model A",
        "predictions_url": base_url + "/models/1234/predictions{/id}",
    },
    "5678": {
        "id": 5678,
        "name": "Model B",
        "predictions_url": base_url + "/models/1234/predictions{/id}",
    }
}
