🕹️ Word Guessing Game (Hangman Style)
This is a fun and interactive command-line game where the computer picks a random English word, and the player tries to guess it letter by letter.

You win the game by correctly guessing all the letters in the hidden word.

🚀 Features
Random word selection from a word list

Hides unguessed letters with dashes (e.g., P--H--)

Tracks and displays your previous guesses

Tells you if a guess is correct or incorrect

Finishes when all letters are guessed correctly

📁 Requirements
Python 3.x

A beginner_words.py file containing a list named words (e.g., words = ["python", "code", "developer", ...])

▶️ How to Run
Make sure your project folder includes:

your_game_script.py

beginner_words.py

Run the game using:

bash
Copy
Edit
python your_game_script.py
📄 Example Output
less
Copy
Edit
I have guessed a 6-letter English word.
Can you guess the letters?
------
Input your guess: p
P-----
Your guesses so far: P
Input your guess: o
P--O--
...
🎉 Congratulations! You have found PYTHON in 8 attempts
