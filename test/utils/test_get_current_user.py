from fastapi import HTTPException, status
from unittest.mock import MagicMock
from src.utils.get_current_user import get_current_user

def test_get_current_user_correct_credentials():
    # Arrange
    credentials = MagicMock()
    credentials.username = "test@example.com"
    credentials.password = "password123"
    
    db_connection = MagicMock()
    user_data = {"email": "test@example.com", "password_hash": "hashed_password"}
    db_connection.get_one_user_by_email.return_value = user_data

    # Act
    result = get_current_user(credentials, db_connection)

    # Assert
    assert result == user_data

def test_get_current_user_incorrect_username():
    # Arrange
    credentials = MagicMock()
    credentials.username = "test@example.com"
    credentials.password = "password123"
    
    db_connection = MagicMock()
    db_connection.get_one_user_by_email.side_effect = Exception("User not found")

    # Act and Assert
    try:
        get_current_user(credentials, db_connection)
    except HTTPException as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED
        assert e.detail == "Incorrect username or password"
        assert e.headers == {"WWW-Authenticate": "Basic"}

def test_get_current_user_incorrect_password():
    # Arrange
    credentials = MagicMock()
    credentials.username = "test@example.com"
    credentials.password = "incorrect_password"
    
    db_connection = MagicMock()
    user_data = {"email": "test@example.com", "password_hash": "hashed_password"}
    db_connection.get_one_user_by_email.return_value = user_data

    # Act and Assert
    try:
        get_current_user(credentials, db_connection)
    except HTTPException as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED
        assert e.detail == "Incorrect username or password"
        assert e.headers == {"WWW-Authenticate": "Basic"}

