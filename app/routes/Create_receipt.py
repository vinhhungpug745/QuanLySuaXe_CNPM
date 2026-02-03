from app.controllers.Create_receiptController import Create_receiptController
from flask import Blueprint

create_receipts = Create_receiptController()

create_receipts_bp = Blueprint('create_receipts_bp', __name__)


create_receipts_bp.add_url_rule('/', view_func=create_receipts.index, methods=['GET'])

# API lập hóa đơn (POST)
create_receipts_bp.add_url_rule('/api-createreceipt', view_func=create_receipts.create_receipt, methods=['POST'])
