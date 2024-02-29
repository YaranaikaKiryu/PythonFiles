for letter in "Python Love":
    print(letter)

print("==========")
#prints multiple of 2
for x in range(2,21,2): #for 'VARIABLE' in range('START', 'END')
    print(x)
    
print("==========")

for x in reversed(range(1,5)):
    print(x)
    
print("==========")
for t in range(1,21):
    if t == 13:
        continue #Will not Print the number 13
    else:
        print(t)
        
    
print("==========")
for t in range(1,21):
    if t == 13:
        break 
    else:
        print(t)

print("==========")
names = ["John", "James", "Jack", "Jill"]
for name in names:
    print("Hello!",name)
    
print("==========")
for index in range(10): #will print 0 to 9
    print(index)
    
print("==========")
    
for a in range(10,20):
    print(a)

print("==========")

fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    print("Current fruits >> ",fruits[index])
    
print("==========")
    
list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
for list in list_of_list:
    for x in list:
        print(x,end="")
     


for x in range(6):
    print(x)
else:
    print("Finally finished!")
    
print("==========")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
    
    
