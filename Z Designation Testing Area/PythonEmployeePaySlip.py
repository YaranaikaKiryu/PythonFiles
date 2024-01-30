sss = 894
philHealth = 583
pagIbig = 200
taxRate = 0.10

print("====Employee Pay Slip====")
Name = input("ENTER YOUR NAME >>")
Age =int(input("ENTER YOUR AGE >> "))
DateundMonth = input("ENTER MM/DD/YY >> ")
EmployeeID = (int(input("ENTER EMPLOYEE NUMBER >> ")))
BasicSalary = (float(input("ENTER YOUR SALARY >> ")))

Total_Deduction = sss + philHealth + pagIbig + (BasicSalary*taxRate)
Net_Salary = BasicSalary - Total_Deduction

print("=====EMPLOYEE SLIP=====")
print("NAME >> ",Name)
print("AGE >> ", Age)
print("DATE >> ", DateundMonth)
print("EMPLOYEE ID >> ", EmployeeID)
print("BASE SALARY >> ","$",BasicSalary)
print("TOTAL DEDUCTION >> ","$",Total_Deduction)
print("TOTAL SALARY >> ","$",Net_Salary)
print("===============")

