class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item, amount):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += amount

    def remove(self, item, amount):
        if item in self.items and self.items[item] >= amount:
            self.items[item] -= amount
            if self.items[item] == 0:
                del self.items[item]
        else:
            print("Not enough of the item in the inventory to remove.")

    def display(self):
        print(self.items)


inventory = Inventory()

while True:
    action = input("What would you like to do? (add/remove/display/quit): ")

    if action.lower() == "add":
        item = input("What item would you like to add?: ")
        amount = int(input("How much would you like to add?: "))
        inventory.add(item, amount)

    elif action.lower() == "remove":
        item = input("What item would you like to remove?: ")
        amount = int(input("How much would you like to remove?: "))
        inventory.remove(item, amount)

    elif action.lower() == "display":
        inventory.display()

    elif action.lower() == "quit":
        break