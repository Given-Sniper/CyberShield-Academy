from flask import Flask, render_template

from app.blueprints.admin import admin_bp
from app.blueprints.auth import auth_bp
from app.blueprints.dashboard import dashboard_bp
from app.blueprints.lessons import lessons_bp
from app.blueprints.main import main_bp
from app.blueprints.phishing import phishing_bp
from app.blueprints.quizzes import quizzes_bp
from app.extensions import csrf, db, login_manager, mail, migrate


def init_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(lessons_bp)
    app.register_blueprint(quizzes_bp)
    app.register_blueprint(phishing_bp)
    app.register_blueprint(admin_bp)


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(403)
    def forbidden(_error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def not_found(_error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(_error):
        return render_template('errors/500.html'), 500


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    from app import models  # noqa: F401

    return app
