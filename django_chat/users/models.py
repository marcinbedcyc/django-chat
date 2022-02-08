from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext as _

from ..utils.models import TimestampedModel


class User(AbstractUser, TimestampedModel):
    """Default custom user model for django_chat."""

    def get_absolute_url(self):
        """
        Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"uuid": self.uuid})

    class Meta:
        verbose_name = _('User')
        ordering = ['username']
