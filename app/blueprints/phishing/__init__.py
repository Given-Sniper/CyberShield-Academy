from flask import Blueprint

phishing_bp = Blueprint('phishing', __name__, url_prefix='/phishing')

from app.blueprints.phishing import routes  # noqa: E402,F401
