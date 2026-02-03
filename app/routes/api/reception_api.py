from flask import Blueprint
from app.controllers.ReceptionController import ReceptionController

reception_api = Blueprint("reception_api", __name__)
controller = ReceptionController()

reception_api.add_url_rule("/update/<id>",view_func=controller.updata_form,methods=["PUT"])
reception_api.add_url_rule("/remove/<id>",view_func=controller.delete_form,methods=["DELETE"])
