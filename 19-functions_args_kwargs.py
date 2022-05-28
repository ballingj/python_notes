###############################################################################
# function(*args)  - allows to pass two or more arguments into a function
# the arguments becomes part of tuples i.e. (1,2,3,4)
# *args is not a set name -- name it whatever you want
##############################################################################

def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total/len(args)

print(average(1,2,3,4,5,6))     # 3.5

print(average(5,8,2))       # 5.0

# *args is useful for collecting non-required arguments

def req_args(first_req, second_req, *others_optional):
    print(f"first is: {first_req}")
    print(f"second is: {second_req}")
    print(f"others are: {others_optional}")

req_args("first", "second", True, "Silly", False, 5, 10)


#################################################################################
# function(**kwargs) - allows to pass any number of keyword arguments
#  becomes dictionaries
# **kwargs is not a set name - - name it whatever you want
################################################################################

# def print_ages(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} is {v} years old")

# print_ages(max=67, sue=59, kim=21)


def print_ages(**ages):
    for k, v in ages.items():
        print(f"{k} is {v} years old")

print_ages(max=67, sue=59, kim=21)

# order of argument matters
# ( parameters, *args, default parameters, **kwargs )
# 

def display_info(person, *args, status="married"):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")

display_info("John", 1,2,3,4, status="married")
# person is: John
# status is: married
# args is: (1, 2, 3, 4)


def display_info2(person, *args, status="married", **kwargs):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

display_info2("John", 1, 2, 3, 4, status="married", age=44, height=72)
# person is: John
# status is: married
# args is: (1, 2, 3, 4)
# kwargs is: {'age': 44, 'height': 72}


# Some annoying thing to note and a workaround
#############################################

# this example will not work because the mutable lst retains the value from one function call 
# to the next function call

# def add_twice(val, lst={}):
#     lst.append(val)
#     lst.append(val)
#     return lst

# instead use the value "None" and place an if statement
# to check if the value is NONE, then assign lst = []
def add_twice(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    return lst

print(add_twice(99))
print(add_twice(00))


# unpacking argument
###############################################

def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

nums = [5,4,8,9,3,5,4]

print(sum(*nums))   # unpack the list of nums with *nums
