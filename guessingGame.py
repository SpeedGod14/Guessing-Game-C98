import random
print("Number Guessing Game")
rand = random.randint(1, 9)
userChances = 5
while userChances > 0:
    userInput = int(input("Enter a number from 1 to 9: "))
    if userInput == rand:
        print("Congratulations, YOU WON!!!")
        break
    elif userInput > rand:
        print("Lower")
    elif userInput < rand:
        print("Higher")
    else:
        print("Enter a number from 1 to 9")
    userChances = userChances - 1
if userChances == 0:
    print("You lost the game.")