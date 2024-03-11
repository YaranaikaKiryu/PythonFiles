""" a = input("Enter 1 >> ")
b = input("Enter 2 >> ")
c = input("Enter 3 >> ")

d = a.lower()

replace =  c
final = d.replace(b, c)
final = final.upper()

print(final) """


""" Multiply = int(input("Enter a number to multiply >> "))
end_index = int(input("Enter An Ending Index >> " ))

for i in range(Multiply,end_index+1):
    result = i * Multiply
    print(f"{i} * {Multiply} = {result}")
     """
"""     
Phrase = input("Enter a Phrase >> ")
try:
    number = int(input("Enter a Number >> "))
except ValueError:
    print("Please enter a number")
else:
    for i in range(1,10+1):
        result = i * number
        print(i, " * ",number," = ",result)
        print(Phrase,"Number - ",i)
    
try:
    Multiply = int(input("Enter a number to multiply >> "))
    UserDefined = int(input("Enter an Ending Index >> "))
except ValueError:
    print("please enter a number")
    
else:
    count = 0



    while count < UserDefined+1:
        result = count * Multiply
        
        count = count + 1
        print(result)
        
        
        
list_of_names = ["John","Paul","George","Ringo"]

for names in range(len(list_of_names)):
    print("Hello", list_of_names[names])
    
     """
""" try:
    
    number = int(input("Enter a number >> "))
except ValueError:
    print("Please enter a number")

else:
    for i in range(1,number+1):
        cube = (i * i * i)
        print("The cube of", i, "and the cube is ",cube)
        
    
StringList = input("Words with Space >> ")
words = StringList.split()

for i in words:
    print("We will display each letter of ",i)
    for words in i:
        print(words)
        
        
for i in range(0,10,3):
    print(i)
else:
    print("Done Printing Numbers") """