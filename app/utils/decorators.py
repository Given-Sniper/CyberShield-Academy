from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user

from app.models.admin import Admin
from app.models.user import User


def login_required_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user._get_current_object(), User):
            flash('Please log in as a user to access this page.', 'warning')
            return redirect(url_for('auth.user_login'))
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user._get_current_object(), Admin):
            flash('Please log in as an admin to access this page.', 'warning')
            return redirect(url_for('auth.admin_login'))
        return func(*args, **kwargs)

    return wrapper
