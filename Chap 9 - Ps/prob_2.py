# import random


# def game():
#     print("You are playing a dice game..")

#     score = random.randint(1, 62)
#     # fetch the high score
#     with open("highScore.txt") as f:
#         highScore=f.read()
#         if highScore!="":
#             highScore=int(highScore)
#         else:
#             highScore=0
#     print(f"Your score: {score}")


#     if score > highScore:
#         #write this hight score to the file
#         with open("highScore.txt","w") as f:
#             f.write(str(score))

#     return score


# game()

# import random


# def game():
#     print("You are playing the game..")
#     score = random.randint(1, 62)
#     # Fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if hiscore != "":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score: {score}")
#     if score > hiscore:
#         # write this hiscore to the file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score


# game()

import random

def game():
    print("You are playing the game...")

    # Generate a random score
    score = random.randint(1, 62)

    # Fetch the hiscore from the file
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            if hiscore:
                hiscore = int(hiscore)
            else:
                hiscore = 0
    except FileNotFoundError:
        # If the file doesn't exist, start with a hiscore of 0
        hiscore = 0

    print(f"Your score: {score}")

    if score > hiscore:
        # Update the hiscore
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
            print("New hiscore recorded!")

    return score

game()
