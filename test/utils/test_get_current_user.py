from unittest.mock import MagicMock

from fastapi import HTTPException, status

from src.utils.get_current_user import get_current_user
from test.test_utils.database_mocks import MockedDBNotFound, override_get_db


def test_get_current_user_correct_credentials():
    # Arrange
    credentials = MagicMock()
    credentials.username = "test@example.com"
    credentials.password = "password123"

    user_data = {"email": "test@email.com", "password_hash": "$2b$12$SNEZNiJRv/i4fH8ttAzVU.5kPAhNM90Yq.zKVn5g5Pdy7qEsoYPR."}

    # Act
    with override_get_db() as db_connection:
        result = get_current_user(credentials, db_connection)

    # Assert
    assert str(result) == 'User(id=1, user_email=test@email.com, password_hash=$2b$12$SNEZNiJRv/i4fH8ttAzVU.5kPAhNM90Yq.zKVn5g5Pdy7qEsoYPR., activation_code=1234, activation_code_expiration_time=2099-03-08 09:39:50.365025 is_active=False)'



def test_get_current_user_incorrect_username():
    # Arrange
    credentials = MagicMock()
    credentials.username = "test@example.com"
    credentials.password = "password123"

    db_connection = MockedDBNotFound()

    # Act and Assert
    try:
        get_current_user(credentials, db_connection)
    except HTTPException as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED
        assert e.detail == "Incorrect username or password"
        assert e.headers == {"WWW-Authenticate": "Basic"}
