# Loan Eligibility Management System

A Django-based Loan Eligibility Management System that allows administrators to manage loan products, customers, and automatically evaluate customer eligibility based on predefined loan criteria.

---

## 🚀 Features

- User Login Authentication
- Admin Dashboard
- Loan Product Management (CRUD)
- Customer Management (CRUD)
- Automatic Loan Eligibility Calculation
- Eligibility Report Generation
- MySQL Database Support
- Bootstrap 5 Responsive UI

---

## 🛠 Technology Stack

- Python 3.x
- Django 6
- MySQL
- Bootstrap 5
- HTML5
- CSS3
- Git & GitHub

---

## 📂 Project Structure

```
Loan/
│
├── accounts/
├── dashboard/
├── eligibility/
├── products/
├── users_directory/
│
├── templates/
├── static/
├── Loan/
├── manage.py
└── README.md
```

---

## Modules

### 1. Authentication

- Login
- Logout
- Admin Access

---

### 2. Dashboard

- Total Customers
- Total Products
- Eligible Customers
- Not Eligible Customers

---

### 3. Product Management

- Add Product
- Update Product
- Delete Product
- Product List

---

### 4. Customer Management

- Add Customer
- Edit Customer
- Delete Customer
- Customer List

---

### 5. Eligibility Engine

The system checks:

- Minimum Age
- Maximum Age
- Minimum Salary
- Credit Score
- Employment Type
- Salary Type

If all conditions match:

Eligible

Otherwise:

Not Eligible

Reason is also stored.

---

## Database

MySQL

Tables

- auth_user
- products_product
- users_directory_customer
- users_directory_eligibilityresult

---

## Installation

Clone Repository

```bash
git clone https://github.com/yourusername/loan-eligibility-management.git
```

Move to project

```bash
cd loan-eligibility-management
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

---

## Login

Admin URL

```
http://127.0.0.1:8000/admin/
```

Application Login

```
http://127.0.0.1:8000/accounts/login/
```

---

## Future Improvements

- Role Based Login
- PDF Report Download
- Excel Export
- Search & Filter
- Email Notification
- REST API
- Charts & Analytics

---

## Author

Amit Prasad


