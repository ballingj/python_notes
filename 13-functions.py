# function with no input
def laugh():
    print("HA! " * 20)
    print("LA, " * 20, "LOL!")

laugh()

# function with one parameter
def laugh1(strength):
    print("HA! " * strength)

laugh1(5)   #passing an argument to function


#function with two or more parameters
def announce(name, msg):
    print(name, msg)

announce("Jeff", "Hello World")

# return function
def divide(x,y):
    if x == 0:
        return "Don't Divide by Zero!"
    return x/y

result = divide(20,2)
print(result)


# default parameters - adds a default value if no argument was provided
# required value must always comes first
def slugify(words, sep="-"):
    return words.strip().lower().replace(" ", sep)

print(slugify("    Hello World Jeff  "))
print(slugify("    Hello World Jeff  ", "_"))


# named argument or keyword argument
# ordering id=s important when using named argument
def get_total(price, qty=2, tax=0.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1 + tax))

get_total(9.75, 5, 0.01, 0.2)  # this is not using named argument -- hard to tell what value goes to what parameters
get_total(price = 9.75, qty = 5, tax = 0.01, discount = 0.2)  # arguments with key
get_total(price=9.75, tax=0.01, qty=5,  discount=0.2)  # order does not matter if all keys are used

