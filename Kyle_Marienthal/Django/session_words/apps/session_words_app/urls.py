from django.conf.urls import url
from . import views
urlpatterns = [
    url (r'^$', views.index),
    url(r'^words$', views.create),
    url(r'^reset$', views.reset),
]