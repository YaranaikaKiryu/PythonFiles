
#we are going to use Import math to use the math.ceil() funtion to round up the class interval
import math

from prettytable import PrettyTable #pip install prettytable 

#The user will enter the raw data here 
#Dont use int here in user input else it will not be read by the program
while True:
    try:
        Raw_Data = input("Enter Raw Data separated by a comma >> ")

        #Raw Data will be split into a list of strings 
        Raw_Data = Raw_Data.split(",")
        #Varialbe new_data will be used to store the new data 
        new_data = []
        
        #by using a for loop, the program will convert the string into an 
        # int and assign it to the new_data list and store it on a varialbe named Raw Data
        for x in Raw_Data:
            new_data.append(int(x))
        Raw_Data = new_data
    except ValueError as e:
        print("Invalid Input, Please enter a number")
    else:
        print("=====================================")
        #Once the user is done entering the raw data, the user will then enter his/hers chosen number of class
        try:
            Classes = int(input("Enter the number of Classes >> "))
            print("=====================================")
            #The minimum and maximum value of the raw data will be determined here
            Upper_Class_Limit = max(Raw_Data)
            Lower_Class_Limit = min(Raw_Data)


            Range = Upper_Class_Limit - Lower_Class_Limit

            #Now for the next step the program will now determin the class interval or the width of the class
            #In here for the result, Example, if the Class Interval is 7.2, it will round up into 8 due to being

            #There are no such thing as 7.2 of a person, it will always be a whole number when it comes to Class Intervals
        

            Class_Interval = Range / Classes
            Class_Interval = math.ceil(Class_Interval)

            #Now Program will print all the Data needed like the Range, Number of Classes, Class Interval, Upper Class Limit 
            # and the lower class limit determine the class Limit for each class

            #prints the Range
            print("The Range for the Data Set is >> ", Range)
            print("=====================================")
            #prints the Number of Classes
            print("Number of Classes >> ", Classes)
            print("=====================================")
            #prints the Class Interval
            print("Class Interval >> ", Class_Interval)
            print("=====================================")
            #PRINTS THE UPPER AND LOWER CLASS LIMIT
            print("Upper Class Limit >> ", Upper_Class_Limit)
            print("Lower Class Limit >> ", Lower_Class_Limit)
            print("=====================================")
            
        except ValueError as e:
            print("Invalid Input, Please enter a number")
            
        else:
            #The program will now use a for loop to determine the Lower Class Limit and the Upper Class Limit for each class
            Lower_Class_Limit_List = [Lower_Class_Limit]
            #the upper class limit will be determined by adding the class interval to
            Upper_Class_Limit_List = [Lower_Class_Limit + Class_Interval]

            for i in range(Classes - 1):
                Lower_Class_Limit_List.append(Upper_Class_Limit_List[i])
                Upper_Class_Limit_List.append(Upper_Class_Limit_List[i] + Class_Interval)
                
            #Frequency will be determined by using a for loop to count the number of data points that fall within the class limits
            Frequency = [0] * Classes
            #a nested for loop will be used to determine the frequency of each class
            for Data_Point in Raw_Data:
                for i in range(Classes):
                    if Lower_Class_Limit_List[i] <= Data_Point < Upper_Class_Limit_List[i]:
                        Frequency[i] += 1
                        break
            
            Class_Boundaries = []
            for Bound in range(Classes):
                # Lower Boundary will be determined by using ternary operator a short cut and more efficient way to determine the lower boundary of each class
                Lower_Boundary = Lower_Class_Limit_List[Bound] - 0.5 if Bound == 0 else Upper_Class_Limit_List[Bound - 1] + 0.5

                # Upper Boundary will be determined by using ternary operator to determine the upper boundary of each class
                Upper_Boundary = Upper_Class_Limit_List[Bound] + 0.5

                # The lower and upper boundaries will be appended to the Class Boundaries list
                Class_Boundaries.append([Lower_Boundary, Upper_Boundary])
                
            #Class Midpoint will be determined by using a for loop to determine the midpoint of each class
            i = 0
            Midpoint = [0] * Classes
            while i < Classes:
                #Midpoint will be determined by adding the lower class limit and the upper class limit and dividing it by 2
                Midpoint[i] = (Lower_Class_Limit_List[i] + Upper_Class_Limit_List[i]) / 2
                i += 1

            #RElative Frequency 
            i = 0
            Relative_Frequency = [0] * len(Frequency)
            #Relative Frequency will be determined by dividing the frequency of each class by the total number of data points
            while i < len(Frequency):
                Relative_Frequency[i] = Frequency[i] / len(Raw_Data)
                i += 1

            #Cumulative Frequency
            i = 0
            Cumulative_Frequency = [0] * Classes
            #wHILE LOOP TO DETERMINE THE CUMULATIVE FREQUENCY
            while i < Classes:
                #if the index is 0, the cumulative frequency will be the frequency of the first class
                #Example if the frequency is 5, the cumulative frequency will be 5
                Cumulative_Frequency[i] = sum(Frequency[:i + 1])
                i += 1

            #tABLE 
            Table = PrettyTable()
            Table.field_names = ["Class", "Tally", "Frequency", "Midpoint", "Cumulative Frequency", "Relative Frequency", "Class Boundaries"]
            #for loop to print the data in a table
            for i in range(Classes):
                Table.add_row([f"{Lower_Class_Limit_List[i]} - {Upper_Class_Limit_List[i]}", f"{Lower_Class_Limit_List[i]} - {Upper_Class_Limit_List[i]}", Frequency[i], Midpoint[i], Cumulative_Frequency[i], round(Relative_Frequency[i],3), Class_Boundaries[i]])
            print(Table)
            print("=====================================")
            
            RetryProgram = input("Do you want to try again? (Yes/No) >> ")
            if RetryProgram.lower() == "yes":
                continue
            if RetryProgram.lower() == "no":
                print("Ending Program....")
                break
            else:
                print("Invalid Input, Please enter Yes or No")
                print("Terminating Program....")
                break
                
"""  [Acknowledgements: w3schools.com, stackoverflow.com, GitHub.com, CodeAcademy.com] """