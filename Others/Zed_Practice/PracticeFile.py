""" NumberOFValues = int(input("Enter Number of Values >> "))


values = []
for i in range(NumberOFValues):
    Value = int(input(f"Enter Value {i+1} >> "))
    values.append(Value)

print(list(reversed(values))) """


""" rows = int(input("Enter the number of rows: "))
multiplier = int(input("Enter the multiplier: "))
print("==========")
for x in range(rows):
    for y in range(x+1):
        print(multiplier*y, end =" ")
    print("\r")

 """

""" rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

for x in range(1,rows+1):
    for y in range(1,column+1):
        print(x*y, end="\t ")
    print() """
    
""" 
rows = int(input("Enter the number of rows: "))
multiplier = int(input("Enter the multiplier: "))

for x in range(rows):
    for y in range(x+1):
        print(multiplier*y,end="-")
    print("\r") """


""" n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Error! Factorial is not defined for negative numbers.")
else:
    for x in range(1,n+1):
        factorial *= x
        
print(f"The factorial of {n} is {factorial}")
        
         """
         
# string ='abcde'
# counter = 0 

# for str in string:
#     user_input = (input(f"Enter the {str} >> "))
#     counter += 1
#     if user_input.upper() == str.upper():
#         print(f"correct!'{str}' was found")
#     else:
#         print(f"incorrect!'{str}' was not found")
#         break
    
# print("Total Attempts: ", counter)

# from collections import Counter

# input_string = input("Enter integers separated by space: ")

# input_int = input_string.split(" ")

# counter = Counter(input_int)

# for value in sorted(counter, key=int):
#     value_int = int(value)
#     if value_int >= 90:
#         grade = 'A'
#     elif value_int >= 80:
#         grade = 'B'
#     elif value_int >= 70:
#         grade = 'C'
#     elif value_int >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     print(f"{value} : {counter[value]} times, Grade: {grade}")
    
    
    
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# numberslist = [num1,num2,num3]

# numberslist.sort(reverse=True)

# for num in  numberslist:
#     print(num)
    
    
# attempts = 0 
# password = 'str'
# max_attempt = 3

# intial_password = input("Enter the password: ")
# while intial_password != password:
#     attempts += 1
#     print("Incorrect Password")
#     if attempts == max_attempt:
#         print("You have reached the maximum number of attempts")
#         break
#     intial_password = input("Enter the password: ")
    
# if intial_password == password:
#     print("Correct")


# rows = int(input("Enter the number of rows: "))
# column = int(input("Enter the number of columns: "))


# for x in range(1,rows+1):
#     for y in range(1,column+1):
#         print(x*y, end="\t ")
#     print()
    
    

 
""" multipkier = int(input("Enter the multiplier: "))
end_vale = int(input("Enter the end value: "))


for x in range(1,end_vale+1):
    print(f"{multipkier} * {x} = {multipkier*x}") """
    
    
""" def Add(*values):
    return sum(values)

def Subtract(*values):
    return values[0] - sum(values[1:])

def Multiply(*values):
    product = 1
    for value in values:
        product *= value
    return product

def Divide(*values):
    try:
        return values[0] / values[1]
    except ZeroDivisionError:
        return "Cannot divide by zero"

Number = int(input("Enter Number >> "))
Values = []
for _ in range(Number):
    value = int(input("Enter Value >> "))
    Values.append(value)

print("==================")
# Call the functions and pass the values
Sum = Add(*Values)
Difference = Subtract(*Values)
Product = Multiply(*Values)
Quotient = Divide(*Values)

print("SUM >>", Sum)
print("DIFFERENCE >> ", Difference)
print("PRODUCT >> ", Product)
print("QUOTIENT >> ", Quotient) """


def Add(*values):
    Sum = sum(values)
    return Sum

def Subtract(*values):
    Difference = values[0] - sum(values[1:])
    return Difference

def Multiply(*values):
    Product = 1
    for value in values:
        Product *= value
    return Product

def Divide(*values):
        Quotient = values[0] / values[1]
        return Quotient

Number = int(input("Enter Number >> "))
Values = []
for x in range(Number):
    value = int(input())
    Values.append(value)

print("==================")
Sum = Add(*Values)
Difference = Subtract(*Values)
Product = Multiply(*Values)
Quotient = Divide(*Values)

print("SUM >>", Sum)
print("DIFFERENCE >> ", Difference)
print("PRODUCT >> ", Product)
print("QUOTIENT >> ", Quotient)