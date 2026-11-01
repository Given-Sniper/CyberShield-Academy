from flask import Blueprint

lessons_bp = Blueprint('lessons', __name__)

from app.blueprints.lessons import routes  # noqa: E402,F401
