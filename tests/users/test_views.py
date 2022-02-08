import pytest
from django.http import HttpResponseRedirect
from rest_framework import status

from django_chat.users.views import UserDetailView


@pytest.mark.django_db
def test_user_detail_view_authenicated(client, user_with_password):
    client.force_login(user_with_password)
    response = client.get(f'/users/{user_with_password.uuid}/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_detail_view_not_authenicated(client, user_with_password):
    url = f'/users/{user_with_password.uuid}/'
    response = client.get(url)

    assert response.status_code == status.HTTP_302_FOUND
    assert isinstance(response, HttpResponseRedirect)
    # TODO: assert correct redirect to login page url
    # assert response.url == f'{login_url}?next={url}'


@pytest.mark.parametrize('data', [
    {'first_name': 'new', 'last_name': 'identify'},
])
@pytest.mark.django_db
def test_user_update_view_authenicated(client, user_with_password, data):
    client.force_login(user_with_password)
    response = client.post('/users/~update/', data, follow=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.resolver_match.func.__name__ == UserDetailView.as_view().__name__
