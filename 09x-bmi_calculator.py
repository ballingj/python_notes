# https://plum-poppy-0ea.notion.site/BMI-Exercise-82a2fd55bca7481f9957fd06e2e5d451
height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in lbs: "))
bmi = (weight * 703) / (height ** 2)
bmi = round(bmi, 1)

if bmi < 16.0:
    category = "Severely Underweight"
elif bmi < 18.4:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal"
elif bmi < 29.9:
    category = "Overweight"
elif bmi < 34.9:
    category = "Moderately Obese"
elif bmi < 39.9:
    category = "Severely Obese"
else:
    category = "Morbidly Obese"

print(f"Your BMI of {bmi} makes you {category}")