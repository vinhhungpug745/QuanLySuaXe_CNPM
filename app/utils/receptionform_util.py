from flask import current_app
from flask_login import current_user

from app.dao import receptionform_dao
from app.models.model import Form_status
from app._init_ import create_app

def get_receptionform(status, page=None):
    if (current_user.role.name == 'CUSTOMER'):
        data = receptionform_dao.receptionFormCustomer(current_user.id,status)
    else:
        data = receptionform_dao.load_receptionForm()
        if status:
            data = receptionform_dao.receptionFormUserState(status)

    if page:
        size = current_app.config["PAGE_SIZE"]
        start = (int(page) - 1) * size
        end = start + size
        data = data[start:end]
    return data

def parse_state():
    FORM_STATUS_VI = {
        Form_status.WAIT_APPROVAL: "Chờ duyệt",
        Form_status.REFUSE: "Từ chối",
        Form_status.WAIT_REPAIR: "Chờ sửa chữa",
        Form_status.REPAIRED_WAIT_PAY: "Hoàn thành Chờ thanh toán",
        Form_status.SUCCESS: "Hoàn thành"
    }
    return FORM_STATUS_VI


