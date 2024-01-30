Rate_of_Hour = 457.52
Rate_Per_OT = 753.00
Tax = 0.20

print("==============")
name = input("Enter Your Name >> ")
Hours_of_Work = float(input("Enter Your Number of Hours Worked >> "))
Hours_of_OT = float(input("Enter Overtime >> "))
SSS_Contribution = float(input("Enter SSS Contribution >> "))
Pagibig = float(input("Pagibig Contribution >> "))
Housing_Loan = float(input("Housing Loan >> "))

GrossSalary = (Hours_of_Work * Rate_of_Hour) + (Hours_of_OT * Rate_Per_OT)
TotalDeduction = (SSS_Contribution + Pagibig + Housing_Loan)
TaxDeduction = (GrossSalary * Tax)
Net_Salary =  GrossSalary - TotalDeduction - TaxDeduction

print("====PRINTING PAYSLIP====")
print("NAME >> ", name)
print("GROSS_SALARY >> ",GrossSalary)
print("SSS Contribution >>", SSS_Contribution)
print("PagIbig Contribution >>", Pagibig)
print("Housing Loan >> ", Housing_Loan)
print("TAX >>", TaxDeduction)
print("Total Deduction >> ",TotalDeduction)
print("Net Salary >> ", Net_Salary)

