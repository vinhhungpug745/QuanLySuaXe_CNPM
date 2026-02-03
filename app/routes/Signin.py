from app.controllers.SigninController import SigninController
from flask import Blueprint

controller = SigninController()

signin_bp = Blueprint("signin", __name__)

signin_bp.add_url_rule('/', view_func=controller.index, methods=["GET"], endpoint="signin_index")

# POST /signin
signin_bp.add_url_rule("/signin", view_func=controller.signin, methods=["GET","POST"],endpoint="signin_post")

# POST /signin/signup
signin_bp.add_url_rule("/signup", view_func=controller.signup, methods=["GET","POST"],endpoint="signup_post")

signin_bp.add_url_rule("/signin-google", view_func=controller.auth_callback)

signin_bp.add_url_rule("/auth-google", view_func=controller.login_google)

# GET logout
signin_bp.add_url_rule("/signout", view_func=controller.signout, methods=["GET"], endpoint="signout")