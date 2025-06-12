import mysql.connector as db
import getpass
import datetime
from tabulate import tabulate

class foodCourt:
    def __init__(self):
        self.datb = db.connect(
            host="localhost",
            user="root",
            password="root",
            database="foodcourt",
            auth_plugin="mysql_native_password"
        )
        self.admin_username = "Asher"
        self.admin_password = "Whynotasher"
        self.logged_customer = None

# ---------------------------- ADMIN LOGIN ----------------------------
    def admin_login(self):
        print("--- Admin Login ---")
        username = input("Enter Admin Username: ")
        password = getpass.getpass("Enter Admin Password: ")
        if username != self.admin_username or password != self.admin_password:
            print("Access Denied | Enter Username & Password Right")
            return
        admin = self.datb.cursor()
        while True:
            print("\n--- Admin Menu ---")
            print("1 : Add Food ")
            print("2 : View Menu ")
            print("3 : Delete Food Item ")
            print("4 : Exit/Admin-Menu")
            choice = int(input("Enter the choice : "))
            if choice == 1:
                name = input("Enter Food Name : ")
                price = float(input("Enter Price : "))
                category = input("Enter Category (e.g., Pizza, Drinks): ")
                subcategory = input("Enter Subcategory (e.g., Veg, Non-Veg): ")
                admin.execute("INSERT INTO food_items (name, price, category, subcategory) VALUES (%s, %s, %s, %s)",
                              (name, price, category, subcategory))
                self.datb.commit()
                print("Item added")
            elif choice == 2:
                admin.execute("SELECT * FROM food_items ORDER BY category, subcategory")
                record = admin.fetchall()
                headers = ["ID", "Name", "Price", "Category", "Subcategory"]
                table = [[row[0], row[1], f"₹{row[2]:.2f}", row[3], row[4]] for row in record]
                print(tabulate(table, headers=headers, tablefmt="grid"))
            elif choice == 3:
                item_id = int(input("Enter ID to delete Food Item : "))
                admin.execute("DELETE FROM food_items WHERE id = %s", (item_id,))
                self.datb.commit()
                print("Item Deleted !!!")
            elif choice == 4:
                break
            else:
                print("Enter Valid choice !!!")

# ---------------------------- CUSTOMER LOGIN ----------------------------
    def customer_register_login(self):
        cust = self.datb.cursor()
        print("---- Customer Login/Register ----")
        name = input("Enter Your Name: ")
        password = getpass.getpass("Enter Your Password: ")

        cust.execute("SELECT * FROM customers WHERE name = %s", (name,))
        existing = cust.fetchone()

        if existing:
            if existing[2] == password:
                self.logged_customer = name
                print(f"Welcome back, {name}!")
            else:
                print("Incorrect password. Try again.")
                self.logged_customer = None
        else:
            cust.execute("INSERT INTO customers (name, password) VALUES (%s, %s)", (name, password))
            self.datb.commit()
            self.logged_customer = name
            print("Account created successfully. You are logged in.")

# ---------------------------- CUSTOMER MENU ----------------------------
    def cust_menu(self):
        if not self.logged_customer:
            self.customer_register_login()
            if not self.logged_customer:
                return

        cust = self.datb.cursor()
        while True:
            print("\n---- Customer Menu ----") 
            print("1 : View Menu ")
            print("2 : Place Order ")
            print("3 : Exit")
            choice = int(input("Enter Choice : "))
            if choice == 1:
                cust.execute("SELECT * FROM food_items ORDER BY category, subcategory")
                record = cust.fetchall()
                headers = ["ID", "Name", "Price", "Category", "Subcategory"]
                table = [[row[0], row[1], f"₹{row[2]:.2f}", row[3], row[4]] for row in record]
                print(tabulate(table, headers=headers, tablefmt="grid"))
            elif choice == 2:
                name = self.logged_customer
                ordered_items = []

                while True:
                    item_id = input("Enter Food ID to order (or 'done' to finish): ")
                    if item_id.lower() == 'done':
                        break
                    if not item_id.isdigit():
                        print("Invalid ID. Please enter a number.")
                        continue

                    item_id = int(item_id)
                    cust.execute("SELECT name, price FROM food_items WHERE id = %s", (item_id,))
                    item = cust.fetchone()

                    if item:
                        ordered_items.append({
                            'id': item_id,
                            'name': item[0],
                            'price': item[1]
                        })
                    else:
                        print(f"Item ID {item_id} not found. Please try again.")

                if not ordered_items:
                    print("No items ordered. Exiting...")
                else:
                    order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    total = 0

                    print("\n--- Bill ---")
                    print(f"Customer Name : {name}")
                    order_table = []
                    for food in ordered_items:
                        cust.execute(
                            "INSERT INTO orders (customer_name, item_id, order_time) VALUES (%s, %s, %s)",
                            (name, food['id'], order_time)
                        )
                        order_table.append([food['name'], f"₹{food['price']:.2f}"])
                        total += food['price']

                    self.datb.commit()
                    print(tabulate(order_table, headers=["Item", "Price"], tablefmt="fancy_grid"))
                    print(f"Total Price   : ₹{total:.2f}")
                    print(f"Order Time    : {order_time}")
                    print("Thank you for your order!")
            elif choice == 3:
                self.logged_customer = None
                break
            else:
                print("Invalid Choice!!!")

# ---------------------------- RUN PROJECT ----------------------------
    def run_project(self):
        while True:
            print("\n---- Enter Choice ----")
            print("1 : Admin Login ")
            print("2 : Customer ")
            print("3 : Exit")
            choice = int(input("Enter Choice : "))
            if choice == 1:
                self.admin_login()
            elif choice == 2:
                self.cust_menu()
            elif choice == 3:
                print("Visit Again")
                break
            else:
                print("Invalid Choice")

fc = foodCourt()
fc.run_project()
