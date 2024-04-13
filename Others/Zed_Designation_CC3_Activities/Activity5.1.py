
Name = input("Enter Ur Name >> ")
try:
    Math = float(input("Enter Grade In Math >> "))
    Science = float(input("Enter Grade In Science >> "))
    English = float(input("Enter Grade In English >> "))


    Sum = Math + Science + English
    Average = Sum/3


except ValueError:
    print("Please enter a numeric grade, not an alphabet.")
except NameError as e:
    print(e)
    print("Please enter a numeric grade, not an alphabet.")
    
print("===============")
print("Name >> ",Name)
print("Math >> ",Math)
print("Science >> ",Science)
print("English >> ",English)
print("===============")
print("Average >> ",round(Average,2))

if Average > 74:
    print("you Passed the semester")
else:
    print("You Failed the semester")

subjects = {"Math": Math, "Science": Science, "English": English}

for subject, grade in subjects.items():
    try:
        if grade < 75:
            raise Exception
    except:
        print(f"You Failed {subject} you need to reinroll in the Subject")

print("===============")
print("Program Will Run No Matter What")
