#Create a Class Person
class Person:
    #Initialze using the __init_ function the (name,country,year_of_birth,date_and_month_of_birth)
    def __init__(self, name, country, year_of_birth, date_and_month_of_birth):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth
        self.date_and_month_of_birth = date_and_month_of_birth

#to compute the age first we must(Call the CurrentYear, Current Month, CurrentDay, BirthMonth and birthDay)
    def YearComputation(self, currentYear, currentMonth, currentDay, birthMonth, birthDay):
        
        #To get the age of the person, we must Subtract the current year to the Person's Year of Brith
        self.age = currentYear - self.year_of_birth
        
        #WE SHALL USE TUPLE COMPLEX COMPARISION INORDER TO ILLUSTRATE THIS
        """
currentMonth = 4
currentDay = 15

birthMonth = 5
birthDay = 10
    if (birthMonth, birthDay) > (currentMonth, currentDay):
    print "NOT HAPPENING YET"
    else
    print "BIRTHDAY HAS ALREADY PASSED"
    
    (5, 10) > (4, 15) - RETURNS TO "BIRTHDAY NOT HAPPENING YET"
    (3, 10) > (4, 15) - RETURNS TO "BRITHDAY HAS ALREADY PASSED" 

        """
        if (birthMonth, birthDay) > (currentMonth, currentDay):
            self.age -= 1 #IF THE PERSON'S BIRTHDAY HASNT HAPPNED IN THE CURRENT YEAR
        if self.age < 0: 
            self.age = 0  #CHECKS IF THE AGE IS LESS THAN ZERO. IF THE AGE IS LESS THAN 0, II'S SET THE AGE TO ZERO
        return self.age
    
    #this is for the final function which displays all the Information of the Person
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
        birthMonth = int(date_and_month_of_birth.split('/')[0]) 
        birthDay = int(date_and_month_of_birth.split('/')[1]) 
        person = Person(name, country, year_of_birth, date_and_month_of_birth)
        person.YearComputation(currentYear, currentMonth, currentDay, birthMonth, birthDay)
        Persons1.append(person)

    return Persons1

Persons1 = MainInputForPersonWhichIsTheMainProgramThatITurnedIntoAFunctionAlso() #CALL THE MAIN FUNCTION

for personas in Persons1:
    personas.DisplayInformation()