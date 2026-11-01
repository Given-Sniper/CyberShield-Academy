from app.utils.decorators import login_required_user
from flask import abort, render_template

from app.blueprints.dashboard import dashboard_bp

@dashboard_bp.route('/', methods=['GET'])
@login_required_user
def index():
    return render_template('dashboard/user_dashboard.html')

@dashboard_bp.route('/progress', methods=['GET'])
@login_required_user
def progress():
    """TODO: Implement progress route."""
    abort(501)

@dashboard_bp.route('/activity', methods=['GET'])
@login_required_user
def activity_history():
    """TODO: Implement activity_history route."""
    abort(501)

