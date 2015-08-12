# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from .forms import RegForm
from django.db  import IntegrityError
from polls.models import UserProfile
from .sms import send_sms_confirmation

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        try:
            user_profile=UserProfile.objects.get(uid=user)
        except UserProfile.DoesNotExist:
            user = None

        if (user is not None):
            auth.login(request, user)

            if user_profile.is_confirmed:
                return redirect('/')
            else:
                args['username']=user.username
                args['tel']=user_profile.tel
                args['last_sms_time'] = user_profile.last_sms_time
                return render_to_response('sms_confirm.html', args)
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegForm()
    if request.POST:
        newuser_form =RegForm(request.POST)
        if newuser_form.is_valid():
            tel=newuser_form.cleaned_data['tel']
            pwd1=newuser_form.cleaned_data['pwd1']
            pwd2=newuser_form.cleaned_data['pwd2']
            email=newuser_form.cleaned_data['email']
            f=newuser_form.cleaned_data['f']
            i=newuser_form.cleaned_data['i']
            employment=newuser_form.cleaned_data['employment']
            position=newuser_form.cleaned_data['position']
            ranks=newuser_form.cleaned_data['ranks']
            specialize=newuser_form.cleaned_data['specialize']

            if pwd1==pwd2:
                try:
                    user = User.objects.create_user(email,email,pwd2,first_name=i, last_name=f)
                    user_profile = UserProfile.objects.create(uid=user, tel=tel, employment=employment, position=position, ranks=ranks, is_confirmed=False, specialize=specialize)
                    send_sms_confirmation(user_profile)
                except IntegrityError:
                    args['errorvalue']='Ошибка добавления пользователя. Пользователь %s существует.' % email
                else:
                    newuser = auth.authenticate(username=email, password=pwd2)
                    auth.login(request, newuser)
                    user_profile=UserProfile.objects.get(uid=user)
                    args['username']=email
                    args['tel']=tel
                    args['last_sms_time'] = user_profile.last_sms_time
                    return render_to_response('sms_confirm.html', args)
            else:
                args['errorvalue']='Пароли не совпадают.'
        else:
            args['errorvalue'] = 'Заполните правильно все поля формы.'

        args['form'] = newuser_form

    return render_to_response('register.html', args)

def sms_confirm(request, send_sms=0):
    args = {}
    args.update(csrf(request))
    user=auth.get_user(request)
    args['username']=user.username
    user_profile=UserProfile.objects.get(uid=user)
    last_sms = int(user_profile.last_sms)
    last_sms_time = user_profile.last_sms_time
    args['last_sms']=int(last_sms)
    args['last_sms_time'] = last_sms_time

    if send_sms:
        sms_result = send_sms_confirmation(user_profile)
        if sms_result==0:
            args['infovalue'] = "Вам была отправлена повторная СМС с кодом подтверждения телефонного номера."
        elif sms_result==1:
           args['errorvalue'] = "Со времени отправки предидущей СМС прошло слишком мало времени."
        elif sms_result==2:
           args['errorvalue'] = "Произошла ошибка отправки СМС шлюзом."
        else:
           args['errorvalue'] = "Неизвестная ошибка отправки СМС."

        args['last_sms_time'] = user_profile.last_sms_time
        return render_to_response('sms_confirm.html', args)

    if request.POST:
        try:
            sms_code = int(request.POST.get('sms_code', '0'))
        except ValueError:
            sms_code=0

        if sms_code==last_sms:
            user_profile.is_confirmed=True
            user_profile.save()
            return redirect('/')
        else:
            args['errorvalue'] = "Код из SMS неверен."
            return render_to_response('sms_confirm.html', args)
    else:
        return render_to_response('sms_confirm.html', args)

def sms_reconfirm(request):
    return sms_confirm(request,1)