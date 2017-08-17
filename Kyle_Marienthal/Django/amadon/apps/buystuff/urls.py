from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^thankyou$', views.thankyou),
    url(r'^buy$', views.buy)
]