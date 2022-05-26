# Write a Python script that does the following:

# Prints out a “banner” to welcome users to our shop
print("WELCOME TO OUR USELESS STORE!")
print("*"*30)

#- Asks the user for the name of the item they are buying
item = input("What item are you purchasing?  ")

#- Asks the user for the price of that item
price = input(f"What is the price of {item}?  ")

#- Asks the user for the quantity they are purchasing
qty = input(f"How amny {item} are you buying?  ")

#- Prints out a message that includes their subtotal (quantity 𝚡 price)
print(f"Added {qty} {item}(s) to shopping cart")
print(f"Subtotal: ${int(qty)*float(price)}")
