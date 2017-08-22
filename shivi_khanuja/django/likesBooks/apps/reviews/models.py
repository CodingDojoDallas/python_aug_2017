from __future__ import unicode_literals

from django.db import models
  
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    created_at =models.DateTimeField(auto_now_add=True) 
    updated_at =models.DateTimeField(auto_now=True)
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True) 
    updated_at =models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name='books_liked')
    uploader = models.ForeignKey(User, related_name='books')
