import click
from sqlalchemy import func, select
from app.extensions import db
from app.models import Admin


def register_commands(app):
    @app.cli.command('create-admin')
    @click.option('--email', prompt=True)
    @click.password_option(confirmation_prompt=True)
    def create_admin(email, password):
        """Provision an administrator; public admin registration is disabled."""
        from email_validator import validate_email, EmailNotValidError
        try:
            email = validate_email(email.strip(), check_deliverability=False).normalized.lower()
        except EmailNotValidError as exc:
            raise click.ClickException(str(exc)) from exc
        if not 12 <= len(password) <= 128:
            raise click.ClickException('Password must contain 12–128 characters.')
        if db.session.scalar(select(Admin).where(func.lower(Admin.email) == email)):
            raise click.ClickException('Admin email already exists.')
        admin = Admin(email=email)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        click.echo('Admin account created.')
