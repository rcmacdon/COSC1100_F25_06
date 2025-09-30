# Create a program that will display a grid of stars, spaced out by one space, given the width of the grid obtained by user input

# Get user input for the width of the grid

MIN = 1
MAX = 20
doContinue = True



while (doContinue):
    print("-"*60)
    try:
        width = int(input("Enter the width of the grid (%i-%i, 0 to exit): " % (MIN, MAX)))
        
        #Validations
        isValid = True

        #check exit condition
        if width ==0: 
            doContinue = False
            isValid = False

        # validate range
        if width <= 0 or width > 20:
            print("Please enter a positive integer between %i and %i." % (MIN, MAX))
            isValid = False
        
    # failure of type conversion
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        isValid = False

    # catch all other exceptions ``
    except Exception:
        print("An unexpected error occurred. Please try again.")
        isValid = False
    
    # only print out grid if passed both validations and exception handling
    if isValid:
        # Display the grid of stars
        for i in range(width):
            for j in range(width):
                print("*", end=" ")
            print() 

print("Thank you for using the grid generator. Goodbye!")
exit()
