from functools import wraps
from flask import redirect, url_for
from flask_login import current_user
from core.models import Institute


def institute_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if not current_user.is_authenticated or not isinstance(current_user,Institute): 
 
      print("User is not authenticated or not an Institute")
      return redirect(url_for("auth.institute_login"))
    print("User is authenticated and an Institute")
    return f(*args, **kwargs)
  return decorated_function

