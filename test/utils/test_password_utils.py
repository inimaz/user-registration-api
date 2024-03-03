# Example passwords for testing
from src.utils.password_utils import get_password_hash, validate_password


PASSWORD = "password12345"
HASHED_PASSWORD = get_password_hash(PASSWORD)

def test_get_password_hash():
    # Test if get_password_hash returns a string
    hashed_password = get_password_hash(PASSWORD)
    assert isinstance(hashed_password, str)

def test_validate_password_correct():
    # Test if validate_password returns True for correct password
    assert validate_password(PASSWORD, HASHED_PASSWORD)

def test_validate_password_incorrect():
    # Test if validate_password returns False for incorrect password
    assert not validate_password("incorrect_password", HASHED_PASSWORD)