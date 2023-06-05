
# Password Generator
import random

def passwordGenerator():

    def user_input():
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        return nr_letters, nr_symbols, nr_numbers

    def easy_password(arr, nr_input):
        password_list = []

        for i in range(0, nr_input):
            password_list.append(random.choice(arr))

        return password_list

    def random_generator():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        nr_letters, nr_symbols, nr_numbers = user_input()

        password = easy_password(letters, nr_letters) + easy_password(numbers, nr_numbers) + easy_password(symbols, nr_symbols)

        random.shuffle(password)
        password = ''.join(password)

        print(password)

    # Main

    print("Welcome to the Password Generator!")
    random_generator()