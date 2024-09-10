import pytest


# Override the built-in input to capture prompts
def mock_input(expected_prompts, inputs):
    """ Helper function to mock input and capture prompts """
    input_iter = iter(inputs)
    prompt_iter = iter(expected_prompts)

    def mocked_input(prompt):
        expected_prompt = next(prompt_iter)  # Store the next expected prompt
        assert prompt == expected_prompt, f"Expected: {expected_prompt}, but got: {prompt}"
        return next(input_iter)  # Return the next user input
    
    return mocked_input

# Test to verify correct prompts for user inputs
def test_correct_output_message(monkeypatch, run_script):
    # Expected input prompts
    expected_prompts = [
        "please enter your first name: ",
        "please enter your last name: ",
        "enter your height in feet: ",
        "please enter height in inches: ",
        "please enter weight in lbs: "
    ]
    
    # Mock inputs that would be provided by the user
    user_inputs = ['Amit', 'Patel', '6', '7', '140']

    # Patch the built-in input function with mock_input
    monkeypatch.setattr('builtins.input', mock_input(expected_prompts, user_inputs))

    # Run the script using the run_script fixture (it doesn't return output here)
    run_script()


# # Parametrized test for BMI calculations
# @pytest.mark.parametrize("user_inputs, expected_name, expected_bmi", [
#     (['Amit', 'Patel', '6', '7', '140'], "Amit Patel", "15.77"),  # Amit Patel
#     (['John', 'Doe', '5', '10', '200'], "John Doe", "28.69"),    # John Doe
#     (['Jane', 'Doe', '5', '5', '150'], "Jane Doe", "24.96"),     # Jane Doe
# ])
# def test_bmi_calculation(run_script, user_inputs, expected_name, expected_bmi):
#     output = run_script(user_inputs)
#     assert f"{expected_name} has a BMI of {expected_bmi}." in output[-1]


# # Parametrized test for BMI categories
# @pytest.mark.parametrize("user_inputs, expected_category", [
#     (['Amit', 'Patel', '6', '7', '140'], "Underweight"),    # Amit Patel
#     (['Jane', 'Doe', '5', '5', '150'], "Normal weight"),    # Jane Doe
# ])
# def test_bmi_category(run_script, user_inputs, expected_category):
#     output = run_script(user_inputs)
#     assert f"The associated category is: {expected_category}." in output[-1]


# # Test for specific BMI output with rounding
# def test_bmi_rounding(run_script):
#     user_inputs = ['John', 'Doe', '5', '10', '200']  # Direct test input for John Doe
#     output = run_script(user_inputs)

#     assert "John Doe has a BMI of 28.69." in output[-1]


# # Test for full output format, including both BMI and category
# def test_full_output_format(run_script):
#     user_inputs = ['Jane', 'Doe', '5', '5', '150']  # Direct test input for Jane Doe
#     expected_output = "Jane Doe has a BMI of 24.96. The associated category is: Normal weight."

#     output = run_script(user_inputs)
#     assert expected_output in output[-1]