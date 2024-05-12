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
     Quo = 1 
     for value in values:
         Quo /= value
     Quo = round(Quo,3)
     return Quo
 

    


Number = int(input("Enter Number >> "))
print("Enter Values >> ")

Values = []
for x in range(Number):
    value = int(input())
    Values.append(value)
    
print("==================")

Sum = Add(*Values)
Difference = Subtract(*Values)
Product = Multiply(*Values)
Quo = Divide(*Values)

print("SUM >>", Sum)
print("DIFFERENCE >> ",Difference)
print("PRODUCT >> ",Product)
print("QUOTIENT/ROUNDED OFF BY 3 DECIMAL PLACES >> ",Quo)