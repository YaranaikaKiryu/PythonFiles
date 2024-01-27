is_male = True
is_Tall = True

if is_male and is_Tall:
    print("You are indeed a male or tall or both")
    
elif is_male and not(is_Tall):
    print("You are a short male")
    
elif not(is_male) and (is_Tall):
    print("You are a female and tall")

else:
    print("You not male and not tall ;<")