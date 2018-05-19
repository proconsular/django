from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.user),
    url(r'^books/add$', views.add),
    url(r'^books/add_review$', views.add_review),
    url(r'^books/create$', views.create),
    url(r'^logout$', views.logout),
    url(r'^books/(\d+)', views.book),
    url(r'^users/(\d+)', views.profile)
]
