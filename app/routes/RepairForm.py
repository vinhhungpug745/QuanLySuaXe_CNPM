from app.controllers.AppointmentController import AppointmentController
from app.controllers.RepairFormController import RepairFormController
from flask import Blueprint


repairform = RepairFormController()

repairform_bp = Blueprint('repairform_bp', __name__)

repairform_bp.add_url_rule('/', view_func=repairform.index)
