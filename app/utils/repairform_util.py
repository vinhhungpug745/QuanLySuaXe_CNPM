from calendar import monthrange

from app._init_ import db
from app.dao import repairform_dao,appointment_dao
from app.models.model import Form_status


def createRepairform(data):
    try:
        receptionform_id = data.get('receptionform_id')
        items = data.get('items', [])
        repair_form = repairform_dao.create_repair_form(receptionform_id)
        for item in items:
            repairform_dao.create_repair_component(
                id_repair_form=repair_form.id,
                id_component=item['component_id'],
                quantity=item['quantity'],
                action=item['action'],
                cost=item['cost']
            )
        return appointment_dao.update_status(receptionform_id,status=Form_status.REPAIRED_WAIT_PAY)

    except Exception as e:
        print(f"Error: {e}")
        db.session.rollback()
        return False

def get_month_range(year_month):
    year, month = map(int, year_month.split('-'))

    first_day = f"{year}-{month:02d}-01"

    last_day_num = monthrange(year, month)[1]
    last_day = f"{year}-{month:02d}-{last_day_num}"

    return first_day, last_day
