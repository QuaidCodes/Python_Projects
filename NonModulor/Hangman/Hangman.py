# Hangman
import random
from hangmanData import word_list, logo, stages

win = False
word = random.choice(word_list)
guessed_word = ""
lives = 0

print(logo)
# print("psst, the solution is", word)

for i in range(len(word)):
    guessed_word += "_"

while not win:
    guess = input("Guess the letter: ").lower()

    if guess in guessed_word:
        print("You've already guessed the letter", guess)
    elif guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
        print(stages[lives])
    else:
        lives += 1
        if lives:
            print(stages[lives])
            print(f"The letter '{guess}' is not in the word. You lose a life! Careful now.")

    print(guessed_word)

    if guessed_word == word:
        win = True
        print("You win!")
        continue

    if lives == len(stages) - 1:
        print("Game Over, ran out of lives.")
        break

