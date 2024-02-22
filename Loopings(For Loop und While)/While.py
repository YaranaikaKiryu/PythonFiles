""" score_of_the_player = int(input(  "Enter the score of the player: "))
total_score = 0
scorcecount = 0
while score_of_the_player != -1:
    total_score += score_of_the_player
    scorcecount = scorcecount + 1
    score_of_the_player = int(input( "Enter the score of the player: "))
print("The average for the text is ", total_score/scorcecount) """



#calculate the sum of numbers entered by the user until the user enters 0
""" number = int(input("Enter a number: "))
total = 0
while number != 0:
    total += number
    number = int(input("Enter a number: "))
print("The sum is: ", total)
 """
 
""" ans = "YES"

while ans.upper() == "YES":
   num = int(input("Enter a number: "))
   print("The Number is: ", + num )
   ans = input("Do you want to continue? (YES/NO): ")
   if ans.upper() == "NO":
       print("Goodbye")
       break """
"""        
x=0
courses = ["BSCS","BSIT","BSIS"]

while x < len(courses):
    print(courses[x])
    x += 1 """
    
"""     
weekSalary = 0
dayofweek = 1
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
while(True):
    if(week[dayofweek]=="Sunday"):
        print("Week Over, Its Holiday!!")
        break
    weekSalary +=2000
    dayofweek += 1
    
print(weekSalary) """