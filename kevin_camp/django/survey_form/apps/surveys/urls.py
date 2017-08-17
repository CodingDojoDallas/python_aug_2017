from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^results$', views.results),
    url(r'^redirect$', views.redirect),

]
