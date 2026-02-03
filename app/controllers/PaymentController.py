from flask import Flask, render_template, request, flash, redirect, url_for,abort,send_file
from flask_login import current_user, login_required

import app.dao.dao as dao
from app.utils.receptionform_util import Form_status
from app._init_ import db
from app.middleware.authenticate import role_required
from app.models.model import UserRole


class PaymentController():
    @role_required(UserRole.CUSTOMER)
    @login_required
    def index(self):
        receipt = dao.get_my_unpaid_receipt(current_user.id)
        vat = dao.get_VAT()
        # POST = xác nhận thanh toán
        # if request.method == 'POST':
        #     try:
        #         receipt.paid_by = "CUSTOMER"
        #
        #         updated_receptions = set()
        #
        #         for rf in receipt.repair_forms:
        #             reception = rf.reception_form
        #             if reception and reception.id not in updated_receptions:
        #                 reception.status = Form_status.SUCCESS
        #                 updated_receptions.add(reception.id)
        #
        #         db.session.commit()
        #
        #         flash("Thanh toán thành công!", "success")
        #         return redirect(url_for(
        #             'payments_bp.index',
        #             receipt_id=receipt.id,
        #         ))
        #     except Exception as e:
        #         db.session.rollback()
        #         flash("Lỗi khi thanh toán, vui lòng thử lại", "danger")

        return render_template("payment.html", page="Thanh toán", receipt=receipt,vat=vat)
