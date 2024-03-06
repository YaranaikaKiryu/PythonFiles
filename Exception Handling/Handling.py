

#exception =  events detected during execution that interrupt the flow of a program
#exception handling =  process of responding to the occurrence, during computation, of exceptions – anomalous or exceptional conditions requiring special processing – often changing the normal flow of program execution
#try block =  block of code that will be attempted
#except block = block of code that will execute if there is an exception in the try block
#finally block = block of code that will execute regardless of an exception
#pass = keyword that is used to define an empty block


try:
    numerator = int(input("Enter a number to divide >> "))
    denominator = int(input("Enter a number to divide by >> "))
    result = numerator / denominator
    print(round(result,2))
        
except ValueError as e:
    print("You must enter a number!")
    #MULTIPLE EXCEPTION HANDLING 
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero!")
except SyntaxError as e:
    print(e)
    print("You must enter a number!")
except:
    print("something went wrong")
else:
    print("No Error")
finally:
    print("This will always execute!")
        
print("End of program")