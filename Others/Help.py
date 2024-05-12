class Person:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.date_of_birth = birthday

    def calculate_age(self, currentyear):
        return currentyear - self.date_of_birth

def main():
    persons = []
    num_persons = int(input("Enter the number of persons: "))
    current_year = int(input("Enter the current year: "))

    for _ in range(num_persons):
        name = input("Enter the person's name: ")
        country = input("Enter the person's country: ")
        birthday = int(input("Enter the person's year of birth: "))
        person = Person(name, country, birthday)
        persons.append(person)

    for person in persons:
        age = person.calculate_age(current_year)
        print(f"Name: {person.name}, Country: {person.country}, Date of Birth: {person.date_of_birth}, Age: {age}")

if __name__ == "__main__":
    main()