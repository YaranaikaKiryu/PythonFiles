class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department, emp_hours, rate_per_hour):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        self.emp_hours = emp_hours
        self.rate_per_hour = rate_per_hour

    def calculate_emp_salary(self):
        self.emp_salary = self.rate_per_hour * self.emp_hours

    def calculate_emp_overtime(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            self.emp_salary += overtime_amount

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.emp_name)
        print("Salary:", self.emp_salary)
        print("Department:", self.emp_department)
        print("Hours Worked:", self.emp_hours)
        print("Rate per Hour:", self.rate_per_hour)


num_employees = int(input("Enter the number of employees: "))
employees = []

for i in range(num_employees):
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_salary = float(input("Enter Employee Salary: "))
    emp_department = input("Enter Employee Department: ")
    emp_hours = float(input("Enter Employee Hours Worked: "))
    rate_per_hour = float(input("Enter Rate per Hour: "))

    emp = Employee(emp_id, emp_name, emp_salary, emp_department, emp_hours, rate_per_hour)
    emp.calculate_emp_salary()
    emp.calculate_emp_overtime(emp_hours)
    employees.append(emp)

print("\nEmployee Details:")
for emp in employees:
    emp.print_employee_details()
    print()