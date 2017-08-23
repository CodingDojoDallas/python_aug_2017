from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
]
