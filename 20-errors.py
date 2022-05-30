# Raising errors or exceptions
# Common exceptions: SyntaxError; NameError; IndexError; TypeError; ValueError; KeyError
########################################

# custom message
#raise ValueError("invalid characters")

# When to raise an error?

def get_user_name():
    inp = input('please enter your name: ')
    if not inp.isalpha():       # check to see if entered name is alpha
        raise ValueError('alpha characters only')
        # if non-alpha is entered, this error appears:  ValueError: alpha characters only
    return inp

user = get_user_name()
print(user)

# handling exceptions
#############################################

# catch all
try:
    enter_num = ("Please enter a number: ")
except:
    print("Something went wrong!")


# specific exceptions (one or chain multiple)
###############################################
try:
    num = int(input("Please enter a number: "))
    print(10/num)
except ValueError:
    print("That is not a number!")
except ZeroDivisionError:
    print("Try a non zero number!")

################################################################################
# EAFP or LBYL : is a concept about programming style that handles exceptions
################################################################################


# EAFP:  Easy to Ask for Forgiveness that Permission
# Assume things exist or will work, and catch exceptions if wrong
# Lots of try/except blocks
####################################################################



# LBYL: Look Before You Leap
# explicitly test for pre-conditions before making calls or leaping
# Lots of if statements
######################################################################
year = input("Enter a year: ")
if year.isnumeric():
    year = int(year)
else:
    year = 2025     # define the year for them
    print(f"Fine, I'll define a year for you!")
print(f"Year {year}")