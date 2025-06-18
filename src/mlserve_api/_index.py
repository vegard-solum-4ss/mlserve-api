from flask import Blueprint, jsonify

from . import db

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def index():
    return jsonify(db.get_index()), 200
