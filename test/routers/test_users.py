import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database.database import get_db
from test.test_utils.database_mocks import override_get_db

# Override the db
app.dependency_overrides[get_db] = override_get_db

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