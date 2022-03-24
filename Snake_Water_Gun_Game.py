# Snake, Water, Gun Game Using Python.
import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("PC Turn: Snake(s) Water(w) or Gun(g)...?")

randnum = random.randint(1,3)
if randnum == 1:
    comp = "s"
elif randnum == 2:
    comp = "w"
elif randnum == 3:
    comp = "g"
else:
    print("Invalid Option.")

you = input("\nYour Turn: Snake(s) Water(w) or Gun(g)...?\n\tEnter Your Choice: ")

gamestatus = gamewin(comp, you)

print(f"\nComputer Choice {comp} and Your Choice {you}")

if(gamestatus == None):
    print("\nGame Tie")
elif(gamestatus):
    print("\nCongratulations, You've Won the Game...!")
else:
    print("\nYou've Lost the Game, Better Luck Next Time...")

