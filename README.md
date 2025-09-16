#### Assignment 2
# Loan Risk Assessment

You’ll be creating a simple Python program that prompts the user for financial information and calculates their Debt-to-Income (DTI) ratio. Based on the DTI value, your program will also categorize the user's loan risk.

Put your code in the `a02_loan_risk_assessment.py` file. Do not edit or delete any other files.

## Logical Flow
1. Prompt the user to enter their information with the following prompts:
    - `Enter your first name: `
    - `Enter your last name: `
    - `Enter your annual income in dollars: `
    - `Enter your total monthly debt payments in dollars: `
    - Store each of the inputs in a variable.
    - Allow decimal numbers for income and debt.
    - Be sure to include a colon and an extra space at the end of each input prompt, and use the exact spelling and wording shown above.

2. Calculate the DTI (Debt-to-Income Ratio) using the following formula:
    - DTI = monthly debt / (annual income / 12)
    - The DTI should be rounded to the 2nd decimal place.
    - Note: to simplify the assignment, assume the user will never enter in 0 for their income. If you want to try and handle that case, feel free but it won't improve the score you get on this assignment.

3. Classify the DTI according to the following categories:
    - Low Risk: DTI < 0.20
    - Moderate Risk: 0.20 <= DTI < 0.36
    - Elevated Risk: 0.36 <= DTI < 0.50
    - High Risk: DTI >= 0.50

4. At the end, print out the user's first name, last name, DTI, and DTI category in the following format:
    - `<first name> <last name> has a DTI of <dti>. The associated category is: <category>.`

Be sure to include comments in your code. Push your code to your GitHub repository in order to receive credit for the assignment.

## Rubric
- See `RUBRIC.md` for details on each of the tests you're scored on.
- To see what score you'll receive, run the tests using the testing tab (it looks like a beaker).
    - In the testing tab, press `Configure Python Tests`, then choose `pytest`, then `tests`, and then press the `Run Tests` button.
        - If you accidentally choose the wrong options for `Configure Python Tests`, to choose again, go to `View` > `Command Palette` and then type `Python: Configure Tests`. Then choose the options above again.
- To see your results and any error messages, right click the `TEST_RESULTS_SUMMARY.md` file and choose `Open Preview`.

## Example Output

```
Enter your first name: Taylor
Enter your last name: Nguyen
Enter your annual income in dollars: 60000
Enter your total monthly debt payments in dollars: 900
Taylor Nguyen has a DTI of 0.18. The associated category is: Low Risk.
```