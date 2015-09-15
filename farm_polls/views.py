# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from farm_polls.models import anketa, poll, question, preparat, anketa_result, poll_result, preparat_result
from mbrc_profile.models import specialize, UserProfile
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone
from django.core.context_processors import csrf
import json

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

def anketa_show(request, anketa_id=-1, poll_id=-1):
    args = RequestContext(request)
    user=auth.get_user(request)
    if not user.is_authenticated():
        return render_to_response('hello.html', args)
    args['username']=user.username
    try:
        if int(anketa_id)>0:
            canketa=anketa.objects.get(id=anketa_id)
        else:
            canketa=anketa.objects.first()
    except anketa.DoesNotExist:
        args['alert_message']='Ошибка. Анкета не существует.'
        args['alert_type']='alert'
#        raise Http404()
        return render_to_response('error.html',args)

    # для формирования ссылок передаем id текущей анкеты
    args['anketa_id']=anketa_id

    # Отмечаем вход в анкету в БД
    try:
        cares = anketa_result.objects.get(anketa=canketa, user=user)
        cares.a_nsessions+=1
        cares.a_ls_start=timezone.now()
        cares.save()
    except anketa_result.DoesNotExist:
        cares = anketa_result.objects.create(anketa=canketa, user=user)
        cares.a_nsessions=1
        cares.a_start=timezone.now()
        cares.a_ls_start=cares.a_start
        cares.save()

    # получаем самый первый опрос в анкете (надо будет предусмотреть вариант если вообще нет опросов)
    cpolls = poll.objects.filter(anketa=canketa)
    if int(poll_id)>0:
        cpoll= cpolls.get(id=poll_id)
    else:
        cpoll = cpolls.first()

    if cpoll:
        p_current = None
        p_next = None
        p_prev = None
        prev_is_set = 0
        for p in cpolls:
            if prev_is_set:
                p_next = p
            if p == cpoll:
                p_prev = p_current
                prev_is_set = 1
            p_current = p

        if p_next:
            args['p_next_id']=p_next.id
        if p_prev:
            args['p_prev_id']=p_prev.id


        args['polls']=cpolls
        args['poll']=cpoll

        # Получаем список вопросов по самому первому опросу
        cquestion = question.objects.filter(poll=cpoll)
        args['questions']=cquestion

        # Получаем список препаратов по самому первому опросу
        pr = preparat.objects.filter(poll=cpoll)
        args['preparats']=pr

        try:
            json_dict=json.loads(cares.json_data)
        except:
            json_dict={}

        args['data']=json_dict.get('%s'%cpoll.id)
        #raise

    return render_to_response('anketa.html', args)


def poll_save(request, poll_id=-1):
    args = RequestContext(request)
    user=auth.get_user(request)
    if not user.is_authenticated():
        return render_to_response('hello.html', args)
    args['username']=user.username

    cpoll = poll.objects.get(id=poll_id)
    canketa = cpoll.anketa

    ca_res = anketa_result.objects.get(anketa=canketa, user=user)
    try:
        json_dict=json.loads(ca_res.json_data)
    except:
        json_dict={}

    #try:
    #    cp_res = poll_result.objects.get(anketa_result=ca_res, poll=cpoll)
    #except poll_result.DoesNotExist:
    #    cp_res = poll_result.objects.create(anketa_result=ca_res, poll=cpoll)

    args.update(csrf(request))
    if request.POST:
        cpr = preparat.objects.filter(poll=cpoll)
        cquestion = question.objects.filter(poll=cpoll)
        query_dict={}
        for q in cquestion:
            pr_dict={}
            # pr0 это общее имя для все radiobutton
            id_name='q%spr0'%(q.id)
            value = request.POST.get(id_name, '')
            if value!='':
                pr_dict['0'] = '%s'%value

            for p in cpr:
                id_name='q%spr%s'%(q.id,p.id)
                value = request.POST.get(id_name, '')
                if value!='':
                    pr_dict['%s'%p.id] = '%s'%value
            query_dict['%s'%q.id] = pr_dict
        if query_dict!={}:
            json_dict['%s'%cpoll.id]=query_dict

        json_data=json.dumps(json_dict)
        ca_res.json_data=json_data
        ca_res.save()

    return anketa_show(request, canketa.id, cpoll.id)
