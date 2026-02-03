from flask import Blueprint
from app.controllers.AppointmentController import AppointmentController

appointment_api = Blueprint("appointment_api", __name__)
controller = AppointmentController()

appointment_api.add_url_rule("/limit",view_func=controller.limitVehicle,methods=["GET"])
appointment_api.add_url_rule("/info",view_func=controller.infoCustomer,methods=["GET"])