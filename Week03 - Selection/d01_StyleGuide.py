# -------------------------------------
# Title:        Style Guide and Variable Guide
# Author:       Clint MacDonald
# Date:         Sept. 16, 2025
# Purpose:      To introduce style guide and naming conventions
# -------------------------------------

import math


# Variables (Variant) Names

# Variable names are used reference data in memory.
# Variables are used to store data in memory

# appropriate for the student's first name:

first_name = "Clint"        # decent - could be more specific
student_fname = "Clint"     # unacceptable - no shortcuts
student_name = "Clint"      # bad - not explicit enough
studentFirstName = "Clint"  # Good - camel case
StudentFirstName = "Clint"  # Unacceptable - Pascal Case - not for variables.
student_first_name = "Clint"# Good - matches the style guide - snake case!
studentfirstname = "Clint"  # Bad - not Camel Case nor snake case
fName = "Clint"             # Unacceptable
std_First_Name = "Clint"    # Unacceptable - std means many things!
STUDENT_FIRST_NAME = "Clint"# Unacceptable - narsicism - needs to change

# Camel Case - starts with a small letter, each word starts with a capital
# Pascal Case - starts with a capital, each word starts with a capital
# Snake Case - each word separated by an _
# Upper Case - ALL Letters are capitals, combine with snake case.
#            - used for Constants only
PI = 3.14159
GRAVITY_CONSTANT = -9.81
HST = 13.0

vehicle_id_num = "1234567890abcdef"  # acceptable as shortcuts are universally accepted
vehicleIdNum = "1234567890abcdef"
vin = "1234567890abcdef"            # UNACCEPTABLE

social_insurance_num = 123456789
SIN = 123456789             # UNACCEPTABLE - acronyms are not permitted.

C = 299792458                   # unacceptable
SPEED_OF_LIGHT = 299792458      # good

TEMPERATURE_CONVERSION_RATIO = 9.0 / 5.0
TEMPERATURE_CONVERSION_CONSTANT = 32.0



x = 5   # acceptable ONLY for math
i = 4   # software acceptable for iteration.

# Pythagorean Theorem
#  a^2 = b^2 + c^2
a = 5
b = 12
c = math.sqrt( a**2 + b**2)

c = ( a**2 + b **2 )  ** 0.5


