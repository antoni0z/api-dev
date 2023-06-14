from app import schemas
import pytest
from jose import jwt
from app.config import settings
# def test_root(client,session):
#     res = client.get("/")
#     print(res.json().get("message"))
#     assert res.json().get("message") == 'A ver como de sincronizado está G'
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json = {"email":"hola10@gmail.com","password":"pollagigante45"})
    new_user  = schemas.UserOut(**res.json())
    assert new_user.email == "hola10@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user,client):
    res = client.post(
         "/login", data = {"username":test_user['email'],"password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms= [settings.algorithm])
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",[
    ("wrongemail@gmail.com", "pollagigante45",403),
    ("hola10@gmail.com","wrongpassword",403),
    ("wrongemail@gmail.com","wrongpassword",403),
    (None, "password123",422),
    ("hola10@gmail.com",None, 422),
    (None, None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login",data = {"username":email, "password":password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid Credentials"