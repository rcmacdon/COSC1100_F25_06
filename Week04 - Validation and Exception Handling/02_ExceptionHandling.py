# -------------------------------------
# Title:        Week 4 - Exception Handling
# Author:       Clint MacDonald
# Date:         Sept. 25, 2025
# Purpose:      Learning the Try Catch Scenario
# -------------------------------------

# Try-Catch-Raise-Finally structure

# syntax

# try:
#     do stuff
# except Exception as e:
#     what to do if something goes wrong (crash)
# finally:
#     occurs in BOTH scenarios (always executes)

# try:
#     userInput = input("Enter your favorite number: ")
#     sqrt = int(userInput) ** 0.5
#     print("The square root is: %.2f" % sqrt)
# except Exception as e:
#     print("Hey Dummy, that was not an integer!")


# try:
#     userInput = input("Enter your a number (can be a decimal): ")
#     userInput = float(userInput)
#     print("Conversion Successful")
#     print(10.0/ userInput)
# except ValueError as v:
#     print("That was not a number!")
# except ZeroDivisionError as z:
#     print("0 is an invalid division denominator!")
# except Exception as e:
#     print("An error occurred, try again later!")


try:
    userInput = input("Enter your a number (can be a decimal): ")
    userInput = float(userInput)
    print("Conversion Successful")

    try:
        print(10.0/ userInput)
    except ZeroDivisionError as z:
        print("0 is an invalid division denominator!")
    except Exception as e:
        print("2. An error occurred, try again later!")
    
    
except ValueError as v:
    print("That was not a number!")
except Exception as e:
    print("1. An error occurred, try again later!")









