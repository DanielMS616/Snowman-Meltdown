import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""

    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """Starts the Snowman Meltdown game"""

    secret_word = get_random_word()

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Empty game loop. More game logic will be added later.
    game_running = True

    while game_running:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        # Stop the loop for now, so the program only asks once.
        game_running = False


if __name__ == "__main__":
    play_game()