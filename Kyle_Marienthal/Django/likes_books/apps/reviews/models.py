# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='books_liked')
    uploader = models.ForeignKey(User, related_name='books')

    #user = User.objects.get(id=1)
    #user.books_liked.all()
    #user.books.all()

    #either lookup the user
    #user = User.objects.first() or User.objects.get(id=1)
    #create two books
    #Book.objects.create(
    #   name="my new book",
    #   desc="my new desc",
    #   uploader=User.objects.first()
    #)
    #Book.objects.create(
    #   name="my new second book",
    #   desc="my new second desc",
    #   uploader=User.objects.first()
    #)
    #Book.objects.create(
    #   name="my new second book",
    #   desc="my new second desc",
    #   uploader=User.objects.get(id=2)
    #)
    #Book.objects.create(
    #   name="my new second book",
    #   desc="my new second desc",
    #   uploader=User.objects.get(id=2)
    #)

    