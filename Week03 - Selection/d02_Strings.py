# -------------------------------------
# Title:        String Basics
# Author:       Clint MacDonald
# Date:         Sept. 16, 2025
# Purpose:      Learning about native data types and strings
# -------------------------------------

# Native Data Types:
# -------------------
# Integer
# float
# decimal
# character
# boolean

# non-native types
# ------------------
# Strings
# Dates
# custom objects

# Strings are not stored as a single entity
# A string is a collection of characters


my_name = "Clint MacDonald"  # collection of characters (15)

print(my_name)
print(my_name[6])
print(my_name[1])
print(my_name[0])

print(my_name[14])
#print(my_name[15]) - ERROR: index out of range

print(my_name[-1]) 
print(my_name[-3]) 

print(my_name[3:7])

print(my_name[:9])
print(my_name[:-1])

print(my_name[4:])
print(my_name[-1:])

print(my_name[-3:])

# given [ a:b ]  a is inclusive, b is exclusive
