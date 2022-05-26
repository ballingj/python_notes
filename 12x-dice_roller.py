# https://plum-poppy-0ea.notion.site/Dice-Roller-faf046ef3f4b4ce2800d210cf13183ab
from random import randint

num_dice = int(input("How many dice are we rolling? " ))
num_sides = int(input("How many sides on each die? " ))

while True:
    result = "|"
    for die in range(num_dice):
        rand = randint(1,num_sides)
        result += f"{rand}|"
    print(result)
    again = input("Roll again? ('q' to quit) ")
    if again == "q":
        break
