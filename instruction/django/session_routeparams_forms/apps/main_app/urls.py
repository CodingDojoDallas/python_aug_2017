from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^favoriteNumber/(?P<fave_num>\d+)$', views.favoriteNumber),
    url(r'^favoriteTeam/(?P<fave_team>\w+)$', views.favoriteTeam),

]