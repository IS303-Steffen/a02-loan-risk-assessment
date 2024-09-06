import pytest

def run_script_with_input(inputs, monkeypatch):
    # Mock input with monkeypatch
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    # Run the script
    with open('a2_BMI.py') as f:
        code = compile(f.read(), 'a2_BMI.py', 'exec')
        exec(code)

def test_correct_output_message(monkeypatch, capsys):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']
    run_script_with_input(user_inputs, monkeypatch)

    # Capture printed output
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Check output messages
    assert output[0] == "please enter your first name: "
    assert output[1] == "please enter your last name: "
    assert output[2] == "enter your height in feet: "
    assert output[3] == "please enter height in inches: "
    assert output[4] == "please enter weight in lbs: "

def test_bmi_calculation(monkeypatch, capsys):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']
    run_script_with_input(user_inputs, monkeypatch)

    # Capture printed output
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Check BMI output
    assert "Amit Patel has a BMI of 15.77." in output[-1]

def test_bmi_category(monkeypatch, capsys):
    user_inputs = ['Amit', 'Patel', '6', '7', '140']
    run_script_with_input(user_inputs, monkeypatch)

    # Capture printed output
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Check BMI category output
    assert "The associated category is: Underweight." in output[-1]

def test_bmi_rounding(monkeypatch, capsys):
    user_inputs = ['John', 'Doe', '5', '10', '200']
    run_script_with_input(user_inputs, monkeypatch)

    # Capture printed output
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Check BMI output for rounding
    assert "John Doe has a BMI of 28.69." in output[-1]

def test_full_output_format(monkeypatch, capsys):
    user_inputs = ['Jane', 'Doe', '5', '5', '150']
    run_script_with_input(user_inputs, monkeypatch)

    # Expected output
    expected_output = "Jane Doe has a BMI of 24.96. The associated category is: Normal weight."

    # Capture printed output
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Check the full output format
    assert expected_output in output[-1]