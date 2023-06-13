
# Random Bill picker
# Description: A game played between friends in which the python program will pick a random person to pay the bill from a list of names.

def randomBillPicker():
    import random

    print("Welcome to random person picker!")
    namesString = input("Enter in everyone's names, seperated by a comma and space: ")

    names = namesString.split(", ")


    randomInt = random.randint(0, len(names)-1)

    # Should use random.choice(names); this will do the same function as the above code.

    print(names)

    print(f"{names[randomInt]} is going to pay the bill today!")
