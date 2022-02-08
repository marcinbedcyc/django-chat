import pytest
from celery.result import EagerResult

from django_chat.users.tasks import get_users_count


@pytest.mark.django_db
def test_user_count(users_10):
    task_result = get_users_count.delay()
    assert isinstance(task_result, EagerResult)
    assert task_result.result == 10
