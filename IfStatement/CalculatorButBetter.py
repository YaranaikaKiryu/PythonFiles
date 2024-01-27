def Add (num1, num2):
    return num1 + num2

def Subtract(num1, num2):
    return  num1 - num2

def Multiply(num1, num2):
    return num1 * num2

def Divide(num1, num2):
    return num1 / num2

x = float(input("Enter First Number >> "))
y = float(input("Input Second Number >> ")) 

print("==========================")
print("Please Select an Operator")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print("==========================")

operator = input("Type 1,2,3 or 4 to Choose whether to Add, Subtract, to Multiply or To Subtract >> ")

if operator == "1":
    print(x, "+", y ,"is equals to" ,Add(x,y))
    
elif operator == "2":
        print(x, "-", y ,"is equals to" ,Subtract(x,y))
        
elif operator == "3":
        print(x, "*", y ,"is equals to" ,Multiply(x,y))
        
elif operator == "4":
        print(x, "/", y ,"is equals to" ,Divide(x,y))
        
else:
    print("Invalid Input!")