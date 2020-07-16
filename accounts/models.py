from django.db import models
from django import forms


# Create your models here.
class Account(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64, unique=False)
