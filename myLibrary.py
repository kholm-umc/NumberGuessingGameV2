# Nicely display error messages
def displayErrorMessage(message="An unknown error occurred", exception="Unknown exception"):
    print()
    print(" ERROR ".center(30, "*"))
    print(f"{message}")
    print(f"Exception: {exception}")
    print(" EXITING THE GAME ".center(30, "*"))
    print()
    return True


# Once a guess is made, this function will look at the guess and determine
#  if the guess is high, low, or correct.
# This function returns two values:
#  numberOfGuesses, incremented by 1
#  correctGuess, 0 == False, 1 == True
def testGuess(playerGuess="0", numberOfGuesses="0", someNumber=0, playerName="Anonymous"):
    correctGuess = 0

    # Is the guess a number?  If so, we can process it as such
    if str.isnumeric(playerGuess):

        # Guessing out of bounds?  That's a no-no
        if int(playerGuess) < 1 or int(playerGuess) > 100:
            print()
            print(" Integers from 1 to 100 only! ".center(30, "*"))
            print()

        # Test for a low guess
        elif int(playerGuess) < someNumber:
            numberOfGuesses = numberOfGuesses + 1
            print(f"{playerGuess} is too low.  Guess again.")

        # Test for a high guess
        elif int(playerGuess) > someNumber:
            numberOfGuesses = numberOfGuesses + 1
            print(f"{playerGuess} is too high.  Guess again.")

        # Woohoo!  Correct guess.  Winner, winner, chicken dinner!
        else:
            numberOfGuesses = numberOfGuesses + 1
            print()
            print(f" {playerGuess} IS CORRECT! ".center(30, "*"))
            print(f"It took you {numberOfGuesses} guesses, {playerName}!")
            print()
            correctGuess = 1

    # Allow the player to put in nothing; but, do not _do_ anything
    elif len(playerGuess) < 1:
        print()
        print(" Integers from 1 to 100 only! ".center(30, "*"))
        print()

    # If the guess is not a number, does the player want to quit?
    elif playerGuess.lower()[0] == "q":
        correctGuess = 2

    # Well, we only want digits
    else:
        print()
        print(" Integers from 1 to 100 only! ".center(30, "*"))
        print()

    return numberOfGuesses, correctGuess


# Read the scores from the score file
# Break each line into component parts
# Add our new score to the list
# Sort
# Write our scores back to the file
def updateScores(playerName, numberOfGuesses):
    # We will need a couple of lists to
    #  track our scores while sorting
    lines = []
    tempList = []
    quit = False

    try:
        # Read the scores into our lines list
        scoresFile = open("topPlayers.txt", "r")
        for eachLine in scoresFile.readlines():
            lines.append(eachLine)

        scoresFile.close()

        # One line of code, to demonstrate the following
        # numberOfGuesses = 30
        # newScore = str(numberOfGuesses)
        # newScore = "30"
        # newScore = newScore + "          " # 10 spaces
        # newScore = "30" + "          "
        # newscore = "30          "
        # newscore = newScore[0:10] # First 10 characters
        # newScore "30         "
        # newScore = newScore + playerName
        # newScore = "30        " + "Ken"
        # newScore = "30        Ken"
        newScore = str(str(numberOfGuesses) + "          ")[0:10] + playerName
        lines.append(newScore)

        # Now, we must do some sorting magic
        # For each line:
        #   Split the components into score and name
        #   Add a bunch of zeroes to the beginning of each score
        #   Grab the last ten digits from each score
        #   Fill our temporary list with the zero-paddes score and name
        #     separated by a colon
        # "30        Ken"
        for aSingleScore in lines:
            [score, name] = aSingleScore.split(" ", 1)
            score = "0000000000" + score
            # score = "000000000030"
            score = score[-10:]
            # score = "0000000030"
            tempList.append(score + ":" + name.strip())
            # "0000000012:Ken"
            # "0000000007:Joe"
            # "0000000007:Bob"
            # "0000000018:Sue"
            # "0000000032:Dan"

            # Sorted
            # "0000000007:Bob"
            # "0000000007:Joe"
            # "0000000012:Ken"
            # "0000000018:Sue"
            # "0000000032:Dan"

        # We can now safely sort our list of scores, regardless of
        #  how many digits are in the score (up to 9,999,999,999)
        tempList.sort()

        # We have used this list before, now we need to
        #  reuse it.  However, we need to clear it out first
        lines.clear()

        # Now that we have a nicely sorted list, we need to
        #  format it properly.
        # For each line:
        #   Split the components into score and name
        #   Remove the preceding zeroes from the scores
        #   Reassemble our scores, nicely formatted, into our
        #    original list
        #   Only grab the first five scores though
        for aSingleScore in tempList[0:5]:
            [score, name] = aSingleScore.split(":")
            newScore = str(str(int(score)) + "          ")[0:10] + name
            lines.append(newScore)

        # And, write the file back out
        scoresFile = open("topPlayers.txt", "w")
        for eachScore in lines:
            scoresFile.write(eachScore + " \n")

        scoresFile.close()

    #  Cannot find the file?
    except FileNotFoundError as exception:
        quit = displayErrorMessage("Unable to locate the file to update the scores.", exception)

    # Some unknown error
    except Exception as exception:
        quit = displayErrorMessage("An unknown error has occurred when trying to update the scores.", exception)

    finally:
        return quit


def displayScores():
    quit = False
    try:
        print(" TOP PLAYERS ".center(30, "*"))
        scoresFile = open("topPlayers.txt", "r")
        scores = scoresFile.read()
        scoresFile.close()
        print(scores)
        print()
    except Exception as exception:
        quit = displayErrorMessage("An unknown error has occurred when trying to update the scores.", exception)
    finally:
        return quit

