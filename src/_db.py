# base_url = r"https://api.mlserve.com"
base_url = r"http://127.0.0.1:8000"


INDEX = {
    "models_url": base_url + r"/models{/id}",
}


MODELS = [
    {
        "id": 1,
        "url": base_url + "/models/1",
        "name": "Model A",
    },
    {
        "id": 2,
        "url": base_url + "/models/2",
        "name": "Model B",
    },
]
