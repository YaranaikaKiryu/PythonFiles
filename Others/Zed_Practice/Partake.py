def Swapping(Swap1, Swap2):
     List[Swap1], List[Swap2] = List[Swap2], List[Swap1] 
     return List


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
        
        EnterChoice = int(input("Enter Your Choice >> "))
        
        if EnterChoice == 1:
            print("LIST SWAPPING")
            print("==========")
            print("Your entered: ",List)
            print("==========")
            EleOne = int(input(f"Enter 1st Index to Swap  (0 to {NoOfEle - 1}) >> "))
            EleTwo = int(input(f"Enter 2nd Index to Swap (0 to {NoOfEle - 1}) >> "))
            Swapping(EleOne,EleTwo)
            print("==========")
            print("List After Swapping: ",List)
            print("==========")
            break
            
    except ValueError as e:
        print("Resistancce")