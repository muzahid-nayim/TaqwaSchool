from functools import wraps
from flask import redirect, url_for,abort
from flask_login import current_user
from core.models import Institute

def institute_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            # Redirect to the institute login page if the user is not authenticated
            return redirect(url_for("auth.institute_login"))
        elif not isinstance(current_user, Institute):
            # Optionally, handle the case where the user is authenticated but not an institute
            return redirect(url_for("auth.institute_login"))
        return f(*args, **kwargs)

    return decorated_function
