from flask_login import current_user
from sqlalchemy import func
from app.models.model import *
from app._init_ import create_app,db
from datetime import datetime, date

def countLimitVehicle():
    return ReceptionForm.query.filter(ReceptionForm.status.__eq__(Form_status.WAIT_REPAIR),
                                      db.func.date(ReceptionForm.created_date) == datetime.today().date()).count()

def limitVehicle():
    return db.session.query(SystemParameters).first().limitcar


def create_receptionForm(
        name,
        phonenumber,
        carnumber,
        appointment_date,
        description,
        veType_id,
        customer_id=None,
        staff_id=None
):
    receptionForm = ReceptionForm(
        name=name,
        phonenumber=phonenumber,
        carnumber=carnumber,
        appointment_date=appointment_date,
        description=description,
        veType_id=veType_id,
        customer_id=customer_id,
        staff_id=staff_id
    )

    if (current_user.is_authenticated and current_user.role.name == 'CUSTOMER'):
        receptionForm.customer_id = current_user.id

    if(current_user.is_authenticated and current_user.role.name == 'STAFF'):
        receptionForm.staff_id = current_user.id
        receptionForm.status = Form_status.WAIT_REPAIR

    db.session.add(receptionForm)
    db.session.commit()

def update_status(id, status):
    try:
        form = ReceptionForm.query.get(id)
        form.status = status
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        db.session.rollback()
        return False

def update_appointment(
    id,
    name,
    phone,
    car,
    vehicle_type,
    status,
    appointment_date,
    description
):
    appointment = ReceptionForm.query.get(id)
    if appointment:
        appointment.name = name
        appointment.phonenumber = phone
        appointment.carnumber = car
        appointment.vehicle_type = vehicle_type
        appointment.status = status
        appointment.appointment_date = appointment_date
        appointment.description = description
        if (current_user.role.name == 'STAFF'):
            appointment.staff_id = current_user.id
        db.session.commit()
        return True
    else:
        return False

def delete_appointment(id):
    form = ReceptionForm.query.get(id)
    if form:
        db.session.delete(form)
        db.session.commit()
        return True
    return False

def get_dataStatisticalByVehicle():
    return db.session.query(
        Vehicletype.id,
        Vehicletype.name,
        func.count(ReceptionForm.id).label('total_receptions')
        ).join(
            ReceptionForm,
            ReceptionForm.veType_id == Vehicletype.id
        ).filter(
            ReceptionForm.status.__eq__(Form_status.SUCCESS)
        ).group_by(
            Vehicletype.id
        ).all()

def get_dataStatisticalByTime(date_from, date_to):
    return db.session.query(
        func.date(Receipt.created_date).label('date'),
        func.sum(
            RepairForms_Components.cost + (RepairForms_Components.quantity * Component.price)
        ).label('total_revenue')
        ).join(
            RepairForm,
            RepairForm.receipt_id == Receipt.id
        ).join(
            RepairForms_Components,
            RepairForms_Components.id_repair_form == RepairForm.id
        ).join(
            Component,
            Component.id == RepairForms_Components.id_component
        ).filter(
            Receipt.created_date >= date_from,
            Receipt.created_date <= date_to
        ).group_by(
            func.date(Receipt.created_date)).all()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(get_dataStatisticalByTime('2025-12-1'))