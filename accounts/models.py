from django.db import models
from django.contrib.auth.models import AbstractUser

class UsernameOrEmailUser(AbstractUser):
    # Updating original email field to be unique and required
    email = models.EmailField(max_length=254, unique=True, blank=False)

    def __str__(self):
        return self.username + '|' + self.email
    
