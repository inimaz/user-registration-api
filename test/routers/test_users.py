from test.test_utils.database_mocks import override_get_db
from test.test_utils.security_mocks import override_security
from unittest.mock import Mock

# Create a Mock object
mock_email = Mock()

import pytest
from fastapi.testclient import TestClient

from src.database.database import get_db
from src.main import app
from src.routers.users import security
from src.utils.send_email import send_activation_email

# Override the db
app.dependency_overrides[get_db] = override_get_db

app.dependency_overrides[security] = override_security


def override_activation_email():
    def mock_email_func(email, activation_code):
        mock_email(email, activation_code)
        return True

    return mock_email_func


app.dependency_overrides[send_activation_email] = override_activation_email


@pytest.mark.anyio
async def test_create_user():
    input_body = {"email": "test@email.com", "password": "testPassword"}
    with TestClient(app=app) as ac:
        response = ac.post("/register", json=input_body)
    # Check that the response status is correct
    assert response.status_code == 201
    # Check that the response body is correct
    expected_response = {"message": "User test@email.com created successfully"}
    assert response.json() == expected_response
    mock_email.assert_called()


@pytest.mark.anyio
async def test_activate_user():
    input_body = {"activation_code": "1234"}
    with TestClient(app=app) as ac:
        response = ac.post("/activate", json=input_body)
    # Check that the response status is correct
    print(str(response.json()))
    assert response.status_code == 200
    # Check that the response body is correct
    expected_response = {"message": "User test@email.com activated."}
    assert response.json() == expected_response
