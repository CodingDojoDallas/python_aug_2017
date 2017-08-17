from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    # id will be created automatically
    name = models.CharField(max_length=255) #VARCHAR(255)
    email = models.CharField(max_length=255) #VARCHAR(255)
    age = models.IntegerField() #INT
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
