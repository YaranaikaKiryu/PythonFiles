




while True:
    try:
        NoOfEle = int(input("Enter the Number of Elements >> "))
        List = []
        for x in range(NoOfEle):
            element = input(f"Enter elements {x+1} >> ")
            List.append(element)

        print("==========")
        print("These are the Elements you entered")
        print("Your entered: ",List)
        print("==========")
        
        print("==========")
        print("Please Choose What Operation to do")
        print("[1] Swapping")
        print("[2] Index Insertion")
        print("[3] Popping")
        print("[4] End The Program")
        print("==========")
        
        EnterChoice = int(input("Enter Your Choice >> "))
        
        if EnterChoice == 1:
            print("LIST SWAPPING")
            print("==========")
            print("Your entered: ",List)
            print("==========")
            EleOne = int(input(f"Enter 1st Index to Swap  (0 to {NoOfEle - 1}) >> "))
            EleTwo = int(input(f"Enter 2nd Index to Swap (0 to {NoOfEle - 1}) >> "))
            List[EleOne], List[EleTwo] = List[EleTwo], List[EleOne] 
            print("==========")
            print("List After Swapping: ",List)
            print("==========")
            break
            
        elif EnterChoice == 2:
            print("Index Insertion")
            print("==========")
            print("Your entered: ",List)
            print("==========")
            Index = int(input(f"Insert Index that you want to Insert ({NoOfEle - 1}) >> "))
            Word = input("Enter the Value >> ")
            List.insert(Index,Word)
            print("==========")
            print("List After Index Insertion: ",List)
            print("==========")
            break
            
        elif EnterChoice == 3:
            print("Index Popping")
            print("==========")
            print("Your entered: ",List)
            print("==========")
            EnterValue = int(input("Enter Index that you want to Delete >> "))
            List.pop(EnterValue)
            print("==========")
            print("List After Index Pop: ",List)
            print("==========")
            break
        
        elif EnterChoice == 4:
            break
    except ValueError as e:
        print("==========")
        print("PLEASE ENTER A PROPER INTEGER")
        print("==========")
            
        