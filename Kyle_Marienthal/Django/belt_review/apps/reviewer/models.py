# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def validate_registration(self, post):
        errors=[]
        if post['name'] == '':
            errors.append('fill out your damn name')
        if post['alias'] == '':
            errors.append('gimme dat code name')
        if len(post['email']) < 5:
            errors.append('email por favor')
        if len(post['password']) < 3:
            errors.append('keep it secret, keep it safe')
        if post['password'] != post['confpass']:
                errors.append('get your shit together')
        if not errors:
            user=User.objects.create(
                name = post['name'],
                alias =  post['alias'],
                email = post['email'],
                password = bcrypt.hashpw(post['password'].encode(),bcrypt.gensalt(5))                
            )
            return {'status':True, 'user':user}
        else:
            return {'status':False, 'errors':errors}
    
    def login():
        pass

class User(models.Model):
    name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
