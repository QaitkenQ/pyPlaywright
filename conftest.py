import pytest
import httpx

@pytest.fixture

def get_token():
    user_url = "https://conduit-api.bondaracademy.com/api/users/login"
    payload = {
        "user":
            {"email":"kvolkov_qa@outlook.com",
             "password":"Bladlite2021"
             }
    }
    response = httpx.post(user_url, json=payload)
    assert response.status_code == 200
    data = response.json()
    auth_token = data["user"]['token']
    return auth_token, user_url