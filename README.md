Here's a `README.md` file you can use for your **Food Court Management System** project on GitHub:

---

# 🥘 Food Court Management System (Python + MySQL)

This is a simple **command-line based food court management system** built with **Python** and **MySQL**. It includes two user roles: **Admin** and **Customer**, with features for managing food items, placing orders, and viewing sales.

---

## 🚀 Features

### 👨‍💼 Admin Panel

* Secure admin login
* Add food items
* View current menu
* Delete food items
* View customer orders

### 🧑‍🍽️ Customer Panel

* Browse menu
* Place multiple orders
* See itemized bill with total and timestamp

---

## 🛠️ Requirements

* Python 3.x
* MySQL Server (Running locally)
* Python MySQL Connector:

```bash
pip install mysql-connector-python
```

---

## 🧱 MySQL Database Setup

### Database: `foodcourt`

```sql
CREATE DATABASE foodcourt;
USE foodcourt;

CREATE TABLE food_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    item_id INT,
    order_time DATETIME
);

CREATE TABLE order_list (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    item_name VARCHAR(100),
    item_price FLOAT,
    order_time DATETIME
);
```

---

## 🔑 Admin Credentials

| Username | Password      |
| -------- | ------------- |
| `Asher`  | `Whynotasher` |

> ⚠️ Credentials are hardcoded in the script. Consider externalizing for better security.

---

## 📦 How to Run

1. Make sure your MySQL server is running and database is set up.
2. Update MySQL credentials in the script if needed:

```python
host="localhost"
user="root"
password="root"
```

3. Run the script:

```bash
python foodcourt.py
```

---

## 🧪 Sample Flow

```
---- Enter Choice ----
1 : Admin Login
2 : Customer
3 : Exit

# Admin can add, view, or delete food items and see orders.

# Customers can:
- View menu
- Order items by ID
- See total bill
```

---

## ✅ To-Do / Improvements

* [ ] Password encryption
* [ ] GUI interface
* [ ] Inventory tracking
* [ ] Login system for customers
* [ ] Session-based ordering

---

