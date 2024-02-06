""" def increment(number, by):
    result = number + by
    return result


result = increment(1,by=2)
print(result)
 """

#Multple Args

def multiply(*numbers):
    print(numbers)

product=multiply(1,2,3,4,5)
print(product)