# -------------------------------------
# Title:        Intro to Selection
# Author:       Clint MacDonald
# Date:         Sept. 18, 2025
# Purpose:      Learning IF and Match structures
# -------------------------------------

# conditional statements

# expressions using one or more comparator that results in a boolean value

x = 5
y = 7
z = x < 7

x = 5
y = 7
z = 9
answer = x < y and z < y


#  ------------------------------
# example 2

# Menu System

menu = '''--- Main Menu ---
1. New Game
2. Continue
3. Options
4. Exit to Desktop
'''

print(menu)
user_input = input("Enter your choice (1-4): ")

if user_input == '1':
    print("You chose to start a new game!")
elif user_input == '2':
    print("You chose to continue an existing game!")
elif user_input == '3':
    print("You want to set the options!")
elif user_input == '4':
    print("Good-bye")
    exit()
else:
    print("Dummy, that was not an option!")



## -- where order matters

percentage_grade = input("Enter Your grade as a decimal: ")

if not percentage_grade.replace(".","").isdigit():
    print("That was not a number!")
    exit()

percentage_grade = float(percentage_grade)

letter_grade = ""
gpa = 0.0

if percentage_grade >= 90:
    letter_grade = 'A+'
    gpa = 5.0
elif percentage_grade >= 85:
    letter_grade = "A"
    gpa = 4.5
elif percentage_grade >= 80:
    letter_grade = "A-"
    gpa = 4.0
elif percentage_grade >= 75:
    letter_grade = "B+"
    gpa = 3.5
elif percentage_grade >= 70:
    letter_grade = "B"
    gpa = 3.0
else:
    letter_grade = "F"
    gpa = 0.0



# output the answer
print("Your grade of %.2f gives you a %s and a gpa of %.1f" %(percentage_grade, letter_grade, gpa))



#  match algorithm
print("\n")
print("-"*43)
print(menu)
user_input = input("Enter your choice (1-4): ")

match user_input:
    # New Game
    case "1":                                               # New Game
        print("You chose to start a new game!")
    case "2":                                               # Continue Game
        print("You chose to continue an existing game!")
    case "3":                                               # Options
        print("You want to set the options!")
    case "4":                                               # Exit
        print("👋 Good-bye")
        exit()
    case _:
        print("❌ Invalid choice.")


#  PRACTICE EXERCISE
# 1 - redo the C to F converter, where the user enters the temperature followed by a c or an f, and the program converts it to the other one.

# 2 - make a calendar reminder....
# have the user type in the day of the week, and the program will tell the user what they are doing that day!  (Make it up)  Do not limit the user to typing a specific case!