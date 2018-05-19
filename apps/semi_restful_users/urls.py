from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users$', views.users),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^user/(\d+)/destroy$', views.destroy),
    url(r'^user/(\d+)$', views.show),
    url(r'^user/(\d+)/edit$', views.edit),
    url(r'^users/update$', views.update),
]
