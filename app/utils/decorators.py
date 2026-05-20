from functools import wraps


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """TODO: Implement admin role authorization check."""
        raise NotImplementedError('admin_required decorator is not implemented yet.')

    return wrapper


def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """TODO: Implement regular user authorization check."""
        raise NotImplementedError('user_required decorator is not implemented yet.')

    return wrapper
