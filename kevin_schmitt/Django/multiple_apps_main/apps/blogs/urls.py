from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^blogs', views.index),
    url(r'^blogs/create', views.new),
    url(r'^blogs/{n}', views.display),
    url(r'^blogs/{n}/edit', views.edit),
    url(r'^blogs/{n}delete', views.destroy)
]