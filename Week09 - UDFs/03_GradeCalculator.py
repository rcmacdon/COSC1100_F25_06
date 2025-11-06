# -------------------------------------
# Title:        Student Grade Calculator
# Author:       Clint MacDonald
# Date:         Nov. 6, 2025
# Purpose:      To see and practice more examples of implementing functions
# -------------------------------------

#region IMPORTS
#endregion

#region DECLARATIONS
WELCOME_MESSAGE = '''Welcome to the grade calculator.'''
MAIN_MENU = '''Main Menu
---------------------------
1. Add a student grade
2. Find a student grade
3. Show Statistics
4. Show all grades
5. Exit'''

MIN_GRADE = 0.0
MAX_GRADE = 100.0
students = []
grades = []     # using index number to match student to grade!

#endregion

#region FUNCTIONS
    #region INPUT FUNCTIONS
    # get a string
def getString(prompt: str):
    user_input = ""

    while len(user_input.strip()) < 1:
        user_input = input(prompt)

    return user_input


    # get a float in a range
def getFloatInRange(prompt: str, min: float, max: float):
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

    #region CUSTOM FUNCTIONS
def addStudent():
    # Get student name and grade
    name = getString("Please enter the student name: ")
    grade = getIntInRange("Please enter the student grade (%f-%f):" % (MIN_GRADE, MAX_GRADE), MIN_GRADE, MAX_GRADE)

    # add to the arrays
    students.append(name)
    grades.append(grade)

def findStudent():
    # get name from user
    name = getString("Please enter the student name: ") 
    # find index number in students array for entered name (make a function)
    index = findStudentIndexNumber(name)
    # use index number to get grade from grades array
    if index > -1: 
        print("%s got %.2f percent" % (name, grades[index]))


def showStats():
    # calculate average (make a function for that)
    print("The average is: %.2f" % calcAverageGrade())
    # calculate min (make a function)
    print("The minimum grade was: %.2f" % findMinGrade())
    # calculate max (make a function)
    print("The maximum grade was: %.2f" % findMaxGrade())

def showAllGrades():
    # print a table of grades
    print("%20s %6s" % ("Student", "Grade"))
    print("-"*26)
    for i in range (0,len(students)):
        print("%20s %6.2f" % (students[i], grades[i]))

def findStudentIndexNumber(name: str):
    # dependent on students array existing
    if name in students:
        #get the assiciated index number
        return students.index(name)
    else:
        print("That student could not be found")
        return -1
    #endregion

def calcSumGrades():
    sum = 0
    for grade in grades:
        sum += grade
    return sum

def calcAverageGrade():
    sum = calcSumGrades()
    count = len(grades)
    if count > 0:
        return float(sum)/float(count)
    return 0

def findMinGrade():
    min = MAX_GRADE
    for grade in grades:
        if grade < min:
            min = grade
    return min

def findMaxGrade():
    max = MIN_GRADE
    for grade in grades: 
        if grade > max: max = grade
        
    return max



#endregion

#region MAIN PROGRAM

# Welcome message
print(WELCOME_MESSAGE)
menu_choice = 0
while menu_choice != 5:
    # Show Main Menu
    print(MAIN_MENU)
    menu_choice = getIntInRange("Enter your choice (1-5): ", 1, 5)

    # Process the menu
    if menu_choice == 1:    addStudent()
    elif menu_choice == 2:  findStudent()
    elif menu_choice == 3:  showStats()
    elif menu_choice == 4:  showAllGrades()

print("Good-bye!")

#endregion