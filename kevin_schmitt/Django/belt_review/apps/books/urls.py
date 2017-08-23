from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
    # url(r'^book_show/(?P<book_id>\d+)$', views.book_show),
    url(r'^book_show$', views.book_show),
]
