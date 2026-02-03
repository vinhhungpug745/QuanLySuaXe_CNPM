from flask import Blueprint
from app.controllers.RepairFormController import RepairFormController

repairform_api = Blueprint("repairfomr_api", __name__)
controller = RepairFormController()

repairform_api.add_url_rule("/create",view_func=controller.createform,methods=["POST"])