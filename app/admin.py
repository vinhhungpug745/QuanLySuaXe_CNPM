from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash

from app.middleware.authenticate import role_required
from app.models.model import Component, Vehicletype, BrandVehicle, UserRole, User, SystemParameters


class AdminBaseView:
    def is_accessible(self):
        return (
            current_user.is_authenticated
            and current_user.role == UserRole.ADMIN
        )

    def inaccessible_callback(self, name, **kwargs):
        flash("Bạn không phải ADMIN", "error")
        return redirect("/")

class MyAdminIndexView(AdminBaseView, AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

class AdminSecureView(ModelView):
    pass

class ComponentAdminView(AdminSecureView):
    # Giống file mẫu - KHÔNG dùng column_formatters
    column_list = ['id', 'name', 'price', 'vehicletype', 'brandvehicle']

    column_labels = {
        'id': 'ID',
        'name': 'Tên linh kiện',
        'price': 'Giá',
        'vehicletype': 'Loại xe',
        'brandvehicle': 'Hãng xe'
    }

    column_searchable_list = ['name']


class UserAdminView(AdminSecureView):
    column_list = ['id', 'name', 'username', 'phonenumber', 'role', 'active', 'joined']

    column_labels = {
        'id': 'ID',
        'name': 'Họ tên',
        'username': 'Tên đăng nhập',
        'phonenumber': 'Số điện thoại',
        'role': 'Vai trò',
        'active': 'Hoạt động',
        'joined': 'Ngày tham gia',
        'avatar': 'Ảnh đại diện',
        'password': 'Mật khẩu'
    }

    column_searchable_list = ['name', 'username', 'phonenumber']
    form_excluded_columns = ['password', 'reception_forms_as_customer',
                             'reception_forms_as_staff', 'repair_form',
                             'receipts_as_customer', 'receipts_as_accountant']

    column_exclude_list = ['password']

    column_formatters = {
        'joined': lambda v, c, m, p: m.joined.strftime('%d/%m/%Y %H:%M') if m.joined else ''
    }

class SystemParametersAdminView(AdminSecureView):
    column_list = ['id', 'VAT', 'limitcar']

    column_labels = {
        'id': 'ID',
        'VAT': 'VAT (%)',
        'limitcar': 'Giới hạn xe'
    }

    can_create = False
    can_delete = False

    column_descriptions = {
        'VAT': 'Thuế VAT tính theo phần trăm (%)',
        'limitcar': 'Số lượng xe tối đa cho phép tiếp nhận trong ngày'
    }

def init_admin(app, db):
    from flask_admin.theme import Bootstrap4Theme

    admin = Admin(
        app=app,
        name='SUA XE 3TL',
        index_view=MyAdminIndexView(),
        theme=Bootstrap4Theme()
    )

    # BỎ endpoint - để Flask-Admin tự generate
    admin.add_view(ComponentAdminView(Component, db.session, name='Linh kiện'))
    admin.add_view(UserAdminView(User, db.session, name='Người dùng'))
    admin.add_view(SystemParametersAdminView(SystemParameters, db.session, name='Tham số hệ thống'))
    return admin