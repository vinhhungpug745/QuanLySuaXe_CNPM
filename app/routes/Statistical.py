from app.controllers.StatisticalController import StatisticalController
from flask import Blueprint

controller = StatisticalController()

statistical_bp = Blueprint('statistical_bp', __name__)

statistical_bp.add_url_rule('/', view_func=controller.index)
statistical_bp.add_url_rule('/create', view_func=controller.createStatistical)

