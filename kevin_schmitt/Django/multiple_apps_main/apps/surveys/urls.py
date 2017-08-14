from django.conf.urls import url
from . import views        


urlpatterns = [
    url(r'^surveys', views.index),
    url(r'^surveys/new', views.new)
]