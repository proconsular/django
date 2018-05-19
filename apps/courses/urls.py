from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^destroy/(\d+)$', views.confirm),
    url(r'^delete/(\d+)$', views.destroy),
]
