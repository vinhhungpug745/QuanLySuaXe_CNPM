let isDataLoaded = false;

function showToast(message, category = "success") {
    const toastId = `toast-api-${Date.now()}`;

    const headerClass =
        category === "success"
            ? "bg-success text-white"
            : "bg-danger text-white";

    const title =
        category === "success" ? "Thành công" : "Thất bại";

    const toastHtml = `
        <div id="${toastId}" class="toast position-fixed top-0 end-0 m-3"
             role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="10000">

            <div class="toast-header ${headerClass}">
                <strong class="me-auto">${title}</strong>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast"></button>
            </div>

            <div class="toast-body"
                 style="color:black;background:white;padding:15px;">
                ${message}
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML("beforeend", toastHtml);

    const toastEl = document.getElementById(toastId);
    const toast = new bootstrap.Toast(toastEl);
    toast.show();

    toastEl.addEventListener("hidden.bs.toast", () => toastEl.remove());
}

document.addEventListener("DOMContentLoaded", () => {
    const message = sessionStorage.getItem("toast_message");
    const category = sessionStorage.getItem("toast_category");

    if (message && category) {
        showToast(message, category);

        // Xóa để tránh hiện lại khi refresh
        sessionStorage.removeItem("toast_message");
        sessionStorage.removeItem("toast_category");
    }
});


function limitVehicleRender() {
    fetch('/api/appointment/limit', {method: 'GET'})
        .then(res => res.json()
        .then(data => ({ status: res.status, data })))
        .then(({ status, data }) => {
            if (status === 403) {
                sessionStorage.setItem("toast_message", data.message);
                sessionStorage.setItem("toast_category", data.category);
            }
        })
        .catch(err => {
            showToast("Có lỗi xảy ra khi kiểm tra giới hạn!", "error");
        });
}


function fillInfor() {
    if(!isDataLoaded){
        fetch('/api/appointment/info', {
            method: 'GET'
        })
        .then(res => res.json())
        .then(data => {
            document.querySelector(".fill-info-name").value = data.name;
            document.querySelector(".fill-info-phonenumber").value = data.phonenumber;
            isDataLoaded = true;
        });
    }
}


