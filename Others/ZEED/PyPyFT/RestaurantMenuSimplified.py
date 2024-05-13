class Restaurant:
    def __init__(self):
        self.menu_items = {}

    def add_items_to_menu(self):
        num_of_items = int(input("Please input the number of products you want to add: "))
        for _ in range(num_of_items):
            item_name = input("Please add the name of the product: ")
            item_price = float(input("Please enter the price of the product: "))
            self.menu_items[item_name] = item_price

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price} pesos")


restaurant = Restaurant()

while True:
    action = input("What would you like to do? (add/display/quit): ")

    if action.lower() == "add":
        restaurant.add_items_to_menu()

    elif action.lower() == "display":
        restaurant.display_menu()

    elif action.lower() == "quit":
        break