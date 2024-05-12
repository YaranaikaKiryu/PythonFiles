""" def factorial(x): #1st (3) 2nd(2) 3rd(1)
    if x == 1: # F F #T
        return 1
    else: 
        return (x * factorial(x-1)) #1st(3*2 = 6) #2nd (2 * 1 = 2)
        
        
num = 3 
print("the factorial of ", num, "is", factorial(num)) """


""" def add_items(dictionary, key, value):
    dictionary[key] = value
    print(f"Item {key} has been added with the value of {value}")


student = {}



add_items(student, "Mark", 89)
add_items(student, "Mar", 19)
add_items(student, "Ma", 49)
add_items(student, "M", 59)
add_items(student, "Morkite", 69)
add_items(student, "Markite", 79)



student['M'] = "Mark Louis cadiente"
student.popitem()
print("Dictionary", student)

kys = student.keys()
print(kys) """


programmers = {"C","C++","Java"}

programmers.add("Ruby")
programmers.update(["PHP, HTML"])

print(programmers)

