
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^(\d)/$','farm_polls.views.anketa_show'),
                       url(r'^(\d)/(\d)/$','farm_polls.views.anketa_show'),
                       url(r'^save/(\d)/$','farm_polls.views.poll_save'),
                       url(r'^', 'farm_polls.views.anketa_list'),
                       )