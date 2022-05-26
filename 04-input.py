age = input("How old are you in years? ")
days = float(age) * 365
print("you are " + str(days) + " old.")

# interpolation can be achieve by f string
print(f"{age} years is {days} days old")
