for letter in "Python":
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