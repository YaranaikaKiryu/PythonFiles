while True:
    def sum(x,y):
        z = x + y
        return z

    def difference(x,y):
        z = x - y
        return z
        
        
    def product(x,y):
        z = x * y
        return z
        
        
    def DivisionAnswer(x,y):
        if y == 0:
            print("Cannot Divide by Zero")
            return None
        else:
            z = x / y
            return z

        
    def Remainder(x,y):
        if y == 0:
            print("Cannot Divide by Zero")
            return None
        else:
            z = x % y
            return z
        
        
    num1 = int(input("Enter 1st Variable >> "))
    num2 = int(input("Enter 2nd Varialbe >> "))

    print("==========")

    print(num1, "+", num2 ,"is equals to" ,sum(num1,num2))
    print(num1, "-", num2 ,"is equals to" ,difference(num1,num2))
    print(num1, "*", num2 ,"is equals to" ,product(num1,num2))
    print(num1, "/", num2 ,"is equals to" ,DivisionAnswer(num1,num2))
    print(num1, "%", num2 ,"is equals to" ,Remainder(num1,num2))

    Continue = input("Do you want to Continue? enter yes or no >> ")
    Continue.casefold()
    if Continue == "yes":
        continue
    elif Continue == "no":
        break
    else:
        break
        
