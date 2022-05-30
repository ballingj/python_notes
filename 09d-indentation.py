# indentations changes the code

mood = 'happy'

if mood == 'happy':
    print("I'm happy you are happy")
    print("this will be part of the 'if block'")
    #print("this will cause an error")
print("This is not part of the if block")

unit = "celsius"
#unit = "fahrenheit"
temp = 32

if unit == 'fahrenheit':
    if temp <= 32:
        print("It's freezing out!")
    else:
        print("It's not freeaing ")
else:
    print("I don't know celsius")


# nested Conditionals
fav_color = "green"
fav_movie = "amadeus"
fav_food = "pasta"

if fav_color == "green":
    print("I like pasta too")
    if fav_movie == "amadeus":
        print("I like Amadeus too")
        if fav_food == "pasta":
            print("I like pasta too")
# because of indentations, the if statements above each if statement act as a gatekeeper.  they only run if the prior if statement was truthy


# more nested example:
elevation = 7500
pan_type = "loaf"

if elevation < 5000:
    if pan_type == "bundt":
        print("BAKE FOR 43 MINUTES")
    else:
        print("BAKE FOR 38 MINUTES")
else:
    if pan_type == "bundt":
        print("BAKE FOR 35 MINUTES")
    else:
        print("BAKE FOR 30 MINUTES")