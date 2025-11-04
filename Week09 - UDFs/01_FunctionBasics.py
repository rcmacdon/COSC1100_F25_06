# -------------------------------------
# COSC1100 - Week 9
# Clint MacDonald
# Nov. 4, 2025
# Introduction to Modularity and User-Defined Functions
# -------------------------------------

# Functions are a way to group code together and give it a name.  This allows a developer to reuse code multiple times without having to write it out each time.  Functions can receive data through PARAMETERS, and RETURN output.  This allows you to create more flexible and reusable code.

# ----------------------------------------
# Verbage of Functions
# ----------------------------------------

# Various different Names used for Functions
# - Function
# - Method
# - Procedure
# - Subroutine
# - Constructor
# - Destructor
# - Getter or Accessor
# - Setter or Mutator
# - Lambda or Anonymous Function (Arrow Notation)

# Real definition of a Functions

# - An algorithm that receives some stuff, does some stuff, and returns 1 thing!

# RULES OF FUNCTIONS
# ---------------------------------------------
# 1. Function names should be descriptive and meaningful.  Usually start with a verb.
# 2. In Python, functions are declared seperately from where they are called and using the "def" keyword.
# 3. In Python, functions are declared BEFORE they are used.
# 4. Functions are called using the name of the functions and with parenthesis ().  The parenthesis mean "execute this now!"
# 5. Functions can take in Parameters (Optional) which are values passed into the function.
# 6. Parameters may have default values.  If a value is not provided, a default value can be assigned.
# 7. Functions can RETURN a value using the keyword "return"
# 8. Functions can have multiple return statements, but only one will ever be executed.  The function is terminated when the return statement is executed.
# ---------------------------------------------


# KEY CONCEPTS OF FUNCTIONS (Design ideas)
# ---------------------------------------------
# 1. Functions should be rather small and do ONLY ONE thing, but does it perfect!
# 2. Functions should be reusable
# 3. Functions should be testable
# 4. Functions should be purpose agnostic - they do not care why they are being called.  They only do their job!
# 5. Functions should be absolutely INDEPENDENT - including other functions.


# ------------------------------------------
# Example Function 1

def sayHello():    # sub-routine or a void function
    '''A function that prints out "Hello World" '''
    print("Hello World")
    # end of sayHello() function


myString = sayHello()
print(myString)

print ('-'*40)

# Example 2
def sayHelloTo(name):
    '''Function to say hello to a specific string that is received.'''
    return_string = "Hello %s" % name
    return return_string

hello1 = sayHelloTo('Clint')
# becomes:  hello1 = "Hello Clint"
hello2 = sayHelloTo('Sally')

print(hello1)
print(hello2)
print(sayHelloTo('Johnny'))
print(sayHelloTo(5))

name = "Bob"
print(sayHelloTo(name))

print('-'*40)

# Example 3
def sayGreetingToName(greeting: str, name: str):
    '''Prints out a greeting to a specific name.'''
    print("%s %s!" % (greeting, name))

sayGreetingToName("Good Morning", "John")

greeting_string = "Why were you not in class today"
student_name = "Gary"
sayGreetingToName(greeting_string, student_name)


# Example 4
def add(num1, num2):
    '''adds two numbers together'''
    return num1 + num2

x = 2
y = 5
answer = add(x, y)
print(answer)

print(add(5,4))
print("%i + %i = %.2f" % (8, 6, add(8,6)))



