# while loop exercise
# loop until you get snake eyes
import random
roll1 = random.randint(1,6)
roll2 = random.randint(1, 6)
count = 1

while roll1 != 1 or roll2 != 1:
    print(roll1, roll2)
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    count += 1

print(roll1, roll2, "SNAKE EYES!", f"It took {count} tries")