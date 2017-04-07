from functools import wraps
from flask import redirect, session as login_session


def logged_in(function):
    @wraps(function)
    def wrapper(*a, **kw):
        # If not logged in redirect to login page
        if 'username' not in login_session:
            return redirect('/login')
        return function(*a, **kw)
    return wrapper
