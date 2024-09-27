import pytest
from fastapi.testclient import TestClient
from simple_api import app

client = TestClient(app)

# Test root endpoint

def test_get(): # got status ok and text body
    response = client.get("/")
    assert response.status_code == 200
    assert  response.json() == {"message": "Hello, World!"}