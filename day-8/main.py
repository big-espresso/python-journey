alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def decrypt(text, shift):
    deciphered_text = ""

    for char in text:
        letter_index_alphabet = alphabet.index(char.lower())

        shifted_index = letter_index_alphabet - shift

        if abs(shifted_index) >= len(alphabet):
            shifted_index = -(abs(shifted_index) % len(alphabet))

        deciphered_text += alphabet[shifted_index]

    print(deciphered_text)


def encrypt(text, shift):
    ciphered_text = ""

    for char in text:
        if char.lower() not in alphabet:
            ciphered_text += char
            continue

        letter_index_alphabet = alphabet.index(char.lower())

        ciphered_text += alphabet[(letter_index_alphabet + shift) % len(alphabet)]

    print(ciphered_text)


direction = ""

while direction != "exit":

    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit program:\n"
    )
    if direction == "exit":
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text=text, shift=shift)
    elif direction == "decode":
        decrypt(text=text, shift=shift)
    else:
        print("Wrong input for variable 'direction'")
