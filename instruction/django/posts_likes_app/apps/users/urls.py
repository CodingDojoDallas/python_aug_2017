from django.conf.urls import url
from . import views

# users/5

#users/<user_id>

urlpatterns = [
    url(r'^$', views.home),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^authenticate$', views.authenticate),
    url(r'^logout$', views.logout),
    url(r'^(?P<user_id>\d+)$', views.show),
]