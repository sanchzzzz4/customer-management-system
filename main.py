import sqlite3
from prettytable import PrettyTable

# Connect to the database (or create one if it doesn't exist)
connection = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()
print('Cursor opened')

class Customer_Operations:
    phone=age=0
    name=email=location=""
    def insert_customer_detials(self,cursor):
        name=input('Enter Customer Name:')
        phone=input("Enter customer contact number:")
        email=input('Enter Customer email:')
        location=input("Enter location:")
        age=input("Enter customer age:")

        query="""insert into Customers(name,phone,email,location,age) values(?,?,?,?,?)"""
        cursor.execute(query,(name,phone,email,location,age))
        print('Customer details added successfully')
    
    def display_record(self,cursor,name):
        query="select * from Customers where name like '{}%'".format(name)
        result=cursor.execute(query)
        if not result:print('No infomation found')
        col_name=[description[0] for description in cursor.description]
        table=PrettyTable()
        table.field_names=col_name

        for row in result:
            table.add_row(row)
        print(table)
    
    def display_records(self, cursor):
        query = "SELECT * FROM Customers"
        cursor.execute(query)  # Executes the SQL query to fetch all records
        results = cursor.fetchall()  # Fetches all rows from the query result

        if results:
            print("Displaying all customer records:\n")
            col_name=[description[0] for description in cursor.description]
            table=PrettyTable()
            table.field_names=col_name

            for row in results:
                table.add_row(row)
            print(table)
        else:
            print("No records found in the Customers table.")

        
class Product_Operations:
    id = 0
    name, description = "", ""
    price = 0.0
    stock = 0

    def insert_product_details(self, cursor):
        name = input("Enter Product Name: ")
        description = input("Enter Product Description: ")
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock: "))

        query = """
        INSERT INTO Products (name, description, price, stock)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (name, description, price, stock))
        print("Product details added successfully.")

    def view_all_products(self, cursor):
        query = "SELECT * FROM Products"
        cursor.execute(query)
        products = cursor.fetchall()
        print("Product List:")
        if product:
            col_name=[description[0] for description in cursor.description]
            table=PrettyTable()
            table.field_names=col_name
            for row in products:
                table.add_row(row)
            print(table)


class Purchase_Operations:
    id, customer_id, product_id, quantity = 0, 0, 0, 0
    total_price = 0.0

    def record_purchase(self, cursor):
        customer_id = int(input("Enter Customer ID: "))
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))

        # Fetch product price
        cursor.execute("SELECT price, stock FROM Products WHERE id = ?", (product_id,))
        product = cursor.fetchone()

        if product is None:
            print("Invalid Product ID.")
            return

        price, stock = product
        if quantity > stock:
            print("Not enough stock available.")
            return

        total_price = price * quantity

        # Insert purchase record
        query = """
        INSERT INTO Purchases (customer_id, product_id, quantity, total_price)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (customer_id, product_id, quantity, total_price))

        # Update product stock
        cursor.execute(
            "UPDATE Products SET stock = stock - ? WHERE id = ?", (quantity, product_id)
        )
        print("Purchase recorded successfully.")

    def view_purchases(self, cursor):
        query = """
        SELECT p.id, c.name AS customer_name, pr.name AS product_name, p.quantity, p.total_price, p.purchase_date
        FROM Purchases p
        JOIN Customers c ON p.customer_id = c.id
        JOIN Products pr ON p.product_id = pr.id
        """
        cursor.execute(query)
        purchases = cursor.fetchall()
        if purchases:
            col_name=[description[0] for description in cursor.description]
            table=PrettyTable()
            table.field_names=col_name
            for row in purchases:
                table.add_row(row)
            print(table)
        


class Feedback_Operations:
    id, customer_id, rating = 0, 0, 0
    feedback_text = ""

    def submit_feedback(self, cursor):
        customer_id = int(input("Enter Customer ID: "))
        feedback_text = input("Enter Feedback: ")
        rating = int(input("Enter Rating (1-5): "))

        if rating < 1 or rating > 5:
            print("Invalid rating. Please enter a value between 1 and 5.")
            return

        query = """
        INSERT INTO Feedback (customer_id, feedback_text, rating)
        VALUES (?, ?, ?)
        """
        cursor.execute(query, (customer_id, feedback_text, rating))
        print("Feedback submitted successfully.")

    def view_feedback(self, cursor):
        query = """
        SELECT f.id, c.name AS customer_name, f.feedback_text, f.rating, f.submitted_at
        FROM Feedback f
        JOIN Customers c ON f.customer_id = c.id
        """
        cursor.execute(query)
        feedbacks = cursor.fetchall()
        if feedbacks:
            col_name=[description[0] for description in cursor.description]
            table=PrettyTable()
            table.field_names=col_name
            for row in feedbacks:
                table.add_row(row)
            print(table)


print('Welcome to the program')

customer=Customer_Operations()
product=Product_Operations()
purchase=Purchase_Operations()
feedback=Feedback_Operations()

while True:
    print("1. Customer Operations")
    print("2. Product Operations")
    print("3. Purchase Operations")
    print("4. Feedback Operations")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1. Insert Customer Details")
        print("2. Display Customer Record")
        print("3. Display All Customer Records")
        operation = int(input("Enter your choice: "))

        if operation == 1:
            customer.insert_customer_detials(cursor)
        elif operation == 2:
            name = input("Enter Customer Name: ")
            customer.display_record(cursor, name)
        elif operation == 3:
            customer.display_records(cursor)
        else:
            print("Invalid Operation.")

    elif choice == 2:
        print("1. Insert Product Details")
        print("2. View All Products")
        operation = int(input("Enter your choice: "))

        if operation == 1:
            product.insert_product_details(cursor)
        elif operation == 2:
            product.view_all_products(cursor)
        else:
            print("Invalid Operation.")

    elif choice == 3:
        print("1. Record Purchase")
        print("2. View Purchases")
        operation = int(input("Enter your choice: "))

        if operation == 1:
            purchase.record_purchase(cursor)
        elif operation == 2:
            purchase.view_purchases(cursor)
        else:
            print("Invalid Operation.")

    elif choice == 4:
        print("1. Submit Feedback")
        print("2. View Feedback")
        operation = int(input("Enter your choice: "))

        if operation == 1:
            feedback.submit_feedback(cursor)
        elif operation == 2:
            feedback.view_feedback(cursor)
        else:
            print("Invalid Operation.")

    elif choice == 5:
        break

    else:
        print("Invalid Choice. Please try again.")

connection.commit()
print('Saved into DB')
cursor.close()
print('Cursor closed')