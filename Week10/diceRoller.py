# -------------------------------------
# Title:        Rolling Any Dice
# Author:       Clint MacDonald
# Date:         Nov. 11, 2025
# Purpose:      To demonstrate importing a library of tools
# -------------------------------------

#region IMPORTS
import tools
#endregion

#region CONSTANTS AND GLOBAL VARIABLES
num_dice = 0
WELCOME_MESSAGE = 'How many dice and how many sides!'
ALLOWABLE_SIDES = [4, 6, 8, 10, 12, 20]
#endregion

#region CUSTOM FUNCTIONS
def get_number_of_sides():
    '''gets input from the user on the number of sides of a dice, given the restrictions of dice that exist.'''
    isValid = False
    while not isValid:
        num_sides = tools.getIntInRange("How many sides (" + str(ALLOWABLE_SIDES) + ")?", 4, 20)
        # data validate
        if num_sides in ALLOWABLE_SIDES:
            isValid = True
    # end of loop
            
    return num_sides

def roll_dice(num_dice: int, num_sides: int):
    '''Given the number of dice and the number of sides, roll the random dice and return the total roll'''
    total = 0
    for dice in range(0,num_dice):
        total += tools.getRandIntRange(1, num_sides)
    return total

#endregion

#region MAIN PROGRAM
def main():
    '''Main Function to organize the structure of the program'''
    print(WELCOME_MESSAGE)

    # create a loop to try again
    doAgain = True
    while doAgain:
        # ask the user for which kind of dice
        num_sides = get_number_of_sides()
        # ask the user for how many dice
        num_dice = tools.getIntInRange("How many dice?", 1, 12)
        # output the random total rolled
        total = roll_dice(num_dice, num_sides)
        print("You rolled a %i" % total)

        doAgain = input("Do you want to roll again (y/n)?")[0].strip().lower() == 'y'

#endregion

main()
print("Good-bye!")
exit()
