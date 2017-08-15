from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),    #don't include beginning and ending slashes
    url(r'generate$', views.generate)
]