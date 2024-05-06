
# Caesar Cipher

from caesarData import logo


def caesar(user_input, shift_num, mode):
    encrypted_text = ""

    if shift_num > 26:
        shift_num %= 26

    if mode == "encode":
        for char in user_input:
            if char in alphabet:
                encrypted_text += alphabet[alphabet.index(char) + shift_num]
            else:
                encrypted_text += char

    elif mode == "decode":
        reverse_alphabet = alphabet[::-1]

        for char in user_input:
            if char in alphabet:
                encrypted_text += reverse_alphabet[reverse_alphabet.index(char) + shift_num]
            else:
                encrypted_text += char

    print(encrypted_text)

    restart = input("Type 'y' of you would like to go again. Otherwise type anything: \n")

    if restart == "y":
        start()


def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
start()

