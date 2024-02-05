coke = 10
sprite = 15
fanta = 12
royal = 13
pepsi = 16

def Coke(Quantity, Cash):
    Soda = "Coke"
    total = 10 * Quantity
    balance = Cash - total
    return Soda, total, balance

def Sprite(Quantity, Cash):
    Soda = "Sprite"
    total = 15 * Quantity
    balance = Cash - total
    return Soda, total, balance


def Fanta(Quantity, Cash):
    Soda = "Fanta"
    total = 12 * Quantity
    balance = Cash - total
    return Soda, total, balance


def Royal(Quantity, Cash):
    Soda = "Royal"
    total = 13 * Quantity
    balance = Cash - total
    return Soda, total, balance


def Pepsi(Quantity, Cash):
    Soda = "Pepsi"
    total = 16 * Quantity
    balance = Cash - total
    return Soda, total, balance


print("=====SODA=VENDING=MACHINE====")
print("[1]$10---------COCA-COLA" ) 
print("[2]$15---------SPRITE")
print("[3]$12---------FANTA")
print("[4]$13---------ROYAL")
print("[5]$16---------PEPSI")
print("=============================")

Choice = int(input("Enter Soda Choice(Input the Number of your choice) >> "))
if Choice < 1 or Choice > 5:
    print("INVALID INPUT OUT OF BOUNDS")
else:
    Quantity = int(input("How many Cans of Soda? >> "))
    Cash = int(input("Enter Your Cash Amount >> "))

if Choice == 1:
        if Cash < coke * Quantity:
            print("INSIFFICIENT FUNDS")
        else:
            print("-------RECEIPT-------")
            Soda, total, balance = Coke(Quantity, Cash)
            print("You Have Chosen: ",Soda)
            print("Total: $" + str(total))
            print("Balance: $" + str(balance))
            print("-------END-------")
            
elif Choice == 2:
        if Cash < sprite * Quantity:
            print("INSIFFICIENT FUNDS")
        else:
            print("-------RECEIPT-------")
            Soda, total, balance = Sprite(Quantity, Cash)
            print("You Have Chosen: ",Soda)
            print("Total: $" + str(total))
            print("Balance: $" + str(balance))
            print("-------END-------")
        
elif Choice == 3:
        if Cash < fanta * Quantity:
            print("INSIFFICIENT FUNDS")
        else:
            print("-------RECEIPT-------")
            Soda, total, balance = Fanta(Quantity, Cash)
            print("You Have Chosen: ",Soda)
            print("Total: $" + str(total))
            print("Balance: $" + str(balance))
            print("-------END-------")
        
elif Choice == 4:
        if Cash < royal * Quantity:
            print("INSIFFICIENT FUNDS")
        else:
            print("-------RECEIPT-------")
            Soda, total, balance = Royal(Quantity, Cash)
            print("You Have Chosen: ",Soda)
            print("Total: $" + str(total))
            print("Balance: $" + str(balance))
            print("-------END-------")
        
elif Choice == 5:
        if Cash < pepsi * Quantity:
             print("INSIFFICIENT FUNDS")
        else:
            print("-------RECEIPT-------")
            Soda, total, balance = Pepsi(Quantity, Cash)
            print("You Have Chosen:",Soda)
            print("Total: $" + str(total))
            print("Balance: $" + str(balance))
            print("-------END-------")



