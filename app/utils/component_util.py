from app.dao import dao


def get_components_data(args,  page=None):
    q = args.get('q')
    vehicle_id = args.get("vehicle_id")
    brand_id = args.get("brand_id")

    comps = dao.load_component(q=q, vehicle_id=vehicle_id, brand_id=brand_id, page = page)
    vehicles = dao.load_vehicletype()
    brands = dao.load_brandveghicle()

    selected_vehicle_name = "Loại linh kiện"
    if vehicle_id and vehicle_id.isdigit():
        selected_vehicle = next((c for c in vehicles if c.id == int(vehicle_id)), None)
        if selected_vehicle:
            selected_vehicle_name = selected_vehicle.name

    selected_brand_name = "Hãng linh kiện"
    if brand_id and brand_id.isdigit():
        selected_brand = next((b for b in brands if b.id == int(brand_id)), None)
        if selected_brand:
            selected_brand_name = selected_brand.name

    return comps, vehicles, brands, selected_vehicle_name, selected_brand_name
