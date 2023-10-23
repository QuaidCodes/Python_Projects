# Python file manipulation

# Opening/creating a file in python 
file1 = open('data.txt', 'w')

# Getting file info
print("Name: ", file1.name)  # Gets the name of the file
print("Is closed: ", file1.closed) # Checks if the file is closed; returns-True/False
print("Opening mode: ", file1.mode) # When opened it is ready to be written into

# Write to file
file1.write("I am Quaid Tahir")
file1.write(" and I am a Software developer.")
file1.close()

# Append to file - After the file is closed
file1 = open("data.txt", "a") # To avoid overriding the written text in the file we use the 'a' to append to the current content of the file
file1.write(" I am a CS major @ RU.")
file1.close()

# Reading from the file
file1 = open("data.txt", 'r')
text = file1.read(100)          # Returns the first 100 characters in the file.
print(text)