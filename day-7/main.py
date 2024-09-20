import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = ["_" for char in chosen_word]
word_len = len(chosen_word)

life_points = 6
game_over = False

print(chosen_word)
print(display)
print(stages[life_points])

while not game_over:

    correct_guess = False
    guess = input("Guess a letter: ").lower()

    for index in range(word_len):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
            correct_guess = True

    print(display)

    if not correct_guess:
        print("Wrong guess...")
        life_points -= 1

        if life_points == 0:
            print("GAME OVER!")
            game_over = True

    print(stages[life_points])

    if "_" not in display:
        print("YOU WIN!!!")
        game_over = True
