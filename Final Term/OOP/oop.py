class Employee:
    def __init__(spex, name, employee_number, age):
        spex.data = {
        'name': name,
        'employee_number': employee_number,
        'age': age
        }
        
    def display(spex):
        print("====================")
        print(f"Name: {spex.data['name']}")
        print(f"Employee Number: {spex.data['employee_number']}")
        print(f"Age: {spex.data['age']}")
        print("====================")

employees = []
num_employees = int(input("Enter the number of employees: "))

for i in range(num_employees):
    name = input(f"Enter the name of employee {i+1}: ")
    employee_number = int(input(f"Enter the employee number of employee {i+1}: "))
    age = int(input(f"Enter the age of employee {i+1}: "))
    employees.append(Employee(name, employee_number, age))

for employee in employees:
    employee.display()