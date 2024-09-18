# Max functionality

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# FizzBuzz
fizzbuzz = False

if fizzbuzz:
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


# Password Generator Project
import random

letters = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

GEN_PASSWORD = True

if GEN_PASSWORD:

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    def gen_letter():
        return letters[random.randint(0, len(letters) - 1)]

    def gen_number():
        return numbers[random.randint(0, len(numbers) - 1)]

    def gen_symbol():
        return symbols[random.randint(0, len(symbols) - 1)]

    character_list = []

    for i in range(1, nr_letters + 1):
        character_list.append(random.choice(letters))
    for i in range(1, nr_symbols + 1):
        character_list.append(gen_symbol())
    for i in range(1, nr_numbers + 1):
        character_list.append(gen_number())

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    random.shuffle(character_list)
    out_password = "".join(character_list)
    # while character_list:
    #     out_password += character_list.pop(random.randint(0, len(character_list) - 1))

    print(out_password)
