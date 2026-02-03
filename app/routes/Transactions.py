from app.controllers.TransactionController import TransactionController
from flask import Blueprint

Transaction = TransactionController()

Transaction_bp = Blueprint('Transaction_bp', __name__)


Transaction_bp.add_url_rule('/<slug>', view_func=Transaction.show)
Transaction_bp.add_url_rule('/', view_func=Transaction.index)