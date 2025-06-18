from flask import Flask, jsonify

from ._db import INDEX
from ._models import bp as models_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(models_bp)


    @app.route("/")
    def index():
        return jsonify(INDEX)

    return app