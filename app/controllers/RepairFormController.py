from flask import render_template, request, jsonify

from app.middleware.authenticate import role_required
from app.utils import repairform_util
from app.models.model import Form_status, UserRole
from app.utils import receptionform_util
from app.utils.component_util import get_components_data


class RepairFormController:

    def createform(self):
        data = request.get_json()
        try:
            res = repairform_util.createRepairform(data)
            if res:
                return jsonify({
                    "message": "Tạo phiếu sửa chửa thành thành công",
                    "category": "success"
                })
        except:
            return jsonify({
                "message": "Tạo phiếu thất bại vui lòng không chọn cùng 1 linh kiện trên cùng 1 phiếu",
                "category": "error"
            })

    @role_required(UserRole.TECHNICK)
    def index(self):
        args = request.args.to_dict()
        comps, vehicles, brands, selected_vehicle_name, selected_brand_name = get_components_data(args)
        comps_data = []
        for comp in comps:
            comps_data.append({
                'id': comp.id,
                'name': comp.name,
                'price': float(comp.price) if comp.price else 0,
                'brand_id': comp.brand_id,
                'vehicle_id': comp.vehicle_id
            })

            vehicles_data = []
            for vehicle in vehicles:
                vehicles_data.append({
                    'id': vehicle.id,
                    'name': vehicle.name
                })

            brands_data = []
            for brand in brands:
                brands_data.append({
                    'id': brand.id,
                    'name': brand.name
                })
        return render_template("repairform.html", page="Phiếu sửa xe",
                               comps=comps_data, vehicles=vehicles_data, brands=brands_data, current_args=args,
                               selected_vehicle_name=selected_vehicle_name,
                               selected_brand_name=selected_brand_name,
                               data=receptionform_util.get_receptionform(Form_status.WAIT_REPAIR),
                               state=receptionform_util.parse_state(),
                               Form_status=Form_status
                               )
