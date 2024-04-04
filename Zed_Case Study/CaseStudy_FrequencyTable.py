#BEFORE RUNNING THE PROGRAM, PLEASE INSTALL THE FOLLOWING LIBRARY
#pip install prettytable
#type the following command in the terminal to install the prettytable library


try:
    #IMPORTANT!!!! PLEASE INSTALL PRETTYTABLE FIRST BY TYPING IN THE TERMINAL
    #pip install prettytable
    from prettytable import PrettyTable #pip install prettytable 
    
except ModuleNotFoundError as e:
    print("PrettyTable Module is not yet Installed, please install it first by using the command 'pip install prettytable' in the console/terminal")
    print("Terminating Program....")
    exit()
#we are going to use Import math to use the math.ceil() funtion to round up the class interval
import math


#The user will enter the raw data here 

while True:
    try:
        #Dont use int here in user input else it will not be read by the program
        Raw_Data = input("Enter Raw Data separated by a COMMA >> ")

        #Raw Data will be split into a list of strings 
        Raw_Data = Raw_Data.split(",")
        #Varialbe new_data will be used to store the new data 
        new_data = []
        
        #by using a for loop, the program will convert the string into an 
        # int and assign it to the new_data list and store it on a varialbe named Raw Data
        for x in Raw_Data:
            new_data.append(int(x))
        Raw_Data = new_data
        #value error will be raised if the user enters a string that is not a number
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
            #In here for the result, Example, if the Class Interval is 7.2, it will round up into 8 due to being a whole number
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
    
            #Lower & Upper Class
            Lower_Class_Limit_List = [] #empty list
            Upper_Class_Limit_List = [] #empty List

            for index in range(Classes):
                ClassVal = Lower_Class_Limit + index * Class_Interval
                Lower_Class_Limit_List.append(ClassVal)
                Upper_Class_Limit_List.append(ClassVal + Class_Interval-1)
                
                       
                       #CODE BLOCK FOR FREQUENCY TABLE
            Frequency = []
            for indexOf in range(Classes):
                minInterval = Lower_Class_Limit_List[indexOf]
                maxInterval = Upper_Class_Limit_List[indexOf]

                count = 0
                for j in Raw_Data:
                    if minInterval <= j <= maxInterval:
                        count += 1
                Frequency.append(count)

                                
            Class_Boundaries = []
            for Bound in range(Classes):
                #by using ternary operator a short cut and more efficient way to determine the lower boundary of each class
                Lower_Boundary = Lower_Class_Limit_List[Bound] - 0.5 if Bound == 0 else Upper_Class_Limit_List[Bound - 1] + 0.5
                Upper_Boundary = Upper_Class_Limit_List[Bound] + 0.5

                # The lower and upper boundaries will be appended to the Class Boundaries list
                Class_Boundaries.append([Lower_Boundary, Upper_Boundary])
                
                #USED WHILE LOOP HERE TO DEMOSTRATE THE USE OF 2 LOOP TYPES THE FOR LOOP AND WHILE LOOP
                
           #by using a while loop to we are able determine the midpoint of each class
            i = 0
            Midpoint = [0] * Classes #the length of midpoint is samw as classes
            #Midpoint = [0,0,0,0,0,0]
            while i < Classes:
                #to get midpoint we will add the lower and upper class limit and divide it by 2
                Midpoint[i] = (Lower_Class_Limit_List[i] + Upper_Class_Limit_List[i]) / 2
                i += 1



            #RElative Frequency 
            i = 0
            Relative_Frequency = [0] * len(Frequency) #can also use class interval #The length of the Relative Frequency will be the same as the Frequency
            #example Frequency list [3,7,7,8,8,7] the length of the Relative Frequency will be 6
            #in visulaization, the inside of relative frequency will be like tis = [0,0,0,0,0,0]
            #by dividing the frequency of each class by the total number of data points we can get the result of the relative frequency
            while i < len(Frequency): 
                Relative_Frequency[i] = Frequency[i] / len(Raw_Data) #instead of getting the sum of the frequency, weill just use the lenght function
                i += 1



            #Cumulative Frequency
            i = 0
            Cumulative_Frequency = [0] * len(Frequency)
            #wHILE LOOP TO DETERMINE THE CUMULATIVE FREQUENCY
            while i < len(Frequency):
                #to get the cumulative frequency, we will add the frequency of each class to the previous class
                #ternary operator is used here.
                Cumulative_Frequency[i] = Frequency[i] if i == 0 else Cumulative_Frequency[i-1]+Frequency[i]
                i += 1
<<<<<<< Updated upstream
                
                
            #tABLE 
