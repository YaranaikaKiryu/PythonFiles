total = 0
count = 0
phrase = ''

Iteration = int(input("Enter Number >> "))

for i in range(Iteration):
    value = input("Enter Value >> ")
    if value.replace('.','',1).isdigit():
        if "." in value:
            value = float(value)
        else:
            value = int(value)
        total += value
        count += 1
    else:
        phrase += value + ' '
        
if count > 0:
    avg = total/count
    print("Average >> ",avg)
else:
    print("No numeric input")

print("Phrase >> ",phrase.rstrip())