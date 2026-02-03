from app.controllers.PaymentController import PaymentController
from flask import Blueprint

payments = PaymentController()

payments_bp = Blueprint('payments_bp', __name__)


payments_bp.add_url_rule('/',view_func=payments.index,methods=['GET', 'POST'])
