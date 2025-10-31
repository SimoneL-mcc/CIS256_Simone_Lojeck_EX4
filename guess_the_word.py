# Simone Lojeck
# 10/30/2025
# CIS256 33284, Fall 2025
# Exercise 4.0 (EX4) - Game to guess

import random

# Define word list
words = ['Enterprise', 'Columbia', 'Challenger', 'Discovery',
         'Atlantis', 'Endeavour']
topic = 'Space Shuttle Names'
# Expansion: include other topics & word lists..possibly as a dictionary or other structure

# select random word
word = random.choice(words)
# Expansion: random choice of topic, and then word from topic's list

# Welcome message
print('*' * 40)
print("   Welcome to the Guess The Word Game!  ")
print(f"  the topic is {topic}")
print('*' * 40)

# Set # of guesses
num_guesses = 20
print(f"--> You have {num_guesses} chances to guess the name.")

# Loop through for each guess
index = 0 # starting index
while num_guesses > 0:
    num_guesses -= 1 # reduce number of guesses

    # Prompt user to guess one letter at a time
    guess = input(f"\nGuess the letter of the word: ").lower()

    # If correct, reveal letter
    if (guess == word[index].lower()):
        print(f"Correct! '{guess}' is the next letter!!  You have {num_guesses} guesses left.")

        # If final letter in word, They won!
        if index == len(word) - 1:
            print(f"\n\n ***  CONGRATULATIONS!!! YOU WON!!  The ship was {word}")    # end game
            break # end game
        else:
            index += 1  # Increment to next letter

    # If incorrect, note wrong letter
    else:
        print(f"Sorry, '{guess}' is not the next letter.  You have {num_guesses} guesses left.")

        # If they are out of guesses, They lost
        if num_guesses == 0:
            print(f"\n\n ***  GAME OVER....You are out of guesses. The ship was '{word}'") # end game

