from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    kc_id = models.CharField(max_length=255, null=True, blank=True)
    modified_timestamp = models.DateTimeField(auto_now=False, default=timezone.now)
