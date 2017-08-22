# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# class BookManager(models.Manager):
#     def createBook(self,post):
#         book = Book.objects.create(
#         title =
#         )



class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    author = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#    objects = BookManager()
