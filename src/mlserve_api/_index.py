from flask import Blueprint, jsonify

from ._db import INDEX

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def index():
    return jsonify(INDEX)
