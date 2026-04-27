# 🔐 Django Login System

A secure authentication system built using Django and Django REST framework with user registration, password hashing, and REST API support.

---

## 🚀 Features

* ✅ User Registration API
* ✅ Secure Password Hashing
* ✅ Username Validation
* ✅ Confirm Password Matching
* ✅ Django Admin Panel
* ✅ REST API Ready
* ✅ Clean Project Structure

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST framework
* SQLite
* PBKDF2 Authentication

---

## 📂 Project Structure

```bash id="5g0e1z"
login_system/
│── manage.py
│── db.sqlite3
│── app/
│── login_system/
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash id="35a59v"
git clone https://github.com/your-username/login_system.git
cd login_system
```

### Create Virtual Environment

```bash id="nuy3uk"
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash id="g8s02p"
pip install -r requirements.txt
```

### Run Migrations

```bash id="skh4m9"
python3 manage.py migrate
```

### Create Superuser

```bash id="87tvg0"
python3 manage.py createsuperuser
```

### Run Server

```bash id="jlwm5s"
python3 manage.py runserver
```

---

## 🔗 API Endpoints

### Register User

```http id="a7zpx5"
POST /api/register/
```

#### Request

```json id="cqj0w3"
{
  "username": "swapnanil",
  "email": "swap@gmail.com",
  "password": "StrongPass123",
  "password2": "StrongPass123"
}
```

---

## 🔒 Security

* Passwords stored as hashed values
* PBKDF2 + SHA256 hashing
* Strong password validation
* Duplicate username prevention

---

## 👨‍💻 Author

**Swapnanil Maity**

---

## ⭐ Support

If you like this project, give it a star ⭐
