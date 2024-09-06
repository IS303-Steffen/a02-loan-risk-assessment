# conftest.py can be accessed by all test_ files with pytest is invoked. Put fixtures here to avoid redundancy.
import pytest

# Enter the file name, use the solution file when testing.
file_to_test = "a2_BMI_solution.py"


# This runs the script with an expected number of inputs. Returns the output
@pytest.fixture
def run_script(monkeypatch, capsys):
    def _run(user_inputs):
        input_iter = iter(user_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

        with open(file_to_test) as f:
            code = compile(f.read(), file_to_test, 'exec')
            exec(code)

        captured = capsys.readouterr()
        return captured.out.strip().split('\n') # returns the output as a list of strings, with each line being separated.
    
    return _run

# Set of test cases, each meant to capture something at the individual weight categories.
@pytest.fixture
def user_data():
    return [
        (['Amit', 'Patel', '6', '7', '140'], "Amit Patel", "15.77", "Underweight"),
        (['John', 'Doe', '5', '10', '200'], "John Doe", "28.69", "Overweight"),
        (['Jane', 'Doe', '5', '5', '150'], "Jane Doe", "24.96", "Normal weight")
    ]