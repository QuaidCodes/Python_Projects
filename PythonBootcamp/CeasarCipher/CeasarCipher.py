
def encrypt(text: str, shift: int):
    shift_alphabet = []
    shift_alphabet.extend(alphabet)
    encrypted_text = ""

    for i in range(shift):
        shift_alphabet.append(" ")

    for j in text:
        encrypted_text += shift_alphabet[alphabet.index(j) + 5]

    print(encrypted_text)


def dycrypt(text: str, shift: int):
    ...


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    dycrypt(text, shift)

