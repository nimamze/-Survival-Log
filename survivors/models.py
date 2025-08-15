from django.db import models
from django.contrib.auth.models import AbstractUser

class Survivor(AbstractUser):
    is_suspicious = models.BooleanField(default=False)
    consecutive_even_numbers = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

    

