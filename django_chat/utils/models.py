import uuid

from django.db import models


class TimestampedModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
