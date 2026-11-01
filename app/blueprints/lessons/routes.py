from app.utils.decorators import login_required_user
from flask import abort

from app.blueprints.lessons import lessons_bp

@lessons_bp.route('/', methods=['GET'])
@login_required_user
def lessons_list():
    """TODO: Implement lessons_list route."""
    abort(501)

@lessons_bp.route('/<int:lesson_id>', methods=['GET'])
@login_required_user
def lesson_detail(lesson_id):
    """TODO: Implement lesson_detail route."""
    abort(501)

@lessons_bp.route('/<int:lesson_id>/complete', methods=['POST'])
@login_required_user
def lesson_complete(lesson_id):
    """TODO: Implement lesson_complete route."""
    abort(501)

