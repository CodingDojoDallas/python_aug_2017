from django.conf.urls import url
from . import views

blog_id = 0
urlpatterns = [
	url(r'^$', views.index),
	url(r'^/(?P<blog_id>\d+)$', views.index),
	url(r'^/new$', views.new),
	url(r'^/create$', views.create)
        ]
