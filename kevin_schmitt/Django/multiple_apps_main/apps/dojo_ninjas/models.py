from __future__ import unicode_literals
from django.db import models

  # Create your models here.

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name='ninjas')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length = 255)
    # email = models.CharField(max_length = 255)
    # age = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)