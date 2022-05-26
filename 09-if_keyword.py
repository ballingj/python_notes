age = input("How old are you? ")
age = int(age)

if age >= 21:
    print("Come on in")
    ans = input("Do you want a drink? ")
    ans = ans.lower()
    if ans == "yes":
        print("Cheers Mate! ")
    elif ans == "no":
        print("Boo, go home!")
else:
    print("Go home!")

temperature = 80
if temperature > 212:
    print("SUPER SUPER HOT!")
elif temperature > 100:
    print("HOT!")
elif temperature > 32:
    print("MEH")
else:
    print("COLD!")

if temperature > 212:
    print("SUPER SUPER HOT!")
elif temperature > 100:
    print("HOT!")
elif temperature > 32:
    print("MEH")
else:
    print("COLD!")

password = "choppedliver"
if len(password) < 10:
    print("invalid password!")
elif " " in password:
    print("invalid password!")
else:
    print("valid password!")
