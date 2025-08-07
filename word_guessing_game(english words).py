# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 17:16:00 2025

@author: Nasimjon
"""
# Importing the word list and the random module
from beginner_words import words
import random as r

# Function to choose a random word from the word list
def get_word(words):
    word = words[r.randrange(0, 1000)]  # Picks a word using a random index
    return word.upper()  # Convert it to uppercase for consistency

# Function to return the hidden version of the word based on guesses
def hide(word, guess):
    new_word = ""
    for w in word:
        if w not in guess:
            new_word += "-"  # Hide letters that haven't been guessed
        else:
            new_word += w   # Show guessed letters
    return new_word

# Main game logic
def play():
    word = get_word(words)  # Select a random word
    print(f"I have guessed a {len(word)}-letter English word.\nCan you guess the letters?")
    
    user_letters = ""           # Letters guessed by the user so far
    word_letters = set(word)   # Unique letters in the word to be guessed

    while len(word_letters) > 0:
        print(hide(word, user_letters))  # Show the word with guessed letters revealed

        if len(user_letters) > 0:
            print(f"Your guesses so far: {user_letters}")

        letter = input("Input your guess: ").upper()  # Ask the user for a new letter

        # Check if the letter has already been guessed
        if letter in user_letters:
            print("❗ You have used this letter before! Try another one.")
            continue

        # If the guessed letter is correct
        elif letter in word:
            word_letters.remove(letter)  # Remove it from the set of remaining letters
            print(f"✅ {letter} is correct!")

        # If the guessed letter is not in the word
        else:
            print("❌ This letter is not in the word.")

        user_letters += letter  # Add the guessed letter to the list

    # Game over message
    print(f"\n🎉 Congratulations! You have found the word **{word}** in {len(user_letters)} attempts.")

# Run the game
play()

     
         
        
    
    






    
    