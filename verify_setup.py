from app import create_app
from config import DevelopmentConfig


def main():
    try:
        app = create_app(DevelopmentConfig)

        with app.app_context():
            from app.models.user import User
            from app.models.admin import Admin

            user_count = User.query.count()
            admin_count = Admin.query.count()

            print('✅ Database connectivity check passed.')
            print(f'Users table query OK. Count: {user_count}')
            print(f'Admins table query OK. Count: {admin_count}')

            routes = list(app.url_map.iter_rules())
            print(f'✅ Route registration check passed. Total routes: {len(routes)}')

    except Exception as exc:
        print('❌ Setup verification failed.')
        print(f'Error: {exc}')
        print('Tip: Ensure DATABASE_URL is correct, PostgreSQL is running, and migrations are applied.')


if __name__ == '__main__':
    main()
