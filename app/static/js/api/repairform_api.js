document.getElementById('repair-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const receptionFormId = formData.get('receptionform_id');

    // Parse items từ FormData
    const items = [];
    const formObject = Object.fromEntries(formData.entries());

    // Tìm tất cả các index của items
    let index = 0;
    while (formObject[`items[${index}][action]`] !== undefined) {
        items.push({
            action: formObject[`items[${index}][action]`],
            cost: parseInt(formObject[`items[${index}][cost]`]),
            component_id: parseInt(formObject[`items[${index}][component_id]`]),
            quantity: parseInt(formObject[`items[${index}][quantity]`])
        });
        index++;
    }

    // Tạo JSON
    const jsonData = {
        receptionform_id: parseInt(receptionFormId),
        items: items
    };

    fetch('/api/repairform/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        sessionStorage.setItem("toast_message", data.message);
        sessionStorage.setItem("toast_category", data.category);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Có lỗi xảy ra khi lưu dữ liệu!');
    });
});