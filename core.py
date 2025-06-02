import mysql.connector as db
import getpass
import datetime

class foodCourt:
    # Database Connection 
    def __init__(self):
        self.datb = db.connect(
            host="localhost",
            user="root",
            password="root",
            database="foodcourt",
            auth_plugin="mysql_native_password"
        )
        # Admin Cardinel
        self.admin_username = "Asher"
        self.admin_password = "Whynotasher"
        
    # Admin Login 
    def admin_login(self):
        print("--- Admin Login ---")
        # Admin Cardinel check
        username = input("Enter Admin Username: ")
        password = getpass.getpass("Enter Admin Password: ")
        if username != self.admin_username or password != self.admin_password:
            print("Access Denied | Enter Username & Password Right")
            return
        admin = self.datb.cursor()
        while True:
            print("\n--- Admin Menu ---")
            print("1 : Add Food")
            print("2 : View Menu")
            print("3 : Delete Food Item")
            print("4 : View Order List")
            print("5 : Exit/Admin-Menu")
            choice = int(input("Enter the choice : "))
            # Add Food To Menu 
            if choice == 1:
                name = input("Enter Food Name : ")
                price = float(input("Enter Price : "))
                admin.execute("INSERT INTO food_items (name, price) VALUES (%s, %s)", (name, price))
                self.datb.commit()
                print("Item added.")
            # View Menu
            elif choice == 2:
                admin.execute("SELECT * FROM food_items")
                record = admin.fetchall()
                print("ID | Name | Price")
                for row in record:
                    print(f"{row[0]} | {row[1]} | ₹{row[2]:.2f}")
            # Delete Food From menu
            elif choice == 3:
                item_id = int(input("Enter ID to delete Food Item : "))
                admin.execute("DELETE FROM food_items WHERE id = %s", (item_id,))
                self.datb.commit()
                print("Item Deleted.")
            # View Order List
            elif choice == 4:
                admin.execute("SELECT * FROM order_list ORDER BY order_time DESC")
                orders = admin.fetchall()
                print("Order ID | Customer Name | Item Name | Price | Time")
                for order in orders:
                    print(f"{order[0]} | {order[1]} | {order[2]} | ₹{order[3]:.2f} | {order[4]}")
            # Exit
            elif choice == 5:
                break
            else:
                print("Enter Valid choice!")

    def cust_menu(self):
        cust = self.datb.cursor()
        while True:
            print("\n---- Customer Menu ----") 
            print("1 : View Menu")
            print("2 : Place Order")
            print("3 : Exit")
            choice = int(input("Enter Choice : "))
            # View Menu
            if choice == 1:
                cust.execute("SELECT * FROM food_items")
                record = cust.fetchall()
                print("ID | Name | Price")
                for row in record:
                    print(f"{row[0]} | {row[1]} | ₹{row[2]:.2f}")
            # Place order       
            elif choice == 2:
                name = input("Please Enter Your Name: ")
                if not name.isalpha():
                    print("Name must contain only alphabetic characters.")
                    return
                ordered_items = []
                cust.execute("SELECT * FROM food_items")
                record = cust.fetchall()
                print("ID | Name | Price")
                for row in record:
                    print(f"{row[0]} | {row[1]} | ₹{row[2]:.2f}")
                while True:
                    item_id = input("Enter Food ID to order (or 'done' to finish): ")
                    if item_id.lower() == 'done':
                        break
                    try:
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
                    except ValueError:
                        print("Invalid input. Please enter a valid ID or 'done'.")

                if not ordered_items:
                    print("No items ordered. Exiting...")
                else:
                    order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    total = 0
                    # Bill Printing
                    print("\n--- Bill ---")
                    print(f"Customer Name : {name}")
                    print("Items Ordered:")
                    for food in ordered_items:
                        cust.execute(
                            "INSERT INTO orders (customer_name, item_id, order_time) VALUES (%s, %s, %s)",
                            (name, food['id'], order_time)
                        )
                        cust.execute(
                            "INSERT INTO order_list (customer_name, item_name, item_price, order_time) VALUES (%s, %s, %s, %s)",
                            (name, food['name'], food['price'], order_time)
                        )
                        print(f"  - {food['name']}: ₹{food['price']:.2f}")
                        total += food['price']
                    self.datb.commit()
                    print("---------------------")
                    print(f"Total Price   : ₹{total:.2f}")
                    print(f"Order Time    : {order_time}")
                    print("Thank you for your order!")
            # Exit
            elif choice == 3:
                break
            else:
                print("Invalid Choice!")

    def run_project(self):
        while True:
            print("\n---- Enter Choice ----")
            print("1 : Admin Login")
            print("2 : Customer")
            print("3 : Exit")
            choice = int(input("Enter Choice : "))
            if choice == 1:
                self.admin_login()
            elif choice == 2:
                self.cust_menu()
            elif choice == 3:
                print("Visit Again!")
                break
            else:
                print("Invalid Choice!")

# Run the program
fc = foodCourt()
fc.run_project()
