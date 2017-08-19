from __future__ import unicode_literals
from django.db import models

  # Create your models here.



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name='uploaded_books')
    likes = models.ManyToManyField(User, related_name="books_liked")

# class Like(models.Model):
#     user = models.ForeignKey(User, related_name='likes')
#     book = models.ForeignKey(Book, related_name='likes')

# class Book_author(models.Model):
#     book = models.ForeignKey(Book, related_name='book')
#     author = models.ForeignKey(Author, related_name='author')

    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length = 255)
    # email = models.CharField(max_length = 255)
    # age = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)