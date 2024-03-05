from src.routers.users import security
from src.utils.send_email import send_activation_email
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database.database import get_db
from test.test_utils.database_mocks import override_get_db
from test.test_utils.security_mocks import override_security

# Override the db
app.dependency_overrides[get_db] = override_get_db

app.dependency_overrides[security] = override_security
def override_activation_email():
    return True
app.dependency_overrides[send_activation_email] = override_activation_email

@pytest.mark.anyio
async def test_create_user():
    input_body = {"email":"test@email.com", "password":"testPassword"}
    with TestClient(app=app) as ac:
        response = ac.post("/register", json =input_body)
    # Check that the response status is correct
    assert response.status_code == 201
    # Check that the response body is correct
    expected_response = {"message": "User test@email.com created successfully"}
    assert response.json() == expected_response

@pytest.mark.anyio
async def test_activate_user():
    input_body = {"activation_code":"1234"}
    with TestClient(app=app) as ac:
        response = ac.post("/activate", json =input_body)
    # Check that the response status is correct
    assert response.status_code == 201
    # Check that the response body is correct
    expected_response = {"message": "User test@email.com created successfully"}
    assert response.json() == expected_response