from app.controllers.Export_receiptsController import Export_receiptsController
from flask import Blueprint

export_receipts = Export_receiptsController()

export_receipts_bp = Blueprint('export_receipts_bp', __name__)


export_receipts_bp.add_url_rule('/', view_func=export_receipts.index)

export_receipts_bp.add_url_rule('/export/<int:receipt_id>', view_func=export_receipts.export,methods=['GET'])

