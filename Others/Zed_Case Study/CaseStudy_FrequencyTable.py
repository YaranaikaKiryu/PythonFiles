#BEFORE RUNNING THE PROGRAM, PLEASE INSTALL THE FOLLOWING LIBRARY
#type the following command in the terminal to install the prettytable library

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print("pandas or matplotlib.pyplot Module is not yet Installed, please install it first by using the command 'pip install matplotlib pandas' in the console/terminal")
    print("Terminating Program....")
    exit()

import math

while True:
    try:
        Raw_Data = input("Enter Raw Data separated by a COMMA >> ")
        Raw_Data = Raw_Data.split(",")
        new_data = []
        for x in Raw_Data:
            new_data.append(int(x))
        Raw_Data = new_data
    except ValueError as e:
        print("Invalid Input, Please enter a number")
    else:
        
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

            # Create a DataFrame #No More Pretty Table Library
            df = pd.DataFrame({
                "Class": [f"{Lower_Class_Limit_List[i]} - {Upper_Class_Limit_List[i]}" for i in range(Classes)],
                "Frequency": Frequency,
                "Class Boundaries": Class_Boundaries,
                "Midpoint": Midpoint,
                "Relative Frequency": [round(x, 4) for x in Relative_Frequency],
                "Cumulative Frequency": Cumulative_Frequency
            })
            print(df)
   
            print("Sum of Frequency >> ", df['Frequency'].sum())
            print("Sum of Relative Frequency >> ", round(df['Relative Frequency'].sum(), 4))
            print("=====================================")
           
            Frequency_series = pd.Series(Frequency)

        
            mean = Frequency_series.mean().round(2)
            median = Frequency_series.median()
            mode = Frequency_series.mode()[0]
            
       
            print("Mean of Frequency: ", mean)
            print("Median of Frequency: ", median)
            print("Mode of Frequency: ", mode)
                    
            
            lower_boundaries = []
            upper_boundaries = []
            bins = []
            for boundary in Class_Boundaries:
                lower_boundaries.append(boundary[0])
                upper_boundaries.append(boundary[1])
                bins.append(boundary[0])
            bins.append(Class_Boundaries[-1][1])

            plt.figure(figsize=(10, 6))
            plt.hist(Raw_Data, bins=bins, edgecolor='black')
            plt.title('Frequency Distribution Histogram')
            plt.xlabel('Class Boundaries')
            plt.ylabel('Frequency')


            #Give this a detailed explanation. 
            #MARKED AS DONE.
            xticks = lower_boundaries + [upper_boundaries[-1]]
            xticklabels = []
            for i in range(len(lower_boundaries)):
                xticklabels.append(f"{lower_boundaries[i]} - {upper_boundaries[i]}")
            xticklabels.append(f"{lower_boundaries[-1]} - {upper_boundaries[-1]}")

            plt.xticks(xticks, xticklabels)
            plt.show()
            
            
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
"""
GITHUB REPOSITORIES USED FOR REFERENCE:

1. https://github.com/SrBlecaute01/FrequencyDistribution/blob/master/main.py
2. https://github.com/Adr-hyng/Frequency-Distribution-Table-Generator/blob/main/main.py
3. 
"""
""" 

VISUALUZATION OF HOW TO GET THE CLASS LIMITS 

RAW DATA >> 10,10,5,5,8,8,3,2,1,1
UPPER >> 1
LOWER >> 10
CLASSES >> 5

Lower_Class_Limit_List.append(ClassVal)
Upper_Class_Limit_List.append(ClassVal + Class_Interval-1)


Iteration 1:
    index = 0
    ClassVal = 1 + 0 * 2 = 1
    Lower_Class_Limit_List = [1]
    Upper_Class_Limit_List = [1 + 2 - 1] = [2]
    
    OUTPUT: 
    Lower_Class_Limit_List = [1]
    Upper_Class_Limit_List = [2]
    

Iteration 2:
    index = 1
    ClassVal = 1 + 1 * 2 = 3
    Lower_Class_Limit_List = [1, 3]
    Upper_Class_Limit_List = [2, 3 + 2 - 1] = [2, 4]
    
    OUTPUT:
    Lower_Class_Limit_List = [1, 3]
    Upper_Class_Limit_List = [2, 4]
    

Iteration 3:
    index = 2
    ClassVal = 1 + 2 * 2 = 5
    Lower_Class_Limit_List = [1, 3, 5]
    Upper_Class_Limit_List = [2, 4, 5 + 2 - 1] = [2, 4, 6]
    
    OUTPUT:
    Lower_Class_Limit_List = [1, 3, 5]
    Upper_Class_Limit_List = [2, 4, 6]
    

Iteration 4:
    index = 3
    ClassVal = 1 + 3 * 2 = 7
    Lower_Class_Limit_List = [1, 3, 5, 7]
    Upper_Class_Limit_List = [2, 4, 6, 7 + 2 - 1] = [2, 4, 6, 8]
    
    OUTPUT:
    Lower_Class_Limit_List = [1, 3, 5, 7]
    Upper_Class_Limit_List = [2, 4, 6, 8]
    
Iteration 5:
    index = 4
    ClassVal = 1 + 4 * 2 = 9
    Lower_Class_Limit_List = [1, 3, 5, 7, 9]
    Upper_Class_Limit_List = [2, 4, 6, 8, 9 + 2 - 1] = [2, 4, 6, 8, 10]
    
    OUTPUT:
    Lower_Class_Limit_List = [1, 3, 5, 7, 9]
    Upper_Class_Limit_List = [2, 4, 6, 8, 10]
    
    
    """
