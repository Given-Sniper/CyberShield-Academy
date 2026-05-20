from flask import Flask, render_template

from config import DevelopmentConfig
from app.extensions import csrf, db, login_manager, mail, migrate


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from app.models import (  # noqa: F401
            activity,
            admin,
            lesson,
            phishing_example,
            quiz,
            quiz_question,
            quiz_result,
            user,
            user_lesson,
        )

    from app.blueprints.main import main_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.dashboard import dashboard_bp
    from app.blueprints.lessons import lessons_bp
    from app.blueprints.quizzes import quizzes_bp
    from app.blueprints.phishing import phishing_bp
    from app.blueprints.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(lessons_bp, url_prefix='/lessons')
    app.register_blueprint(quizzes_bp, url_prefix='/quizzes')
    app.register_blueprint(phishing_bp, url_prefix='/phishing')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @app.errorhandler(403)
    def forbidden(_error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def not_found(_error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(_error):
        return render_template('errors/500.html'), 500

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.admin import Admin
        from app.models.user import User

        if not user_id:
            return None

        try:
            scope, raw_id = user_id.split(':', 1)
            obj_id = int(raw_id)
        except (ValueError, AttributeError):
            return User.query.get(int(user_id)) if str(user_id).isdigit() else None

        if scope == 'admin':
            return Admin.query.get(obj_id)
        if scope == 'user':
            return User.query.get(obj_id)
        return None

    return app
