from app.models import User


def test_user_model_exists():
    assert User is not None
