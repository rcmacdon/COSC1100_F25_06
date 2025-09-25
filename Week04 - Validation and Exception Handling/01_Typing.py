# -------------------------------------
# Title:        Week 4 - Data Types
# Author:       Clint MacDonald
# Date:         Sept. 25, 2025
# Purpose:      Learning how to work with data types in Python
# -------------------------------------

# play with data types
myInt = 5
myFloat = 5.0
myString = "Hello"

# print the data type
print(type(myInt))
print(type(myFloat))
print(type(myString))

if (type(myInt) == int):
    print("MyInt is an integer")
else:
    print("MyInt is NOT an integer")

print(type(myInt) == type(myFloat))

print(myInt == myFloat)


# isinstance
if (isinstance(myInt, int)): print("is an integer!")

# iddigit
print('-'*60)

myNumber = "5"  # String

print(type(myNumber))
# check if it is convertible and if so go ahead and convert it!
if myNumber.isdigit():  myNumber = int(myNumber)
print(type(myNumber))

myNumber = "5.4"
print(type(myNumber))
if myNumber.replace(".", "").isdigit():  myNumber = float(myNumber)
print(type(myNumber))

myNumber = "Clint"
print(type(myNumber))
if myNumber.replace(".", "").isdigit():  
    myNumber = float(myNumber)
print(type(myNumber))