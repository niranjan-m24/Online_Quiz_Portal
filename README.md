# 🧠 Online Quiz Portal (Django)

A simple and fully functional Online Quiz Portal built using Django.  
This project allows users to log in, attempt multiple-choice quizzes, and view their scores.  
The admin can dynamically manage quiz questions using the Django Admin Panel.

---

## 🚀 Features

- 🔐 User Authentication (Login System)
- 🛠 Admin Panel for Managing Questions
- ❓ Multiple Choice Questions (MCQs)
- 📊 Automatic Score Calculation
- 🗄 SQLite Database Integration
- 🧩 Django MVT Architecture

---

## 🛠 Tech Stack

- Python 3
- Django
- SQLite
- HTML
- Git & GitHub

---

## 📂 Project Structure

```
Online_Quiz_Portal/
│
├── manage.py
├── db.sqlite3
├── quiz/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/
│       ├── quiz/
│       └── registration/
│
└── quiz_portal/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/niranjan-m24/Online_Quiz_Portal.git
```

### 2️⃣ Navigate into Project

```bash
cd Online_Quiz_Portal
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install django
```

### 5️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧪 How It Works

1. Admin logs into `/admin/`
2. Adds quiz questions
3. User logs in
4. Attempts quiz
5. Score is calculated automatically
6. Result is stored in the database

---

## 🎯 Learning Outcomes

- Understanding Django MVT architecture
- Working with Django ORM
- Implementing Authentication System
- Managing Database Migrations
- Using Git & GitHub for Version Control

---

## 👨‍💻 Developed By

**Niranjan Muley**  
B.Tech CSE (AI & Data Science)  
GitHub: https://github.com/niranjan-m24

---

⭐ If you found this project useful, consider giving it a star!