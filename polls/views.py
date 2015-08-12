# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib import auth
import datetime

# Create your views here.
def hello(request):
    now=datetime.datetime.now()
    arg = {'now':now,'username':auth.get_user(request).username}
    return render_to_response('current_time.html', arg)

def hours_ahead(request,offset=0):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now=datetime.datetime.now()
    dt=now+datetime.timedelta(hours=offset)
    arg = {'now':now,'offset':offset,'dt':dt,'username':auth.get_user(request).username}
    return render_to_response('ahead_time.html',arg)