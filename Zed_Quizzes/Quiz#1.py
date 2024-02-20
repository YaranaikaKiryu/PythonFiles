
Name = input("Enter Your Name >> ")
Address = input("Enter Your Address >> ")
print("==========")

Subject1 = input("Enter 1st Subject >> ")
Unit1 = input("Enter 1st Unit >> ")

Subject2 = input("Enter 2nd Subject >> ")
Unit2 = input("Enter 2nd Unit >> ")

Subject3 = input("Enter 3rd Subject >> ")
Unit3 = input("Enter 3rd Unit >> ")

Subject4 = input("Enter 4th Subject >> ")
Unit4 = input("Enter 4th Unit >> ")

Subject5 = input("Enter 5th Subject >> ")
Unit5 = input("Enter 5th Unit >> ")

Total_Unit = float(Unit1) + float(Unit2) + float(Unit3) + float(Unit4) + float(Unit5)
TuitionFee = float(Total_Unit) * 750.87


print("====REGISTRATION OF SUBJECTS=====")
print("Name  >>", Name)
print ("Address  >>", Address)
print("Subjects----------Units")
print(Subject1, ">>", float(Unit1))
print(Subject2, ">>", float(Unit2))
print(Subject3, ">>", float(Unit3))
print(Subject4, ">>", float(Unit4))
print(Subject5, ">>", float(Unit5))
print("Tuition Fee >> ", float(TuitionFee))
print("Total Of Units >> ",float(Total_Unit))
print("====ENTER THE AMOUNT TO PAY=====")
Amount = float(input("Enter Amount >> "))
Change = float(Amount) - float(TuitionFee)
print("Change >> ", round(float(Change), 2))

Cent = Change * 100

Pesos = Cent // 100
print("Pesos >>", Pesos)

Remaining_Cent = Cent % 100

TwentyFiveCent = Remaining_Cent // 25
print("25 Cent >>", TwentyFiveCent)

RemainingTwentyFiveCent = Remaining_Cent % 25

TenCent = RemainingTwentyFiveCent // 10
print("Ten Cent >>", TenCent)

RemainingTenCent = RemainingTwentyFiveCent % 10

FiveCent = RemainingTenCent // 5
print("Five Cent >>", FiveCent)

RemainingFiveCent = RemainingTenCent % 5

Cent = RemainingFiveCent
print("Cent >>", round(Cent))