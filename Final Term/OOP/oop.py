""" class Employee:
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
    employee.display() """
    
""""
class Employee:
    def __init__(self, name, employee_number, age):
        self.data = {
        'name': name,
        'employee_number': employee_number,
        'age': age
        }
        
    def display(self):
        print("====================")
        print(f"Name: {self.data['name']}")
        print(f"Employee Number: {self.data['employee_number']}")
        print(f"Age: {self.data['age']}")
        print("====================")

def create_employees():
    employees = []
    num_employees = int(input("Enter the number of employees: "))

    for i in range(num_employees):
        name = input(f"Enter the name of employee {i+1}: ")
        employee_number = int(input(f"Enter the employee number of employee {i+1}: "))
        age = int(input(f"Enter the age of employee {i+1}: "))
        employees.append(Employee(name, employee_number, age))
    
    return employees

employees = create_employees()

for employee in employees:
    employee.display()
    """
    
class Person:
    def __init__(self, name, country, year_of_birth, date_and_month_of_birth):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth
        self.date_and_month_of_birth = date_and_month_of_birth

    def YearComputation(self, currentYear, currentMonth, currentDay):
        self.age = currentYear - self.year_of_birth
        birth_month = int(self.date_and_month_of_birth.split('/')[0])
        birth_day = int(self.date_and_month_of_birth.split('/')[1])
        if (birth_month, birth_day) > (currentMonth, currentDay):
            self.age -= 1
        if self.age < 0:
            self.age = "You are still not birth hence your age is 0"
        return self.age
    
    def DisplayInformation(self):
        print("===============================================")
        print(f"Name Of Person : {self.name}")
        print(f"Country of Origin : {self.country}")
        print(f"Person's Year Of Birth : {self.year_of_birth}")
        print(f"Person's Month and Day of Birth: {self.date_and_month_of_birth}")
        print(f"Person's Age : {self.age}")
        print("===============================================")

def MainInputForPersonWhichIsTheMainProgramThatITurnedIntoAFunctionAlso():
    Persons1 = []
    number_of_persons = int(input("Enter the number of Persons >> "))
    currentYear = int(input("Enter the current year >> "))
    currentMonthUndDate = input("Enter the Current Month and Date by this format (MM/DD) >> ")
    currentMonth = int(currentMonthUndDate.split('/')[0])
    currentDay = int(currentMonthUndDate.split('/')[1])
    print(f"THE CURRENT DATE TODAY IS SET TO THE YEAR {currentYear} MONTH AND DAY OF {currentMonthUndDate}")

    for i in range(number_of_persons):
        print("===============================================")
        name = str(input(f"Enter the name for Person ({i+1}) >> "))
        country = str(input(f"Enter the country of origin of Person ({i+1}) >> "))
        date_and_month_of_birth = input(f"Enter The Birth Month and Birth Date of Person ({i+1}) BY THIS FORMAT (MM/DD) >> ")
        year_of_birth = int(input(f"Enter the Year of birth of Person ({i+1}) >> "))
        person = Person(name, country, year_of_birth, date_and_month_of_birth)
        person.YearComputation(currentYear, currentMonth, currentDay)
        Persons1.append(person)

    return Persons1

Persons1 = MainInputForPersonWhichIsTheMainProgramThatITurnedIntoAFunctionAlso() #CALL THE MAIN FUNCTION

for personas in Persons1:
    personas.DisplayInformation()