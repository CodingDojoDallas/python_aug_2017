from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^submit$', views.submit),
        url(r'^result$', views.result),
        url(r'^process$', views.process)
        ]
