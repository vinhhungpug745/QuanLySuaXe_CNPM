# 🚗 Quản Lý Sửa Xe – Vehicle Repair Management System

Hệ thống quản lý sửa chữa xe dành cho gara, hỗ trợ quản lý khách hàng, lịch hẹn,
quy trình sửa chữa, hóa đơn, thanh toán và thống kê doanh thu.

Dự án được xây dựng nhằm mô phỏng một hệ thống quản lý thực tế, phù hợp cho
mục đích học tập, thực hành và đưa vào CV xin việc / thực tập Backend.

---

## 📸 Demo
- 🔗 Live demo: (đang cập nhật)
- 📷 Screenshots: (đang cập nhật)

---

## ✨ Features
- 🔐 Đăng nhập & xác thực người dùng
- 🔑 Đăng nhập bằng Google OAuth 2.0
- 👤 Quản lý khách hàng
- 📅 Quản lý lịch hẹn sửa xe
- 🧾 Tạo và xuất hóa đơn sửa chữa
- 💳 Quản lý thanh toán
- 📊 Thống kê & báo cáo
- 🛠 Phân quyền người dùng (Admin / User)

---

## 🛠 Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: Google OAuth 2.0
- **PDF Export**: ReportLab
- **Other Services**: Cloudinary
- **Version Control**: Git & GitHub

---

## 📂 Project Structure
```text
QuanLySuaXe_CNPM/
├── app/
│   ├── controllers/      # Xử lý logic nghiệp vụ
│   ├── dao/              # Data Access Object
│   ├── data/             # Dữ liệu mẫu / hỗ trợ
│   ├── middleware/       # Middleware
│   ├── models/           # Database models
│   ├── routes/           # Routing / API
│   ├── utils/            # Tiện ích dùng chung
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JS, images
│   ├── __init__.py
│   ├── admin.py
│   └── index.py
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes

