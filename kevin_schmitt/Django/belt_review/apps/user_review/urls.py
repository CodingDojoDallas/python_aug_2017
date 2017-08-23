from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^new', views.new),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^logout', views.logout),
]