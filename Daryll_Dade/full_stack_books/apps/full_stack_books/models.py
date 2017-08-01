from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookManager(models.Manager):
    def validate(self, form_data):
        errors = []
        
        if len(form_data['name']) ==0:
            errors.append('Name is required')
        if len(form_data['title']) ==0:
            errors.append('Title is required')
        if len(form_data['category']) ==0:
            errors.append('Category is required')

        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author= models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()
