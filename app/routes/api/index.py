from app.routes.api.appointment_api import appointment_api
from app.routes.api.reception_api import reception_api
from app.routes.api.repairform_api import repairform_api
from app.routes.api.payment_api import payment_api_bp

def route_api(app):
    app.register_blueprint(appointment_api, url_prefix="/api/appointment")
    app.register_blueprint(reception_api, url_prefix="/api/receptions")
    app.register_blueprint(repairform_api, url_prefix="/api/repairform")
    app.register_blueprint(payment_api_bp, url_prefix="/api/payment")
