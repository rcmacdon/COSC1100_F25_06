# --------------------------------------
# Title:    My Tools Library for Python Console Applications
# Author:   Clint MacDonald
# Date:     Nov. 11, 2025
# Purpose:  A set of tools to resuse in future applications
# Modified By:
# Modified Date:
# -------------------------------------

'''Note that this file does use print statements, meaning it will only function for Console Applications.  If you want to use a GUI, you will have to modify this library to not use print statements!'''

#region IMPORT
import random
#endregion

#region USER INPUT FUNCTIONS

# get a string
def getString(prompt: str):
    '''Prompt the user for a string based input.'''
    user_input = ""

    while len(user_input.strip()) < 1:
        user_input = input(prompt)

    return user_input

def getStringLengthRange(prompt: str, min: int, max: int):
    '''Prompt the user for a string based input where the length is within a given range.'''
    isValid = False
    while not isValid:
        user_input = input(prompt).strip()
        # validate the length
        if min <= len(user_input) <= max: return user_input

    # get a float in a range
def getFloatInRange(prompt: str, min: float, max: float):
    '''Prompt the user for input of a float type value within a given range.'''
    user_input = min - 1.0

    while user_input < min or user_input > max:
        try:
            user_input = float(input(prompt))

            if user_input < min or user_input > max:
                print("Please enter an number between %.2f and %.2f" % (min, max))
            
        except ValueError:
            print("Please enter only an number!")

    return user_input

    # get an integer
def getInt(prompt: str):
    '''prompt the user for any integer'''
    user_input = ""

    isValid = False
    while not isValid:
        try:
            user_input = int(input(prompt))
            isValid = True
        except ValueError:
            print("Please enter only an integer!")

    return user_input

    # get an integer in a range
def getIntInRange(prompt: str, min: int, max: int):
    '''Prompt the user for any integer within a given range'''
    user_input = min - 1

    while user_input < min or user_input > max:
        try:
            user_input = int(input(prompt))

            if user_input < min or user_input > max:
                print("Please enter an integer between %i and %i" % (min, max))
            
        except ValueError:
            print("Please enter only an integer!")

    return user_input

#endregion

#region RANDOM NUMBER GENERATIONS
def getRandIntRange(min: int, max: int):
    '''Returns a random integer within the given range.'''
    return random.randint(min, max)

def getRandFloatRange(min: float, max: float, numDec: int):
    '''Returns a random float within a given range with a given number of decimals!'''
    rnd = random.randint(min*(10**numDec), max*(10**numDec))/(10**numDec)
    return rnd
#endregion

