from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'/blogs$', views.index),
    url(r'/blogs/create$', views.new),
    url(r'/blogs/', views.blognumber),
    url(r'/blogs/{{number}}/edit$', views.edit),
    url(r'/blogs/{{number}}delete$', views.delete)
]