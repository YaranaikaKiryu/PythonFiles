class Employee:
    def __init__(self, name, title, manager=None):
        self.name = name
        self.title = title
        self.manager = manager
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

def create_employee_hierarchy():
    manager_name = input("Enter the manager's name: ")
    manager_title = input("Enter the manager's title: ")
    manager = Employee(manager_name, manager_title)

    while True:
        employee_name = input("Enter the employee's name (or 'q' to quit): ")
        if employee_name.lower() == 'q':
            break

        employee_title = input("Enter the employee's title: ")
        employee = Employee(employee_name, employee_title, manager)
        manager.add_subordinate(employee)

    return manager

manager = create_employee_hierarchy()

print(f"Manager: {manager.name}, Title: {manager.title}")
for emp in manager.subordinates:
    print(f"Employee: {emp.name}, Title: {emp.title}, Manager: {emp.manager.name}")