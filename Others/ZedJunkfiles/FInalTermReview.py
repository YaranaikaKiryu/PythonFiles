dictionary = {}

noofval = int(input("Enter Number of Values >> "))

for x in range(0, noofval):
    key = input(f"enter key {x+1} >> ")
    value = input(f"enter Value {x+1} >> ")
    dictionary[key] = value
    
    
print(dictionary)

print("=====================================")

lister = []

numericvalues = int(input("Enter Number of Entry >> "))

for x in range(0,numericvalues):
    insidethelist = input(f"Enter Value inside list {x+1}>> ")
    lister.append(insidethelist)
    
print(lister)

print("=====================================")

user_set = set()

noofset = int(input("Enter Number of Set >> "))
for x in range(0, noofset):
    setvalue = input(f"Enter Value of Set {x+1} >> ")
    user_set.add(setvalue)
    
print(user_set)

print("=====================================")

tupler = []

numericvalues = int(input("Enter Number of Entry >> "))

for x in range(0,numericvalues):
    insidethelist = input(f"Enter Value inside list {x+1}>> ")
    tupler.append(insidethelist)
    
print(tupler)