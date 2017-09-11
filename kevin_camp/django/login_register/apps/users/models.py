# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def validate_login(self, post):
		user = User.objects.filter(user_name=post['user_name']).first()
		if user and bcrypt.checkpw(post['password'].encode(), user.password.encode()):
			return { 'status':True, 'user':user }
		else:
			return { 'status':False, 'error': "Invalid Credentials"  }


	def validate_registration(self, post):
		errors = []
		if len(post['name']) < 3:
			errors.append('Name must be at least three characters')
		if len(post['user_name']) < 3:
			errors.append('Name and Username must be at least three characters')
		if len(post['password']) < 8:
			errors.append('Password must be at least 8 characters')
		if not errors:
			user = User.objects.create(
				name=post['name'],
				user_name=post['user_name'],
				password=bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt(10)),
			)
			return {'status': True, 'user': user}
		else:
			return {'status': False, 'errors': errors}


class User(models.Model):
	name = models.CharField(max_length=255)
	user_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
