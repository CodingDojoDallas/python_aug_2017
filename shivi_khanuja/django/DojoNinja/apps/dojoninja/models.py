from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
      name = models.CharField(max_length=255)
      city = models.CharField(max_length=255)
      state = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
class Ninja(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # Notice the association made with ForeignKey for a one-to-many relationship
      # There can be many comments to one blog
      dojo = models.ForeignKey(Dojo,related_name='ninjas')
