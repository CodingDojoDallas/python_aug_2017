from __future__ import unicode_literals

from django.db import models

from ..users.models import User

class PostManager(models.Manager):
	#DO NOT PASS THE FULL REQUEST OBJECT TO THE MANAGER!
	def validate_post(self, post, user_id):
		errors = []
		if post['content'] == '':
			errors.append('Content cannot be blank')

		if not errors:
			#data is valid, create the post
			Post.objects.create(
				content=post['content'],
				user=User.objects.get(id=user_id)
			)
			return { 'status': True }
		else:
			return { 'status': False, 'errors': errors }

# Create your models here.
class Post(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, related_name="posts")
	likes = models.ManyToManyField(User, related_name="posts_liked")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PostManager()
	
