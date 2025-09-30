# -------------------------------------
# Title:        Week 05.1 - Iteration Basics
# Author:       Clint MacDonald
# Date:         September 30, 2025
# Purpose:      Learning the basics of looping structures in Python
# -------------------------------------

# In mainstream programming there are 4 types of loops....

# 1. For Loop - use when you know exactly how many iterations you want
# 2. While Loop - used when we have unknown num of iterations, exit on a condition
# 3. Do While Loop - same as while exacept guarenteed one iteration
# 4. For Each Loop - iterating through a container of objects (All of them)

# ------------------------------------------------
# used to iterate when we know exactly how many there are
print("-"*60)
print("Basic For Loop")

# Java, JavaScript, C, C++, C#, PhP, ......
# for (int i = 1; i < 5, i++) { // (Iterator and Start, Exit Strategy, Increment)
#       command block
# }

for i in range(5):   # iterator, start at 0, end at 4, increment by 1
    print(i)
    print('in the loop')
    # end of loop

print('-'*60)

# for loop with not normal range
for i in range(5, 10):  # starts at 5, ends at 9
    print(i)

print('-'*60) 

# for loop with different increment
for i in range(15, 7, -3):
    print(i)

print('-'*60)
print(i)
print('-'*60) 

# While Loop - most used
print('While Loop')

num_students = 12
while num_students > 0:
    print('Good-bye, there are %i students left' % num_students)
    num_students = num_students - 1
    # num_students -= 1

print('-'*60) 

# THE FOLLOWING IS UNACCEPTABLE and will result in reduced marks
i = 0
while True:
    print(i)
    i += 1
    if i > 10:
        break

print('-'*60) 

# replace the above with!
i = 0
doLoop = True
while doLoop:
    print(i)
    i += 1
    if i > 10:
        doLoop = False
# end of while
print('-'*60)

# -------------------
# Do While Loop
# in other languages
#  
# do {
#       command block
#
#
# } while ( condition );

# remember, this does not exist in Python....

# -----------------------
# For Each Loop

myString = "Welcome to COSC1100"
print(myString)
for letter in myString:  # letter = element, myString = container
    print(letter.upper())

print('-'*60)

