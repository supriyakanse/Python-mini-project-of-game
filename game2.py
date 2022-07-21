import random

randNo=random.randint(1,10)
guess=0
userNo=None
print("Computer selected its number Guess it!")
while(userNo!=randNo):
    userNo=int(input("Enter guess "))
    guess=guess+1
    if userNo==randNo:
        print("\n***yeah!! u guessed it***")
    else:
        if userNo > randNo:
            print("\nEnter smaller number")
        elif userNo < randNo:
            print("\nEnter large number")
print(f"\n---you took {guess} guess")

with open("file.txt") as f:
   data= f.read()

if guess< int(data):
    with open("file.txt","w") as f:
        print("### Congrats!! you set new record")
        f.write(str(guess))