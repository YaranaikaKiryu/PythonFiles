class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self):
        item = input("Enter the name of the item: ")
        price = float(input("Enter the price of the item: "))
        self.menu_items[item] = price

    def book_tables(self):
        table_number = int(input("Enter the table number to book: "))
        self.book_table.append(table_number)

    def customer_order(self):
        table_number = int(input("Enter your table number: "))
        order = input("Enter your order: ")
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))

    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))
            
    def total_prices(self):
        total = 0
        for order in self.customer_orders:
            item = order['order']
            if item in self.menu_items:
                total += self.menu_items[item]
        return total

restaurant = Restaurant()

while True:
    print("\n1. Add item to menu")
    print("2. Book a table")
    print("3. Place an order")
    print("4. Print menu items")
    print("5. Print table reservations")
    print("6. Print customer orders")
    print("7. Total the prices")
    print("8. Quit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        numofitems = int(input("Enter the number of items you want to add: "))
        for _ in range(numofitems):
            restaurant.add_item_to_menu()
    elif choice == 2:
        restaurant.book_tables()
    elif choice == 3:
        restaurant.customer_order()
    elif choice == 4:
        restaurant.print_menu_items()
    elif choice == 5:
        restaurant.print_table_reservations()
    elif choice == 6:
        restaurant.print_customer_orders()
    elif choice == 7:
        total = restaurant.total_prices()
        print(f"The total price of the orders is: {total}")
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")