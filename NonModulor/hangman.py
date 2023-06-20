# Hangman Game
import random


# ------------------------------------------------------------------------------
def hangman(counter):
    if counter == 1:
        print("Head")
    elif counter == 2:
        print("Right limb")
    elif counter == 3:
        print("Left limb")
    elif counter == 4:
        print("Torso")
    elif counter == 5:
        print("Both Legs")
    else:
        return True

def user_input():
    # word_list = input("Enter in your words: ").split(" ")
    word_list = ["Abnegation", "Aggrandize", "Denigrate"]

    word = random.choice(word_list).lower()
    hidden_word = ""

    # Creation of hidden_word
    for i in range(len(word)):
        hidden_word += "_"

    print("Your word is " + hidden_word)

    counter = 0
    while hidden_word != word:
        letter = input("Your letter (if more than one character, only first one will be recognized): ")[0].lower()

        if word.find(letter) != -1:
            hidden_word = list(hidden_word)
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
        else:
            counter += 1
            if hangman(counter) == True:
                print("YOU WERE HANGED!")
                return 0

        hidden_word = "".join(hidden_word)
        print(hidden_word.capitalize())
    else:
        print("CONGRATS, YOU WILL NOT BE HANGED TODAY.")
# ------------------------------------------------------------------------------


# Main
print("Welcome to HANGMAN!, This is where the undead come to play with there lives.")
user_input()

