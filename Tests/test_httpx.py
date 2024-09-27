from http.client import responses

import pytest
import httpx

TAG_URL = "https://conduit-api.bondaracademy.com/api/tags"
USER_URL = "https://conduit-api.bondaracademy.com/api/users/login"
ARTICLE_URL = "https://conduit-api.bondaracademy.com/api/articles/"

# Test root endpoint

def test_get_httpx_Check_response_status(): # got status ok
    response = httpx.get(TAG_URL)
    ## debugging
    print('')
    print("status code is", response.status_code)
    print("response body is", response.json())
    ##
    assert response.status_code == 200
    # assert  response.json() == {'tags': ['Test', 'GitHub', 'Coding', 'Bondar Academy', 'qa career', 'Git', 'Zoom', 'Enroll', 'YouTube', 'Blog']} # body is flexible can raise error

def test_get_httpx_Check_in_body():
    response = httpx.get(TAG_URL)
    data = response.json()
    assert "Test" in data["tags"] # find Test in the response body

def test_post_httpx_Get_token():
    payload = {
        "user":
            {"email":"kvolkov_qa@outlook.com",
             "password":"Bladlite2021"
             }
    }
    response = httpx.post(USER_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    authToken = data["user"]['token']
    ## debugging
    print('')
    print(data)
    print(authToken)
    ##

def test_POST_Send_article():
    payload = {
        "user":
            {"email":"kvolkov_qa@outlook.com",
             "password":"Bladlite2021"
             }
    }
    response_auth = httpx.post(USER_URL, json=payload)
    assert response_auth.status_code == 200
    data = response_auth.json()
    authToken = data["user"]['token']
    payload_article = {
        "article":
            {"title":"Pytest title",
             "description":"Pytest article",
             "body":"Pytest body",
             "tagList":[]
             }
    }
    headers = {
        "Authorization":f"Token {authToken}"
        # "Authorization":authToken # will trigger 401 Unauthorized
    }
    response_article = httpx.post(ARTICLE_URL, headers = headers, json=payload_article)
    ## debugging
    print('')
    print(headers)
    print(response_article.status_code)
    # will raise 422 if the article exists.

    data = response_article.json()

    print('')
    slug = data["article"]["slug"]
    print(slug)

def test_DELETE_Remove_article():
    payload = {
        "user":
            {"email": "kvolkov_qa@outlook.com",
             "password": "Bladlite2021"
             }
    }
    response_auth = httpx.post(USER_URL, json=payload)
    data = response_auth.json()
    authToken = data["user"]['token']
    payload_article = {
        "article":
            {"title": "Pytest title 2",
             "description": "Pytest article 2",
             "body": "Pytest body 2",
             "tagList": []
             }
    }
    headers = {
        "Authorization": f"Token {authToken}"
    }
    response_article = httpx.post(ARTICLE_URL, headers=headers, json=payload_article)
    data2 = response_article.json()
    slug = data2["article"]["slug"]

    url = f"https://conduit-api.bondaracademy.com/api/articles/{slug}"
    response_del = httpx.delete(url, headers=headers)
    print(slug)
    assert response_del.status_code == 204