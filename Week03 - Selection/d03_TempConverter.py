# -------------------------------------
# Title:        Temperature Converter
# Author:       Clint MacDonald
# Date:         Sept. 16, 2025
# Purpose:      Convert C to F
# -------------------------------------

# Constants
TEMPERATURE_CONVERSION_RATIO = 9.0 / 5.0
TEMPERATURE_CONVERSION_CONSTANT = 32.0

# IIPO 

# Instructions
# greet the user
print("Welcome to the C to F temperature converter!")
# give some instructions that the user will enter C and get F
# celcius to fahrenheit
print('''You will be asked for a 
decimal temperature in 
Celcius and the Fahrenheit
equivalent will be returned''')
# Input
# get the C value from the user!  Returned as a string
user_input = input('Enter the temperature in Celcius: ')

# Processing
# math to perform calculated conversion
    # convert user input from a string to a number
    # ASSUMPTION: The user entered a valid value
celcius_temperature = float(user_input)

# use the universal conversion formula F = 9/5 C + 32
fahrenheit_temperature = celcius_temperature * TEMPERATURE_CONVERSION_RATIO + TEMPERATURE_CONVERSION_CONSTANT

# Output
# Give the user the answer!
print('''Given the temperature of %.2f Celcius,
The new temperture is %.2f Fahrenheit''' % (celcius_temperature, fahrenheit_temperature))



# --------------------------
# DESK CHECKS

# TEST      INPUT       EXPECTED RESULT     ACTUAL RESULT   Pass/Fail
# 1         0           32                  32.00           Pass
# 2         -40         -40                 -40.00          Pass
# 3         30          86                  86.00           Pass
# 4         50          122                 122.00          Pass
# 5         a           invalid input       Crash           Fail