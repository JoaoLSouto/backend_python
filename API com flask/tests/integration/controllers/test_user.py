from http import HTTPStatus
from src.app import Role, User, db

def test_get_user_success(client):
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    user = User(username='john-doe', password='test', role_id=role.id)
    db.session.add(user)
    db.session.commit()

    response = client.get("/users/{user.id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"id": user.id, "username": user.username}

def test_get_user_success(client):
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    user_id = 1


    response = client.get(f"/users/{user_id}")

    assert response.status_code == HTTPStatus.NOT_FOUND