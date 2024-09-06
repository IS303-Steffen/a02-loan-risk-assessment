import pytest
from io import StringIO
import sys
from unittest.mock import patch

@pytest.fixture
def captured_output():
    # Fixture to capture stdout output
    held_output = StringIO()
    sys.stdout = held_output
    yield held_output
    sys.stdout = sys.__stdout__

def run_script_with_input(inputs):
    # Utility to run the script with mocked inputs
    with patch('builtins.input', side_effect=inputs):
        with open('a2_BMI.py') as f:
            code = compile(f.read(), 'a2_BMI.py', 'exec')
            exec(code)

def test_correct_output_message(captured_output):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']
    run_script_with_input(user_inputs)

    output = captured_output.getvalue().strip().split('\n')

    assert output[0] == "please enter your first name: "
    assert output[1] == "please enter your last name: "
    assert output[2] == "enter your height in feet: "
    assert output[3] == "please enter height in inches: "
    assert output[4] == "please enter weight in lbs: "

def test_bmi_calculation(captured_output):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']
    run_script_with_input(user_inputs)

    output = captured_output.getvalue().strip().split('\n')
    assert "Amit Patel has a BMI of 15.77." in output[-1]

def test_bmi_category(captured_output):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']
    run_script_with_input(user_inputs)

    output = captured_output.getvalue().strip().split('\n')
    assert "The associated category is: Underweight." in output[-1]

def test_bmi_rounding(captured_output):
    user_inputs = ['John', 'Doe', '5', '10', '200']
    run_script_with_input(user_inputs)

    output = captured_output.getvalue().strip().split('\n')
    assert "John Doe has a BMI of 28.69." in output[-1]

def test_full_output_format(captured_output):
    user_inputs = ['Jane', 'Doe', '5', '5', '150']
    run_script_with_input(user_inputs)

    expected_output = "Jane Doe has a BMI of 24.96. The associated category is: Normal weight."
    output = captured_output.getvalue().strip().split('\n')
    assert expected_output in output[-1]