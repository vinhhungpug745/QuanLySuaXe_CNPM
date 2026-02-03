from app.models.model import SystemParameters

def calc_labor_cost(repairform):
    total=0
    for rf in repairform:
        for c in rf.components:
            total+= c.cost
    return total

def calc_total_component(repairform):
    total=0
    for rf in repairform:
        for c in rf.components:
            total+= c.quantity * c.component.price
    return total

def calc_total_receipt(repairform):
    return calc_labor_cost(repairform) + calc_total_component(repairform)

def calc_total_VAT(repairform):
    params=SystemParameters.query.first()
    vat=params.VAT/100
    return calc_total_receipt(repairform)+calc_total_receipt(repairform)*vat