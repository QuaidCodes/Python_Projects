# Python Trivia Game
import random


def python_trivia():

    def new_game():
        print("Welcome to Python Trivia")
        print("1. Start\n2. Admit Defeat")
        option = int(input("Selection one option: "))

        if option == 1:
            check_answer()
        elif option == 2:
            print("\"There is no defeat unless admitted.\"")
        else:
            print("Why can't you read?")

    def check_answer():
        question_list = [
            "Q. Who is the author of Python?\n A. Albert Einstein\n B. Guido van Rossum\n C. Leonardo da Vinci\n D. Quaid Tahir",
            "Q. How can you use braces in Python?\n A. __future__ module\n B. Just Use them",
            "Q. Python was named after?\n A. The Burmese Python\n B. Monty Python Band\n C. Python that ate Pythons",
            "Q. ...?\n A. Cute\n B. Cute\n C. Cute\n D. placeholder"
        ]

        point = 0

        play = True
        while play:
            question = random.choice(question_list)
            currIndex = question_list.index(question)

            print(question)
            guess = input("Answer: ").lower()

            if currIndex == 0:
                if guess == 'b':
                    print("Correct, +1 point for Gryffindor!")
                    point += 1
                elif guess == 'd':
                    print("Seriously. I mean sure. 10 points!")
                    point += 10
                else:
                    print("Wrong, -1 Point")
                    point -= 1

            elif currIndex == 1:
                if guess == 'a':
                    print("NOT A CHANCE, -10 points!")
                    point -= 10
                elif guess == 'b':
                    print("Sure Buddy!")

            elif currIndex == 2:
                if guess == 'b':
                    print("Bdum! +1 point")
                    point += 1
                else:
                    print("That's what the Python said!, -1 point")
                    point -= 1
            elif currIndex == 3:
                if guess == 'd':
                    print("No, It's purpose is cuteness! -10 points")
                    point -= 10
                elif guess == 'a' or guess == 'b' or guess == 'c':
                    print("No, The correct answer was D. -1 point")
                    point -= 1
            else:
                print("Invalid guess.")
                point = 0

            display_score(point)
            if not play_again():
                print("Game Over.")
                play = False

    def display_score(score):
        print("Your score is " + str(score))

    def play_again():
        play = input("Would you like to play again? (y/n): ").lower()

        if play == 'yes' or play == 'y':
            return True
        elif play == 'no' or play == 'n':
            return False
        else:
            print("Don't bother if you cannot even read the instructions.")
            print("Game Over!")

    new_game()
