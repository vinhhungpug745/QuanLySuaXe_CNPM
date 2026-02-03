import hashlib, json

from app.models.model import Vehicletype, BrandVehicle, User, Component, UserRole, RepairForm, ReceptionForm,Receipt,Form_status,SystemParameters
from flask import current_app
from app._init_ import create_app,db
from sqlalchemy import or_

def load_vehicletype():
    # with open("data/category.json", 'r', encoding='utf-8') as f:
    #     return json.load(f)
    return Vehicletype.query.all()

def load_brandveghicle():
    return BrandVehicle.query.all()

def count_product():
    return Component.query.count()

def load_component(q=None, vehicle_id=None, brand_id=None,page=None):
    # with open("data/component.json", 'r', encoding='utf-8') as f:
    #     component = json.load(f)
    #     if q:
    #         component = [c for c in component if c["name"].find(q)>=0]
    #     if vehicle_id:
    #         component = [c for c in component if c["cate_id"].__eq__(int(vehicle_id))]
    #     if brand_id:
    #         component = [c for c in component if c["brand_id"].__eq__(int(brand_id))]
    #     return component
    query = Component.query
    if q:
        query = query.filter(Component.name.contains(q))

    if vehicle_id:
        query = query.filter(Component.vehicle_id.__eq__(int(vehicle_id)))

    if brand_id:
        query = query.filter(Component.brand_id.__eq__(int(brand_id)))

    if page:
        size = current_app.config["PAGE_SIZE"]
        start = (int(page) - 1) * size
        query = query.slice(start, (start + size))

    return query.all()

def add_user(name, phonenumber =None ,username =None, password =None, email = None, **kwargs):
    if password: password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(
        name=name.strip(),
        phonenumber=phonenumber.strip() if phonenumber else None,
        username=username.strip() if username else None,
        password=password if password else None,
        email=email.strip() if email else None,
        avatar=kwargs.get("avatar")
    )
    db.session.add(user)
    db.session.commit()

def check_userEmail(email):
    return User.query.filter(User.email == email).first()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

# lấy phiếu sửa chữa
def get_repair_form(q=None):
    query = RepairForm.query.join(RepairForm.reception_form)

    if q:
        query = query.filter(ReceptionForm.name.ilike(f"%{q}%"))

    return query.all()

# Lấy phiếu tiếp nhận
def get_reception_form():
    return ReceptionForm.query.all()


def load_repairform_receptionform(q=None):
    query = RepairForm.query.join(RepairForm.reception_form)

    if q:
        query = query.filter(
            or_(
                ReceptionForm.name.contains(q),
                ReceptionForm.phonenumber.contains(q),
                ReceptionForm.carnumber.contains(q)
            )
        )

    return query.all()
#lấy vat
def get_VAT():
    return SystemParameters.query.first()

#Lấy hóa đơn
def get_receipt_by_id(receipt_id):
    return Receipt.query.get(receipt_id)

def get_receipt_success(q=None):
    query = (
        Receipt.query
        .join(Receipt.repair_forms)
        .join(RepairForm.reception_form)
        .filter(ReceptionForm.status == Form_status.SUCCESS)
    )

    if q:
        query = query.filter(
            ReceptionForm.name.ilike(f"%{q}%")
        )

    return query.all()



def get_unpaid_receipt(receipt_id, customer_id):
    return Receipt.query.filter(
        Receipt.id == receipt_id,
        Receipt.status == Form_status.REPAIRED_WAIT_PAY,
        Receipt.customer_id == customer_id
    ).first()

def get_my_unpaid_receipt(customer_id):
    return (
        Receipt.query
        .join(Receipt.repair_forms)
        .join(RepairForm.reception_form)
        .filter(
            ReceptionForm.status == Form_status.REPAIRED_WAIT_PAY,
            Receipt.customer_id == customer_id
        ).first()
    )


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(get_my_unpaid_receipt(1))

