class Person:
    def __init__(self, name, address, course, year, birth, month, day):
        self.name = name
        self.address = address
        self.course = course
        self.year = year
        self.yl = 2024 - year
        self.birth = birth
        self.age = 2024 - birth
        self.month = month
        self.day = day
    def display(self):
        print(f" NAME: {self.name} \n ADDRESS: {self.address} \n COURSE: {self.course} \n YEAR OF ENROLLMENT: School Year {self.year} \n YEAR LEVEL: Year {self.yl} in College \n BIRTH YEAR: {self.birth} \n BIRTH MONTH: {self.month} \n BIRTH DAY: {self.day} \n AGE: {self.age} Years Old " )

def main():
    count = 0
    name = []
    address = []
    course = []
    year = []
    birth = []
    month = []
    day = []

    input_num = int(input("HOW MANY PERSON DO YOU WANT TO ENTER?: "))
    while input_num > count:
        print(f"INFORMATION OF A PERSON: {count+1}")
        name.append(input("NAME: "))
        address.append(input("ADDRESS: "))
        course.append(input("COURSE: "))
        year.append(int(input("YEAR OF ENROLLMENT: ")))
        birth.append(int(input("BIRTH YEAR: ")))
        month.append(input("BIRTH MONTH: "))
        day.append(int(input("BIRTH DAY: ")))
        count += 1

    count = 0
    while input_num > count:
        show = Person(name[count], address[count], course[count], year[count], birth[count], month[count], day[count])
        print(f" \n PERSON # {count + 1} INFORMATION: ")
        show.display()
        count += 1

main()