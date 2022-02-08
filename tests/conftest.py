import pytest

from django_chat.users.models import User
from tests.users.factories import UserFactory


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture()
def users_10():
    return UserFactory.create_batch(10)


@pytest.fixture
def user_with_password():
    return UserFactory(username='john.levis', password='password')
