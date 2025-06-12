# 🍔 Food Court Management System

A simple command-line-based food ordering and management system built using **Python** and **MySQL**.

---

## 📋 Features

### 👨‍💼 Admin Panel
- Secure admin login
- Add new food items
- View complete food menu
- Delete food items by ID

### 🧑 Customer Panel
- Register or login with username & password
- Browse menu
- Place food orders
- View detailed bill (with total and timestamp)

---

## 🛠️ Technologies Used

- **Python 3**
- **MySQL** (with `mysql-connector-python`)
- `getpass` for secure password input
- `tabulate` for tabular data display in the terminal

---

## 🗂️ Database Setup

1. Open your MySQL client or CLI.
2. Run the following SQL script to create required tables:

```sql
CREATE DATABASE IF NOT EXISTS foodcourt;
USE foodcourt;

CREATE TABLE IF NOT EXISTS food_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50),
    subcategory VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    item_id INT,
    order_time DATETIME,
    FOREIGN KEY (item_id) REFERENCES food_items(id),
    FOREIGN KEY (customer_name) REFERENCES customers(name) ON DELETE SET NULL
);
````

---

## 💻 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/foodcourt.git
   cd foodcourt
   ```

2. Install required Python libraries:

   ```bash
   pip install mysql-connector-python tabulate
   ```

3. Update your MySQL credentials in `foodCourt` class (if needed):

   ```python
   self.datb = db.connect(
       host="localhost",
       user="root",
       password="root",  # <- change if needed
       database="foodcourt"
   )
   ```

4. Run the application:

   ```bash
   python foodcourt.py
   ```

---

## 🔐 Default Admin Credentials

* **Username:** Asher
* **Password:** Whynotasher

> You can change these in the `foodCourt.__init__()` method.

---

## 📌 Future Improvements

* Password hashing (bcrypt or passlib)
* GUI version with Tkinter or Flask
* Order history for customers
* Search/filter menu items

---

