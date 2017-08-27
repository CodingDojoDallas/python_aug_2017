from __future__ import unicode_literals

from django.db import models

import bcrypt
	
class UserManager(models.Manager):
    def validate_registration(self, post):
        errors=[]
        if post['name'] == '':
            errors.append('Name cannot be blank')
        if len(post['email']) < 5:
            errors.append('email can not be blank')
        if len(post['password']) < 3:
            errors.append('password can not be blank')
        if post['password'] != post['confpass']:
                errors.append('password can not be blank')
        if not errors:
            user=User.objects.create(
                name = post['name'],
                email = post['email'],
                password = bcrypt.hashpw(post['password'].encode(),bcrypt.gensalt(5))                
            )
            return {'status':True, 'user':user}
        else:
            return {'status':False, 'errors':errors}
    
    def login():
        if request.method == 'POST':
              result = User.objects.validate_login(request.POST)
        if result ['status'] == False:
              messages.error(request, result['error'])
              return redirect('/users/main')
        else:
              
              return redirect('/users/travels')



class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()