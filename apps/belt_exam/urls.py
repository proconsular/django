from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.main),
    url(r'^main$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^travels$', views.travels),
    url(r'^logout$', views.logout),
    url(r'^travels/destination/(\d+)$', views.destination),
    url(r'^travels/delete/(\d+)$', views.deleteTrip),
    url(r'^travels/unjoin/(\d+)$', views.unjoinTrip),
    url(r'^travels/add$', views.addTrip),
    url(r'^processTrip$', views.processTrip),
    url(r'^processJoin/(\d+)$', views.processJoin),
]
