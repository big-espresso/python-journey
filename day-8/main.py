from art import logo

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


def caesar(cipher_operation, text, shift):
    ciphered_text = ""

    if cipher_operation == "decode":
        shift *= -1

    for char in text:
        if char.lower() not in alphabet:
            ciphered_text += char
            continue

        letter_index_alphabet = alphabet.index(char.lower())

        ciphered_text += alphabet[(letter_index_alphabet + shift) % len(alphabet)]

    print(f"Here is the {cipher_operation}d result: {ciphered_text}")


direction = ""

print(logo)

running = True

while running:

    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exit program:\n"
    )

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        caesar(cipher_operation=direction, text=text, shift=shift)
    else:
        print("Wrong input for variable 'direction'")

    continue_execution = input("Continue using the program? (y/n)")
    running = True if continue_execution.lower() in ["y", "yes"] else False

print("Goodbye!")
