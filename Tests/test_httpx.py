import httpx

TAG_URL = "https://conduit-api.bondaracademy.com/api/tags"
ARTICLE_URL = "https://conduit-api.bondaracademy.com/api/articles/"

# Test root endpoint

def test_get_httpx_check_response_status(): # got status ok
    response = httpx.get(TAG_URL)
    ## debugging
    print('')
    print("status code is", response.status_code)
    print("response body is", response.json())
    ##
    assert response.status_code == 200

def test_get_httpx_check_in_body():
    response = httpx.get(TAG_URL)
    data = response.json()
    assert "Test" in data["tags"] # find Test in the response body


def test_post_send_article(get_token):
    user_url = get_token[1]
    auth_token = get_token[0]
    payload = {
        "user":
            {"email":"kvolkov_qa@outlook.com",
             "password":"Bladlite2021"
             }
    }
    response_auth = httpx.post(user_url, json=payload)
    assert response_auth.status_code == 200
    payload_article = {
        "article":
            {"title":"Pytest title",
             "description":"Pytest article",
             "body":"Pytest body",
             "tagList":[]
             }
    }
    headers = {
        "Authorization":f"Token {auth_token}"
        # "Authorization":auth_token # will trigger 401 Unauthorized
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
    assert  response_article.status_code == 201

def test_delete_remove_article(get_token):
    auth_token = get_token[0]
    payload_article = {
        "article":
            {"title": "Pytest title 2",
             "description": "Pytest article 2",
             "body": "Pytest body 2",
             "tagList": []
             }
    }
    headers = {
        "Authorization": f"Token {auth_token}"
    }
    response_article = httpx.post(ARTICLE_URL, headers=headers, json=payload_article)
    data = response_article.json()
    slug = data["article"]["slug"]

    url = f"https://conduit-api.bondaracademy.com/api/articles/{slug}"
    response_del = httpx.delete(url, headers=headers)
    print(slug)
    assert response_del.status_code == 204


def test_del_article_by_id(get_token):
    auth_token = get_token[0]
    headers = {
        "Authorization": f"Token {auth_token}"
    }

    response = httpx.get(ARTICLE_URL, headers=headers)
    data = response.json()
    for val in data['articles']:
        if (val['title']).__contains__('Pytest title'):
            slug = (val['slug'])
            url = f"https://conduit-api.bondaracademy.com/api/articles/{slug}"
            response_del = httpx.delete(url, headers=headers)
            assert response_del.status_code == 204