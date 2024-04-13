correct_password = None
corect_username = None
max_attempts = 3

while True:
    print("Welcome to the Login and Sign Up Page!")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")
    
    choice = int(input("Please Enter Your Choice >> "))
    
    while choice < 1 or choice > 3:
        print("invalid input! OUT OF BOUNDS!")
        choice = int(input("Please Enter Your Choice >> "))
        
        
    if choice == 1:
        print("Welcome to the Sign Up Page!")
        username = input("Username >> ")
        password = input("Password >> ")
        
        correct_password = password
        correct_username = username
        
        print("==========")
        print("you have successfully Signed Up!")
        print("==========")
        continue
    
    elif choice == 2:
        
        if correct_password is None or correct_username is None:
            print("Please Sign Up First!")
            continue
        
        print("Welcome to the Log In Page!")
        attempts = 0
        while True:
            username = input("Username >> ")
            password = input("Password >> ")
            
            if username == correct_username and password == correct_password:
                print("you have successfully Login!")
                print("WELCOME! ",username)
                break
            
            else:
                print("username or password is incorrect")
                attempts += 1
                if attempts == max_attempts:
                    print("You have reached the maximum attempt")
                    print("SYSTEM LOCKDOWN....")
                    break
        break
   

    elif choice == 3:
        print("Exiting...")
        break



    