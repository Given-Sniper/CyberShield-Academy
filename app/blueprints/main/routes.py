from flask import abort

from app.blueprints.main import main_bp

@main_bp.route('/', methods=['GET'])
def index():
    """TODO: Implement index route."""
    abort(501)

@main_bp.route('/about', methods=['GET'])
def about():
    """TODO: Implement about route."""
    abort(501)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """TODO: Implement contact route."""
    abort(501)

@main_bp.route('/privacy', methods=['GET'])
def privacy():
    """TODO: Implement privacy route."""
    abort(501)

