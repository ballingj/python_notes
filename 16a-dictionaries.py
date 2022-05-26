##############################################################################
# Dictionaries are datastructure that are in a key: value format
# key must be any immutable type: number, strings, booleans, etc
# value can be any data types, like another dictionaries
###############################################################################

from operator import methodcaller


movie = {
    "title": "Amadeus",
    "review": 10379,
    "imdb": 8.3,
    "runtime": '3h',
    "year": 2002,
    "rating": "R"
}

# numbers as key
numbers = {
    1: "one",
    2: "two",
    3: "three"
}

# Accessing dictionaries - provide the key as an argument in a mivie["title"]
print(movie["title"])

# Adding and updating value
# updating existing value
movie["imdb"] += .5
print(movie["imdb"])

# adding key:value pair
movie["genre"] = "drama"
print(movie)

###########################################
# The "in" operator and dict.get() method
############################################
prices = {
    "arugal": 1.10,
    "basil": 2.54,
    "blackberries": 4.93,
    "blueberrie": 2.88,
    "coconut": 5.15,
    "fennel": 3.36
}
# in 
# product = input("What product are you buying?\n> ")
# if product in prices:
#     price = prices[product]
#     print(f"{product} is ${price}")
# else:
#     print("Sorry, I don't have that today.")

# dict.get() method is easier
product = input("What product are you buying?\n> ")
price = prices.get(product)
if price:
    print(f"{product} is ${price}")
else:
    print("Sorry, I don't have that today.")

################################################
# Removing with pop(), popitem(), clear(), del
##################################################

# pop(): pass the key as an argument, and the key: value pair goes away: returns the removed value
dict1 = {"a" : 1, "b": 2, "c": 3}
pop_value = dict1.pop("b")
print(pop_value)    # 2

# popitem(): deletes the most recently added key-value pair: returns the key: value pair
dict2 = {"a": 1, "b": 2, "c": 3}
pop_item = dict2.popitem()
print(pop_item)     # ("c":  3)

# clear(): deletes/clear the entire dictionary
dict3 = {"a": 1, "b": 2, "c": 3}
dict3.clear()
print(dict3)    # {}

# del[]: not a method hence the syntax, but deletes the item passed as an argument
dict4 = {"a": 1, "b": 2, "c": 3}
del dict4["a"]
print(dict4)    # {"b": 2, "c": 3}

# dictionaries are mutable too
d1 = {1: "one"}
d2 = d1
d1 == d2 # True
d1 is d2 # true

d2[2] = "two"

d1 == d2  # still True
d1 is d2  # still True

d3 = d1.copy()

d3 is d2   # False 

id(d3) != id(d1)    # not the same location in memory

#################################################
#  iterating over dictionaries
# dict.keys()  - dict.values()  - dict.items()
#################################################
test_scores = {
    "Marsha": 78,
    "Baker": 69,
    "Rosa": 92,
    "Leif": 97,
    "Peng": 61,
    "Juan": 73,
    "Esteban": 84,
    "Amir": 91,
    "Sakura": 99
}
####################
# dict.keys() : returns a dict_keys structure that looks like a list (but not a list)
##############
students = test_scores.keys()
print(students)
# dict_keys(['Marsha', 'Baker', 'Rosa', 'Leif', 'Peng', 'Juan', 'Esteban', 'Amir', 'Sakura'])

for student in students:
    print(student)
#################
# dict.values() : returns a dict_values structure
##################
scores = test_scores.values()
print(scores)
# dict_values([78, 69, 92, 97, 61, 73, 84, 91, 99])

for score in scores:
    print(score)

# average out the score
total = 0
for score in scores:
    total+= score
print("avg: ", total / len(test_scores))

######################
# dict items
#################
# basic 
for item in test_scores.items():
    print(item)
# ('Marsha', 78)
# ('Baker', 69)
# ('Rosa', 92)
# ('Leif', 97)
# ('Peng', 61)
# ('Juan', 73)
# ('Esteban', 84)
# ('Amir', 91)
# ('Sakura', 99)

# we can unpack the key value pair like so:
for k,v in test_scores.items():
    print(k, ":", v)
# Marsha: 78
# Baker: 69
# Rosa: 92
# Leif: 97
# Peng: 61
# Juan: 73
# Esteban: 84
# Amir: 91
# Sakura: 99

# then we can do cool stuff like finding the best score by whom:
max_score = 0
best_student = ""
for student,score in test_scores.items():
    max_score = score
    best_student = student
print(f"Highest score was {max_score} by {best_student}")

# Last note: no need to use ".keys() in dict.keys() because the default iterable in dictionaries is the keys

for student in test_scores:
    print(student)

###############################################
# Merging Dictionaries
# update():  
# unpacking dictionaries: (**dict1, **dict2)
# dict union: dict3 = dict1 | dict2
# order matters - rightside overwrites the value on left side
###############################################

# update() - adds the dict passed in as argument and updates a matching key - i.e. "a" below -- mutates the updated dict
d1 = {"a": 1, "b": 2}
stuff = {"c": 3, "d": 4, "d": 5, "a": "apple"}

d1.update(stuff)
print(d1)   # {'a': 'apple', 'b': 2, 'c': 3, 'd': 5}

# **: unpacking the dict to combine
d3 = {"a": 1, "b": 2}
d4 = {"c": 3}
d5 = {**d3, **d4}
print(d5)   # {'a': 1, 'b': 2, 'c': 3}
d6 = {"c": "car"}
print({**d5, **d6})  # {'a': 1, 'b': 2, 'c': 'car'}    # C gets updated with "car"

# dict union  using "|"  -- only on python >= 3.9 
d7 = d1|d2
print(d7)

#############################
#  Nested Dictionaries
# ############################

produce = {
    "arugala": {
        "price": 1.10,
        "qty": 61,
        "organic": True,
        "producer": "Blue Kitty Farms"
    },
    "coconut": {
        "price": 7.15,
        "qty": 12,
        "organic": False,
        "producer": "Tropical Dream House"
    }
}

print(produce["arugala"]["producer"])
