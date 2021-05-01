import random as r

#Assining variables for the options
s = "Snake"
g = "Gun"
w = "Water"

#Giving Info to player what to type to choose
print("Type Snake for Snake\nType Water for Water \nType Gun for Gun")

#Taking Inputs from both Comp and Player
yourInput = input("Enter the Options:")
Comp_choiuce_List = [s,w,g]
compinput = r.choice(Comp_choiuce_List)

#conditions
if compinput == yourInput:
    print(f"You chose {yourInput} and computer chose {compinput}")
    print("Tie!")

if compinput == s:
    if yourInput == w:
        print(f"You chose {yourInput} and computer chose {compinput}")
        print("You Lost!")
    elif yourInput == g:
        print(f"You chose {yourInput} and computer chose {compinput}")
        print("You Win!")

if compinput == w:
    if yourInput == s:
        print(f"You chose {yourInput} and computer chose {compinput}")
        print("You win!")
    elif yourInput == g:
        print(f"You chose {yourInput} and computer chose {compinput}")
        print("You Lost!")

if compinput == g:
    if yourInput == w:
        print(f"You chose {yourInput} and computer chose {compinput}")
        print("You Win!")
    elif yourInput == s:
        print(f"You chose {yourInput} and computer chose {compinput}")
        print("you Lost!")
