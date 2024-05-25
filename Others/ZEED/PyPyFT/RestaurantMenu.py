class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.tables = {}
        self.customer_orders = {}

    def add_items_to_menu(self):
        num_of_items = int(input("Please input the number of products you want to add: "))
        for _ in range(num_of_items):
            item_name = input("Please add the name of the product: ")
            item_price = float(input("Please enter the price of the product: "))
            self.menu_items[item_name] = item_price

    def book_tables(self):
        num_tables = int(input("Please input the number of table reservations: "))
        for i in range(num_tables):
            table_number = input(f"Please input the table number for reservation {i+1}: ")
            self.tables[table_number] = False

    def take_customer_order(self):
        table_number = input("Enter the table number for the order: ")
        if table_number in self.tables and not self.tables[table_number]:
            order = input("Enter the products separated by commas: ")
            self.customer_orders[table_number] = order.split(',')
            self.tables[table_number] = True
        else:
            print("Invalid table number or table already occupied.")

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price} pesos")

    def display_tables(self):
        print("Table Reservations:")
        for table, occupied in self.tables.items():
            status = "Occupied" if occupied else "Available"
            print(f"Table {table}: {status}")

    def display_orders(self):
        print("Customer Orders:")
        for table, orders in self.customer_orders.items():
            print(f"Table {table}: {', '.join(orders)}")

    def bill_out(self):
        table_number = input("Enter the table number to bill out: ")
        if table_number in self.tables and self.tables[table_number]:
            total_bill = sum(self.menu_items[item] for item in self.customer_orders[table_number] if item in self.menu_items)
            print(f"Total bill for Table {table_number}: {total_bill} pesos")
            del self.customer_orders[table_number]
            self.tables[table_number] = False
        else:
            print("Invalid table number or no orders for this table.")

def main():
    restaurant = Restaurant()
    while True:
        print("\nRestaurant Management System:")
        print("1. Add items to menu")
        print("2. Book tables")
        print("3. Take customer order")
        print("4. Display menu")
        print("5. Display table reservations")
        print("6. Display customer orders")
        print("7. Bill Out")
        print("8. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            restaurant.add_items_to_menu()
        elif choice == '2':
            restaurant.book_tables()
        elif choice == '3':
            restaurant.take_customer_order()
        elif choice == '4':
            restaurant.display_menu()
        elif choice == '5':
            restaurant.display_tables()
        elif choice == '6':
            restaurant.display_orders()
        elif choice == '7':
            restaurant.bill_out()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Number out of range, please try again.")


main()