from datetime import datetime, date

from flask import Flask, render_template, request, jsonify, redirect, flash, abort
from flask_login import current_user
from app.middleware.authenticate import role_required
from app.models.model import UserRole
from app.dao import appointment_dao, dao


class AppointmentController:

    # [POST] api/appontment/limit
    def infoCustomer(self):
        return jsonify({
            "name": current_user.name,
            "phonenumber": current_user.phonenumber
        })

    def is_limit_reached(self):
        count = appointment_dao.countLimitVehicle()
        limit = appointment_dao.limitVehicle()
        return count >= limit

    # [POST] api/appontment/limit
    def limitVehicle(self):
        if self.is_limit_reached():
            return jsonify({
                "message": "Hôm nay đã đủ số lượng xe tiếp nhận!",
                "category": "error"
            }), 403
        return jsonify({
            "category": "success"
        }), 200

    # [POST] /APPOINTMENT/CREATE
    def receptionForm(self):
        if(request.method.__eq__("POST")):
            if self.is_limit_reached():
                flash("Đã đủ số lượng phiếu nhận trong ngày", "error")
                return redirect("/appointment")
            else:
                data = {
                    "name": request.form.get("name"),
                    "phonenumber": request.form.get("phone"),
                    "carnumber": request.form.get("car_number"),
                    "veType_id": request.form.get("vehicle_type"),
                    "description": request.form.get("description")
                }
                try:
                    mess = "cccccc"
                    if (current_user.is_authenticated and current_user.role.name == 'CUSTOMER'):
                        mess = "Tạo phiếu thành công đăng chờ nhân viên xét duyệt"
                        data["appointment_date"] = datetime.strptime(
                            f"{request.form.get("date")} {request.form.get("time")}",
                            "%Y-%m-%d %H:%M")

                    if (current_user.is_authenticated and current_user.role.name == 'STAFF'):
                        mess = "Tạo phiếu tiếp nhận thành công"
                        data["appointment_date"] = datetime.now()

                    appointment_dao.create_receptionForm(**data)
                    flash(mess, "success")
                    return redirect("/appointment")
                except:
                    flash("Có lỗi xảy ra!", "error")
                    return render_template("error.html")



    # [GET] /components
    @role_required(UserRole.CUSTOMER,UserRole.STAFF)
    def index(self):
        if (current_user.is_authenticated and current_user.role.name == 'STAFF'):
            tilte = "Tạo phiếu tiếp nhận"
        if (current_user.is_authenticated and current_user.role.name == 'CUSTOMER'):
            tilte = "Tạo phiếu đặt lịch sửa xe"

        today = date.today().strftime('%Y-%m-%d')
        return render_template("appointment.html", page="Đặt lịch sửa xe",tilte = tilte,vehicleType = dao.load_vehicletype(),today = today)


