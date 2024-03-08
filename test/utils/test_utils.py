from src.utils.utils import generate_random_code_and_expiration_time
from datetime import datetime, timedelta


def test_generate_random_code():
    # Generate a random code
    code, expiration_time = generate_random_code_and_expiration_time()

    # Check if the code is a string
    assert isinstance(code, str)

    # Check if the code has a length of 4
    assert len(code) == 4

    # Check if the code consists only of digits
    assert code.isdigit()

    # Convert the code to an integer to check if it's within the valid range
    code_int = int(code)
    assert 0 <= code_int <= 9999

    # Check if expiration time is a datetime object
    assert isinstance(expiration_time, datetime)
    # Check if expiration time is approximately one minute from the current time
    current_time = datetime.now()
    expected_expiration_time = current_time + timedelta(minutes=1)
    assert abs(expiration_time - expected_expiration_time) < timedelta(seconds=1)