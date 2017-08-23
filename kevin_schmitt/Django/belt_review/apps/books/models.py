# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..user_review.models import User
# Create your models here.


def create_review(self, post):
    book = Book.objects.create(
        title = post['title'],
        author = post['author'],
        review = post['review'],
        rating = post['rating'],
    )
    return { 'book': book}



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name='uploaded_books')