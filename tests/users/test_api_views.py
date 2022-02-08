import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_list(client, user_with_password):
    client.force_login(user_with_password)
    response = client.get('/api/users/')
    assert response.status_code == status.HTTP_200_OK

    users = response.json()['results']
    assert len(users) == 1


@pytest.mark.django_db
def test_get_me(client, user_with_password):
    client.force_login(user_with_password)
    response = client.get('/api/users/me/')
    assert response.status_code == status.HTTP_200_OK

    user = response.json()
    assert user == {
        'username': user_with_password.username,
        'first_name': user_with_password.first_name,
        'last_name': user_with_password.last_name,
        'uuid': str(user_with_password.uuid),
        'url': f'http://testserver/api/users/{user_with_password.uuid}/',
    }
