import cloudinary.uploader

from flask import render_template, request, redirect, url_for, session
from app.dao import dao
from flask_login import login_user, logout_user
from app.middleware.authenticate import check_login
from app._init_ import google
from app.models.model import User


class SigninController:

    def login_google(self):
        redirect_uri = url_for('signin.auth_callback', _external=True)
        return google.authorize_redirect(redirect_uri)

    def auth_callback(self):
        token = google.authorize_access_token()
        user_info = token.get('userinfo')

        email = user_info['email']
        name = user_info['name']
        avatar = user_info['picture']

        user = dao.check_userEmail(email)

        if not user:
            user = dao.add_user(
                email=email,
                name=name,
                avatar=avatar
            )

        login_user(user)

        return redirect("/")

    # [GET] /signin
    def index(self):
        return render_template("registerLogin.html", page="Tài khoản")

    # [POST] xử lý đăng ký /signup
    def signup(self):
        if request.method == "POST":
            name = request.form.get("name")
            phonenumber = request.form.get("phonenumber")
            username = request.form.get("username")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")
            avatar = request.files.get("avatar")
            avatar_path = None

            existing = dao.get_user_by_username(username)
            if existing:
                return render_template("registerLogin.html",
                                       page="Đăng ký",
                                       alert_message="Username đã tồn tại! Vui lòng chọn tên khác.",
                                       alert_category="danger")

            if password.strip().__eq__(confirm_password.strip()):
                if avatar:
                    res=cloudinary.uploader.upload(avatar)
                    avatar_path = res["secure_url"]
                dao.add_user(name=name,phonenumber=phonenumber, username=username, password=password, avatar=avatar_path)
                return render_template("registerLogin.html",
                                       page="Đăng ký",
                                       alert_message="Đăng ký thành công! Mời bạn đăng nhập.",
                                       alert_category="success")
            else:
                return render_template("registerLogin.html",
                                       page="Đăng ký",
                                       alert_message="Mật khẩu nhập lại không đúng!",
                                       alert_category="danger")

        # Nếu GET thì hiện form đăng ký
        return render_template("registerLogin.html", page="ĐN\ĐK")

    def signin(self):
        if request.method == "POST":
            username = request.form.get('username')
            password = request.form.get('password')
            user= check_login(username, password)

            if user:
                login_user(user=user)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect(url_for("site_bp.index"))
            else:
                return render_template("registerLogin.html",
                                       page="Đăng nhập",
                                       alert_message="Tên tài  khoản hoặc mậu khẩu không đúng",
                                       alert_category="danger")
        return render_template("registerLogin.html")

    def signout(self):
        logout_user()
        return redirect(url_for("site_bp.index"))