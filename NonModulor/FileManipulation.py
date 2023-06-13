# File Manipulation
import os
import shutil


# File detection
def file_detection():

    path = ""  # Path of the file on your PC or web

    if os.path.exists(path):
        if os.path.isfile(path):
            print("That is a file")
        elif os.path.isdir(path):
            print("That is a directory.")
    else:
        print("That location doesn't exist!")


# Reading a File
def file_reading():
    try:
        with open('text.txt') as file:  # "with open" Closes any files automatically after opening them.
            print(file.read())
    except FileNotFoundError:
        print('File not found!')
    except Exception:
        print('Some issues')
    finally:
        print("Finally Statement")


# Writing on a file
def editing_files():                     # Will produce a text.txt file in specified path
    text = "Yes THis is Quaid"

    with open('text.txt', 'w') as file:  # Overwrites the current file
        file.write('\n1. ' + text)

    with open('text.txt', 'a') as file:  # Appends to the current file
        file.write('\n2. ' + text)


def copying_files():
    # copyfile() = copies contents of a file
    # copy()     = copyfile() + permission mode + destination can be a directory
    # copy2()    = copy() + copies metadata (file's creation and modification time)

    shutil.copyfile('text.txt', 'text_copy.txt')  # (src, destination)


def move_files():
    source = "test.txt"
    destination = "G:\\PythonProjects\\test.txt"

    try:
        if os.path.exists(destination):
            print("There is already a file there.")
        else:
            os.replace(source, destination)     # move files from src to dst
            print(source + " was moved")
    except FileNotFoundError:
        print(source + " was not found.")


def delete_files():

    path = 'text.txt'

    try:
        os.remove(path)         # delete a file
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("No permissions!")
    else:
        print(path + " was deleted.")


def delete_directories():

    path = 'empty_folder'

    try:
        os.rmdir(path)          # delete an empty directory
    except FileNotFoundError:
        print("File not found")
    except OSError:
        shutil.rmtree(path)     # delete a directory containing files
        print(path + " was deleted.")
    else:
        print(path + " was deleted.")
