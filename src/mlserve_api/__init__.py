from flask import Flask

from ._index import bp as index_bp
from ._models import bp as models_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(index_bp)
    app.register_blueprint(models_bp)

    return app
