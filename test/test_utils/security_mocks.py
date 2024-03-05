from unittest.mock import MagicMock

def override_security():
    # Arrange
    credentials = MagicMock()
    credentials.username = "test@example.com"
    credentials.password = "password123"
    return credentials