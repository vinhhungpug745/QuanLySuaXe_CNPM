from app.controllers.ReceptionController import ReceptionController
from flask import Blueprint

receptions = ReceptionController()

receptions_bp = Blueprint('receptions_bp', __name__)


receptions_bp.add_url_rule('/', view_func=receptions.index)