
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for i in word:
    print(i)
print("*"*25)    

# Write a while loop that does the same thing!
count = 0
while count < len(word):
    print(word[count])
    count += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
skipper = 100
while skipper < 141:
    print(skipper)
    skipper+=2

# Write a for loop that does the same thing (with range())
for skip in range(100, 141, 2):
    print(skip)


#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
passphrase = "sillygoose"
entre = input("Enter sillygoose here ----> ")
while entre != passphrase:
    entre = input("Enter sillygoose here ----> ")
print("Alrighy then, sillygoose!")