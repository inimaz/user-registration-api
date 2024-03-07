from src.utils.utils import generate_random_code


def test_generate_random_code():
    # Generate a random code
    code = generate_random_code()

    # Check if the code is a string
    assert isinstance(code, str)

    # Check if the code has a length of 4
    assert len(code) == 4

    # Check if the code consists only of digits
    assert code.isdigit()

    # Convert the code to an integer to check if it's within the valid range
    code_int = int(code)
    assert 0 <= code_int <= 9999
