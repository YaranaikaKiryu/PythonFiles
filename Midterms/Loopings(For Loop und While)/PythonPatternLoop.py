print("==========")
#Pyramid pattern of stars in python #1
rows = int(input("Enter the number of rows: "))
print("==========")
for x in range(rows):
    for y in range(x+1):
        print("*", end =" ")
    print("\r")
print("==========")

#Pyramid pattern of stars in python #2
rows = int(input("Enter the number of rows: "))
for j in range(1, rows+1):
    print("* " * j)
print("==========")

#Pyramid pattern of stars in python #3 MIRRORED RIGHT ANGLE TRIANGLE
rows = int(input("Enter the number of rows: "))
k = 2 * rows - 2
for i in range(0, rows):

    for j in range(0, k):
 
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
  
        print("* ", end="")
    print("")

print("==========")
# downward pyramid pattern of stars
rows = int(input("Enter the number of rows: "))
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
    
print("==========")
#Pattern to display letter of the word
word = str(input("Enter a word: "))
x = ""
for i in word:
    x += i
    print(x)

