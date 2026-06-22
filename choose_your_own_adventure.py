name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer1 = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? (left/right): ").lower()

if answer1 == "left":
    answer2 = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()

    if answer2 == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer2 == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer1 == "right":
    answer2 = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back): ").lower()

    if answer2 == "back":
        print("You go back and lose.")
    elif answer2 == "cross":
        answer3 = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ").lower()

        if answer3 == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")
        elif answer3 == "no":
            print("You ignore the stranger, they are offended, and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing,", name + "!")
