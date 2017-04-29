from django.conf.urls import *
from jftapp import views

urlpatterns = [ 
    url(r'^$', views.home),
    url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^(?P<month>\w{3})/$', views.by_month),
    url(r'^(?P<month>\w{3})/(?P<day>\d\d)/$', views.by_date),
    ]
