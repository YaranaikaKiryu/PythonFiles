secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word:
    if guess_count < guess_limit and not (out_of_guess):
        print("Enter the Secret Word!")
        guess = input("Enter Guess: ")
        guess_count += 1
        print("You have", guess_limit - guess_count, "guesses left.")
        
    
    else:
        out_of_guess = True
        break

if out_of_guess:
    print("YOU LOSE!")
else:
    print("You Have enter the Secret Word!")
    