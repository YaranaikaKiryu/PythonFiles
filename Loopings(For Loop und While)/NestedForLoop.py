rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
symbol = input("Enter the symbol to be printed: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end =" ")
    print()
  
    
""" 
for x in range(3):
    for y in range(1, 10):
        print(y, end ="")
    print() """