""" |*******************************************************************************************************|
|This is to certify that this project is my own work, based on my personal efforts in studying and 			|
|applying the concepts learned. I have constructed the functions and their respective algorithms 			|
|and corresponding code by myself. The program was run, tested, and debugged by my own 						|
|efforts. I further certify that I have not copied in whole or otherwise plagiarized the 			        |
|work of other students and/or persons.	
|
|
|MARK LOUIS C. CADIENTE, TSU ID# 202300163 FROM TSM-1A
|
| TEMPLATE FROM DE LA SALLE UNIVERSITY MANILA, COLLEGE OF COMPUTER STUDIES 
|***********************************************************************************************************| """

"""  [Acknowledgements: w3schools.com, stackoverflow.com, GitHub.com, CodeAcademy.com] """
 
#frequency distribution table  showing the classes, tally, frequency, midpoint, cumulative and relative frequency, class boundaries.
#The program will now determine the frequency distribution table showing the classes, tally, frequency, midpoint, cumulative 
# and relative frequency, class boundaries.

#we are going to use Import math to use the math.ceil() funtion to round up the class interval
import math
#The user will enter the raw data here 
#Dont use int here in user input else it will not be read by the program
Raw_Data = input("Enter Raw Data separated by a comma >> ")
#instead, convert the raw data string into an int list


#Raw Data will be split into a list of strings 
Raw_Data = Raw_Data.split(",")
#Varialbe new_data will be used to store the new data 
new_data = []
#by using a for loop, the program will convert the string into an 
# int and assign it to the new_data list and store it on a varialbe named Raw Data
for x in Raw_Data:
    new_data.append(int(x))
Raw_Data = new_data
print("=====================================")
#Once the user is done entering the raw data, the user will then enter his/hers chosen number of class
Classes = int(input("Enter the number of Classes >> "))
print("=====================================")
#The minimum and maximum value of the raw data will be determined here
Upper_Class_Limit = max(Raw_Data)
Lower_Class_Limit = min(Raw_Data)


Range = Upper_Class_Limit - Lower_Class_Limit

#Now for the next step the program will now determin the class interval or the width of the class
#In here for the result, Example, if the Class Interval is 7.2, it will round up into 8 due to being

#There are no such thing as 7.2 of a person, it will always be a whole number when it comes to Class Intervals
#-Quote From Prof. Marlon V. Gamido, Tarlac State University

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

#program will now display the class limit for each class
#The Lower Class Limit will be the starting point of the class
#The Upper Class Limit will be the ending point of the class


    
    
    



