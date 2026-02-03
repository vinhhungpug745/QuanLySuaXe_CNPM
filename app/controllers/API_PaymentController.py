from flask import request,jsonify,flash,url_for,redirect
from app.utils.receptionform_util import Form_status
from app.middleware.authenticate import role_required
from app.models.model import Receipt,UserRole
from app.utils import momo_util
from app._init_ import db


class API_PaymentController():

    @staticmethod
    def momo_pay(receipt_id):
        receipt = Receipt.query.get(receipt_id)
        if not receipt:
            return jsonify({"message": "Hóa đơn không tồn tại"}), 404

        amount = int(receipt.total_cost)
        order_info = f"Thanh toán hóa đơn #{receipt.id}"

        redirect_url = "http://127.0.0.1:5000/api/payment/momo/return"
        ipn_url = "http://127.0.0.1:5000/api/payment/momo/ipn"

        momo_res, order_id = momo_util.create_momo_payment(
            amount=amount,
            order_info=order_info,
            redirect_url=redirect_url,
            ipn_url=ipn_url
        )

        if momo_res.get("resultCode") == 0:
            receipt.momo_order_id = order_id
            db.session.commit()
            return jsonify({"payUrl": momo_res["payUrl"]})

        return jsonify({"message": momo_res.get("message", "MoMo error")}), 400

    @staticmethod
    def momo_return():
        result_code = request.args.get("resultCode")
        order_id = request.args.get("orderId")

        receipt = Receipt.query.filter_by(momo_order_id=order_id).first()

        if result_code == "0" and receipt:
            receipt.paid_by = "CUSTOMER_MOMO"

            updated_receptions = set()

            for rf in receipt.repair_forms:
                reception = rf.reception_form
                if reception and reception.id not in updated_receptions:
                    reception.status = Form_status.SUCCESS
                    updated_receptions.add(reception.id)

            db.session.commit()

            flash("Thanh toán thành công!", "success")
            return redirect(url_for(
                'payments_bp.index',
                receipt_id=receipt.id,
            ))

        return "Thanh toán MoMo thất bại"