import math

from flask import render_template, request, current_app
from app.dao import dao
from app.utils.component_util import get_components_data
from app._init_ import create_app

class ComponentController:

    # [GET] /components
    def index(self):
        args = request.args.to_dict()
        page = request.args.get("page")
        pages = math.ceil(dao.count_product() / current_app.config["PAGE_SIZE"])
        comps, vehicles, brands, selected_vehicle_name, selected_brand_name = get_components_data(args, page)
        return render_template("components.html", page="Linh kiện",
                               comps=comps,vehicles=vehicles,brands=brands,current_args=args,
                               selected_vehicle_name=selected_vehicle_name,
                               selected_brand_name=selected_brand_name,
                               pages=pages)


    # [GET] /components/:slug
    def show(self, slug):
        return render_template("componentDetail.html", slug=slug)
