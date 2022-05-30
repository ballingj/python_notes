#exercise 1 - create a function that accepts one parameter and check if even
# def is_even(num):
#     if num % 2:
#         return False
#     else:
#         return True

# simplified
from itertools import count


def is_even(num):
    return num % 2 == 0


print(is_even(9))
print(is_even(12))
print(is_even(12345))

#2 exercise2  write a function that removes leading/training spaces from a sentence
# then replace remaining spaces with "-" and lower case all

def slugify(words):
    return words.strip().lower().replace(" ", "-")

print(slugify("    Hello World Jeff  "))

#3 count vowels in a word
def count_vowel(word):
    count = 0
    for char in word:
        if char in "aeiou":
            count+=1
    return count

print(count_vowel("Hello World"))

print(count_vowel("Hll Wrld Jff"))