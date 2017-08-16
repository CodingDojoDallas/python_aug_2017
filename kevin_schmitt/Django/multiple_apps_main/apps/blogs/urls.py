from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^blogs', views.index),
    url(r'^blogs/create', views.new),
    url(r'^blogs/(?P<num>\d+)', views.display),
    url(r'^blogs/(?P<num>\d+)/edit$', views.edit),
    url(r'^blogs/(?P<num>\d+)/delete', views.destroy)
]


