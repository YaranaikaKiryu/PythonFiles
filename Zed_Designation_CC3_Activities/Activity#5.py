

Name = input("Enter Ur Name >> ")
try:
  Math = int(input("Enter Grade In Math >> "))
  Science = int(input("Enter Grade In Science >> "))
  English = int(input("Enter Grade In English >> "))

    
except ValueError:
    print("Please Enter A Number")

else:
 

  Sum = Math + Science + English
  Average = Sum/3




  print("===============")
  print("Name >> ",Name)

  print("Math >> ",Math)
  print("Science >> ",Science)
  print("English >> ",English)
  print("===============")
  print("Average >> ",round(Average))


  
  if Average < 75:
    print("you fail")
  else:
    print("you pass")
    


  try:
    if Math < 75:
      raise Exception
  except Exception:
    print("You Failed Math")
    
  try:
    if Science < 75:
      raise Exception
  except Exception:
    print("You Failed Science")
    
  try:
    if English < 75:
      raise Exception
  except Exception:
    print("You Failed English")
    
