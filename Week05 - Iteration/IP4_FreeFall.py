# --------------------------------------
# Title:    Free Fall Calculations
# Author:   Clint MacDonald
# Date:     Feb. 4, 2025
# Purpose:  To calculate the time it takes for an object to fall 
#           to the ground mapping it's location each time interval.
# --------------------------------------

# PROBLEM: Create a program that calculates the time it takes for an 
# object to fall to the ground while outputting the exact position 
# of the object height of the object at each time interval.

# Only after the object hits the ground, you can use the actual formula to 
# determine at the exact time the object will hit the ground.

# The height of the object will be a random number between 50m and 400m.  The user will input the time interval where each measurement will be shown.  The time interval should be between 0.1 and 1 second.

# The program will output the estimated time it takes for the object
# to fall to the ground, represented by position 0.

# The free fall equation is: h = gt^2/2 + v0t + h0 but v0 = 0
# and the time to hit the ground is calculated by: t = sqrt(2h/g) where g is positive
import random

# --------------------------------------
# Global Constants
# --------------------------------------
GRAVITY = -9.81  # acceleration due to gravity (m/s^2)

# --------------------------------------
# Greet User and Explain the program
print("""Welcome to the Free Fall Calculator!
This program will calculate the time it takes for an object to fall to the ground.

By entering an objects starting height and a time interval, the user will receive the relative position of the object at each time interval in addition to knowing when the object hits the ground.""")

# --------------------------------------
# Start Loop
doAgain = True
while doAgain:
    isValid = True
    print("-"*60)
    # --------------------------------------
    # Get User Input
    initial_height = random.randrange(50,400)

    print("The starting height will be %i meters!" % initial_height)
    time_interval = input("Enter the time interval for each position calculation in seconds (0.1 - 1.0): ")

    # --------------------------------------
    # Data Validation
    # Check if the user input for initial height is a positive number

    try:
        # Check if the user input for time interval is a positive number
        time_interval = float(time_interval)

        if not 0.1 <= time_interval <= 1.0:
            print("The time interval should be between 0.1s and 1.0s!")
            isValid = False
    except ValueError:
        print("Invalid input. Please enter a positive number for the time interval.")
        isValid = False


    # --------------------------------------
    # Initialize Variables
    time = 0
    height = initial_height

    if isValid:
        while height > 0:
            
            # output starting height and time
            print(f"At time {time:.2f} seconds, the object is at height {height:.2f} meters.")

            # update data for end of time interval
            time += time_interval
            height = GRAVITY * time**2 / 2 + float(initial_height)

            if height < 0:
                time = (-2*initial_height/GRAVITY)**0.5
                height = 0

                # output final time
                print(f"The object hits the ground at {time:.2f} seconds.")
            
        # --- end while ---

        choice = input("Would you like to calculate another object's fall? (y/n): ")
        if choice.lower() != "y":
            doAgain = False

print("Thank you for using the Free Fall Calculator! Good-bye")
exit()