from flask_login import current_user
from app._init_ import db
from app.models.model import RepairForm, Form_status, RepairForms_Components


def create_repair_form(reception_form_id):
    try:
        repair_form = RepairForm(
            technick_id=current_user.id,
            reception_form_id=reception_form_id,
            receipt_id=None
        )

        db.session.add(repair_form)
        db.session.flush()

        return repair_form

    except Exception as e:
        print(f"Error in create_repair_form: {e}")
        raise


def create_repair_component(id_repair_form, id_component, quantity, action, cost):

    try:
        component = RepairForms_Components(
            id_repair_form=id_repair_form,
            id_component=id_component,
            quantity=quantity,
            action=action,
            cost=cost
        )

        db.session.add(component)

        return component

    except Exception as e:
        print(f"Error in create_repair_component: {e}")
        raise