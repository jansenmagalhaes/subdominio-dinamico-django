from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    organizacao = models.CharField(max_length=20, blank=True)