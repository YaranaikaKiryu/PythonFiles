Name = input("Enter Ur Name >> ")

Math = int(input("Enter Grade In Math >> "))

Science = int(input("Enter Grade In Science >> "))

English = int(input("Enter Grade In English >> "))


Sum = Math + Science + English
Average = Sum/3

print("===============")
print("Name >> ",Name)

print("Math >> ",Math)
print("Science >> ",Science)
print("English >> ",English)
print("===============")
print("Average >> ",round(Average))

try:
    if Average > 74:
        print("you Passed the semester")
    else:
        print("You Failed the semester")
        raise Exception
        
except:
      if Math <= 74:
        print("You Failed Math")

      if Science <= 74:
        print("You Failed Science")
        
      if English <= 74:
        print("you Failed English")

finally:
    print("===============")
    print("Program Will Run No Matter What")