from flask import Blueprint

quizzes_bp = Blueprint('quizzes', __name__, url_prefix='/quizzes')

from app.blueprints.quizzes import routes  # noqa: E402,F401
