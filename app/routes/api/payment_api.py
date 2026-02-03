from flask import Blueprint
from app.controllers.API_PaymentController import API_PaymentController

api = API_PaymentController()
payment_api_bp = Blueprint("payment_api_bp", __name__)



@payment_api_bp.route("/momo/pay/<int:receipt_id>", methods=["POST"])
def momo_pay(receipt_id):
    return API_PaymentController.momo_pay(receipt_id)


@payment_api_bp.route("/momo/return")
def momo_return():
    return API_PaymentController.momo_return()
