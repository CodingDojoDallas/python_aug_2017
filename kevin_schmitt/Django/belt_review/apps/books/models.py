# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..user_review.models import *
# Create your models here.


# def create_review(self, post):
#     book = Book.objects.create(
#         title = post['title'],
#         author = post['author'],
#         review = post['review'],
#         rating = post['rating'],
#     )
#     return { 'book': book}

# def validate_registration(self, post):
#         #step 1: validate the form
#         errors = []
#         if post['name'] == '':
#             errors.append('Name cannot be blank')
#         if post['email'] == '':
#             errors.append('Email cannot be blank')
#         user = User.objects.filter(email=post['email']).first()
#         if user:
#             errors.append('Email already in use')
#         if len(post['password']) < 4:
#             errors.append('Password must be at least 4 characters')
#         elif post['password'] != post['password_confirmation']:
#             errors.append('Passwords must match')
#         #step 2: if invalid create error messages
#         #kinda already covered this part in step 1
#         if not errors:
#             user = User.objects.create(
#                 name = post['name'],
#                 alias = post['alias'],
#                 email = post['email'],
#                 password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt(10))
#             )
#             return {'status':True, 'user':user}
#         else:
#             return { 'status': False, 'errors': errors}
#         #step 3: if valid create the user and the session

class BookManager(models.Manager):
    def make_book(self, post):
        book = Book.objects.create(
                title = post['title'],

            )
        pass

class AuthorManager(models.Manager):
    def make_author(self, post):
        if post['author1'] == '':
            author = Author.objects.create(
                    name = post['author2'],
            )
            return {'author': author}
        else:
            author = Author.objects.create(
                    name = post['author1'],
            )
            return {'author': author}

class ReviewManager(models.Manager):
    def make_book(self, post):
        book = Book.objects.create(
                title = post['title'],

            )
        pass

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books') 
    user = models.ForeignKey(User, related_name='books_uploaded')   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='reviews_uploaded')
    book = models.ForeignKey(User, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    

# make a reviews table/model many to many with ratings as well
# class Review(models.Model):
    # content = models.TextField()
    # rating = models.IntegerField()
    # user = models.ForeignKey(User, related_name='reviews')
    # book = models.ForeignKey(User, related_name='reviews')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)