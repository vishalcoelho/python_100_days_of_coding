import random
import os, time
from typing import List

HANGMANINTRO = """

   ________  ________  ________  ________  ________  ________  ________
  ╱    ╱   ╲╱        ╲╱    ╱   ╲╱        ╲╱        ╲╱        ╲╱    ╱   ╲
 ╱         ╱         ╱         ╱       __╱         ╱         ╱         ╱
╱         ╱         ╱         ╱       ╱ ╱         ╱         ╱         ╱
╲___╱____╱╲___╱____╱╲__╱_____╱╲________╱╲__╱__╱__╱╲___╱____╱╲__╱_____╱
"""

HANGMANPICS = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

MAX_LIVES = 6
DELIMITER = "*" * 12

word_list = ["aardvark", "baboon", "camel"]
n_lives = MAX_LIVES
n_blanks = 0
prompt_win = "Right! You win!!"
prompt_lose = "Wrong! You lose!!"


def reset_counters() -> None:
    """Used by pytest to setup prior to each test"""
    global n_lives, n_blanks
    n_lives = MAX_LIVES
    n_blanks = 0


def render_screen(n_lives: int, unknown_word: List[str]) -> None:
    """Render the game screen on each loop

    :param n_lives: Number of lives left in the game
    :param unknown_word: Word the user is trying to guess
    :returns None:
    """
    _ = os.system("clear")
    print(HANGMANINTRO)
    print(HANGMANPICS[len(HANGMANPICS) - n_lives - 1])
    print(f"{DELIMITER}{n_lives}/{MAX_LIVES} LIVES LEFT{DELIMITER}\n")
    print("Word to guess: " + "".join(unknown_word))


def hangman() -> tuple[int, str]:
    """Play the hangman game"""
    global n_lives, n_blanks

    # Choose a word from the word list
    chosen_word = list(random.choice(word_list))
    n_blanks = len(chosen_word)
    unknown_word = list("_" * n_blanks)

    # Ask the user to make a guess, lowercase letters only
    while n_lives != 0:
        render_screen(n_lives, unknown_word)
        # Get a letter from the user
        guess = input("Guess a letter: ").lower()
        found_letter = False

        # Check if the letter is in the chosen word and replace all occurences
        for idx, letter in enumerate(chosen_word):
            if guess == letter:
                unknown_word[idx] = guess
                n_blanks -= 1
                found_letter = True

        # Did we find a letter? if not, deduct a life
        if not found_letter:
            n_lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            time.sleep(2)

        # Have we found all letters? Break from this loop
        if n_blanks == 0:
            break

    # Finally, Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right"
    # if it is, "Wrong" if it's not.
    render_screen(n_lives, chosen_word)
    if n_blanks == 0:
        retval = prompt_win
    else:
        retval = prompt_lose
    print(retval)
    return n_lives, retval


if __name__ == "__main__":
    hangman()
