name = input("Enter Your Name >> ")
Hours_of_Work = float(input("Enter Your Number of Hours Worked >> "))
Hours_of_OT = float(input("Enter Overtime >> "))
SSS_Contribution = float(input("Enter SSS Contribution >> "))
Pagibig = float(input("Pagibig Contribution >> "))
Housing_Loan = float(input("Housing Loan >> "))
Number_Of_Years = int(input("Enter Number of Years >> "))
Office = input("Enter Office (IT, ACCT, HR) >> ")

GrossSalary = (Hours_of_Work * 457.52) + (Hours_of_OT * 753.00)
TaxDeduction = GrossSalary * 0.20
TotalDeduction = SSS_Contribution + Pagibig + Housing_Loan + TaxDeduction
Net_Salary = GrossSalary - TotalDeduction

if Office.upper() == "IT":
    
    if Number_Of_Years >= 10:
       Bonus = GrossSalary * 0.10
       Bonus2 = round(Bonus, 2)
    else:
       Bonus = GrossSalary * 0.05
       Bonus2 = round(Bonus, 2)

if Office.upper() == "ACCT":
    if Number_Of_Years >= 10:
        Bonus = GrossSalary * 0.12
        Bonus2 = round(Bonus, 2)
    else:
        Bonus = GrossSalary * 0.06
        Bonus2 = round(Bonus, 2)


if Office.upper() == "HR":
    if Number_Of_Years >= 10:
        Bonus = GrossSalary * 0.15
        Bonus2 = round(Bonus, 2)
    else:
        Bonus = GrossSalary * 0.075
        Bonus2 = round(Bonus, 2)
        

print("====PRINTING PAYSLIP====")
print("NAME >> ", name)
print("Number Of Years in Service >> ",Number_Of_Years)
print("Office >> ",Office)
print("Gross Salary >>",round(GrossSalary, 2))
print("SSS Contribution >>", round(SSS_Contribution, 2))
print("PagIbig Contribution >>", round(Pagibig, 2))
print("Housing Loan >> ", round(Housing_Loan, 2))
print("TAX >>", round(TaxDeduction,2 ))
print("Total Deduction >> ",round(TotalDeduction, 2))
print("Net Salary >> ",round(Net_Salary, 2))
print("Bonus >> ", round(Bonus,2))

