from app.utils.decorators import login_required_user
from flask import abort

from app.blueprints.quizzes import quizzes_bp

@quizzes_bp.route('/', methods=['GET'])
@login_required_user
def quiz_list():
    """TODO: Implement quiz_list route."""
    abort(501)

@quizzes_bp.route('/<int:quiz_id>/start', methods=['GET', 'POST'])
@login_required_user
def quiz_start(quiz_id):
    """TODO: Implement quiz_start route."""
    abort(501)

@quizzes_bp.route('/<int:quiz_id>/take', methods=['GET'])
@login_required_user
def quiz_take(quiz_id):
    """TODO: Implement quiz_take route."""
    abort(501)

@quizzes_bp.route('/<int:quiz_id>/submit', methods=['POST'])
@login_required_user
def quiz_submit(quiz_id):
    """TODO: Implement quiz_submit route."""
    abort(501)

@quizzes_bp.route('/results/<int:result_id>', methods=['GET'])
@login_required_user
def quiz_result(result_id):
    """TODO: Implement quiz_result route."""
    abort(501)

@quizzes_bp.route('/history', methods=['GET'])
@login_required_user
def quiz_history():
    """TODO: Implement quiz_history route."""
    abort(501)

