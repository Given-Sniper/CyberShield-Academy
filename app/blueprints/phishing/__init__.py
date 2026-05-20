from flask import Blueprint

phishing_bp = Blueprint('phishing', __name__)

from app.blueprints.phishing import routes  # noqa: E402,F401
