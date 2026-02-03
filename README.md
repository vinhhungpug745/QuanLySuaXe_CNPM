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
```

---

## ⚙️ Installation & Run
1️⃣ Clone repository
git clone https://github.com/<your-username>/QuanLySuaXe_CNPM.git
cd QuanLySuaXe_CNPM

2️⃣ Tạo virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Cài đặt dependencies
pip install -r requirements.txt

4️⃣ Cấu hình biến môi trường

Tạo file .env tại thư mục gốc:

FLASK_SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://user:password@localhost/db_name
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret


⚠️ Không commit file .env lên GitHub.

5️⃣ Chạy project
python app/index.py

## 🔐 Security Notes

Không hard-code secret key, database password

Sử dụng biến môi trường để bảo mật thông tin

Đã cấu hình .gitignore để tránh push dữ liệu nhạy cảm

## 📚 What I Learned

Xây dựng RESTful API với Flask

Áp dụng mô hình MVC trong dự án thực tế

Tích hợp Google OAuth 2.0

Làm việc với MySQL và SQLAlchemy

Quản lý cấu hình bằng environment variables

Sử dụng Git & GitHub trong quá trình phát triển phần mềm

## 🚀 Future Improvements

Deploy hệ thống lên cloud (Render / Railway)

Thêm unit test & integration test

Cải thiện UI/UX

Phân quyền chi tiết theo vai trò

Tối ưu hiệu năng truy vấn database

👤 Author
Name: HungVinh
GitHub: https://github.com/vinhhungpug745
Email: vinhhungpug745@gmail.com
