def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

x = input("enter first num >> ")
y = input("enter second num >> ")
z = input("enter third num >> ")

print(max_num(x,y,z),"is the largest number")
