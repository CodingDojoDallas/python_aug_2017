# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    #DO NOT PASS THE FULL REQUEST OBJECT TO THE MANAGER!
    def validate(self, post):
        errors = []
        if len(post['name']) < 6:
            errors.append('Name must be atleast 6 characters')
        if len(post['desc']) < 15:
            errors.append('Description must be atleast 16 characters')
        #step 2: if invalid create error messages
        #kinda already covered this part in step 1
        if not errors:
            course = Course.objects.create(
                name = post['name'],
                desc = post['desc'],
            )
            return {'status':True, 'course':course}
        else:
            return { 'status': False, 'errors': errors}


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()