from django.db import models
from django.contrib.auth.models import AbstractUser

class CallebautUser(AbstractUser):
    photo = models.ImageField(upload_to="img", blank=True,)
