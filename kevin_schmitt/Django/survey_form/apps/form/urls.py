from django.conf.urls import url
from . import views          


urlpatterns = [
    url(r'^$', views.index),
    url(r'^display$', views.display),
]



# (?P<num>\d+)  is the variable for any number typed into the URI