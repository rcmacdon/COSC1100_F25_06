# -------------------------------------
# Title:        Guess the Number Game
# Author:       Clint MacDonald
# Date:         Nov. 4, 2025
# Purpose:      To learn modularity and functions in practice
# -------------------------------------

#region Design Concepts
'''
IDFIIPO
Imports
Declarations
Functions
Information
Input
Processing
Output
'''
#endregion

#region IMPORTS
import random
#endregion

#region DECLARATIONS
theNumber = 0
MIN_NUMBER = 1
MAX_NUMBER = 100
prompt = "Guess a number between %i and %i!" % (MIN_NUMBER, MAX_NUMBER)
#endregion

#region FUNCTIONS
def greetUser():
    '''A simple function that greets the user and gives instructions!'''
    greeting = '''-----------------------------------
    Welcome the the Guess the number game!
    -----------------------------------'''
    instructions = '''The computer will pick a random number between %i and %i.  You will try to guess the number repeatidly, until you get it correct.  The computer wil respond with Too High, Too Low, or Correct!''' % (MIN_NUMBER, MAX_NUMBER)
    print(greeting)
    print(instructions)

def getRandomNumber(min: int, max: int):
    '''Generates a random number between min and max, requires the random library to be imported.'''
    return random.randint(min, max)

def getIntFromUser(prompt, min: int, max: int):
    '''Receive a number between min and max from the user.  This depends on the console window.'''
    is_valid = False
    while not is_valid:
        try:
            tempNum = int(input(prompt))

            if not min <= tempNum <= max:
                print("Must be between %i and %i" % (min, max))
            else:
                return tempNum
        except ValueError as v:
            print("Invalid Input, must be an integer!")

def checkIfNumberCorrect(actualNumber, guessedNumber):
    '''Compares two numbers to see if the second is too high, too low, and the same'''
    isCorrect = False
    if guessedNumber > actualNumber:
        print("Too High!")
    elif guessedNumber < actualNumber:
        print("Too Low!")
    else:
        isCorrect = True

    return isCorrect

#endregion

#region MAIN PROGRAM

# Greet the user and give instructions
greetUser()

goAgain = True
while goAgain:
    # Generate a random number
    theNumber = getRandomNumber(MIN_NUMBER, MAX_NUMBER)
    guess_count = 0

    # repeat until correct
    isCorrect = False
    while not isCorrect:
        # ask the user for a number
        # validate their input
        user_guess = getIntFromUser(prompt, MIN_NUMBER, MAX_NUMBER)

        # increment the guess count
        guess_count += 1

        # check if the number was correct 
        # respond with too high, too low, or success
        isCorrect = checkIfNumberCorrect(theNumber, user_guess)

    # output congrats with guess count 
    print("You got it in %i guesses" % guess_count)

    # try again?
    goAgain = (input("Do you want to try again (y/n)").lower)[0] == "y"



#endregion