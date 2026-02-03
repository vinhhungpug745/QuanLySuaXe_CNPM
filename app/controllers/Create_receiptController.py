from flask import Flask, render_template,request,jsonify,abort,send_file
from datetime import datetime
import app.dao.dao as dao
from app.middleware.authenticate import role_required
from app.models.model import RepairForm, Receipt, SystemParameters, UserRole
from flask_login import current_user, login_required
from app._init_ import db
from app.utils import receptionform_util,calc_total_repairform

class Create_receiptController:

    @role_required(UserRole.ACCOUNTANT)
    def index(self):
        q = request.args.get("q")
        rp_f=dao.get_repair_form(q=q)
        vat=dao.get_VAT()
        return render_template("create_receipts.html",
                               page="Lập hóa đơn",rp_f=rp_f,
                               state=receptionform_util.parse_state(),
                               vat=vat)

    def create_receipt(self):
        data = request.get_json()
        repair_form_ids = data.get("repair_form_ids", [])

        if not repair_form_ids:
            return jsonify({"error": "Chưa chọn phiếu sửa"}), 400

        repair_forms = RepairForm.query.filter(
            RepairForm.id.in_(repair_form_ids),
            RepairForm.receipt_id == None
        ).all()

        if not repair_forms:
            return jsonify({"error": "Phiếu sửa không hợp lệ"}), 400

        total_component_cost = calc_total_repairform.calc_total_component(repair_forms)
        total_labor_cost=calc_total_repairform.calc_labor_cost(repair_forms)
        total_cost = calc_total_repairform.calc_total_VAT(repair_forms)

        customer_id = repair_forms[0].reception_form.customer_id
        if customer_id is None:
            paid_by="STAFF"
        else:
            paid_by=""

        receipt = Receipt(
            total_labor_cost=total_labor_cost,
            total_component_cost=total_component_cost,
            total_cost=total_cost,
            paid_by=paid_by,
            customer_id=customer_id,
            accountant_id=current_user.id,
            created_date=datetime.now()
        )

        db.session.add(receipt)
        db.session.flush()

        for rf in repair_forms:
            rf.receipt_id = receipt.id

        updated_receptions = set()

        for rf in repair_forms:
            reception = rf.reception_form
            if reception.id not in updated_receptions:
                if reception.customer_id is None:
                    reception.status = receptionform_util.Form_status.SUCCESS
                else:
                    reception.status = receptionform_util.Form_status.REPAIRED_WAIT_PAY
                updated_receptions.add(reception.id)

        db.session.commit()

        return jsonify({
            "receipt_id": receipt.id,
            "total_labor_cost": total_labor_cost,
            "total_component_cost": total_component_cost
        })





