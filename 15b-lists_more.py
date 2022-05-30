##################
# Lists operator
##################

# Addition

added = [1,2,3] + [4,5,6]  # [1,2,3,4,5,6]
worded = ['Super'] + ['man']  # Not the same ... ['Super', 'man']  one list of two words

# multiplication
multiply = [1, 2, 3] * 2   # [1,2,3, 1,2,3]
 
# in:  used in conjunction wit for or while loop.  for item in list -- truthy or falsy
flavors = ['chocolate', 'vanilla', 'lemon', 'strawberry']
response = input('What flavor would you like? ')
# keep repeating input request until correct item in the lists is given
while response.lower() not in flavors:
    response = input("I don't know that flavor!  Try again: ")

print(f"{response} ice cream, coming right up! ")


####################################################
# More lists method - sort() - reverse() - count()
####################################################

# Count: returns the number of times a value occurs in the list:  If not in the lists, returns a zero (0)
lando_2021_results = [4, 3, 5, 8, 3, 5, 5, 5, 3, 4, 14, 10, 2, 7, 7, 8, 10, 1, 10, 9, 10, 7]

lando_2021_results.count(1)  # 1 time
lando_2021_results.count(2)  # 1 time
lando_2021_results.count(3)  # 3 time
lando_2021_results.count(4)  # 2 time

# Reverse:  reverses a list - mutates and returns None
# reversed_lando = lando_2021_results.reverse()
# print(reversed_lando)

print(lando_2021_results)
lando_2021_results.reverse()   # returns None, so this mutates the list
print(lando_2021_results)


evens = [2,4,6]
evens.reverse()
print(evens)

# Sort: sorts ascending or descending - mutates
nums1 = [340,250,5,155, 233, 4, 98, -23, 500, 0]
print(nums1)
nums1.sort()   # sorts in ascending (default)
print(nums1)
nums1.sort(reverse=True)   # sorts in descending order
print(nums1)

# sort alpha
marvel_heroes = ['captain', 'hulk', 'antman', 'wasp', 'black widow', 'iron man', 'thor', 'hawkeye']
print(marvel_heroes)
marvel_heroes.sort()
print(marvel_heroes)

#################################
# comparing lists  '==' and 'is'
#################################
# id(value)  # you get an id of memory container/location
list1 = [12,9,3,7,[2,2]]
list2 = list1  # list2 now points to the same memory container
print(id(list1), id(list2))

# now change list2 contents 
list2.append(6)

# == compares the contents of two lists : if they hold the same values
print(list1 == list2)  # True
[1,2,3] == [1,2,3] # True

# is compares the identity of two losts ; if same container in memory
print(list1 is list2)  # True
[1, 2, 3] is [1, 2, 3]  # False - totally different instances of list that points to different memory

###############################################################################################
# copy() method returns a shallow copy -- shallow means nested members of lists are not copied, but remains as reference
#################################################################################################
print(list1)    # [12, 9, 3, 7,  [2, 2], 6]
list3 = list1.copy()    # copies the values and new memory created - no nested lists here
print(list3)    # [12, 9, 3, 7,  [2, 2], 6]
print(list1 == list3)  # True
print(list1 is list3)  # False

# copying using the slice method
list4 = list1[:]  # this will have the same result
print(list4)

##################################################################################################
# Split()  and Join() -- Not technically a list method, but a string method that returns a list
##################################################################################################

# split: a string method that split a sting on a given character - returns a list
birthday = "3/07/2001"
split_birthday = birthday.split("/")
print(split_birthday)   # ['3', '07', '2001']

# join: a string method that joins elements of iterables into a single string - have to provide the string.join
back_to_birthday = "/".join(split_birthday)
print(back_to_birthday)  # 3/07/2001

fruits = ['apples', 'oranges', 'pears']

print(" ".join(fruits))  # apples oranges pears
print("#".join(fruits))  # apples#oranges#pears

show = ['M', 'A', 'S', 'H']
print("*".join(show))   # M*A*S*H

#################################
# Unpacking Lists
#############################
user = ['Joe', 'Bonamazza', 43]
first, last, age = user
print(first, last, age)    # "Joe Bonamazza 43"

# in between
item = [4, 'Pizza', 'Plain', 16.98]
quantity, *others, price = item
print(quantity) # 4
print(others)   # ['Pizza', 'Plain']
print(price)    #