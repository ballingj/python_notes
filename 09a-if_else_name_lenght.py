first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
name_length = len(first_name) + len(last_name)

print("*"*20)
if name_length < 12:
    print(f"{first_name} {last_name} is shorter than the average American name.")  
elif name_length > 12:
    print(f"{first_name} {last_name}  is longer than the average American name.")
else:
    print(f"{first_name} {last_name}  is exactly the same lenght as an average American name.")

print("*"*20)
