# Scope - wheere can we access the variables
# LEGB = Lexical; Enclosing; Global; Built-in

# Global scope - variable is acccessible from anywhere
animal = "Lemur"

print("Outside of Function: ", animal)

def func():
    print("Inside Func: ", animal)
    def inner_func():
        print("Inside Inner Func: ", animal)
    inner_func()

func()    

# Lexical (local) Scope - variable inside the function are not accessible outside
#
def zoo():
    animal1 = "Tiger"
    print("Inside Zoo Function: ", animal1)

zoo()
#print("Outside Function: ", animal1)  ## errors out due to animal1 being undefined

# for loop; while loop; if statement are not part of local scope


# Enclosing Scope - variables from outside function are available in a nested function
def outer():
    animal2 = "Penguin"
    def inner():
        print("Inside Nested Function: ", animal2)
    inner()
outer()

# Built-in Scope - are available anywhere
#help("builtins")
#str is an example

#Scope precedence is L E G B 
location = "Earth"

def continent():
    location = "Europe"
    def country():
        # location = "France"
        print("From country function: ", location) # because there is no local scope variable in country, it pulls the Enclosing function variable

    print("From continent Function: ", location)
    country()

print("From outside of functions: ", location)
continent()