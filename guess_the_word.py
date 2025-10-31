# Simone Lojeck
# 10/30/2025
# CIS256 33284, Fall 2025
# Exercise 4.0 (EX4) - Game to guess

import random

# Welcome message
print('*' * 40)
print("   Welcome to the Guess The Word Game!  ")
print("  the topic is Space Shuttle Names")
print('*' * 40)

# Define word list
words = ['Enterprise', 'Columbia', 'Challenger', 'Discovery',
         'Atlantis', 'Endeavour']

# Set # of guesses
num_guesses = 20
print(f"You have {num_guesses} chances to guess the name.")

# select random word
word = random.choice(words)

index = 0 # starting index
while num_guesses > 0:
    num_guesses -= 1 # reduce number

    # Prompt user to guess one letter at a time
    guess = input(f"\nGuess the letter of the word: ").lower()

    # If correct, reveal letter
    if (guess == word[index].lower()):
        print(f"Correct! '{guess}' is the next letter!!  You have {num_guesses} guesses left.")

        # If final letter in word, They won!
        if index == len(word) - 1:
            print(f" ***  CONGRATULATIONS!!! YOU WON!!  The ship was {word}")    # end game
            break # end game
        else:
            index += 1  # Increment to next letter
            print(f"index = {index}")

    # If incorrect, note wrong letter
    else:
        print(f"Sorry, {guess} is not the next letter.  You have {num_guesses} guesses left.")

        # If they are out of guesses, They lost
        if num_guesses == 0:
            print(f" ***  GAME OVER....You are out of guesses. The ship was '{word}'") # end game

