
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login/$', 'mbrc_profile.views.login'),
                       url(r'^logout/$', 'mbrc_profile.views.logout'),
                       url(r'^register/$', 'mbrc_profile.views.register'),
                       url(r'^profile/$', 'mbrc_profile.views.edit_profile'),
                       url(r'^password/$', 'mbrc_profile.views.change_password'),
                       url(r'^email_confirm/(\w+)/$', 'mbrc_profile.views.email_confirm'),
                       url(r'^sms_confirm/$', 'mbrc_profile.views.sms_confirm'),
                       url(r'^sms_reconfirm/$', 'mbrc_profile.views.sms_reconfirm'),
                       )