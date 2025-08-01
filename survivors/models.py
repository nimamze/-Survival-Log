from django.db import models


class Survivor(models.Model):
    
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField()

