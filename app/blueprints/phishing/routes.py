from app.utils.decorators import login_required_user
from flask import abort

from app.blueprints.phishing import phishing_bp

@phishing_bp.route('/', methods=['GET'])
@login_required_user
def phishing_home():
    """TODO: Implement phishing_home route."""
    abort(501)

@phishing_bp.route('/example/<int:example_id>', methods=['GET'])
@login_required_user
def phishing_example_view(example_id):
    """TODO: Implement phishing_example_view route."""
    abort(501)

@phishing_bp.route('/example/<int:example_id>/submit', methods=['POST'])
@login_required_user
def phishing_submit(example_id):
    """TODO: Implement phishing_submit route."""
    abort(501)

@phishing_bp.route('/feedback/<int:activity_id>', methods=['GET'])
@login_required_user
def phishing_feedback(activity_id):
    """TODO: Implement phishing_feedback route."""
    abort(501)

@phishing_bp.route('/history', methods=['GET'])
@login_required_user
def phishing_history():
    """TODO: Implement phishing_history route."""
    abort(501)