=======

            
>>>>>>> Stashed changes
            Table = PrettyTable()
            Table.field_names = ["Class","Frequency", "Class Boundaries", "Midpoint", "Relative Frequency", "Cumulative Frequency"]
            #for loop to print the data in a table
            for i in range(Classes):
                Table.add_row([f"{Lower_Class_Limit_List[i]} - {Upper_Class_Limit_List[i]}",Frequency[i], Class_Boundaries[i], Midpoint[i], round(Relative_Frequency[i],4), Cumulative_Frequency[i]])
            print(Table)
            print("Sum of Frequency >> ", sum(Frequency))
            print("Sum of Relative Frequency >> ", round(sum(Relative_Frequency),4))
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
<<<<<<< Updated upstream
"""
GITHUB REPOSITORIES USED FOR REFERENCE:

1. https://github.com/SrBlecaute01/FrequencyDistribution/blob/master/main.py
2. https://github.com/Adr-hyng/Frequency-Distribution-Table-Generator/blob/main/main.py
"""
""" 

VISUALUZATION OF HOW TO GET THE CLASS LIMITS 

RAW DATA >> 10,10,5,5,8,8,3,2,1,1
UPPER >> 1
LOWER >> 10

Iteration 1:
    index = 0
    ClassVal = 1 + 0 * 2 = 1
    Lower_Class_Limit_List = [1]
    Upper_Class_Limit_List = [1 + 2 - 1] = [2]

Iteration 2:
    index = 1
    ClassVal = 10 + 1 * 20 = 30
    Lower_Class_Limit_List = [10, 30]
    Upper_Class_Limit_List = [29, 30 + 20 - 1] = [29, 49]

Iteration 3:
    index = 2
    ClassVal = 10 + 2 * 20 = 50
    Lower_Class_Limit_List = [10, 30, 50]
    Upper_Class_Limit_List = [29, 49, 50 + 20 - 1] = [29, 49, 69] """


""""
VISUALIZATION OF HOW TO GET FREQUENCY

First iteration (indexOf = 0): minInterval = 1, maxInterval = 2

It checks each number in Raw_Data. The numbers 1 and 2 fall within this range. So, count becomes 3 (as there are two 1s and one 2).
count is appended to Frequency, so Frequency becomes [3].
Second iteration (indexOf = 1): minInterval = 3, maxInterval = 4

It checks each number in Raw_Data. The number 3 falls within this range. So, count becomes 1.
count is appended to Frequency, so Frequency becomes [3, 1].
Third iteration (indexOf = 2): minInterval = 5, maxInterval = 6

It checks each number in Raw_Data. The numbers 5 fall within this range. So, count becomes 2 (as there are two 5s).
count is appended to Frequency, so Frequency becomes [3, 1, 2].
Fourth iteration (indexOf = 3): minInterval = 7, maxInterval = 8

It checks each number in Raw_Data. The numbers 8 fall within this range. So, count becomes 2 (as there are two 8s).
count is appended to Frequency, so Frequency becomes [3, 1, 2, 2].
Fifth iteration (indexOf = 4): minInterval = 9, maxInterval = 10

It checks each number in Raw_Data. The numbers 10 fall within this range. So, count becomes 2 (as there are two 10s).
count is appended to Frequency, so Frequency becomes [3, 1, 2, 2, 2].
So, the final Frequency list is [3, 1, 2, 2, 2]. This list represents how many numbers in Raw_Data fall within each of the defined ranges (classes).
"""













"""""
Iteration 1:
    index = 0
    ClassVal = 10 + 0 * 20 = 10
    Lower_Class_Limit_List = [10]
    Upper_Class_Limit_List = [10 + 20 - 1] = [29]

Iteration 2:
    index = 1
    ClassVal = 10 + 1 * 20 = 30
    Lower_Class_Limit_List = [10, 30]
    Upper_Class_Limit_List = [29, 30 + 20 - 1] = [29, 49]

Iteration 3:
    index = 2
    ClassVal = 10 + 2 * 20 = 50
    Lower_Class_Limit_List = [10, 30, 50]
    Upper_Class_Limit_List = [29, 49, 50 + 20 - 1] = [29, 49, 69] """
=======

"""GITHUB REPOSITORY ACKNOWLEDGEMENTS:
    https://github.com/SrBlecaute01/FrequencyDistribution/blob/master/main.py
    https://github.com/sam17896/FrequencyDistributionTable/blob/master/prob.cpp
    https://github.com/BeepBoopBit/frequency-distribution-calculator/blob/master/main.py
"""
>>>>>>> Stashed changes
