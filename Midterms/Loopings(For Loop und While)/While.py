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




""" 
sum = 0 
total = 0
number = int(input("ENter a Number and Enter Zero if you're done >> "))

while number != 0:
    sum += number
    total +=1
    number = int(input("ENter a Number and Enter Zero if you're done >> "))

if total > 0:
    average = sum / total
    print("The average is:", average)
else:
    print("No numbers were entered.") """


# count = 0
# while count < 5:
#     count = count + 1
#     print("I am Loop Number",count)
# print("End Of Loop")
    
    

# attempts = 0 
# while True:
 
#  name = input("Enter Name >> ")
 
#  if name == 'Mark':
#      print("Hello Mark!")
#      break
#  else:
#      print("HOLY SHIT YOU ARE NOT MARK!")
#      attempts += 1
#      if attempts == 3:
#          uppername = name.upper()
#          print("FUCK OFF "+uppername+" YOU'RE NOT MARK!")
#          break
     


# Iteration = int(input("Enter Number of Iteration >> "))

# counter = 1
# avg_count = 0
# sum = 0

# for i in range(0,Iteration):
#     value = float(input("Enter Value " + str(counter) + " >> "))
#     counter +=1
#     sum+= value
#     avg_count += 1
    
# if avg_count > 0:
#     print("SUM >> ",sum)
#     average = sum/avg_count
#     print("AVG >> ",average)

# else:
#     print("No Numbers were Inputted")
    
    
#MULTIPLICATION TABLE
# number = int(input("Enter a number >> "))
# endVal = int(input("Enter a End Value >> "))

# for i in range(1,endVal):
#     product = number * i
#     print(product)
    
    
# numbers = [12,75,150,180,145,525,50]

# for items in numbers:
#     if items > 500:
#         break
#     elif items > 150:
#         continue
    
#     elif (items % 5 == 0):
#         print(items)


# counter = 0 
# number = 75869

# while number != 0:
#     number = number // 10
#     counter += 1
# print(counter)



# list1 = [10,20,30,40,50]

# list1 = reversed(list1)

# for items in list1:
#     print(items)



# for items in range(-10,0,1):
#     print(items)


# start = 25
# end = 50

# for num in range(start,end+1):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
            
#         else:
#             print(num)


# #Reverses a Word
# str = input("Word >> ")
# for i in range(len(str)-1,-1,-1):
#     print(str[i], end="")
# print("\n")

# counter = 0
# number = 43521

# while number != 0:
#     rem = number % 10
#     counter = counter * 10 + rem
#     number=number //10
    
# print(counter)
    
   
# n = int(input("Enter a Range >> "))
# while n != 0:
#     print(n, end=" ")
#     n = n-1
    
    

# sum_even = 0
# sum_odd = 0

# for i in range(1011):
    
#     if i%2 == 0:
#         sum_even+=1
        
#     else:
#         sum_odd+=1
        
        
# print("The sum of all even numbers is", sum_even)
# print("The sum of all odd numbers is", sum_odd)


