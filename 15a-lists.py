#############################################################
# Lists: The basics
# Lists are ordered collections of data that can hold any data types
##############################################################

# Lists in python can be of any types
tasks = ["Trash", "Dishes", "Laundry", "Dinner"]
high_scores = [99, 78, 89, 99]
# can even have another list inside
stuff = [55, 43, True, False, "toys", ["a", "b", "c"]]

# You can make a list by using a built-in function list()
print(list("hello"))  # will produce ['h', 'e', 'l', 'l', 'o']
print(list(range(3, 10)))   # will produce [3, 4, 5, 6, 7, 8, 9]

# updating member of list
waitlist = ['tom', 'arya', 'amar']
waitlist[1] = 'aria'
print(waitlist)  # ['tom', 'aria', 'amar']


#######################################
# Adding methods
#######################################

# append:  adding element into a list - can only add one element
waitlist.append('juan')
print(waitlist)  # ['tom', 'aria', 'amar', 'juan']

# extend:  adding element into a list - more than one
people = ['carl', 'marco']

waitlist.extend(people)
print(waitlist)  # ['tom', 'aria', 'amar', 'carl', 'marco']

# below is wrong 
# waitlist.append(people) # this results in nested list ['tom', 'arya', 'amar', ['jess', 'marco'] ]
# print(waitlist)

# insert: inserting anywhere in the list: we have to specify in first argument where to insert
nums = [7,8,9]
nums.insert(1, "HI")
print(nums)   # prints [7, 'HI', 8, 9]

more = ['uma', 'amir', 'rosa', 'colt', 'charlie', 'drew', 'emi']
waitlist.extend(more)  # ['tom', 'aria', 'amar', 'juan', 'carl', 'marco', 'uma', 'amir', 'rosa', 'colt', 'charlie', 'drew', 'emi']
print(waitlist)


# slicing list
waitlist1 = waitlist[5:10]  #
print(waitlist1)    # ['marco', 'uma', 'amir', 'rosa', 'colt']


#slicing list with step
waitlist2 = waitlist[1:7:2]
print(waitlist2)   # ['aria', 'juan', 'marco']

# replacing values with a slice 
nums1 = [4,5,6,7,8,9]
nums1[1:3] = ['a', 'b']
print(nums1)   # [4, 'a', 'b', 7, 8, 9]

######################################
# Remove methods
######################################

# clear: removes all list contents
langs = ["c", "java", "basic", "cobol"]
langs.clear()   
print(langs)  # []

# remove: removes an element matching the argument : only removes the first match
langs = ["c", "java", "basic", "cobol"]
langs.remove("cobol")
print(langs)  # ["c", "java", "basic"]

# pop: removes the very last element in the list: also returns that value
gone = langs.pop()  # returns "basic"
print(gone)    # basic
print(langs)  # ['c', 'java']

# pop(idx): instead of last element, define the index
waitlist3 = ['jeff', 'jacqui', 'jason', 'jennifer']
gone2 = waitlist3.pop(0)  # removes 'jeff' and returns it
print(gone2)   # jeff
print(waitlist3)   # ['jacqui', 'jason', 'jennifer']

# del: not a method, but a statement
nums2 = [1, 2, 3, 4, 5, 6, 7]
print(nums2)
print(nums2[4:])  # [5, 6, 7]
del nums2[4:]  # deleted [5, 6, 7]
print(nums2)  # new nums2 [1, 2, 3, 4]

###########################################
# iterating over list with loops
############################################

# for loop
emails = ['abby@yahoo.com', 'bobby@yahoo.com', 'candy@yahoo.com',
          'dan@yahoo.com', 'eddy@gmail.com', 'fred@gmail.com', 'gary@hotmail.com']

for email in emails:
    print("***Sending email to***")
    print(email)

# while loop
idx = 0
while idx < len(emails):
    print(f"Email sent - {emails[idx]}")
    idx += 1

###############################################
# Some common patterns with lists
##############################################

# Average: Finding Average
lando_2021_results = [4, 3, 5, 8, 3, 5, 5, 5, 3,
                      4, 14, 10, 2, 7, 7, 8, 10, 1, 10, 9, 10, 7]

total = 0
for num in lando_2021_results:
    total += num

avg = total / len(lando_2021_results)
print(total, avg)

# Lowest - finding the min
mini = lando_2021_results[0]   # use the first element as starting
for num in lando_2021_results:
    if num < mini:
        mini = num
print(mini)


# Nested Lists
nums = [1, 2, 3, 4, [5, 6]]
couples = [
    ['Beyonce', 'Jay-Z'],
    ['Johnny', 'June'],
    ['John', 'Yoko'],
    ['Will', 'Jada']
]

# how to access a certain name?
# Will
couples[3][0]
# June
couples[1][1]

# iterate over each person in a couple
for couple in couples:
    for person in couple:
        print(f"Inviting {person}...")

# initial for Beyonce - this works because strings are iterables
couples[0][0][0]
