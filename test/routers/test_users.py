import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.mark.anyio
async def test_create_user():
    input_body = {"email":"test@email.com", "password":"testPassword"}
    with TestClient(app=app) as ac:
        response = ac.post("/register", json =input_body)
    print(response)
    # Check that the response status is correct
    assert response.status_code == 201
    # Check that the response body is correct
    assert response.json() == input_body