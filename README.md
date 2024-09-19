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

## Example Output

```
Enter your first name: Amit
Enter your last name: Patel
Enter the feet of your height: 6
Enter the inches of your height: 7
Enter your weight in pounds: 140
Amit Patel has a BMI of 15.77. The associated category is: Underweight.
```

## Rubric
This assignment contains the automated tests listed below. The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.
<table>
<thead>
    <tr>
        <th>Test</th>
        <th>Description</th>
        <th>Points</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>1. Input Prompts</td>
        <td>You must use <code>input()</code> to ask the user the following prompts:
        <ul>
          <li><code>Enter your first name: </code></li>
        </ul>
        <ul>
          <li><code>Enter your last name: </code></li>
        </ul>
        <ul>
          <li><code>Enter the feet of your height: </code></li>
        </ul> 
        <ul>
          <li><code>Enter the inches of your height: </code></li>
        </ul> 
        <ul>
          <li><code>Enter your weight in pounds: </code></li>
        </ul>   
        </td>
        <td>15</td>
    </tr>
    <tr>
        <td>2. Printed Messages</td>
        <td>Your printed output must contain the phrase:
          <ul>
            <li><code>has a BMI of</code></li>
            <li><code>The associated category is</code></li>
          </ul>        
        </td>
        <td>15</td>
    </tr>
    <tr>
        <td>3. BMI Numerical Calculation</td>
        <td>Your printed output must contain an accurately calculated BMI.<br><br>
        The following cases will be tested:<br><br>
        <table border="1">
          <thead>
            <tr>
              <th>Input</th>
              <th>Expected Output</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>"John", "Doe", "5", "6", "114"</code></td>
              <td><code>'18.40' or '18.4'</code></td>
            </tr>
            <tr>
              <td><code>"Jane", "Smith", "5", "6", "115"</code></td>
              <td><code>"18.56"</code></td>
            </tr>
            <tr>
              <td><code>"Bob", "Brown", "5", "6", "154"</code></td>
              <td><code>"24.85"</code></td>
            </tr>
            <tr>
              <td><code>"Charlie", "Johnson", "5", "6", "185"</code></td>
              <td><code>"29.86"</code></td>
            </tr>
            <tr>
              <td><code>"Diana", "Wilson", "5", "6", "186"</code></td>
              <td><code>"30.02"</code></td>
            </tr>
          </tbody>
        </table>
        </td>
        <td>30</td>
    </tr>
        <tr>
        <td>4. BMI Categorical Calculation</td>
        <td>Your printed output must contain an accurately calculated BMI category.<br><br>
        The following cases will be tested:<br><br>
        <table border="1">
          <thead>
            <tr>
              <th>Input</th>
              <th>Expected Output</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>"John", "Doe", "5", "6", "114"</code></td>
              <td><code>"Underweight"</code></td>
            </tr>
            <tr>
              <td><code>"Jane", "Smith", "5", "6", "115"</code></td>
              <td><code>"Normal weight"</code></td>
            </tr>
            <tr>
              <td><code>"Bob", "Brown", "5", "6", "154"</code></td>
              <td><code>"Normal weight"</code></td>
            </tr>
            <tr>
              <td><code>"Charlie", "Johnson", "5", "6", "185"</code></td>
              <td><code>"Overweight"</code></td>
            </tr>
            <tr>
              <td><code>"Diana", "Wilson", "5", "6", "186"</code></td>
              <td><code>"Obese"</code></td>
            </tr>
          </tbody>
        </table>
        </td>
        <td>30</td>
    </tr>
    <tr>
        <td>5. Sufficient Comments </td>
        <td>Your code must include at least <code>5</code> comments. You can use <code>#</code>, <code>''' '''</code>, or <code>""" """</code></td>
        <td>10</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>
