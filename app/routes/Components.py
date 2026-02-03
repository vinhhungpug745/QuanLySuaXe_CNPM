from app.controllers.ComponentController import ComponentController
from flask import Blueprint

components = ComponentController()

components_bp = Blueprint('components_bp', __name__)


components_bp.add_url_rule('/<slug>', view_func=components.show)
components_bp.add_url_rule('/', view_func=components.index)