# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    #DO NOT PASS THE FULL REQUEST OBJECT TO THE MANAGER!
    def validate_login(self, post):
        user = User.objects.filter(email=post['email']).first()
        if user and bcrypt.checkpw(post['password'].encode(), user.password.encode()):
            #confirms whether or not I found one
            return { 'status': True, 'user': user }
        else:
            return { 'status': False, 'error': "Invalid credentials"}

    def validate_registration(self, post):
        #step 1: validate the form
        errors = []
        if post['name'] == '':
            errors.append('Name cannot be blank')
        if post['email'] == '':
            errors.append('Email cannot be blank')
        user = User.objects.filter(email=post['email']).first()
        if user:
            errors.append('Email already in use')
        if len(post['password']) < 4:
            errors.append('Password must be at least 4 characters')
        elif post['password'] != post['password_confirmation']:
            errors.append('Passwords must match')
        #step 2: if invalid create error messages
        #kinda already covered this part in step 1
        if not errors:
            user = User.objects.create(
                name = post['name'],
                alias = post['alias'],
                email = post['email'],
                password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt(10))
            )
            return {'status':True, 'user':user}
        else:
            return { 'status': False, 'errors': errors}
        #step 3: if valid create the user and the session

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()