
# Name: Pirate Booty
# Description: In this game, you try your luck as the captain of the "Pearl".


def pirateBooty():
    print('''
You're the captain of the "Pearl', You have been following a 
treasure map, which has led you to this 3x3 island, you have 
3 moves. Try your luck, if you dare!
    ''')

    row1 = ["😈", "😈", "😈"]
    row2 = ["😈", "😈", "😈"]
    row3 = ["😈", "😈", "😈"]

    theMap = [row1, row2, row3]

    print(f"{row1}\n{row2}\n{row3}")

    for i in range(len(theMap)):
        position = input("Write two digits, Where do you want dig? ")

        row = int(position[0]) - 1
        col = int(position[1]) - 1

        if int(position) == 33:
            theMap[row][col] = "💰"

            print(f"{row1}\n{row2}\n{row3}")

            print("Alas, Yee have hit treasure, Would you squander it on rum?")
            break
        else:
            theMap[row][col] = "X"
            print(f"{row1}\n{row2}\n{row3}")
            if i == 2:
                print("You broke the shovel and went back defeated!")
