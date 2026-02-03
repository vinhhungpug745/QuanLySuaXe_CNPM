from app.controllers.AppointmentController import AppointmentController
from flask import Blueprint

appointment = AppointmentController()

appointment_bp = Blueprint('appointment_bp', __name__)

appointment_bp.add_url_rule('/create', view_func=appointment.receptionForm, methods=['GET', 'POST'])
appointment_bp.add_url_rule('/', view_func=appointment.index)