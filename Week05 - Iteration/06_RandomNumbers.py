# -------------------------------------
# Title:        Random Number Generation
# Author:       Clint MacDonald
# Date:         Oct. 3, 2025
# Purpose:      To learn how to make random numbers
# -------------------------------------

import random

# random integer
for i in range(5):
    myNum = random.randint(1,10)
    print(myNum)

#random float with 1 decimal place 
for i in range(5):
    myNum = random.randint(10,100)
    print(myNum/10)

#random float with 2 decimal places
for i in range(5):
    myNum = random.randint(100,1000)
    print(myNum/100)

random.randrange()