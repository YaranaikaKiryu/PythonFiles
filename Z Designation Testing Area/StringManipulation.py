while True:

    word=input("Enter a Word >> ")

    print("==========")

    lwc = word.lower()
    print("LOWERCASE FORM >> "+lwc)

    upc = word.upper()
    print("UPPERCASE FORM >> "+upc)

    length = len(word)
    print("Lenght of Word >> ",length)

    print("==========")

    print("ANALYZE WORD")
    print("[1] Word is Equals")
    print("[2] casefold")
    print("[3] index")
    print("[4] replace")

    choice = input("Enter the number of your Choice >> ")

    if choice == "1":
        w2=input("Enter Second Word to Compare >> ")
        Comparison = (word == w2)
        print("Result >> ",Comparison)
        
    elif choice == "2":
        w2 = input("Enter Word to Casefold Compare >> ")
        Comparison = (word.casefold() == w2.casefold())
        print("Result >> ",Comparison)
        
    elif choice == "3":
        lettertofind = input("Input Letter to Find >> ")
        foundat = word.index(lettertofind)
        print(lettertofind, " can be found at index ", foundat)
        
    elif choice =="4":
        enterwordtobereplaced = input("Enter Word To Be Replaced >> ")
        wordtobereplaced = input("Enter Word to be replaced with >> ")
        wordlereplace  = word.replace(enterwordtobereplaced, wordtobereplaced)
        
        print("Result >> ", wordlereplace)
        
    else:
        print("Invalid Input")
    
    a = input("Enter yes/no to continue >> ")
    if a=="yes":
        continue
        
    elif a=="no":
        break
    else:
            print("Enter either yes/no >> ")