"""
Author: Ken Holm
Purpose: Upgrade our number guessing game.

Guessing Game
Randomly choose a number between 1 and 100.
Have the player enter a guess
Tell the player the guess is high, low, or on the money
If high or low, allow another guess
Give the player an option to quit at any time
Reward the player for a correct guess
Tell the player how many guesses it took to guess correctly

"""

from random import randint
from myLibrary import *

# Initialize our variables
numberOfGuesses = 0
correctGuess = 0
playerGuess = ""
playerWantsToQuit = False
someNumber = randint(1, 100)

# Print our instructions
print("Guess-a-Number")
print("Rules:")
print("* Enter a guess between 1 and 100")
print("* Guess again if your guess is high or low")
print("* You can enter the letter 'q' to quit")
print("Good luck!")
print()
try:
    playerName = input("Player, what is your name? ")
    if (len(playerName) < 1):
        playerName = "Anonymous"
except EOFError as exception:
    print("Quitting already?")
    exit(0)
except Exception as exception:
    print("Looks like there was a hiccup.  I will call you Anonymous")

# Loop until the player wants to quit
while True:

    try:
        # Begin our guessing loop
        while correctGuess == 0:

            # Gather the player's guess
            try:
                playerGuess = input("What is your guess? ")
            except EOFError as exception:
                print("Quitting already?")
                exit(0)

            except Exception as exception:
                print(f"An error has occurred.")
                print(f"Exception: {exception}")
                print()
                playerWantsToQuit = True

            # Test the player's guess
            try:
                numberOfGuesses, correctGuess = testGuess(playerGuess, numberOfGuesses, someNumber, playerName)
                if correctGuess == 2:
                    playerWantsToQuit = True
            except ValueError as exception:
                playerWantsToQuit = displayErrorMessage("An unknown error has occurred when trying to update the scores.", exception)
            except Exception as exception:
                playerWantsToQuit = displayErrorMessage("An unknown error has occurred when trying to update the scores.", exception)

        # If we have thrown an exception, we need to skip this block.
        #  Otherwise, we can continue.
        if not playerWantsToQuit:

            # Update the scores
            try:
                playerWantsToQuit = updateScores(playerName, numberOfGuesses)
            except Exception as exception:
                playerWantsToQuit = displayErrorMessage("An unknown error has occurred when trying to update the scores.", exception)

            # If we have thrown an exception, we need to skip this block.
            #  Otherwise, we can continue.
            if playerWantsToQuit != True:
                try:
                    playerWantsToQuit = displayScores()
                except Exception as exception:
                    playerWantsToQuit = displayErrorMessage("An unknown error has occurred when trying to update the scores.", exception)

                # Continue on if we do not have an error
                if playerWantsToQuit != True:
                    print("Would you like to play again?")
                    if input("Enter 'q' to quit anything else to play again. ").lower() == "q":
                        playerWantsToQuit = True
                    else:
                        someNumber = randint(1, 100)
                        numberOfGuesses = 0
                        playerGuess = ""
                        correctGuess = 0
                        playerWantsToQuit = False

        # Quitting?  Print out a nice message
        if playerWantsToQuit:
            print()
            print(" GAME OVER ".center(30, "*"))
            if correctGuess == 2:
                print(f"The correct number was {someNumber}.")
            print(f"Thank you, {playerName}, for playing.  I enjoyed it.")
            print(" GAME OVER ".center(30, "*"))
            print()
            break
    except EOFError as exception:
        print(f"No hard feelings.  The game is now over.")
        break

    except Exception as e:
        print(f"Looks like there was a glitch.  Ending the game nicely.")
        break
