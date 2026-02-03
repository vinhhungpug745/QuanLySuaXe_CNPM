import hashlib
from app.models.model import User
from functools import wraps

from flask_login import current_user
from flask import redirect, url_for, abort, flash


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            #chưa đăng nhập => về login
            if not current_user.is_authenticated:
                # flash("Mời đăng nhập để sử dụng chức năng","error")
                return redirect("/signin")
            #sai quyền
            if current_user.role not in roles:
                flash("Bạn không có quyền truy cập chức năng này", "error")
                return redirect("/")
            return f(*args, **kwargs)
        return wrapper
    return decorator



def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password.strip())).first()

