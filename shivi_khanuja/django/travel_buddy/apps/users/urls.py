from django.conf.urls import url
from . import views
	

urlpatterns = [
    url(r'^$', views.main),
    url(r'^login$', views.login),
    url(r'^users/register$', views.register),
    url(r'^users/login$', views.login),
    url(r'^users/success$', views.success),
    url(r'^users/new$', views.new),


]