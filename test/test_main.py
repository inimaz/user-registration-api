import pytest
from fastapi.testclient import TestClient
from src.main import app 

@pytest.mark.anyio
async def test_root():
    with TestClient(app=app) as ac:
        response = ac.get("/")
    # Check that the response status is correct
    assert response.status_code == 200
    # Check that the response body is correct
    assert response.json() == {"message": "User API root page"}
