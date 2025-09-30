# -------------------------------------
# Title:        Week 5 - Iteration Example - Menu
# Author:       Clint MacDonald
# Date:         September 30, 2025
# Purpose:      Learning how to loop a real concept
# -------------------------------------

MENU_STRING = '''Main Menu
--------------------
1. Continue Game
2. New Game
3. Options
4. Quit'''

userChoice = "1"

while userChoice != "4":
    print(MENU_STRING)
    userChoice = input("Make your choice (1-4): ")
    
    if userChoice == "1":
        print("You chose to continue a game!")
    elif userChoice == "2":
        print("You chose to start a new game!")
    elif userChoice == "3":
        print("Showing you the options!")
    elif userChoice == "4":
        continue
    else:
        print("Invalid choice, try again!")
    
    print('-'*60)



print("Good-bye")
exit()