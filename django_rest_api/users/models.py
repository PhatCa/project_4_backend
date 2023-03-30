from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password



# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username