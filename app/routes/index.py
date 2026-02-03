from flask import Flask, render_template,Blueprint
from app.routes.Components import components_bp
from app.routes.RepairForm import repairform_bp
from app.routes.Transactions import Transaction_bp
from app.routes.Site import site_bp
from app.routes.Signin import signin_bp
from app.routes.Cart import cart_bp
from app.routes.Appointment import appointment_bp
from app.routes.Create_receipt import create_receipts_bp
from app.routes.Export_receipts import export_receipts_bp
from app.routes.Payment import payments_bp
from app.routes.Receptions import receptions_bp
from app.routes.Statistical import statistical_bp

def route_web(app):
    app.register_blueprint(components_bp, url_prefix="/components")
    app.register_blueprint(appointment_bp, url_prefix="/appointment")
    app.register_blueprint(signin_bp, url_prefix="/signin")
    app.register_blueprint(cart_bp, url_prefix="/api")
    app.register_blueprint(Transaction_bp, url_prefix="/Transactions")
    app.register_blueprint(receptions_bp, url_prefix="/receptions")
    app.register_blueprint(create_receipts_bp, url_prefix="/create_receipts")
    app.register_blueprint(export_receipts_bp, url_prefix="/export_receipts")
    app.register_blueprint(payments_bp, url_prefix="/payment")
    app.register_blueprint(statistical_bp, url_prefix="/statistical")
    app.register_blueprint(repairform_bp, url_prefix="/repairform")
    app.register_blueprint(site_bp, url_prefix="/")


