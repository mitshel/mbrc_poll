# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from farm_polls.models import anketa
from mbrc_profile.models import specialize, UserProfile
from django.contrib.auth.models import User, AnonymousUser

def farm_polls_processor(request):
    return {'app_ver' : '0.01'}

# Create your views here.
def hello(request):
#    args = {'username':auth.get_user(request).username}
    args = RequestContext(request)
    args['username']=auth.get_user(request).username
    return render_to_response('hello.html', args)

def anketa_list(request):
    args = RequestContext(request)
    user=auth.get_user(request)
    if not user.is_authenticated():
        return render_to_response('hello.html', args)
    args['username']=user.username
    user_profile=UserProfile.objects.get(uid=user)
    list = anketa.objects.filter(specialize=user_profile.specialize)
    args['list']=list
    return render_to_response('anketa_list.html', args)

def anketa_show(request, id=0):
    args = RequestContext(request)
    try:
        canketa=anketa.objects.get(id=id)
    except anketa.DoesNotExist:
        args['alert_message']='Ошибка. Анкета не существует.'
        args['alert_type']='alert'
        raise Http404()
        return render_to_response('error.html',args)

    args['alert_message']='Ошибка. Функционал в разработке.'
    args['alert_type']='info'
    return render_to_response('error.html', args)