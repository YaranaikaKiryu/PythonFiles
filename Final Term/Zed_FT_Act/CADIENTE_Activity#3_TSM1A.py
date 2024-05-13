class Employee:
    def __init__(self, emp_name, emp_id, emp_department, emp_hours, rate_per_hour):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_department = emp_department
        self.emp_hours = emp_hours
        self.rate_per_hour = rate_per_hour
        self.emp_salary = self.calculate_emp_salary()
        
    
    def calculate_emp_salary(self):
        self.emp_salary = self.rate_per_hour * self.emp_hours
        return self.emp_salary
    
    #TAKES 2 ARGUMENTS 
    def calculate_emp_overtime(self, emp_salary, emp_hours):
        if emp_hours > 50:
            overtime = emp_hours - 50
            Overtime_amount = (overtime * (emp_salary / 50))
            OverTimeSalary = Overtime_amount + emp_salary
            return OverTimeSalary


    def print_employee_details(self):
        print(f"EMPLOYEE NAME  >> {self.emp_name}")
        print(f"EMPLOYEE ID >>  {self.emp_id}")
        print(f"Employee's Department >> {self.emp_department}")
        print(f"EMPLOYEE'S WORK PER HOUR >> {self.emp_hours}")
        print(f"EMPLOYEE'S RATE PER HOUR >> {self.rate_per_hour}")
        #CHECKS IF THE HOURS OF THE EMPLOYEE IS GREATER THAN 50
        if self.emp_hours > 50:
            print(f"EMPLOYEE'S SALARY >> {self.calculate_emp_overtime(self.emp_salary, self.emp_hours)}")
        else:
            print(f"EMPLOYEE'S SALARY >> {self.emp_salary}")
            
        print("========================================================")
        
#MAIN FUNCTION

Employees = [] #create empty list

EnterNumberofEmployees = int(input("Enter the Number of Employees >> "))
print("========================================================")
for x in range(0,EnterNumberofEmployees):
    emp_Name = input(f"Enter Employee {x+1} Name >> ")
    emp_ID = int(input(f"Enter Employee {x+1} ID >> "))
    emp_Depart = input(f"Enter Employee {x+1} Department >> ")
    emp_WPH = int(input(f"Enter Employee {x+1} Work Per Hour >> "))
    emp_RPH = int(input(f"Enter Employee {x+1} Rate Per Hour >> "))
    print("========================================================")
    employee = Employee(emp_Name, emp_ID, emp_Depart, emp_WPH, emp_RPH)
    Employees.append(employee)
    
for eployeenas in Employees:
    eployeenas.print_employee_details()
    

