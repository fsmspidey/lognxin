from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^report/(?P<site>(.*))/(?P<format>[0-9]+)$', views.report),
    url(r'^$', views.index),
]
