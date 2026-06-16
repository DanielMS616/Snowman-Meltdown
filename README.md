# Snowman Meltdown

Snowman Meltdown is a small Python terminal game.

The player guesses letters to reveal a secret word. For every wrong guess, the snowman melts step by step. The game ends when the player has guessed the complete word or when the snowman has completely melted.

## Features

* Random secret word selection
* Snowman ASCII art
* Input validation for single letters
* Check for already guessed letters
* Clear game display with word progress, guessed letters and mistakes
* Replay option after each game
* Session score tracking for wins and losses
* External word list with fallback words

## How to run

Run the game from the project folder with:

```bash
python3 snowman.py
```

## Project structure

```text
snowman.py       Starts the game
game_logic.py    Contains the main game logic
ascii_art.py     Contains the snowman ASCII art stages
words.txt        Contains optional custom words
README.md        Describes the project
```

## Word list

The game tries to load secret words from `words.txt`.

Each word should be written on a separate line:

```text
terminal
commit
branch
repository
function
```

If `words.txt` does not exist or is empty, the game uses the default word list from the code:

```python
["python", "git", "github", "snowman", "meltdown"]
```

## How to play

1. Start the game.
2. Guess one letter at a time.
3. Correct guesses reveal letters in the secret word.
4. Wrong guesses melt the snowman.
5. The game ends when the word is guessed or the snowman has melted.
6. After each round, the player can choose to play again.

## Example

```text
Welcome to Snowman Meltdown!

==============================
SNOWMAN MELTDOWN
==============================

      ___
     /___\
     (o o)
     ( : )
     ( : )

Word: _ _ _
Guessed letters: none
Mistakes: 0/3
------------------------------

Guess a letter:
```

## Requirements

This project uses only Python standard library modules.

No additional packages are required.

## Author

Created as part of a Python and Git/GitHub learning project.
