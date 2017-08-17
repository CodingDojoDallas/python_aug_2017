from __future__ import unicode_literals
from django.db import models

  # Create your models here.

class books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class books_authors(models.Model):
    book = models.ForeignKey(books, related_name='books')
    author = models.ForeignKey(authors, related_name='authors')

    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length = 255)
    # email = models.CharField(max_length = 255)
    # age = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)