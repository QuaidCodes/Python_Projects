
# Name: Heads or Tails
# Description: Randomly generates heads or tails

def HeadsTails():
    import random

    headsTails = random.randint(0, 1)

    if headsTails == 1:
        print("Heads")
    else:
        print("Tails")