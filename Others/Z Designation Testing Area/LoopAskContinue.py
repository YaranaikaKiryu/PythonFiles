#VERSION 1
while True:
    
    #Insert code here
    
    cont = input("Another one? yes/no > ")
    while cont.lower() not in ("yes","no"):
        cont = input("Another one? yes/no > ")
    if cont == "no":
        break 
        
#VERSION 2
while True:
       #Insert code here
    
    a = input("Enter yes/no to continue >> ")
    if a=="yes":
        continue
    
    elif a=="no":
        break
    else:
        print("Enter either yes/no >> ")