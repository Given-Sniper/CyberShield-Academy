from flask import Blueprint

quizzes_bp = Blueprint('quizzes', __name__)

from app.blueprints.quizzes import routes  # noqa: E402,F401
