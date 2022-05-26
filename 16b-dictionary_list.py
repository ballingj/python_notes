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

print(produce["arugala"]["producer"])  # Blue Kitty Farms


######################################
#  Combining Lists and Dictionaries
# 
# ########################################

# Dictionaries with lists of values

test_scores = {
    "Marsha": [78, 80, 89],
    "Baker": [69, 65, 52]
}


# # Lists of Dictionaries

waitlist = [
    {
        "email": "tiff@gmail.com",
        "location": "USA",
        "first_name": "Tiffany"
    },
    {
        "email": "carl@gmail.com",
        "location": "USA",
        "first_name": "Carlson"
    },
]


