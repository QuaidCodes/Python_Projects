
# Name: Rock, Paper, Scissors
# Description: Play some Rock, Paper, Scissors.

import random

def rockPaperScissors():
    print("Welcome to the game of ROCK, PAPER, SCISSORS. You have 3 tries to beat the computer!.")

    computerChoices = ["rock", "paper", "scissors"]

    for i in range(3):
        userInput = input("What do you choose? Type Rock, Paper, or Scissors: ").lower()
        computerInput = random.choice(computerChoices)



        if userInput == "rock" and computerInput == "paper":
            print("Computer threw paper.\n")

        elif userInput == "paper" and computerInput == "rock":
            print("You win! Computer used rock.\n")

        elif userInput == "scissors" and computerInput == "paper":
            print("You win! Computer used Paper.\n")

        elif userInput == "paper" and computerInput == "scissors":
            print("Paper looses to scissors; computer used scissors.\n")

        elif userInput == "rock" and computerInput == "scissors":
            print("Rock beats scissors, you win!\n")

        elif userInput == "scissors" and computerInput == "rock":
            print("You lose! Rock beats scissors.\n")

        elif userInput == computerInput:
            print("It is a draw.\n")

        else:
            print("Enter valid response!\n")

