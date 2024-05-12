class Employee:
    def __init__(self, emp_id, emp_name, emp_department, emp_hours, rate_per_hour):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_department = emp_department
        self.emp_hours = emp_hours
        self.rate_per_hour = rate_per_hour
        self.emp_salary = self.calculate_emp_salary()

    def calculate_emp_salary(self):
        return self.rate_per_hour * self.emp_hours

    def calculate_emp_overtime(self):
        if self.emp_hours > 50:
            overtime = self.emp_hours - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            return self.emp_salary + overtime_amount
        else:
            return self.emp_salary

    def print_employee_details(self):
        print(f"EMPLOYEE ID: {self.emp_id}")
        print(f"EMPLOYEE NAME: {self.emp_name}")
        print(f"EMPLOYEE DEPARTMENT: {self.emp_department}")
        print(f"EMPLOYEE HOURS: {self.emp_hours}")
        print(f"EMPLOYEE RATE PER HOUR: {self.rate_per_hour}")
        print(f"EMPLOYEE SALARY: {self.calculate_emp_overtime()}")
        
        
num_employees = int(input("Enter the number of employees: "))
employees = []

for i in range(num_employees):
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    emp_department = input("Enter employee department: ")
    emp_hours = int(input("Enter hours worked: "))
    rate_per_hour = float(input("Enter rate per hour: "))
    employee = Employee(emp_id, emp_name, emp_department, emp_hours, rate_per_hour)
    employees.append(employee)

for employee in employees:
    employee.print_employee_details()