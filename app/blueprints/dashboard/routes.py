from flask import abort

from app.blueprints.dashboard import dashboard_bp

@dashboard_bp.route('/', methods=['GET'])
def index():
    """TODO: Implement index route."""
    abort(501)

@dashboard_bp.route('/progress', methods=['GET'])
def progress():
    """TODO: Implement progress route."""
    abort(501)

@dashboard_bp.route('/activity', methods=['GET'])
def activity_history():
    """TODO: Implement activity_history route."""
    abort(501)

