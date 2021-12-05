from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    age = models.PositiveIntegerField(blank=False, default=18)
    first_name = None
    last_name = None
    image = models.ImageField(blank=True)
