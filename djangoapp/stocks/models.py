from django.db import models


from django.shortcuts import render
from .models import Contact

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    stocks = models.CharField(max_length=30)
    




