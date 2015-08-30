
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^anketa/$', 'farm_polls.views.anketa_list'),
                       url(r'^anketa/(\d)/$','farm_polls.views.anketa_show'),
                       url(r'^', 'farm_polls.views.anketa_list'),
                       )