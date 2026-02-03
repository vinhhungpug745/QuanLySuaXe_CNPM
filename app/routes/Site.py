from app.controllers.SiteController import SiteController
from flask import Blueprint

sites = SiteController()

site_bp = Blueprint('site_bp', __name__)

site_bp.add_url_rule('/', view_func=sites.index)