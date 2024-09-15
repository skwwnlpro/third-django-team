from datetime import datetime

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):

    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
