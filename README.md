#### Assignment 3
# BMI
You’ll be creating a simple python program that prompts the user for information and will calculate BMI (Body Mass Index) based on the information entered, as well as the categories associated with the calculated BMI.

Put your code in the `a3_BMI.py` file. Do not edit or delete any other files.


## Logical Flow
1. Prompt the user to enter their information with the following prompts:
    - `Enter your first name: `
    - `Enter your last name: `
    - `Enter the feet of your height: `
    - `Enter the inches of your height: `
        - For example, if the height you want to enter is 5"7, you would first enter `5` for the feet and then `7` for the inches.
    - `Enter your weight in pounds: `
    - Store each of the inputs in a variable.
    - Make it so that (at least for weight) it can handle decimal numbers. (e.g. the user should be able to enter 150.5 as a weight)
    - It is good practice for this class to always include a colon and an extra space at the end of your input prompt. It looks nicer in the terminal that way.
    - Be sure to use the wording above and use correct spelling so you pass the automated tests.
2. Calculate the BMI based off of the information given. You can use one of these two formulas:
    - ([weight (lbs)] / [height (in)]^2) x 703
    - ([weight (lbs) / [height (in)] / [height (in)]) x 703
    - Note that since the user will input this information as feet and inches separately, you’ll need to calculate the total inches for this to work.
    - The calculated BMI should be rounded to the 2nd decimal place.
3. BMI also has categories associated with the numerical calculation. Calculate the category associated with the numerical BMI:
    - Underweight:  < 18.5
    - Normal weight:  18.5 <= x < 25
    - Overweight:  25 <= x < 30
    - Obese:  30 or greater
4. At the end, you should print out the user’s first name, last name, numerical BMI, and BMI category formatted like this:
    - `<first name> <last name> has a BMI of <bmi>. The associated category is: <category>.`


Be sure to include comments in your code. Push your code to your GitHub repository in order to receive credit for the assignment

## Grading Rubric
See the Rubric.md file.

## Example Output

```
Enter your first name: Amit
Enter your last name: Patel
Enter the feet of your height: 6
Enter the inches of your height: 7
Enter your weight in pounds: 140
Amit Patel has a BMI of 15.77. The associated category is: Underweight.
```

