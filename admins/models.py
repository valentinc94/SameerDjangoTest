from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admins = models.BooleanField(default = False)
    is_manager = models.BooleanField(default = False)
    is_worker = models.BooleanField(default = False)
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.email

