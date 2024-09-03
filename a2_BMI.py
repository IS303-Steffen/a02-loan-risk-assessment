# Name: Jacob Steffen
# Description: Gathers info about the user, then based on their weight and height calculates their BMI and what category they belong in.

# get the name of the user
fName = input("please enter your first name: ")
lName = input("please enter your last name: ")

# gather information on height, and weight
heightFeet = int(input("enter your height in feet: "))
heightInches = int(input("please enter height in inches: "))
weightPounds = int(input("please enter weight in lbs: "))

# calculate BMI. Converts height into inches and uses this formula: [weight (lb)] / [height (in)]^2 x 703
# the results are rounded to the second decimal
bmi = round(weightPounds / (((heightFeet * 12) + heightInches) ** 2) * 703, 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"


# printing out the full name
print(f"{fName} {lName} has a BMI of {bmi}. The associated category is: {category}.")