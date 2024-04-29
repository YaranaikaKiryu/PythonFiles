# def my_function(*arhs):
#     Resulta = [x * 5 for x in arhs]
#     return Resulta

# Resulta = my_function(2,4,6,8,10) 

# print(Resulta)

#====================================================

# def multiply(*numbers):
#     total = 1 
#     for number in numbers:
#         total *= number
#         print(total)
#     return total
    
# total = multiply(2,4,6,8,10)
# print(total)

#====================================================

# def add(*nums):
#     results = []
#     for x in nums:
#         results.append(x + 5)
#     return results

# results = add(2,4,6,8,10)
# print("add parameter ",results)

#====================================================

def UserInformation():
    fname = input("Enter First Name >> ")
    lname = input("Enter Last Name >> ")
    id = int(input("Enter ID Number  >> "))
    age = int(input("Enter Age >> "))
    
    return fname, lname, id, age

def WorkInformation():
    Hours_of_Work = float(input("Enter Your Number of Hours Worked >> "))
    Hours_of_OT = float(input("Enter Overtime >> "))
    SSS_Contribution = float(input("Enter SSS Contribution >> "))
    Pagibig = float(input("Pagibig Contribution >> "))
    Housing_Loan = float(input("Housing Loan >> "))

    return Hours_of_Work, Hours_of_OT, SSS_Contribution, Pagibig, Housing_Loan

def WorkComputation(Hours_of_Work, Hours_of_OT, SSS_Contribution, Pagibig, Housing_Loan):
    GrossSalary = (Hours_of_Work * 457.52) + (Hours_of_OT * 753.00)
    TotalDeduction = (SSS_Contribution + Pagibig + Housing_Loan)
    TaxDeduction = (GrossSalary * 0.20)
    Net_Salary =  GrossSalary - TotalDeduction   
    
    return GrossSalary ,TaxDeduction, TotalDeduction, Net_Salary



fname, lname, id, age = UserInformation()
Hours_of_Work, Hours_of_OT, SSS_Contribution, Pagibig, Housing_Loan = WorkInformation()
GrossSalary ,TaxDeduction, TotalDeduction, Net_Salary = WorkComputation(Hours_of_Work, Hours_of_OT, SSS_Contribution, Pagibig, Housing_Loan)

print("============")
print("Name >> ",fname +" "+ lname)
print("ID >> ", id)
print("Age >> ",age)
print("GROSS_SALARY >> ",GrossSalary)
print("SSS Contribution >>", SSS_Contribution)
print("PagIbig Contribution >>", Pagibig)
print("Housing Loan >> ", Housing_Loan)
print("TAX >>", TaxDeduction)
print("Total Deduction >> ",TotalDeduction)
print("Net Salary >> ", Net_Salary)


