import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the targe or Quit(Q) :")
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. take bigger guess..")
    else:
        print("your number was too big. take smaller guess..")

print("----Game Over----")