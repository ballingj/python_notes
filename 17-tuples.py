##################################
# tuples: like lists, ordered, indexed collections
# unlike lists, tuples are immutable: can not change once created
# order written is how stored
##################################

# creating tuple
dishes = ("burrito", "taco", "fajita", "quesadillas")

type(dishes)

# creating one item tuple -- trailing comma
cup = "cup1",
glass = ("cup2",)

# access an element
dishes[2]   # "fajitas"

# slice
dishes[1:3]    # ['taco', 'fajita']

# index
dishes.index("taco")    # 1

# in
"nachos" in dishes  # False

# for in loop
for dish in dishes:
    print(dish)