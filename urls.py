from django.conf.urls.defaults import *
from mysite.jftapp import views

urlpatterns = patterns('',
    url(r'^$', views.todays_reading),
    url(r'^(?P<month>\w{3})/(?P<day>\d\d)/$', views.page_date),
    )
