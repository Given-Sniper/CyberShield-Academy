from flask import abort, flash, redirect, render_template, session, url_for
from flask_login import current_user, login_user, logout_user
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from app.blueprints.auth import auth_bp
from app.blueprints.auth.forms import LoginForm, RegistrationForm
from app.extensions import db
from app.models import Admin, User


def _destination(account):
    return 'admin.admin_dashboard' if isinstance(account, Admin) else 'dashboard.index'


@auth_bp.route('/register', methods=['GET', 'POST'])
def user_register():
    if current_user.is_authenticated:
        return redirect(url_for(_destination(current_user._get_current_object())))
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        if db.session.scalar(select(User).where(func.lower(User.email) == email)):
            form.email.errors.append('An account with this email already exists.')
        else:
            user = User(email=email, full_name=form.full_name.data.strip())
            user.set_password(form.password.data)
            db.session.add(user)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                form.email.errors.append('An account with this email already exists.')
            else:
                flash('Account created. Please log in.', 'success')
                return redirect(url_for('auth.user_login'))
    return render_template('auth/form.html', form=form, heading='Create your account')


def _login(model, heading):
    if current_user.is_authenticated:
        return redirect(url_for(_destination(current_user._get_current_object())))
    form = LoginForm()
    if form.validate_on_submit():
        account = db.session.scalar(select(model).where(func.lower(model.email) == form.email.data.strip().lower()))
        if account is not None and account.check_password(form.password.data) and account.is_active:
            session.clear()
            login_user(account)
            session.permanent = True
            return redirect(url_for(_destination(account)))
        form.password.errors.append('Invalid email or password.')
    return render_template('auth/form.html', form=form, heading=heading)


@auth_bp.route('/login', methods=['GET', 'POST'])
def user_login():
    return _login(User, 'User login')


@auth_bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    return _login(Admin, 'Admin login')


@auth_bp.route('/logout', methods=['POST'])
def user_logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.user_login'))


@auth_bp.route('/admin/logout', methods=['POST'])
def admin_logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.admin_login'))


@auth_bp.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    # Admin accounts are provisioned by a trusted operator via the CLI.
    abort(403)


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

