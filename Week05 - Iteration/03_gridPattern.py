# ------------------------------------
# Title: Grid Pattern
# Author: Clint MacDonald
# Date: Oct. 2, 2025
# Description: Draws a grid pattern using loops
# ------------------------------------

# Draw a square of stars spaced out by one space, the width of the square is based on user input. Width is between 1 and 20.  The user will enter a 0 to exit.

# IMPORTS or INCLUDES
# no imports are required for this program

# DECLARE CONSTANTS and GLOBAL VARIABLES
# declare 1 and the 20 as constants
MIN = 1
MAX = 20
EXIT_CONDITION = 0
LINE_WIDTH = 60
SYMBOL = "*"

# declare a boolean variable for looping purposes
doContinue = True

# IIPO
# INFORMATION AND INSTRUCTIONS
# greeting and basic concepts
print('-'*LINE_WIDTH)
print("Welcome to the square grid program!")
print("The user will enter an integer and the program will print a square grid of '*' representing that size!")

# START OF MAIN LOOP
while doContinue:
    print('-'*LINE_WIDTH)

    # INPUT
    # prompt the user, receive the value, store the value
    # convert input to an integer
    # exception handling
    isValid = True
    try:
        width = int(input("Please enter the width of the grid: (%i-%i, %i to exit): " % (MIN, MAX, EXIT_CONDITION)))

        # check for the exit condition (0) 
        if width == 0:
            doContinue = False
            isValid = False

        # validation
        if width < 0 or width > 20:
            print("You must enter a number between %i and %i" % (MIN, MAX))
            isValid = False

    # Error on data conversion
    except ValueError:
        print("Please enter an integer! - Try Again!")
        isValid = False

    # all other errors
    except Exception:
        print("An error occurred!  Try Again!")
        isValid = False

    # PROCESSING
    if isValid:
            
        # process the rows
        for row in range(width):

            # start a row
            rowString = ""

            # within that row complete each column
            for column in range(width):
                rowString = rowString + SYMBOL + " "

            print(rowString)


# END OF MAIN LOOP

# OUTPUT
# good-bye and exit
print("Good-Bye!")
exit()