""""
VISUALIZATION OF HOW TO GET FREQUENCY

 
Lower_Class_Limit_List = [1, 3, 5, 7, 9]
Upper_Class_Limit_List = [2, 4, 6, 8, 10]
RAW DATA >> 10,10,5,5,8,8,3,2,1,1


First iteration 
indexOf = 0 
minInterval = 1 
maxInterval = 2



if 1 <= 0 <= 2: False
if 1 <= 1 <= 2: True
if 1 <= 1 <= 2: True
if 1 <= 2 <= 2: True
Count = 3

Frequency = [3]

Second iteration
indexOf = 1
minInterval = 3
maxInterval = 4

if 3 <= 10 <= 4: False
if 3 <= 10 <= 4: False
if 3 <= 5 <= 4: False
if 3 <= 5 <= 4: False
if 3 <= 8 <= 4: False
if 3 <= 8 <= 4: False
if 3 <= 3 <= 4: True
if 3 <= 2 <= 4: False
if 3 <= 1 <= 4: False
if 3 <= 1 <= 4: False

Count = 1
Frequency = [3,1]


Third iteration
indexOf = 2
minInterval = 5
maxInterval = 6

if 5 <= 10 <= 6: False
if 5 <= 10 <= 6: False
if 5 <= 5 <= 6: True
if 5 <= 5 <= 6: True
if 5 <= 8 <= 6: False
if 5 <= 8 <= 6: False
if 5 <= 3 <= 6: False
if 5 <= 2 <= 6: False
if 5 <= 1 <= 6: False
if 5 <= 1 <= 6: False

count = 2
Frequency = [3,1,2]


Fourth iteration
indexOf = 3
minInterval = 7
maxInterval = 8

if 7 <= 10 <= 8: False
if 7 <= 10 <= 8: False
if 7 <= 5 <= 8: False
if 7 <= 5 <= 8: False
if 7 <= 8 <= 8: True
if 7 <= 8 <= 8: True
if 7 <= 3 <= 8: False
if 7 <= 2 <= 8: False
if 7 <= 1 <= 8: False
if 7 <= 1 <= 8: False

count = 2
Frequency = [3,1,2,2]


Fifth iteration 
indexOf = 4 
minInterval = 9
maxInterval = 10

if 9 <= 10 <= 10: True
if 9 <= 10 <= 10: True
if 9 <= 5 <= 10: False
if 9 <= 5 <= 10: False
if 9 <= 8 <= 10: False
if 9 <= 8 <= 10: False
if 9 <= 3 <= 10: False
if 9 <= 2 <= 10: False
if 9 <= 1 <= 10: False
if 9 <= 1 <= 10: False



VISUALIZATION OF HOW TO GET THE CLASS BOUNDARIES

Lower_Class_Limit_List = [1, 3, 5, 7, 9]
Upper_Class_Limit_List = [2, 4, 6, 8, 10]
                
                
    Class_Boundaries = []
            for Bound in range(Classes):
                Lower_Boundary = Lower_Class_Limit_List[Bound] - 0.5 if Bound == 0 else Upper_Class_Limit_List[Bound - 1] + 0.5
                Upper_Boundary = Upper_Class_Limit_List[Bound] + 0.5


                Class_Boundaries.append([Lower_Boundary, Upper_Boundary])
                


Bound = 0
Lower_Boundary = Lower_Class_Limit_List[0] - 0.5 = 1 - 0.5 = 0.5
Upper_Boundary = Upper_Class_Limit_List[0] + 0.5 = 2 + 0.5 = 2.5

Class_Boundaries = [[0.5, 2.5]]

Bound = 1
Lower_Boundary = Lower_Class_Limit_List[1] + 0.5 = 3 + 0.5 = 3.5
Upper_Boundary = Upper_Class_Limit_List[1] + 0.5 = 4 + 0.5 = 4.5

Class_Boundaries = [[0.5, 2.5], [3.5, 4.5]]

Bound = 2
Lower_Boundary = Lower_Class_Limit_List[2] + 0.5 = 5 + 0.5 = 5.5
Upper_Boundary = Upper_Class_Limit_List[2] + 0.5 = 6 + 0.5 = 6.5

Class_Boundaries = [[0.5, 2.5], [3.5, 4.5], [5.5, 6.5]]

Bound = 3
Lower_Boundary = Lower_Class_Limit_List[3] + 0.5 = 7 + 0.5 = 7.5
Upper_Boundary = Upper_Class_Limit_List[3] + 0.5 = 8 + 0.5 = 8.5

Class_Boundaries = [[0.5, 2.5], [3.5, 4.5], [5.5, 6.5], [7.5, 8.5]]

Bound = 4
Lower_Boundary = Lower_Class_Limit_List[4] + 0.5 = 9 + 0.5 = 9.5
Upper_Boundary = Upper_Class_Limit_List[4] + 0.5 = 10 + 0.5 = 10.5

Class_Boundaries = [[0.5, 2.5], [3.5, 4.5], [5.5, 6.5], [7.5, 8.5], [9.5, 10.5]]

END OF LOOP
                
                
                
                
EXAMPLE OF HOW TO GET THE MIDPOINT AND VISUALIZATION

            i = 0
            Midpoint = [0,0,0,0,0]
            Midpoint = [0] * Classes #the length of midpoint is samw as classes
            #Midpoint = [0,0,0,0,0,0]
            
            while i < Classes:
                #to get midpoint we will add the lower and upper class limit and divide it by 2
                Midpoint[i] = (Lower_Class_Limit_List[i] + Upper_Class_Limit_List[i]) / 2
                i += 1

    Lower_Class_Limit_List = [1, 3, 5, 7, 9]
    Upper_Class_Limit_List = [2, 4, 6, 8, 10]
    

    
    i = 0
    Midpoint[i] = (1 + 2) / 2 
    = 3 / 2 = 1.5
    
    i = 1
    midpoint[i] = (3 + 4) / 2 
    = 7 / 2 = 3.5
    
    i = 2
    midpoint[i] = (5 + 6) / 2 
    = 11 / 2 = 5.5
    
    i = 3
    midpoint[i] = (7 + 8) / 2 
    = 15 / 2 = 7.5
    
    i = 4
    midpoint[i] = (9 + 10) / 2 
    = 19 / 2 = 9.5
    
    Midpoint = [1.5, 3.5, 5.5, 7.5, 9.5]
    
    
    
EXAMPLE OF HOW TO GET THE RELATIVE FREQUENCY

    
            #RElative Frequency 
            i = 0
            Relative_Frequency = [0] * len(Frequency) 


    Relative_Frequency = [0,0,0,0,0]

            while i < len(Frequency): 
                Relative_Frequency[i] = Frequency[i] / len(Raw_Data) 
                i += 1

    Frequency = [3,1,2,2,2]
    
    i = 0
    Relative_Frequency[i] = Frequency[i] / len(Raw_Data) = 3 / 10 = 0.3
    
    i = 1
    Relative_Frequency[i] = Frequency[i] / len(Raw_Data) = 1 / 10 = 0.1
    
    i = 2
    Relative_Frequency[i] = Frequency[i] / len(Raw_Data) = 2 / 10 = 0.2
    
    i = 3
    Relative_Frequency[i] = Frequency[i] / len(Raw_Data) = 2 / 10 = 0.2
    
    i = 4
    Relative_Frequency[i] = Frequency[i] / len(Raw_Data) = 2 / 10 = 0.2
    
    Relative_Frequency = [0.3, 0.1, 0.2, 0.2, 0.2]
    
    
EXAMPLE OF HOW TO GET THE CUMULATIVE FREQUENCY


         #Cumulative Frequency
            i = 0
            Cumulative_Frequency = [0] * len(Frequency)
            
            while i < len(Frequency):
               
                Cumulative_Frequency[i] = Frequency[i] if i == 0 
                
                else Cumulative_Frequency[i-1]+Frequency[i]
                i += 1

    Frequency = [3,1,2,2,2]
    Cumulative_Frequency = [0,0,0,0,0]
    
    
    
    i = 0
    Cumulative_Frequency[i] = Frequency[i] = 3
        Cumulative_Frequency = [3,0,0,0,0]
    
    i = 1
    Cumulative_Frequency[i] = Frequency[i] + Cumulative_Frequency[i-1] = 1 + 3 = 4
            Cumulative_Frequency = [3,4,0,0,0]
    
    i = 2
    Cumulative_Frequency[i] = Frequency[i] + Cumulative_Frequency[i-1] = 2 + 4 = 6
    
    i = 3
    Cumulative_Frequency[i] = Frequency[i] + Cumulative_Frequency[i-1] = 2 + 6 = 8
    
    i = 4
    Cumulative_Frequency[i] = Frequency[i] + Cumulative_Frequency[i-1] = 2 + 8 = 10
    
    Cumulative_Frequency = [3,4,6,8,10]
    
"""

