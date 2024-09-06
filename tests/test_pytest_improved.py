import pytest


# Test to verify correct prompts for user inputs
def test_correct_output_message(run_script):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']  # Use this manually since it's specific to this test
    output = run_script(user_inputs)

    assert output[0] == "please enter your first name: "
    assert output[1] == "please enter your last name: "
    assert output[2] == "enter your height in feet: "
    assert output[3] == "please enter height in inches: "
    assert output[4] == "please enter weight in lbs: "


# Parametrized test for BMI calculations
@pytest.mark.parametrize("user_inputs, expected_name, expected_bmi", [
    pytest.lazy_fixture('user_data')[0][:3],  # Amit Patel
    pytest.lazy_fixture('user_data')[1][:3],  # John Doe
    pytest.lazy_fixture('user_data')[2][:3],  # Jane Doe
])
def test_bmi_calculation(run_script, user_inputs, expected_name, expected_bmi):
    output = run_script(user_inputs)
    assert f"{expected_name} has a BMI of {expected_bmi}." in output[-1]


# Parametrized test for BMI categories
@pytest.mark.parametrize("user_inputs, expected_category", [
    (pytest.lazy_fixture('user_data')[0][0], "Underweight"),    # Amit Patel
    (pytest.lazy_fixture('user_data')[2][0], "Normal weight"),  # Jane Doe
])
def test_bmi_category(run_script, user_inputs, expected_category):
    output = run_script(user_inputs)
    assert f"The associated category is: {expected_category}." in output[-1]


# Test for specific BMI output with rounding
def test_bmi_rounding(run_script):
    user_inputs = ['John', 'Doe', '5', '10', '200']  # Direct test input for John Doe
    output = run_script(user_inputs)

    assert "John Doe has a BMI of 28.69." in output[-1]


# Test for full output format, including both BMI and category
def test_full_output_format(run_script):
    user_inputs = ['Jane', 'Doe', '5', '5', '150']  # Direct test input for Jane Doe
    expected_output = "Jane Doe has a BMI of 24.96. The associated category is: Normal weight."

    output = run_script(user_inputs)
    assert expected_output in output[-1]