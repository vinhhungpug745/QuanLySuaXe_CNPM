from app.controllers.CartController import CartController
from flask import Blueprint

cart = CartController()

cart_bp = Blueprint('cart_bp', __name__)
cart_bp.add_url_rule('/add-cart', view_func=cart.add_to_cart, methods=["POST"], endpoint="add_to_cart")