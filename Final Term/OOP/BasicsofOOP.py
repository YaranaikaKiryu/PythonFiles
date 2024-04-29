class Employee:
    def __init__(spex, name, employee_number, age):
        spex.data = {
        'name': name,
        'employee_number': employee_number,
        'age': age
        }
        
    def display(spex):
        print(f"Name: {spex.data['name']}, Employee Number: {spex.data['employee_number']}, Age: {spex.data['age']}")
        

p1 = Employee("Johnson", 12567345, 22)
p2 = Employee("Joan", 9091241, 23)

p1.display()
p2.display()


