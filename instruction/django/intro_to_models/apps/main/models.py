from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=255)
	still_together = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	artist = models.ForeignKey(Artist, related_name="albums")
	
class Song(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	artist = models.ForeignKey(Artist, related_name="songs")
	album = models.ForeignKey(Album, related_name="songs")
