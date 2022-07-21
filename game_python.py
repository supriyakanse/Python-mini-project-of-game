import random

def game(compChoice,userChoice):
    if compChoice==userChoice:
        print("its a tie")
    if compChoice=='s':
        if userChoice=='g':
            print("\n\n***You won!! your gun killed snake***")
        elif userChoice=='w':
            print("\n\n***oops! you lose snake drinked your water***")
    elif compChoice=='g':
        if userChoice=='s':
            print("\n\n***oops!you lose gun killed your snake***")
        elif userChoice=='w':
            print("\n\n***you won! gun drown in water***")
    elif compChoice=='w':
        if userChoice=='g':
            print("\n\n***You lose!! gun drown in water***")
        elif userChoice=='s':
            print("\n\n***you won!! snake drinked your water***")
    

    


print("Snake Gun or Water")
compChoice=print("Computer's turn to choose between \n Snake(1) Gun(2) or water(3)")
comp=random.randint(1,3)
if comp==1:
    compChoice='s'
elif comp==2:
    compChoice='g'
elif comp==3:
    compChoice='w'
userChoice=input("Your turn choose between\n Snake(s) gun(g) water(w)")
game(compChoice,userChoice)
print("Computer choosed : ",compChoice)
print("You choosed : ",userChoice)
