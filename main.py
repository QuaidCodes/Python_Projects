import os

path = "C:\\Users\\quaid\\OneDrive\\Desktop\\text.txt"

if os.path.exists(path):
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location doesn't exist!")