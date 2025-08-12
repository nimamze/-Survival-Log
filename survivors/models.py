from django.db import models
from django.contrib.auth.models import AbstractUser


class Survivor(AbstractUser):
    is_verified = models.BooleanField(default=False)
    need_puzzle = models.BooleanField(default=False)
