from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^new', views.new),
    url(r'^create', views.create),
]