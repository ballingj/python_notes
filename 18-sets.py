###############################################################
#  Sets  - unordered collections with no duplicate elements
# - only immutable elements
# - we can add and delete elements
# - iterate over elements
# - check to see if element in set
# use set operators: union, intersection, difference, etc
###############################################################

###################
# creating sets
####################

nums = {1,2,3,4,5,6}

evens = {2,4,6,8,10}
print(type(evens))

not_a_set = {}  # can't do empty sets because {} becomes a dictionary
print(type(not_a_set))

# immutable element only: no lists

#print({1, 2, True, "Hello", []})        # TypeError: unhashable type: 'list'

# only unique values are stored

unique_val = {1, 2, 3, 1, 1, 5, 4, 5}
print(unique_val)       # {1, 2, 3, 4, 5}

###############################
# Adding elemnts
######################################

# sets.add(): add value
evens.add(12)

####################################
# Removing elements in sets
####################################

# sets.remove():  remove a value
# if the value is not in sets, throws an error
evens.add(7)
evens.remove(7)


# sets.discard():  same as remove but
# if the value is not in sets, does NOT throws an error
evens.discard(7)

# sets.clear()
nums.clear()

######################################
# check to see if element in set
print(2 in evens)


# iterate over sets
for even in evens:
    print(even)


###############################################################
# Set Operators: Intersections, Union, Difference
#
#################################################################

# intersection: returns a new set with members common to left and right
# left $ right
set_odd = {1,3,5,7,9,11}
set_prime = {2,3,5,7,11}

new_intersect = set_odd & set_prime

print(new_intersect)    # {11, 3, 5, 7}

# union: returns a new set with members from left and right
# left | right

new_union = set_odd | set_prime

print(new_union)    # {1, 2, 3, 5, 7, 9, 11}

# difference: returns a new set with members from left not in right
# left - right

new_diff = set_odd - set_prime

print(new_diff)      # {1, 9}

###################################################
# why use sets ?
# - sets make it easy/fast to check if value exists in sets
# - sets makes it easy to remove duplicates
#
###################################################

# searching for a value in set is fast and efficient due to  hashing -- list is slower due to iteration
print(8 in evens)      # True


# remove duplicates

my_state_list = ["CA", "NV", "CO", "CA", "NE", "CO", "CA"]
my_state_set = set(my_state_list)   # convert to set to remove duplicates

print(my_state_set)  # {'CO', 'CA', 'NV', 'NE'}

# then convert back to list
my_state_list = list(my_state_set)
print(my_state_list)        # ['CO', 'NV', 'NE', 'CA']
