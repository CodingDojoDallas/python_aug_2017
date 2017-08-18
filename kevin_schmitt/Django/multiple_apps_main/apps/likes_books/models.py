from __future__ import unicode_literals
from django.db import models

  # Create your models here.



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors = models.ManyToManyField(Author, related_name="books")

class Like(models.Model):
    user = models.ForeignKey(User, related_name='book')
    book = models.ForeignKey(Book, related_name='user')

# class Book_author(models.Model):
#     book = models.ForeignKey(Book, related_name='book')
#     author = models.ForeignKey(Author, related_name='author')

    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length = 255)
    # email = models.CharField(max_length = 255)
    # age = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)