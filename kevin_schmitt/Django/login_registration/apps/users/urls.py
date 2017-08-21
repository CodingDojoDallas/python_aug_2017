from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^new', views.new),
    url(r'^create', views.create),
    url(r'^success', views.success),
    url(r'^login', views.login),
    url(r'^authenticate', views.authenticate),
    url(r'^logout', views.logout),
]