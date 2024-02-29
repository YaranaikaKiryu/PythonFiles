# Simple Python Login
correct_username = None
correct_password = None

max_attempts = 5

while True:
    print("Welcome to the Sign up and Login Page!")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice >> "))

    while choice < 1 or choice > 3:
        print("Invalid Choice!")
        choice = int(input("Enter your choice >> "))

    if choice == 1:
        print("Sign Up")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        correct_username = username
        correct_password = password
        print("You have successfully signed up!")
        continue
        
    elif choice == 2:
        if correct_username is None or correct_password is None:
            print("No user has signed up yet.")
            continue

        print("Login")
        attempts = 0
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            if username == correct_username and password == correct_password:
                print("You have successfully logged in!")
                break
              
            else:
                print("Invalid Username or Password!")
                attempts += 1
                if attempts == max_attempts:
                    print("You have reached the maximum attempts!")
                    break
        break 

    elif choice == 3:
        print("Exiting...")
        break