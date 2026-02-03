function update_form() {
    const id = document.getElementById('modal_id2').value;
    const name = document.getElementById('modal_name2').value;
    const phone = document.getElementById('modal_phone2').value;
    const car = document.getElementById('modal_car2').value;
    const vehicle_type = document.getElementById('modal_typeVehicle2').value;

    const status = document.getElementById('modal_state2')?.value || document.getElementById('modal_state2_1')?.value;

    const appointment_date = document.getElementById('modal_date_book2').value;
    const description = document.getElementById('modal_description2').value;

    fetch(`/api/receptions/update/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            name: name,
            phone: phone,
            car: car,
            vehicle_type: vehicle_type,
            status: status,
            appointment_date: appointment_date,
            description: description
        })
    })
    .then(response => response.json())
    .then(data => {
        sessionStorage.setItem("toast_message", data.message);
        sessionStorage.setItem("toast_category", data.category);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Có lỗi xảy ra!');
    });
}

function deleteForm(id) {
    if(confirm("Bạn đã CHẮC CHƯA?")===true){
        fetch(`/api/receptions/remove/${id}`, {
            method: 'delete',
            headers: {
                "content-type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            sessionStorage.setItem("toast_message", data.message);
            sessionStorage.setItem("toast_category", data.category);
            window.location.reload();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Có lỗi xảy ra!');
        });
    }
}