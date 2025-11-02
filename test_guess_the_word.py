# Simone Lojeck
# 11/01/2025
# CIS256 33284, Fall 2025
# Exercise 4.0 (EX4) - Tests Game

# Note: SL 11/1/2025: Able to run in Terminal with 'pytest -s' command.
# Runs through the full game then performs tests. -->  All 5 passed in 25.68s.

# import game and functions to test
from guess_the_word import select_word, process_guess

# Define Test Functions
def test_select_word():
    """ Function: Test select_word function - assert selected word in word list """
    words = ["Defiant", "Enterprise", "Serenity", "Nostromo"]
    selected_word = select_word(words)
    assert selected_word in words  # make sure the word is from the list

def test_process_guess_correct_guess():
    """ Function: Test process_guess function for correct guess - assert for each output"""
    # Case: Correct guess of letter in middle of the word
    word = "Enterprise"
    index = 3
    guess = "e"
    num_guesses = 5
    index, endgame = process_guess(word, index, guess, num_guesses)
    assert index == 4        # correct guess so index is incremented
    assert endgame == False  # Endgame is False

def test_process_guess_incorrect_guess():
    """ Function: Test process_guess function for incorrect guess - assert for each output """
    # Case: Incorrect guess of letter in middle of the word
    word = "Enterprise"
    index = 5
    guess = "z"
    num_guesses = 12
    index, endgame = process_guess(word, index, guess, num_guesses)
    assert index == 5         # incorrect guess so no change to index
    assert endgame == False   # Endgame is False

def test_process_guess_endgame_Fail():
    """ Function: Test process_guess function for running out of guesses - assert for each output """
    # Case: Incorrect guess of letter in middle of the word with no guesses left -> End of Game
    word = "Enterprise"
    index = 6
    guess = "z"
    num_guesses = 0
    index, endgame = process_guess(word, index, guess, num_guesses)
    assert index == 6        # incorrect guess so no changes to index
    assert endgame == True   # Endgame changed to True since out of guesses

def test_process_guess_endgame_Win():
    """ Function: Test process_guess function for completing guess of word - assert for each output """
    # Case: Correct guess of letter at end of word -> End of Game
    word = "Enterprise"
    index = 9
    guess = "e"
    num_guesses = 10
    index, endgame = process_guess(word, index, guess, num_guesses)
    assert index == 9       # no change to index as the end of the word was reached
    assert endgame == True  # Endgame changes to True since word guess was completed