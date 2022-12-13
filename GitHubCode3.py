from random import randint

# I found this code quite interesting as it is in a similar vein to our software project.
# This code helped me to understand and formulate my own while/elif portion of my menu in my software project
# The Randint function of this code is interesting as it could hold a multitude of uses for future projects of mine
# e.g Number generators/password generators etc.

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0, 2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0, 2)]
