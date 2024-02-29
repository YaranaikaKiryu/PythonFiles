


total = 0
count = 0
phrase = ''

Iteration = int(input("Enter Number >> "))

for i in range(0,Iteration):
    
    value = input("Enter Value >> ")
    if value.replace('.','',1).isdigit():
        if "." in value:
            value = float(value)
        else:
            value = int(value)
        
        total += value
        count += 1
        
    elif value.isalpha():
        phrase += value + ' '
        
    else:
        print("You have ENtered None")
        
if count > 0:
    average = total/count
    print("Average >>",round(average,2))
    print("Phrase >> ",phrase)
    
else:
    average = None
    print("Average >> ",average)
    print("Phrase >> ",phrase)