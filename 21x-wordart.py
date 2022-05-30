"""
This program asks for an imput and creates a wordart
doc:  pypi.org/project/art
pip install art
"""

import art

# print(art.art("woman"))
# print(art.art("coffee"))
# print(art.randart())
print(art.art("train"))

print("Type a word to create into word art:")
wordart = input("--> ")
# Return default style
print(art.text2art(wordart))

# Return ASCII text with block font
print(art.text2art(wordart, font='block', chr_ignore=True))
