# and operator some examples
age = 20
if age > 18 and age < 21:
    print("You can enter the venue but cannot drink.")

# Could also be written using nested conditionals:
# if age > 18:
#     if age < 21:
#         print("You can enter the venue but cannot drink.")


# or operator examples
day = input("what day of the week is it? ")

if day == 'saturday' or day == 'sunday':
    print("it's the weekend!")
else:
    print("ugh it's a workday :(")


# more example:
age = int(input("how old are you? "))
if age < 5 or age >= 65:
    print("you get in for free!")
else:
    print("that will be $5")


# not operator
year = input("what year were you born in? ")

if not year.isnumeric():
    year = input(
        "That isn't a number.  Try again please! what year were you born in? ")

year = int(year)

print(f"You were born {2022-year} years ago")