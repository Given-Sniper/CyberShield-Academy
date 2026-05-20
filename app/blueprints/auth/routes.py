from flask import abort

from app.blueprints.auth import auth_bp

@auth_bp.route('/register', methods=['GET', 'POST'])
def user_register():
    """TODO: Implement user_register route."""
    abort(501)

@auth_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    """TODO: Implement user_login route."""
    abort(501)

@auth_bp.route('/logout', methods=['POST'])
def user_logout():
    """TODO: Implement user_logout route."""
    abort(501)

@auth_bp.route('/reset/request', methods=['GET', 'POST'])
def reset_request():
    """TODO: Implement reset_request route."""
    abort(501)

@auth_bp.route('/reset/security-question', methods=['GET', 'POST'])
def reset_security_question():
    """TODO: Implement reset_security_question route."""
    abort(501)

@auth_bp.route('/reset/token/<token>', methods=['GET', 'POST'])
def reset_token(token):
    """TODO: Implement reset_token route."""
    abort(501)

@auth_bp.route('/reset/password', methods=['GET', 'POST'])
def reset_password():
    """TODO: Implement reset_password route."""
    abort(501)

@auth_bp.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    """TODO: Implement admin_register route."""
    abort(501)

@auth_bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """TODO: Implement admin_login route."""
    abort(501)

@auth_bp.route('/admin/logout', methods=['POST'])
def admin_logout():
    """TODO: Implement admin_logout route."""
    abort(501)

