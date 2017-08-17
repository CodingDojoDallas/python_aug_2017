from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=255)

class Book(models.Model):
	name = models.CharField(max_length=255)
	authors = models.ManyToManyField(Author, related_name="books")



