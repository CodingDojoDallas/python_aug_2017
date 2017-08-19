# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt


class UserManager(models.Manager):
    #DO NOT PASS THE FULL REQUEST OBJECT TO THE MANAGER! REQUEST.SESSION
    def validate_registration(self, post):
        #step 1: Validate Form data
        #instead of request.POST['name'] use post['name']
        #cant use messages here messages.error(request) because we don't have the full "request" object
        #we only have the "post" info
        errors = []
            #empty arrary to hold list of errors
        if post['name'] == '':
            #if name in form is empty string
            errors.append("Name cannot be blank")
        if post['email'] == '':
            #if email blank
            errors.append("Email cannot be blank")
        #check if user's email already exists in the database by
        #checking the database returning the first object in an array of matches
        #if an object exists then same user is already present in the database
        user = User.objects.filter(email=post['email']).first()
        #if a user is found create an error
        if user:
            errors.append('Email already in use')

        #passwords should be at least 4 characters
        if len(post['password']) < 4:
            errors.append('Password must be at least four characters')
        if post['password'] != post['password_confirmation']:
            errors.append('Passwords do not match')
        #step 2: if invalid create error messages
            #Done above "inside the process"

         #step 3: if valid create the user and the session
        if not errors:
            users = user.objects.create(
                name=post['name'],
                email=post['email'],
                #import bcrypt, create a hashed password using bcrypt
                password= bcrypt.hashpw(post['password'].encode(),bcrypt.gensalt(10))
                #timestamp made automatically in the background for this object
                )
            #Test if the user email and password is in the database
            #Else return errors
            #use 'status' to prove success/failure
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'errors': errors}

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
