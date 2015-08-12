
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login/$', 'loginsys.views.login'),
                       url(r'^logout/$', 'loginsys.views.logout'),
                       url(r'^register/$', 'loginsys.views.register'),
                       url(r'^sms_confirm/$', 'loginsys.views.sms_confirm'),
                       url(r'^sms_reconfirm/$', 'loginsys.views.sms_reconfirm'),
                       )