number = int(input("Enter a number enter a zero to stop: "))
sum = 0
count = 0
while number != 0:
    sum += number
    count += 1
    number = int(input("Enter a number enter a zero to stop:: "))

if count > 0:
    average = sum/count
    print("The average of these ",count, "numbers are >> ",average)
    
else:
    print("no Numbers were entered")
