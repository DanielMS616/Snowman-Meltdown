"""Contains the main game logic for Snowman Meltdown."""

import random

from ascii_art import STAGES

# Default list of secret words
DEFAULT_WORDS = ["python", "git", "github", "snowman", "meltdown"]
WORDS_FILE = "words.txt"


def load_words():
    """
    Loads words from an external file.
    If the file does not exist or is empty, the default word list is used.
    """

    try:
        with open(WORDS_FILE, "r") as fileobj:
            lines = fileobj.readlines()

        words = []

        for line in lines:
            word = line.strip().lower()

            if word != "" and word.isalpha():
                words.append(word)

        if len(words) > 0:
            return words

        return DEFAULT_WORDS

    except FileNotFoundError:
        return DEFAULT_WORDS


def get_random_word():
    """Selects a random word from the word list."""

    words = load_words()

    return words[random.randint(0, len(words) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current snowman stage and the guessed word.
    Unknown letters are shown as underscores.
    """

    max_mistakes = len(STAGES) - 1

    print()
    print("=" * 30)
    print("SNOWMAN MELTDOWN")
    print("=" * 30)

    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if len(guessed_letters) > 0:
        print("Guessed letters:", ", ".join(guessed_letters))
    else:
        print("Guessed letters: none")

    print(f"Mistakes: {mistakes}/{max_mistakes}")
    print("-" * 30)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Checks if all letters of the secret word have been guessed."""

    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True


def get_valid_guess(guessed_letters):
    """
    Ask the user for a single alphabetic letter.
    Keeps asking until the input is valid and not guessed before.
    """

    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def ask_play_again():
    """
    Ask the user if they want to play again.
    Keeps asking until the user enters y or n.
    """

    while True:
        answer = input("Do you want to play again? (y/n): ").lower().strip()

        if answer == "y":
            return True

        if answer == "n":
            return False

        print("Please enter y or n.")


def play_game():
    """Starts the Snowman Meltdown game.
    Returns True if the player won, False otherwise.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)

        if guess in secret_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            mistakes += 1
            print("Wrong guess!")

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!")
        return True

    print("Game Over! The word was:", secret_word)
    return False


def main():
    """Runs the game, tracks the session score, and asks to play again."""
    play_again = True

    score = {"wins": 0, "losses": 0}

    while play_again:
        game_won = play_game()

        if game_won:
            score["wins"] += 1
        else:
            score["losses"] += 1

        print()
        print("Current Score")
        print(f"Wins: {score['wins']} | Losses: {score['losses']}")
        print()
        print("=" * 30 + "\n")

        play_again = ask_play_again()

    print("Thanks for playing Snowman Meltdown!")