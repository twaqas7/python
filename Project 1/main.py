# PROJECT 1: SNAKE, WATER, GUN GAME

# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user

"""
1 for snake
-1 for water
0 for gun

"""

import random

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

# by now you have 2 numbers (variables), one from computer and one from user

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if computer == you:
    print("It's a tie!")

else:
    if computer == -1 and you == 1:
        print("You win!")

    elif computer == -1 and you == 0:
        print("You lose!")

    elif computer == 1 and you == 0:
        print("You win!")

    elif computer == 1 and you == -1:
        print("You lose!")

    elif computer == 0 and you == 1:
        print("You lose!")

    elif computer == 0 and you == -1:
        print("You win!")

    else:
        print("comething went wrong!")
